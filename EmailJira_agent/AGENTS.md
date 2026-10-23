# EmailJira development rules

Applies to the entire repository. This file operationalizes the supplied code-development instructions. Read the relevant code, tests, requirements and documentation before each change. Explicit user instructions take precedence; record material conflicts rather than silently changing scope.

## Scope and workflow

Build one local Windows application with one bounded agent: Gmail intake, order/application tracking in Jira, human review, exact-version approval before every outgoing email, daily digest and safe recovery. Use LangChain first; LangGraph only after complete initial acceptance. No additional agents, microservices, vector database, message broker, paid hosting or mandatory tracing platform. Implement one small complete behavior at a time and explain it to the user. Do not delegate to subagents unless explicitly requested.

For each task: identify REQ/AC IDs and phase; inspect existing implementation/tests; choose smallest complete solution; implement and test; run focused then applicable broader checks; review security/recovery and diff; update affected docs; report actual evidence, limitations and next step. Make reversible routine decisions independently; ask only for missing scope/correctness/authorization/external facts. Never invent credentials, identities, provider capabilities or acceptance.

## Architecture and authority

Follow [architecture](docs/architecture.md) and [requirements](docs/requirements.md). Domain rules remain independent of LangChain, HTTP and SQLite. Workflows coordinate; adapters integrate; one agent investigates bounded evidence and proposes structured actions. Deterministic code validates and executes. Agent tools never include sending, unrestricted Gmail/HTTP or shell access. Gmail owns received email/editable drafts; SQLite owns verified mappings/events/business stage and approved snapshots/execution history; Jira owns human notes and verified human decisions. Keep business, review, approval and execution states independent.

## Runtime and dependencies

Python 3.12 only: requires-python = ">=3.12,<3.13". Use uv, pyproject.toml and committed uv.lock; separate runtime/dev dependencies; verify locked installation and Python compatibility. Add dependencies only for current needs; focused tested upgrades. No secrets in dependency/index URLs. Runtime files live under %LOCALAPPDATA%\MailJiraAgent\ outside Git. Store instants in UTC, display/schedule Europe/Berlin; date-only stays a date. No import-time external effects.

## Code quality

Use Ruff format/lint and mypy consistently. Annotate production functions and meaningful structures; unrestricted Any requires rationale. Validate trust-boundary schemas. Descriptive names, cohesive functions, explicit control flow and specific exceptions. No swallowed failures, mutable defaults, wildcard imports or hidden mutable global state. Use context managers; prefer composition. Document public behavior and non-obvious intent, not redundant narration. No arbitrary function-size restrictions or coverage-driven fragmentation. Keep exception causes useful and sanitized; distinguish transient, known failed and uncertain outcomes.

## Production completeness

No placeholders, stubbed required functions, fake API/model results, silent no-ops, fabricated success, or production simulation fallback. TODO/pass/ellipsis/NotImplementedError cannot substitute for required delivered behavior; legitimate syntax is reviewed semantically. Mocks/fakes/synthetic fixtures belong only in tests or clearly identified evaluation tooling and are never selected by normal production. Missing config or service produces explicit unavailable/error state. Do not create empty future modules or speculative extension points; use the planned directory structure incrementally.

## Security and recovery

Apply [security policy](SECURITY.md), [threat model](docs/threat-model.md) and [security plan](docs/security-test-plan.md). Never request secrets in chat/hardcode/log tokens, full config or unnecessary mail. Use minimum Gmail scopes, user-scoped Windows DPAPI and account ACLs for persisted secrets; revoke/rotate exposures. TLS verification enabled for remote services; local callback/Ollama loopback only. Never execute email/attachments. Validate paths/filenames, encode untrusted output, prevent unsolicited remote retrieval and enforce Jira field/content allowlist. Restrict model/tool resources.

Persist intent before external writes; use stable identities, instance exclusion and atomic per-action claims. Uncertain writes reconcile before retry; empty search, elapsed time or restart is not proof of no effect. Keep network outside long DB transactions. Use parameterized SQL, versioned immutable released migrations, constraints including verified foreign keys, transactional related writes and tested upgrades. Back up before risky upgrades; do not promise destructive rollback. Backups must restore safely without replaying completed external actions.

Sending stays disabled until its security acceptance passes and user enables it. Verify authorized human actor, exact proposal version, From/To/CC/BCC/subject/body/attachment identities, relevance and execution history at the executor. Relevant changes require fresh approval; silence/missing/uncertain/rejected approval never authorizes sending. Hashes do not prove human identity.

## Verification and delivery

Use pytest, offline deterministic default tests, synthetic sanitized fixtures and temporary real SQLite. Mock external boundaries, not private implementation. Test public outcomes and domain logic separately from model quality. Hypothesis selectively. Implement tests alongside each feature, not an empty complete-project suite. Use [test strategy](docs/test-strategy.md) and [Phase 1 cases](docs/phase-1-test-cases.md). Live checks/model evaluations explicitly enabled and reported separately; Windows behavior needs Windows evidence.

Critical deterministic policies target 100% statements/branches; other deterministic code 90% statements/85% branches. Classify delivered files, measure separately, review exclusions; never weaken assertions or hide failures. Required scenarios include duplicates/restart, uncertain writes, ambiguity/late events, partial outcomes, stale/unauthorized approval, changed payload/attachments, hostile instructions/exfiltration, token/network failure and limits.

For PRs/release candidates require locked install, Ruff format/lint, mypy, offline tests/coverage, secret scan, vulnerability check and package build; Python 3.12 and Windows jobs where needed; CI no production secrets. Current phase must remain executable; later modules are not generated to satisfy tests. Report unrun/blocked evidence honestly.

## Git, releases and documentation

Keep main releasable; short-lived focused branches/commits; no unrelated refactoring/mass formatting or unauthorized shared-history rewrite. Review diff before committing and checks before merge. Use PRs if remote workflow exists, equivalent local review otherwise. Never commit runtime DB/logs/credentials/private email. Human review required for credential, migration, approval and sending changes; self-review is not human approval.

Start 0.x semantic versions compatible with PEP 440; one authoritative application version, concise changelog and accepted release tags. Record app/prompt/model/lock identities for evaluations; no unverified automatic model/dependency updates. Maintain README, AGENTS, SECURITY, requirements/traceability, architecture/decisions, tests/security plans, later operational runbook and changelog alongside changes. SKILL.md optional only for an established reusable workflow. Do not tag or call a feature accepted until evidence and user acceptance exist.
