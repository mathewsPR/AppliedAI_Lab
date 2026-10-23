"""Integration tests using real temporary SQLite databases."""

import sqlite3
from pathlib import Path

import pytest

from mail_jira_agent.database import DatabaseError, apply_migrations, open_database


def test_foreign_keys_enabled_on_each_connection(tmp_path: Path) -> None:
    database_path = tmp_path / "state.db"

    for _ in range(2):
        with open_database(database_path) as connection:
            assert connection.execute("PRAGMA foreign_keys").fetchone() == (1,)


def test_unusable_database_path_fails_explicitly(tmp_path: Path) -> None:
    with pytest.raises(DatabaseError, match="Cannot open"):
        with open_database(tmp_path):
            pytest.fail("A directory must not open as a database")


def test_corrupt_database_is_not_replaced(tmp_path: Path) -> None:
    database_path = tmp_path / "corrupt.db"
    original = b"not a SQLite database"
    database_path.write_bytes(original)

    with pytest.raises(sqlite3.DatabaseError):
        with open_database(database_path) as connection:
            connection.execute("PRAGMA schema_version").fetchone()

    assert database_path.read_bytes() == original


def test_constraint_error_remains_specific(tmp_path: Path) -> None:
    with open_database(tmp_path / "state.db") as connection:
        connection.execute("CREATE TABLE sample (value TEXT UNIQUE NOT NULL)")
        connection.execute("INSERT INTO sample (value) VALUES (?)", ("same",))

        with pytest.raises(sqlite3.IntegrityError):
            connection.execute(
                "INSERT INTO sample (value) VALUES (?)",
                ("same",),
            )


def test_initial_migration_is_repeatable(tmp_path: Path) -> None:
    database_path = tmp_path / "state.db"

    with open_database(database_path) as connection:
        apply_migrations(connection)
        apply_migrations(connection)

    with open_database(database_path) as connection:
        rows = connection.execute(
            "SELECT version, applied_at_utc FROM schema_migrations"
        ).fetchall()
        assert len(rows) == 1
        assert rows[0][0] == 1
        assert rows[0][1].endswith("+00:00")


def test_migration_version_is_unique(tmp_path: Path) -> None:
    with open_database(tmp_path / "state.db") as connection:
        apply_migrations(connection)

        with pytest.raises(sqlite3.IntegrityError):
            connection.execute(
                """
                INSERT INTO schema_migrations (version, applied_at_utc)
                VALUES (?, ?)
                """,
                (1, "synthetic-time"),
            )

        assert connection.execute(
            "SELECT COUNT(*) FROM schema_migrations"
        ).fetchone() == (1,)


def test_existing_unversioned_database_is_rejected(tmp_path: Path) -> None:
    with open_database(tmp_path / "state.db") as connection:
        connection.execute("CREATE TABLE existing_data (id INTEGER PRIMARY KEY)")

        with pytest.raises(DatabaseError, match="no migration history"):
            apply_migrations(connection)

        assert connection.execute(
            "SELECT name FROM sqlite_master WHERE name = 'existing_data'"
        ).fetchone() == ("existing_data",)
        assert not connection.in_transaction


def test_unknown_migration_history_is_rejected(tmp_path: Path) -> None:
    with open_database(tmp_path / "state.db") as connection:
        apply_migrations(connection)
        connection.execute(
            """
            INSERT INTO schema_migrations (version, applied_at_utc)
            VALUES (?, ?)
            """,
            (2, "synthetic-time"),
        )

        with pytest.raises(DatabaseError, match="history is unsupported"):
            apply_migrations(connection)

        assert not connection.in_transaction


def test_failed_migration_rolls_back_schema_and_history(tmp_path: Path) -> None:
    database_path = tmp_path / "state.db"

    with open_database(database_path) as connection:

        def deny_history_insert(
            action: int,
            table: str | None,
            _column: str | None,
            _database: str | None,
            _trigger: str | None,
        ) -> int:
            if action == sqlite3.SQLITE_INSERT and table == "schema_migrations":
                return sqlite3.SQLITE_DENY
            return sqlite3.SQLITE_OK

        connection.set_authorizer(deny_history_insert)
        with pytest.raises(DatabaseError, match="migration failed"):
            apply_migrations(connection)
        assert not connection.in_transaction

    with open_database(database_path) as connection:
        assert (
            connection.execute(
                """
            SELECT name FROM sqlite_master
            WHERE type = 'table' AND name = 'schema_migrations'
            """
            ).fetchone()
            is None
        )

        apply_migrations(connection)
        assert connection.execute(
            "SELECT version FROM schema_migrations"
        ).fetchall() == [(1,)]
