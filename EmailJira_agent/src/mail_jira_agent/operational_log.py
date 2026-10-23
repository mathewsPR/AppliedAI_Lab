"""Small, structured operational log for the local foundation."""

import json
import re
from datetime import UTC, datetime
from enum import StrEnum
from pathlib import Path


class LogError(RuntimeError):
    """An operational event could not be recorded."""


class Operation(StrEnum):
    INIT = "init"
    RUN = "run"


class Outcome(StrEnum):
    COMPLETED = "completed"
    READY = "ready"
    STOPPED = "stopped"
    FAILED = "failed"


class FailureReason(StrEnum):
    CONFIG = "config"
    RUNTIME_PATH = "runtime_path"
    INSTANCE_LOCK = "instance_lock"
    DATABASE = "database"


_RUN_ID = re.compile(r"[0-9a-f]{32}\Z")


def write_event(
    runtime_root: Path,
    *,
    run_id: str,
    operation: Operation,
    outcome: Outcome,
    duration_ms: int,
    reason: FailureReason | None = None,
) -> None:
    """Append one validated JSON record to the account-local log."""
    if (
        _RUN_ID.fullmatch(run_id) is None
        or not isinstance(operation, Operation)
        or not isinstance(outcome, Outcome)
        or isinstance(duration_ms, bool)
        or not isinstance(duration_ms, int)
        or duration_ms < 0
        or (reason is not None and not isinstance(reason, FailureReason))
        or (outcome is Outcome.FAILED and reason is None)
        or (outcome is not Outcome.FAILED and reason is not None)
    ):
        raise ValueError("Invalid operational log field.")

    record = {
        "timestamp_utc": datetime.now(UTC).isoformat(),
        "run_id": run_id,
        "operation": operation.value,
        "outcome": outcome.value,
        "duration_ms": duration_ms,
    }
    if reason is not None:
        record["reason"] = reason.value

    try:
        with (runtime_root / "events.jsonl").open("a", encoding="utf-8") as log_file:
            log_file.write(json.dumps(record, ensure_ascii=True) + "\n")
    except OSError as exc:
        raise LogError("Cannot write the operational log.") from exc
