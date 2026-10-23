"""Integration checks for sanitized foundation failure records."""

import json
import os
import subprocess
import sys
from pathlib import Path


def invoke_init(runtime_root: Path) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    environment["LOCALAPPDATA"] = str(runtime_root.parent)
    return subprocess.run(
        [sys.executable, "-m", "mail_jira_agent", "init"],
        capture_output=True,
        text=True,
        env=environment,
        check=False,
        timeout=10,
    )


def test_invalid_config_logs_reason_without_private_value(tmp_path: Path) -> None:
    runtime_root = tmp_path / "local" / "MailJiraAgent"
    runtime_root.mkdir(parents=True)
    secret = "synthetic-secret-never-log"
    (runtime_root / "config.toml").write_text(
        '[application]\nmode = "foundation"\nsending_enabled = false\n'
        f'[private]\ntoken = "{secret}"\n',
        encoding="utf-8",
    )

    result = invoke_init(runtime_root)

    assert result.returncode != 0
    assert secret not in result.stdout + result.stderr
    lines = (runtime_root / "events.jsonl").read_text(encoding="utf-8").splitlines()
    assert len(lines) == 1
    assert secret not in lines[0]
    assert json.loads(lines[0])["reason"] == "config"
    assert json.loads(lines[0])["outcome"] == "failed"
    assert not (runtime_root / "state.db").exists()


def test_database_failure_logs_fixed_reason(tmp_path: Path) -> None:
    runtime_root = tmp_path / "local" / "MailJiraAgent"
    runtime_root.mkdir(parents=True)
    (runtime_root / "config.toml").write_text(
        '[application]\nmode = "foundation"\nsending_enabled = false\n',
        encoding="utf-8",
    )
    (runtime_root / "state.db").mkdir()

    result = invoke_init(runtime_root)

    assert result.returncode != 0
    record = json.loads(
        (runtime_root / "events.jsonl").read_text(encoding="utf-8").splitlines()[0]
    )
    assert record["operation"] == "init"
    assert record["outcome"] == "failed"
    assert record["reason"] == "database"
    assert record["duration_ms"] >= 0
