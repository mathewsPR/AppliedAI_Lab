"""Tests for the public configuration loader."""

from pathlib import Path

import pytest

from mail_jira_agent.config import ConfigurationError, load_config


def write_config(tmp_path: Path, content: str) -> Path:
    path = tmp_path / "config.toml"
    path.write_text(content, encoding="utf-8")
    return path


def test_valid_foundation_configuration(tmp_path: Path) -> None:
    config = load_config(
        write_config(
            tmp_path,
            '[application]\nmode = "foundation"\nsending_enabled = false\n',
        )
    )

    assert config.mode == "foundation"
    assert config.sending_enabled is False


@pytest.mark.parametrize(
    "content",
    [
        "",
        "[application",
        '[application]\nmode = "foundation"\n',
        '[application]\nmode = "foundation"\nsending_enabled = true\n',
        '[application]\nmode = "gmail"\nsending_enabled = false\n',
        '[application]\nmode = "foundation"\nsending_enabled = "false"\n',
        '[application]\nmode = "foundation"\nsending_enabled = false\nextra = 1\n',
        '[application]\nmode = "foundation"\nsending_enabled = false\n'
        '[secrets]\ntoken = "synthetic-secret"\n',
    ],
)
def test_invalid_configuration_is_rejected(tmp_path: Path, content: str) -> None:
    with pytest.raises(ConfigurationError) as result:
        load_config(write_config(tmp_path, content))

    assert "synthetic-secret" not in str(result.value)


def test_missing_file_is_reported_without_contents(tmp_path: Path) -> None:
    with pytest.raises(ConfigurationError, match="Cannot read"):
        load_config(tmp_path / "missing.toml")
