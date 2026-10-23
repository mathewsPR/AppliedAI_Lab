"""Command-line entry point for EmailJira."""

import argparse
from collections.abc import Sequence
from importlib.metadata import version

from mail_jira_agent.config import ConfigurationError, load_config
from mail_jira_agent.database import DatabaseError, apply_migrations, open_database
from mail_jira_agent.instance_lock import InstanceLockError, single_instance
from mail_jira_agent.runtime_paths import (
    RuntimePathError,
    initialize_runtime_root,
    resolve_runtime_root,
)


def initialize_foundation() -> None:
    """Validate local settings and initialize the account's SQLite store."""
    runtime_root = resolve_runtime_root()
    load_config(runtime_root / "config.toml")

    runtime_root = initialize_runtime_root()
    with single_instance(runtime_root):
        with open_database(runtime_root / "state.db") as connection:
            apply_migrations(connection)


def main(argv: Sequence[str] | None = None) -> int:
    """Run a supported command or report an unavailable operation."""
    parser = argparse.ArgumentParser(
        prog="mail-jira-agent",
        description="EmailJira local application",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {version('mail-jira-agent')}",
    )
    commands = parser.add_subparsers(dest="command")
    commands.add_parser("init", help="Validate configuration and initialize SQLite")

    arguments = parser.parse_args(argv)
    if arguments.command == "init":
        try:
            initialize_foundation()
        except (
            ConfigurationError,
            RuntimePathError,
            InstanceLockError,
            DatabaseError,
        ) as exc:
            parser.exit(2, f"error: {exc}\n")
        print("Foundation database initialized.")
        return 0

    parser.error("No operation is available yet; use --help or --version.")


if __name__ == "__main__":
    raise SystemExit(main())
