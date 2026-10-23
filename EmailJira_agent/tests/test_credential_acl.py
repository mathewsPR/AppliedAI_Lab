"""Windows ACL checks on isolated credential directories."""

from pathlib import Path

import pytest
import win32security

from mail_jira_agent.credential_acl import (
    CredentialDirectoryError,
    prepare_credential_directory,
)


def test_private_directory_has_only_account_and_system_aces(tmp_path: Path) -> None:
    credential_dir = prepare_credential_directory(tmp_path)

    descriptor = win32security.GetNamedSecurityInfo(
        str(credential_dir),
        win32security.SE_FILE_OBJECT,
        win32security.DACL_SECURITY_INFORMATION,
    )
    dacl = descriptor.GetSecurityDescriptorDacl()

    assert credential_dir.is_dir()
    assert dacl is not None
    assert dacl.GetAceCount() == 2

    system_sid = win32security.ConvertStringSidToSid("S-1-5-18")
    actual_sids = {str(dacl.GetAce(index)[2]) for index in range(2)}
    assert str(system_sid) in actual_sids
    assert len(actual_sids) == 2

    control, _revision = descriptor.GetSecurityDescriptorControl()
    assert control & win32security.SE_DACL_PROTECTED

    assert prepare_credential_directory(tmp_path) == credential_dir


def test_missing_runtime_directory_fails(tmp_path: Path) -> None:
    with pytest.raises(CredentialDirectoryError, match="unavailable"):
        prepare_credential_directory(tmp_path / "missing")
