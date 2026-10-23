"""Windows integration tests for protected credential files."""

from pathlib import Path

import pytest

from mail_jira_agent.credential_store import (
    CredentialStoreError,
    load_credential,
    save_credential,
)


def test_save_load_and_replace_synthetic_credential(tmp_path: Path) -> None:
    first = b"P1-SYNTHETIC-GMAIL-TOKEN"
    second = b"P1-SYNTHETIC-REPLACEMENT"

    save_credential(tmp_path, "gmail", first)
    path = tmp_path / "credentials" / "gmail.dpapi"

    assert path.is_file()
    assert first not in path.read_bytes()
    assert load_credential(tmp_path, "gmail") == first

    save_credential(tmp_path, "gmail", second)

    assert load_credential(tmp_path, "gmail") == second
    assert second not in path.read_bytes()
    assert not list(path.parent.glob("*.tmp"))


def test_credentials_have_separate_files(tmp_path: Path) -> None:
    save_credential(tmp_path, "gmail", b"P1-SYNTHETIC-GMAIL")
    save_credential(tmp_path, "jira", b"P1-SYNTHETIC-JIRA")

    assert load_credential(tmp_path, "gmail") == b"P1-SYNTHETIC-GMAIL"
    assert load_credential(tmp_path, "jira") == b"P1-SYNTHETIC-JIRA"


def test_missing_credential_has_a_clear_error(tmp_path: Path) -> None:
    with pytest.raises(CredentialStoreError, match="not configured"):
        load_credential(tmp_path, "jira")


def test_damaged_credential_cannot_be_recovered(tmp_path: Path) -> None:
    save_credential(tmp_path, "jira", b"P1-SYNTHETIC-JIRA")
    path = tmp_path / "credentials" / "jira.dpapi"
    path.write_bytes(b"damaged protected data")

    with pytest.raises(CredentialStoreError, match="cannot be recovered"):
        load_credential(tmp_path, "jira")


def test_empty_credential_is_rejected_without_writing(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        save_credential(tmp_path, "gmail", b"")

    assert not (tmp_path / "credentials" / "gmail.dpapi").exists()


def test_redirected_credential_file_is_rejected(tmp_path: Path) -> None:
    directory = tmp_path / "credentials"
    directory.mkdir()
    outside = tmp_path / "outside.txt"
    outside.write_text("untouched", encoding="utf-8")
    (directory / "jira.dpapi").symlink_to(outside)

    with pytest.raises(CredentialStoreError, match="redirected"):
        save_credential(tmp_path, "jira", b"P1-SYNTHETIC-JIRA")

    with pytest.raises(CredentialStoreError, match="redirected"):
        load_credential(tmp_path, "jira")

    assert outside.read_text(encoding="utf-8") == "untouched"
