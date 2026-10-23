# EmailJira

One planned local Windows Python application: Gmail intake, one bounded LangChain/Ollama agent, Jira order/application tracking and human review, exact-version approval before outgoing email, daily digest and safe recovery.

**Current state:** **Current state:** Phase 0 documentation is complete and self-reviewed. Phase 1 is in progress. A Python 3.12 package and diagnostic CLI are available. Gmail, Jira, model integration, database startup, and sending are not implemented. No live mail is read or sent.

## Reading order

1. [Phase 0 validation and remaining gates](docs/phase-0-validation.md)
2. [Requirements and selected decisions](docs/requirements.md)
3. [Architecture and agent loop](docs/architecture.md)
4. [Security policy](SECURITY.md) and [threat model](docs/threat-model.md)
5. [Test strategy](docs/test-strategy.md), [security cases](docs/security-test-plan.md), [verification criteria](docs/verification-criteria.md) and [Phase 1 detailed cases](docs/phase-1-test-cases.md)
6. [Standards](docs/standards.md) and [development rules](AGENTS.md)

The three user-supplied source documents remain unchanged. No empty future modules or extra infrastructure are created. See Phase 0 validation for selected defaults versus actual account/provider facts still needed. User acceptance of later features and live sending is separate from document completion.

## Current development commands

Run these from `EmailJira_agent` using Git Bash:

```bash
uv sync --locked
uv run --locked mail-jira-agent --help
uv run --locked mail-jira-agent --version
uv run --locked pytest -q
uv run --locked ruff format --check src tests
uv run --locked ruff check src tests
uv run --locked mypy src
```

Running the CLI without arguments currently exits with an error because no operational command has been delivered yet.

## Foundation configuration

`config.example.toml` documents the settings currently accepted by
`mail_jira_agent.config.load_config()`:

- `mode` must be `"foundation"`.
- `sending_enabled` must be `false`.

The loader rejects malformed files, missing or extra settings, and attempts to
enable unavailable behavior. The CLI does not load configuration yet; operational
startup will be added later in Phase 1. Do not put credentials in this file.

`initialize_runtime_root()` creates the directory and revalidates it afterward.
The CLI does not invoke it yet, and account ACL protection has not been verified.

## Local database foundation

`open_database()` opens a SQLite connection with foreign-key enforcement.
`apply_migrations()` applies numbered migrations in one transaction. The initial
migration creates only `schema_migrations`; business tables are added alongside
the features that use them. The CLI does not initialize a database yet.

Released migration files must not be edited. Add a new numbered migration for
future schema changes. Database startup, upgrade backup, and restore procedures
are still pending.

`single_instance()` holds a Windows file lock inside the runtime directory.
A second process using that directory is rejected. Windows releases the lock
after normal exit or process termination; the lock file itself may remain.
The CLI does not acquire the lock yet.

## Initialize the foundation

From Git Bash in `EmailJira_agent`, create the account-local directory and
copy the safe example configuration:

```bash
runtime_dir="$(cygpath -u "$LOCALAPPDATA")/MailJiraAgent"
mkdir -p "$runtime_dir"
cp -n config.example.toml "$runtime_dir/config.toml"
uv run --locked mail-jira-agent init
```

`cp -n` preserves an existing configuration. Inspect it before changing it.
Successful initialization creates `state.db` and an `instance.lock` file under
`%LOCALAPPDATA%\MailJiraAgent\`. Repeating `init` is safe. Gmail, Jira, Ollama,
and sending are unavailable at this stage.

To hold the foundation open, run:

```bash
uv run --locked mail-jira-agent run


Use an outer four-backtick fence if you’re copying this whole Markdown passage into another Markdown document.

Then review and commit:

```bash
uv run --locked ruff format --check src tests
uv run --locked ruff check src tests
uv run --locked mypy src
uv run --locked pytest -q
git diff --check

git add -- README.md src/mail_jira_agent/__main__.py tests/test_cli.py
git diff --cached --check
git diff --cached --name-only
git commit -m "feat(emailjira): run foundation with exclusive ownership"
git status --short --branch