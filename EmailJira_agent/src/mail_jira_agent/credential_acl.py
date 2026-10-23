"""Prepare a private Windows directory for encrypted credentials."""

from pathlib import Path

import ntsecuritycon
import pywintypes
import win32api
import win32con
import win32security


class CredentialDirectoryError(RuntimeError):
    """The credential directory cannot be prepared safely."""


def prepare_credential_directory(runtime_root: Path) -> Path:
    """Restrict the credential directory to this account and LocalSystem."""
    if not runtime_root.is_dir():
        raise CredentialDirectoryError("Runtime directory is unavailable.")

    credential_dir = runtime_root / "credentials"
    if credential_dir.is_symlink() or credential_dir.is_junction():
        raise CredentialDirectoryError("Credential directory is redirected.")

    try:
        credential_dir.mkdir(exist_ok=True)

        token = win32security.OpenProcessToken(
            win32api.GetCurrentProcess(),
            win32con.TOKEN_QUERY,
        )
        try:
            user_sid = win32security.GetTokenInformation(
                token, win32security.TokenUser
            )[0]
        finally:
            win32api.CloseHandle(token)

        system_sid = win32security.ConvertStringSidToSid("S-1-5-18")
        inheritance = win32con.OBJECT_INHERIT_ACE | win32con.CONTAINER_INHERIT_ACE

        dacl = win32security.ACL()
        dacl.AddAccessAllowedAceEx(
            win32security.ACL_REVISION,
            inheritance,
            ntsecuritycon.FILE_ALL_ACCESS,
            user_sid,
        )
        dacl.AddAccessAllowedAceEx(
            win32security.ACL_REVISION,
            inheritance,
            ntsecuritycon.FILE_ALL_ACCESS,
            system_sid,
        )

        win32security.SetNamedSecurityInfo(
            str(credential_dir),
            win32security.SE_FILE_OBJECT,
            win32security.DACL_SECURITY_INFORMATION
            | win32security.PROTECTED_DACL_SECURITY_INFORMATION,
            None,
            None,
            dacl,
            None,
        )
    except (OSError, pywintypes.error) as exc:
        raise CredentialDirectoryError(
            "Cannot prepare the credential directory."
        ) from exc

    if (
        credential_dir.is_symlink()
        or credential_dir.is_junction()
        or credential_dir.resolve().parent != runtime_root.resolve()
    ):
        raise CredentialDirectoryError("Credential directory is redirected.")

    return credential_dir
