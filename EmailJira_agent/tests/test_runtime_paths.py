"""Tests for account-local runtime path selection."""

import subprocess
from pathlib import Path

import pytest

from mail_jira_agent.runtime_paths import (
    RuntimePathError,
    initialize_runtime_root,
    resolve_runtime_root,
)


def test_runtime_path_uses_local_app_data(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    account_root = tmp_path / "Account Data ü"
    account_root.mkdir()
    monkeypatch.setenv("LOCALAPPDATA", str(account_root))

    result = resolve_runtime_root()

    assert result == account_root.resolve() / "MailJiraAgent"
    assert not result.exists()


def test_missing_local_app_data_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("LOCALAPPDATA", raising=False)

    with pytest.raises(RuntimePathError, match="not set"):
        resolve_runtime_root()


def test_relative_local_app_data_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("LOCALAPPDATA", "relative-folder")

    with pytest.raises(RuntimePathError, match="absolute"):
        resolve_runtime_root()


def test_file_cannot_be_local_app_data(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    account_root = tmp_path / "not-a-directory"
    account_root.write_text("synthetic", encoding="utf-8")
    monkeypatch.setenv("LOCALAPPDATA", str(account_root))

    with pytest.raises(RuntimePathError, match="not a directory"):
        resolve_runtime_root()


def test_nonexistent_local_app_data_fails(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("LOCALAPPDATA", str(tmp_path / "missing"))

    with pytest.raises(RuntimePathError, match="cannot be accessed"):
        resolve_runtime_root()


def test_runtime_junction_is_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    account_root = tmp_path / "account"
    outside = tmp_path / "outside"
    account_root.mkdir()
    outside.mkdir()

    runtime_root = account_root / "MailJiraAgent"
    result = subprocess.run(
        ["cmd.exe", "/c", "mklink", "/J", str(runtime_root), str(outside)],
        capture_output=True,
        text=True,
        check=False,
        timeout=10,
    )
    assert result.returncode == 0, result.stderr

    monkeypatch.setenv("LOCALAPPDATA", str(account_root))
    with pytest.raises(RuntimePathError, match="link or junction"):
        resolve_runtime_root()

    assert not (outside / "MailJiraAgent").exists()


def test_initialize_runtime_root_is_repeatable(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    account_root = tmp_path / "Account Data ü"
    account_root.mkdir()
    monkeypatch.setenv("LOCALAPPDATA", str(account_root))

    first = initialize_runtime_root()
    second = initialize_runtime_root()

    assert first == second == account_root.resolve() / "MailJiraAgent"
    assert first.is_dir()


def test_runtime_path_occupied_by_file_fails(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    account_root = tmp_path / "account"
    account_root.mkdir()
    runtime_root = account_root / "MailJiraAgent"
    runtime_root.write_text("untouched", encoding="utf-8")
    monkeypatch.setenv("LOCALAPPDATA", str(account_root))

    with pytest.raises(RuntimePathError, match="Cannot create"):
        initialize_runtime_root()

    assert runtime_root.read_text(encoding="utf-8") == "untouched"
