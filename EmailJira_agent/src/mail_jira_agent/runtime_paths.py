"""Resolve the account-local runtime location on Windows."""

import os
from pathlib import Path


class RuntimePathError(ValueError):
    """The account-local runtime location cannot be used safely."""


def resolve_runtime_root() -> Path:
    """Return the MailJiraAgent directory beneath LOCALAPPDATA."""
    raw_root = os.environ.get("LOCALAPPDATA")
    if not raw_root:
        raise RuntimePathError("LOCALAPPDATA is not set.")

    account_root = Path(raw_root)
    if not account_root.is_absolute():
        raise RuntimePathError("LOCALAPPDATA must be an absolute directory.")

    try:
        resolved_account_root = account_root.resolve(strict=True)
    except OSError as exc:
        raise RuntimePathError("LOCALAPPDATA cannot be accessed.") from exc

    if not resolved_account_root.is_dir():
        raise RuntimePathError("LOCALAPPDATA is not a directory.")

    runtime_root = resolved_account_root / "MailJiraAgent"

    # An existing link or junction must not redirect runtime data elsewhere.
    if runtime_root.is_symlink() or runtime_root.is_junction():
        raise RuntimePathError("The runtime directory cannot be a link or junction.")

    if runtime_root.resolve(strict=False).parent != resolved_account_root:
        raise RuntimePathError("The runtime directory escapes LOCALAPPDATA.")

    return runtime_root
