# EmailJira security policy

Status: design policy, 2026-10-22. No runnable application or verified secure release exists yet.

## Protected scope and boundaries

Protect Gmail/Jira credentials, private email-derived content, verified business facts, human decisions and execution/recovery history. The single local Windows application uses the user's account privileges; trusted administration and an uncompromised OS/account are assumptions. Tool restrictions inside one process are code-enforced capability boundaries, not an OS sandbox against malicious trusted code. DPAPI/ACLs do not defeat malware already running as the same user.

Email, quoted threads, attachments, model responses, API payloads, configuration and persisted values are validated at their boundaries. Untrusted text never grants approval or permissions. Only the deterministic executor can perform validated writes. Exact approval remains required for every outgoing email. Sending disabled by default; unresolved uncertainty blocks retry. Provider scope and host access do not replace application guards.

Credentials remain outside Git, encrypted with user-scoped Windows DPAPI and account ACLs. Runtime location is %LOCALAPPDATA%\MailJiraAgent\. Normal SQLite backup excludes credential files. Only permitted minimal fields may reach Jira. No full mailbox copy, raw email/attachment logging or plaintext token storage. Remote TLS remains verified; local services bind loopback. No attachment execution or automatic archive expansion.

## Reporting a suspected vulnerability

Until a repository/security contact exists, report privately to the project owner through the existing project communication channel using a sanitized description, affected document/revision, prerequisites, observed versus expected behavior and impact. Do not post tokens, personal mail, private attachments or exploit data containing others' information. No external reporting address or response SLA is invented. Once a remote repository exists, configure its private security-reporting route before wider distribution.

Security testing is limited to owned application instances and explicitly authorized dedicated Gmail/Jira resources. No unauthorized third-party scanning, mailbox access, live sending or destructive tests. Use synthetic fixtures; redact evidence.

## Incident procedure (design baseline)

1. Stop the local runner; keep sending disabled and do not replay uncertain operations.
2. Revoke/rotate exposed Gmail/Jira credentials through the provider; reauthorize locally when appropriate.
3. Preserve minimal sanitized operation IDs, versions and timestamps plus a protected DB copy for investigation. Do not copy a mailbox or disclose secrets.
4. Identify affected data/actions and reconcile remote effects before restarting. Never treat restore/timeout as proof an action did not happen.
5. Fix the cause, add a regression test, review dependency/model identities and obtain relevant human review before resumption.

Detailed installed-version recovery/backup commands belong to the Phase 6 runbook and must be tested before operational release. This procedure does not claim they exist now.

## References and release conditions

The accepted [standards](docs/standards.md) apply proportionately. See [threat model](docs/threat-model.md), [security test plan](docs/security-test-plan.md), and [test strategy](docs/test-strategy.md). No ISO/ASVS/FIPS certification is claimed. Applicable exploitable security findings and failed mandatory acceptance block release; nonapplicable findings require rationale. Recheck provider documentation and deployment privacy/policy obligations before live use.
