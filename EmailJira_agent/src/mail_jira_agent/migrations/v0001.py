"""Migration 1: record applied schema versions."""

VERSION = 1

STATEMENTS = (
    """
    CREATE TABLE schema_migrations (
        version INTEGER PRIMARY KEY CHECK (version > 0),
        applied_at_utc TEXT NOT NULL
    )
    """,
)
