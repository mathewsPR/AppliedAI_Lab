"""Tests for the public command-line interface."""

import os
import runpy
import subprocess
import sys
from pathlib import Path

import pytest

from mail_jira_agent.__main__ import main


def run_cli(
    arguments: list[str], runtime_root: Path
) -> subprocess.CompletedProcess[str]:
    """Invoke the installed module in a separate process."""
    environment = os.environ.copy()
    environment["LOCALAPPDATA"] = str(runtime_root)
    return subprocess.run(
        [sys.executable, "-m", "mail_jira_agent", *arguments],
        capture_output=True,
        text=True,
        env=environment,
        check=False,
        timeout=10,
    )


def test_help_and_version_do_not_create_runtime_files(tmp_path: Path) -> None:
    runtime_root = tmp_path / "isolated-local-appdata"

    help_result = run_cli(["--help"], runtime_root)
    version_result = run_cli(["--version"], runtime_root)

    assert help_result.returncode == 0
    assert "usage:" in help_result.stdout
    assert version_result.returncode == 0
    assert "mail-jira-agent 0.1.0" in version_result.stdout
    assert not runtime_root.exists()


def test_unavailable_operation_fails_clearly(tmp_path: Path) -> None:
    runtime_root = tmp_path / "isolated-local-appdata"

    result = run_cli([], runtime_root)

    assert result.returncode != 0
    assert "No operation is available yet" in result.stderr
    assert not runtime_root.exists()


def test_main_help_exits_successfully(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit) as result:
        main(["--help"])

    assert result.value.code == 0
    assert "usage:" in capsys.readouterr().out


def test_main_version_exits_successfully(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit) as result:
        main(["--version"])

    assert result.value.code == 0
    assert "mail-jira-agent 0.1.0" in capsys.readouterr().out


def test_main_without_operation_exits_with_error(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit) as result:
        main([])

    assert result.value.code == 2
    assert "No operation is available yet" in capsys.readouterr().err


def test_module_entry_point(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(sys, "argv", ["mail_jira_agent", "--version"])

    with pytest.raises(SystemExit) as result:
        runpy.run_path(main.__code__.co_filename, run_name="__main__")

    assert result.value.code == 0
    assert "mail-jira-agent 0.1.0" in capsys.readouterr().out


def test_init_creates_database_and_is_repeatable(tmp_path: Path) -> None:
    runtime_root = tmp_path / "isolated-local-appdata" / "MailJiraAgent"
    runtime_root.mkdir(parents=True)
    (runtime_root / "config.toml").write_text(
        '[application]\nmode = "foundation"\nsending_enabled = false\n',
        encoding="utf-8",
    )

    first = run_cli(["init"], runtime_root.parent)
    second = run_cli(["init"], runtime_root.parent)

    assert first.returncode == 0, first.stderr
    assert second.returncode == 0, second.stderr
    assert "Foundation database initialized." in first.stdout
    assert (runtime_root / "state.db").is_file()

    import sqlite3

    with sqlite3.connect(runtime_root / "state.db") as connection:
        assert connection.execute(
            "SELECT version FROM schema_migrations"
        ).fetchall() == [(1,)]


def test_init_rejects_invalid_config_before_database_write(tmp_path: Path) -> None:
    runtime_root = tmp_path / "isolated-local-appdata" / "MailJiraAgent"
    runtime_root.mkdir(parents=True)
    (runtime_root / "config.toml").write_text(
        '[application]\nmode = "foundation"\nsending_enabled = true\n',
        encoding="utf-8",
    )

    result = run_cli(["init"], runtime_root.parent)

    assert result.returncode != 0
    assert "Sending is unavailable" in result.stderr
    assert not (runtime_root / "state.db").exists()


def test_init_missing_config_does_not_create_database(tmp_path: Path) -> None:
    runtime_root = tmp_path / "isolated-local-appdata" / "MailJiraAgent"
    runtime_root.mkdir(parents=True)

    result = run_cli(["init"], runtime_root.parent)

    assert result.returncode != 0
    assert "Cannot read the configuration file" in result.stderr
    assert "Foundation database initialized" not in result.stdout
    assert not (runtime_root / "state.db").exists()


def test_init_reports_database_failure_without_success(tmp_path: Path) -> None:
    runtime_root = tmp_path / "isolated-local-appdata" / "MailJiraAgent"
    runtime_root.mkdir(parents=True)
    (runtime_root / "config.toml").write_text(
        '[application]\nmode = "foundation"\nsending_enabled = false\n',
        encoding="utf-8",
    )
    (runtime_root / "state.db").mkdir()

    result = run_cli(["init"], runtime_root.parent)

    assert result.returncode != 0
    assert "Cannot open the local database" in result.stderr
    assert "Foundation database initialized" not in result.stdout
    assert (runtime_root / "state.db").is_dir()


def test_run_holds_lock_and_rejects_second_instance(tmp_path: Path) -> None:
    runtime_root = tmp_path / "isolated-local-appdata" / "MailJiraAgent"
    runtime_root.mkdir(parents=True)
    (runtime_root / "config.toml").write_text(
        '[application]\nmode = "foundation"\nsending_enabled = false\n',
        encoding="utf-8",
    )

    environment = os.environ.copy()
    environment["LOCALAPPDATA"] = str(runtime_root.parent)
    process = subprocess.Popen(
        [sys.executable, "-u", "-m", "mail_jira_agent", "run"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=environment,
    )
    try:
        assert process.stdout is not None
        assert "Foundation ready" in process.stdout.readline()

        second = run_cli(["init"], runtime_root.parent)
        assert second.returncode != 0
        assert "Cannot acquire the instance lock" in second.stderr
        assert "initialized" not in second.stdout
    finally:
        if process.poll() is None:
            process.kill()
        process.communicate(timeout=5)
