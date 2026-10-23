"""SQLite connection handling for the local application."""

import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import UTC, datetime
from pathlib import Path

from mail_jira_agent.migrations import v0001

MIGRATIONS = (v0001,)


class DatabaseError(RuntimeError):
    """The local database could not be opened safely."""


@contextmanager
def open_database(path: Path) -> Iterator[sqlite3.Connection]:
    """Open a connection with foreign-key enforcement and close it afterward."""
    try:
        connection = sqlite3.connect(path, timeout=5.0, autocommit=True)
    except sqlite3.Error as exc:
        raise DatabaseError("Cannot open the local database.") from exc

    try:
        connection.execute("PRAGMA foreign_keys = ON")
        enabled = connection.execute("PRAGMA foreign_keys").fetchone()
        if enabled != (1,):
            raise DatabaseError("SQLite foreign-key enforcement is unavailable.")
    except (sqlite3.Error, DatabaseError) as exc:
        connection.close()
        if isinstance(exc, DatabaseError):
            raise
        raise DatabaseError("Cannot configure the local database.") from exc

    try:
        yield connection
    finally:
        connection.close()


def apply_migrations(connection: sqlite3.Connection) -> None:
    """Apply missing migrations atomically in version order."""
    try:
        connection.execute("BEGIN IMMEDIATE")

        table_exists = connection.execute(
            """
            SELECT 1 FROM sqlite_master
            WHERE type = 'table' AND name = 'schema_migrations'
            """
        ).fetchone()

        if table_exists:
            applied_versions = [
                row[0]
                for row in connection.execute(
                    "SELECT version FROM schema_migrations ORDER BY version"
                )
            ]
            known_versions = [migration.VERSION for migration in MIGRATIONS]
            if (
                not applied_versions
                or applied_versions != known_versions[: len(applied_versions)]
            ):
                raise DatabaseError("Database migration history is unsupported.")
        else:
            existing_tables = connection.execute(
                """
                SELECT name FROM sqlite_master
                WHERE type = 'table' AND name NOT LIKE 'sqlite_%'
                """
            ).fetchall()
            if existing_tables:
                raise DatabaseError("Database has tables but no migration history.")
            applied_versions = []

        for migration in MIGRATIONS[len(applied_versions) :]:
            for statement in migration.STATEMENTS:
                connection.execute(statement)
            connection.execute(
                """
                INSERT INTO schema_migrations (version, applied_at_utc)
                VALUES (?, ?)
                """,
                (migration.VERSION, datetime.now(UTC).isoformat()),
            )

        connection.execute("COMMIT")
    except (sqlite3.Error, DatabaseError) as exc:
        if connection.in_transaction:
            connection.execute("ROLLBACK")
        if isinstance(exc, DatabaseError):
            raise
        raise DatabaseError("Database migration failed.") from exc
