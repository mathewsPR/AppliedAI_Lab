"""Validate the currently supported application configuration."""

import tomllib
from dataclasses import dataclass
from pathlib import Path


class ConfigurationError(ValueError):
    """A configuration file cannot be used safely."""


@dataclass(frozen=True)
class FoundationConfig:
    """Settings supported by the Phase 1 foundation."""

    mode: str
    sending_enabled: bool


def load_config(path: Path) -> FoundationConfig:
    """Load a TOML file, accepting only delivered foundation behavior."""
    try:
        with path.open("rb") as config_file:
            data = tomllib.load(config_file)
    except OSError as exc:
        raise ConfigurationError("Cannot read the configuration file.") from exc
    except tomllib.TOMLDecodeError as exc:
        raise ConfigurationError("Configuration file is not valid TOML.") from exc

    if set(data) != {"application"}:
        raise ConfigurationError("Configuration must contain only [application].")

    application = data["application"]
    if not isinstance(application, dict) or set(application) != {
        "mode",
        "sending_enabled",
    }:
        raise ConfigurationError(
            "[application] must contain mode and sending_enabled only."
        )

    if application["mode"] != "foundation":
        raise ConfigurationError("Only foundation mode is currently available.")

    if application["sending_enabled"] is not False:
        raise ConfigurationError("Sending is unavailable and must be false.")

    return FoundationConfig(mode="foundation", sending_enabled=False)
