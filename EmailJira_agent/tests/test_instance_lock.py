"""Windows integration tests for instance ownership."""

import subprocess
import sys
import time
from pathlib import Path

import pytest

from mail_jira_agent.instance_lock import InstanceLockError, single_instance


def test_lock_file_remains_but_lock_is_reusable(tmp_path: Path) -> None:
    with single_instance(tmp_path):
        assert (tmp_path / "instance.lock").is_file()

    # The file remains; ownership is released.
    with single_instance(tmp_path):
        assert (tmp_path / "instance.lock").is_file()


def test_second_process_cannot_acquire_lock(tmp_path: Path) -> None:
    child_code = """
import sys
from pathlib import Path
from mail_jira_agent.instance_lock import InstanceLockError, single_instance

try:
    with single_instance(Path(sys.argv[1])):
        print("acquired")
except InstanceLockError:
    sys.exit(7)
"""

    with single_instance(tmp_path):
        result = subprocess.run(
            [sys.executable, "-c", child_code, str(tmp_path)],
            capture_output=True,
            text=True,
            check=False,
            timeout=10,
        )

        assert result.returncode == 7
        assert "acquired" not in result.stdout

    with single_instance(tmp_path):
        assert (tmp_path / "instance.lock").is_file()


def test_lock_released_after_holder_is_killed(tmp_path: Path) -> None:
    child_code = """
import sys
import time
from pathlib import Path
from mail_jira_agent.instance_lock import single_instance

with single_instance(Path(sys.argv[1])):
    print("READY", flush=True)
    time.sleep(10)
"""

    process = subprocess.Popen(
        [sys.executable, "-u", "-c", child_code, str(tmp_path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    try:
        assert process.stdout is not None
        assert process.stdout.readline().strip() == "READY"

        with pytest.raises(InstanceLockError):
            with single_instance(tmp_path):
                pytest.fail("A second process acquired the lock")

        process.kill()
        process.wait(timeout=5)

        deadline = time.monotonic() + 5
        while True:
            try:
                with single_instance(tmp_path):
                    assert (tmp_path / "instance.lock").is_file()
                break
            except InstanceLockError:
                if time.monotonic() >= deadline:
                    pytest.fail(
                        "The instance lock was not released after process death"
                    )
                time.sleep(0.05)

    finally:
        if process.poll() is None:
            process.kill()
        process.communicate(timeout=5)
