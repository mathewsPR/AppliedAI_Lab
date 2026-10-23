"""User-scoped Windows DPAPI protection for credential bytes."""

import pywintypes
import win32crypt

# Windows CRYPTPROTECT_UI_FORBIDDEN. Do not use CRYPTPROTECT_LOCAL_MACHINE.
_UI_FORBIDDEN = 0x1


class CredentialProtectionError(RuntimeError):
    """Windows could not protect or recover credential bytes."""


def protect_credential(plaintext: bytes) -> bytes:
    """Encrypt nonempty bytes for the current Windows user."""
    if not plaintext:
        raise ValueError("Credential cannot be empty.")

    try:
        return win32crypt.CryptProtectData(
            plaintext,
            "MailJiraAgent credential",
            None,
            None,
            None,
            _UI_FORBIDDEN,
        )
    except pywintypes.error as exc:
        raise CredentialProtectionError(
            "Windows could not protect the credential."
        ) from exc


def recover_credential(ciphertext: bytes) -> bytes:
    """Decrypt bytes belonging to the current Windows user."""
    if not ciphertext:
        raise CredentialProtectionError("Protected credential is empty.")

    try:
        _description, plaintext = win32crypt.CryptUnprotectData(
            ciphertext,
            None,
            None,
            None,
            _UI_FORBIDDEN,
        )
    except pywintypes.error as exc:
        raise CredentialProtectionError(
            "Windows could not recover the credential."
        ) from exc

    if not plaintext:
        raise CredentialProtectionError("Recovered credential is empty.")
    return plaintext
