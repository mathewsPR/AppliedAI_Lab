"""Store user-protected credential bytes outside the SQLite database."""

import os
import tempfile
from pathlib import Path
from typing import Literal

from mail_jira_agent.credential_acl import (
    CredentialDirectoryError,
    prepare_credential_directory,
)
from mail_jira_agent.credential_crypto import (
    CredentialProtectionError,
    protect_credential,
    recover_credential,
)

CredentialName = Literal["gmail", "jira", "model"]


class CredentialStoreError(RuntimeError):
    """A protected credential could not be saved or read."""


def _credential_path(runtime_root: Path, name: CredentialName) -> Path:
    if name not in ("gmail", "jira", "model"):
        raise ValueError("Unknown credential name.")

    try:
        directory = prepare_credential_directory(runtime_root)
    except CredentialDirectoryError as exc:
        raise CredentialStoreError("Credential storage is unavailable.") from exc

    return directory / f"{name}.dpapi"


def save_credential(
    runtime_root: Path,
    name: CredentialName,
    plaintext: bytes,
) -> None:
    """Atomically replace one encrypted credential."""
    if not plaintext:
        raise ValueError("Credential cannot be empty.")

    path = _credential_path(runtime_root, name)
    if path.is_symlink() or path.is_junction():
        raise CredentialStoreError("Credential path is redirected.")

    try:
        ciphertext = protect_credential(plaintext)
    except CredentialProtectionError as exc:
        raise CredentialStoreError("Credential protection failed.") from exc

    temporary_path: Path | None = None
    try:
        descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{name}-",
            suffix=".tmp",
            dir=path.parent,
        )
        temporary_path = Path(temporary_name)

        with os.fdopen(descriptor, "wb") as temporary_file:
            temporary_file.write(ciphertext)
            temporary_file.flush()
            os.fsync(temporary_file.fileno())

        if path.is_symlink() or path.is_junction():
            raise CredentialStoreError("Credential path is redirected.")

        os.replace(temporary_path, path)
        temporary_path = None
    except OSError as exc:
        raise CredentialStoreError("Cannot save the credential.") from exc
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def load_credential(runtime_root: Path, name: CredentialName) -> bytes:
    """Read and decrypt one credential for the current Windows user."""
    path = _credential_path(runtime_root, name)
    if path.is_symlink() or path.is_junction():
        raise CredentialStoreError("Credential path is redirected.")

    try:
        ciphertext = path.read_bytes()
    except FileNotFoundError as exc:
        raise CredentialStoreError("Credential is not configured.") from exc
    except OSError as exc:
        raise CredentialStoreError("Cannot read the credential.") from exc

    try:
        return recover_credential(ciphertext)
    except CredentialProtectionError as exc:
        raise CredentialStoreError("Credential cannot be recovered.") from exc
