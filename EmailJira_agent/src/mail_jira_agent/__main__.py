"""Command-line entry point for EmailJira."""

import argparse
import time
from collections.abc import Sequence
from importlib.metadata import version
from pathlib import Path
from time import monotonic
from uuid import uuid4

from mail_jira_agent.config import ConfigurationError, load_config
from mail_jira_agent.database import DatabaseError, apply_migrations, open_database
from mail_jira_agent.instance_lock import InstanceLockError, single_instance
from mail_jira_agent.operational_log import (
    FailureReason,
    LogError,
    Operation,
    Outcome,
    write_event,
)
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


def initialize_foundation(run_id: str) -> None:
    """Initialize the account's SQLite store and record completion."""
    started = monotonic()
    runtime_root = prepare_foundation()

    with single_instance(runtime_root):
        with open_database(runtime_root / "state.db") as connection:
            apply_migrations(connection)

        write_event(
            runtime_root,
            run_id=run_id,
            operation=Operation.INIT,
            outcome=Outcome.COMPLETED,
            duration_ms=int((monotonic() - started) * 1000),
        )


def run_foundation(run_id: str) -> None:
    """Hold exclusive ownership until the operator stops the foundation."""
    started = monotonic()
    runtime_root = prepare_foundation()

    with single_instance(runtime_root):
        with open_database(runtime_root / "state.db") as connection:
            apply_migrations(connection)

        write_event(
            runtime_root,
            run_id=run_id,
            operation=Operation.RUN,
            outcome=Outcome.READY,
            duration_ms=int((monotonic() - started) * 1000),
        )
        print(
            "Foundation ready. Gmail, Jira, model, and sending are unavailable.",
            flush=True,
        )

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            write_event(
                runtime_root,
                run_id=run_id,
                operation=Operation.RUN,
                outcome=Outcome.STOPPED,
                duration_ms=int((monotonic() - started) * 1000),
            )
            print("Foundation stopped.", flush=True)


def failure_reason(
    error: ConfigurationError | RuntimePathError | InstanceLockError | DatabaseError,
) -> FailureReason:
    """Classify a failure without copying its input or exception text."""
    if isinstance(error, ConfigurationError):
        return FailureReason.CONFIG
    if isinstance(error, RuntimePathError):
        return FailureReason.RUNTIME_PATH
    if isinstance(error, InstanceLockError):
        return FailureReason.INSTANCE_LOCK
    return FailureReason.DATABASE


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
        operation = Operation.INIT if arguments.command == "init" else Operation.RUN
        run_id = uuid4().hex
        started = monotonic()

        try:
            if operation is Operation.INIT:
                initialize_foundation(run_id)
            else:
                run_foundation(run_id)
        except (
            ConfigurationError,
            RuntimePathError,
            InstanceLockError,
            DatabaseError,
            LogError,
        ) as exc:
            log_note = ""
            if isinstance(exc, LogError):
                log_note = " Operational log unavailable."
            else:
                try:
                    runtime_root = resolve_runtime_root()
                    if runtime_root.is_dir():
                        write_event(
                            runtime_root,
                            run_id=run_id,
                            operation=operation,
                            outcome=Outcome.FAILED,
                            duration_ms=int((monotonic() - started) * 1000),
                            reason=failure_reason(exc),
                        )
                    else:
                        log_note = " Operational log unavailable."
                except (RuntimePathError, LogError):
                    log_note = " Operational log unavailable."

            parser.exit(2, f"error: {exc}{log_note}\n")

        if operation is Operation.INIT:
            print("Foundation database initialized.")
        return 0

    parser.error("No operation is available yet; use --help or --version.")


if __name__ == "__main__":
    raise SystemExit(main())
