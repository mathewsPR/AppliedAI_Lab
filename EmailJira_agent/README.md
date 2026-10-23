# EmailJira

One planned local Windows Python application: Gmail intake, one bounded LangChain/Ollama agent, Jira order/application tracking and human review, exact-version approval before outgoing email, daily digest and safe recovery.

**Current state:** Phase 0 documentation complete and self-reviewed. Application implementation has not started. No install/run commands, integrations, database, executable tests, CI or release are available yet. No live mail is read or sent by these documents. Phase 1 will create a runnable Python 3.12/uv foundation in small explainable steps.

## Reading order

1. [Phase 0 validation and remaining gates](docs/phase-0-validation.md)
2. [Requirements and selected decisions](docs/requirements.md)
3. [Architecture and agent loop](docs/architecture.md)
4. [Security policy](SECURITY.md) and [threat model](docs/threat-model.md)
5. [Test strategy](docs/test-strategy.md), [security cases](docs/security-test-plan.md), [verification criteria](docs/verification-criteria.md) and [Phase 1 detailed cases](docs/phase-1-test-cases.md)
6. [Standards](docs/standards.md) and [development rules](AGENTS.md)

The three user-supplied source documents remain unchanged. No empty future modules or extra infrastructure are created. See Phase 0 validation for selected defaults versus actual account/provider facts still needed. User acceptance of later features and live sending is separate from document completion.
