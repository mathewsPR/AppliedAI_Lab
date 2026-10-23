"""Windows integration tests using synthetic credential bytes."""

import pytest

from mail_jira_agent.credential_crypto import (
    CredentialProtectionError,
    protect_credential,
    recover_credential,
)


def test_current_user_dpapi_round_trip() -> None:
    plaintext = b"P1-SYNTHETIC-TOKEN"

    ciphertext = protect_credential(plaintext)

    assert ciphertext != plaintext
    assert plaintext not in ciphertext
    assert recover_credential(ciphertext) == plaintext


def test_empty_input_is_rejected() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        protect_credential(b"")

    with pytest.raises(CredentialProtectionError, match="is empty"):
        recover_credential(b"")


def test_truncated_ciphertext_is_not_accepted() -> None:
    ciphertext = protect_credential(b"P1-SYNTHETIC-TOKEN")

    with pytest.raises(CredentialProtectionError, match="could not recover"):
        recover_credential(ciphertext[:10])
