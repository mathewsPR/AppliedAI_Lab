"""Tests for structured, secret-free operational records."""

import json
from pathlib import Path

import pytest

from mail_jira_agent.operational_log import (
    LogError,
    Operation,
    Outcome,
    write_event,
)


def test_event_is_one_parseable_line_with_useful_fields(tmp_path: Path) -> None:
    write_event(
        tmp_path,
        run_id="a" * 32,
        operation=Operation.INIT,
        outcome=Outcome.COMPLETED,
        duration_ms=12,
    )

    lines = (tmp_path / "events.jsonl").read_text(encoding="utf-8").splitlines()
    assert len(lines) == 1
    record = json.loads(lines[0])
    assert record["run_id"] == "a" * 32
    assert record["operation"] == "init"
    assert record["outcome"] == "completed"
    assert record["duration_ms"] == 12
    assert record["timestamp_utc"].endswith("+00:00")


def test_hostile_identifier_cannot_forge_second_record(tmp_path: Path) -> None:
    hostile = 'a"\\n{"outcome":"completed","token":"synthetic-secret"}'

    with pytest.raises(ValueError, match="Invalid operational log field"):
        write_event(
            tmp_path,
            run_id=hostile,
            operation=Operation.RUN,
            outcome=Outcome.READY,
            duration_ms=0,
        )

    assert not (tmp_path / "events.jsonl").exists()


def test_invalid_duration_is_rejected(tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        write_event(
            tmp_path,
            run_id="b" * 32,
            operation=Operation.RUN,
            outcome=Outcome.READY,
            duration_ms=-1,
        )


def test_log_write_failure_is_explicit(tmp_path: Path) -> None:
    with pytest.raises(LogError, match="Cannot write"):
        write_event(
            tmp_path / "missing-directory",
            run_id="c" * 32,
            operation=Operation.INIT,
            outcome=Outcome.COMPLETED,
            duration_ms=0,
        )
