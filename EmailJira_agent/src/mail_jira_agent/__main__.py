"""Command-line entry point for EmailJira."""

import argparse
import time
from collections.abc import Sequence
from importlib.metadata import version
from pathlib import Path

from mail_jira_agent.config import ConfigurationError, load_config
from mail_jira_agent.database import DatabaseError, apply_migrations, open_database
from mail_jira_agent.instance_lock import InstanceLockError, single_instance
from mail_jira_agent.runtime_paths import (
    RuntimePathError,
    initialize_runtime_root,
    resolve_runtime_root,
)


def prepare_foundation() -> Path:
    """Validate settings and return the account-local runtime directory."""
    runtime_root = resolve_runtime_root()
    load_config(runtime_root / "config.toml")
    return initialize_runtime_root()


def initialize_foundation() -> None:
    """Initialize the account's SQLite store."""
    runtime_root = prepare_foundation()
    with single_instance(runtime_root):
        with open_database(runtime_root / "state.db") as connection:
            apply_migrations(connection)


def run_foundation() -> None:
    """Hold exclusive ownership until the operator stops the foundation."""
    runtime_root = prepare_foundation()
    with single_instance(runtime_root):
        with open_database(runtime_root / "state.db") as connection:
            apply_migrations(connection)

        print(
            "Foundation ready. Gmail, Jira, model, and sending are unavailable.",
            flush=True,
        )
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Foundation stopped.", flush=True)


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
    commands.add_parser("run", help="Run the local foundation until interrupted")

    arguments = parser.parse_args(argv)
    if arguments.command in {"init", "run"}:
        try:
            if arguments.command == "init":
                initialize_foundation()
            else:
                run_foundation()
        except (
            ConfigurationError,
            RuntimePathError,
            InstanceLockError,
            DatabaseError,
        ) as exc:
            parser.exit(2, f"error: {exc}\n")

        if arguments.command == "init":
            print("Foundation database initialized.")
        return 0
    parser.error("No operation is available yet; use --help or --version.")


if __name__ == "__main__":
    raise SystemExit(main())
