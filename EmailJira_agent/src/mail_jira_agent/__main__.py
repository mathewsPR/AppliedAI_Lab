"""Command-line entry point for EmailJira."""

import argparse
from collections.abc import Sequence
from importlib.metadata import version


def main(argv: Sequence[str] | None = None) -> int:
    """Show supported diagnostics and reject unavailable operations."""
    parser = argparse.ArgumentParser(
        prog="mail-jira-agent",
        description="EmailJira local application",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {version('mail-jira-agent')}",
    )
    parser.parse_args(argv)
    parser.error("No operation is available yet; use --help or --version.")


if __name__ == "__main__":
    raise SystemExit(main())
