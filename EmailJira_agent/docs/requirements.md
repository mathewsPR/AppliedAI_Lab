# EmailJira — Complete requirements specification

Version: 0.2.0 · Date: 2026-10-22 · Status: revised review baseline; engineering defaults selected; live deployment details pending.

This document specifies the agreed scope, not implemented software. It preserves the accepted standards baseline and the earlier AUTH-001–008 content. Source files are unchanged. No application code is generated.

## 1. Sources and precedence

- **S1:** Code development instructions.md, sections 1–15 and “No unfinished or simulated production behavior”.
- **S2:** Project goasl, Plan and phases.md, sections 1–12 (phase numbers 0–8).
- **S3:** Project directory structure.md; target structure, created incrementally rather than as empty modules.
- **S4:** Explicit decisions in this conversation: accepted standards baseline; stepwise development; reviewed Gmail authorization requirements.

Explicit user decisions override inferred interpretations. Any conflict affecting scope, authority, or correctness is recorded for resolution rather than silently resolved. Stronger wording introduced during review is identified in the decision register where it needs user confirmation.

## 2. Goal and boundary

Build one local Windows Python application that monitors Gmail from a configured activation date, uses one bounded agent to interpret evidence and propose actions, tracks orders/applications in Jira, creates human review tasks, prepares replies with exact-version authorized human approval before every outgoing email, generates daily digests, and recovers safely after downtime and uncertain writes.

Technology constraints: Python 3.12, uv, LangChain first, local Ollama, SQLite, Gmail OAuth, Jira, pytest, Git. qwen3:8b is an evaluation candidate, not a guaranteed accepted model. LangGraph is deferred until the complete LangChain application is accepted. No additional agents, microservices, vector database, message broker, paid hosting, mandatory tracing platform, or custom web dashboard.

## 3. Authorities and terminology

| Information | Authority |
| --- | --- |
| Received email and current editable draft | Gmail |
| Verified mappings, accepted events, derived business progress | SQLite |
| Human notes, review decisions, verified approval decisions | Jira |
| Immutable approved payload, execution and reconciliation history | SQLite |

**Consequential ambiguity:** unresolved evidence that could change entity matching, obligations, recipients, deadlines, or an external action. **Uncertain write:** submission may have succeeded remotely but confirmation is unavailable. **Approved version:** immutable snapshot of all protected outgoing content linked to a verified human decision. **Evidence:** source identity and relevant facts sufficient to support a decision; not an unnecessary mailbox copy. **Shall:** binding obligation after acceptance. **Candidate:** not selected or verified. **Known failure:** evidence establishes the operation failed without the intended effect; a timeout alone is not such evidence.

## 4. Interpretation and verification rules

All requirements are mandatory for their indicated phase after acceptance. Numeric engineering defaults in section 11 are selected before evaluation and must be verified on target hardware. Phase 8 is conditional and excluded from initial-release completion. Phase ranges mean introduced and completed incrementally; the phase gates below govern earliest external effects. Each requirement identifies its responsible application or process. Acceptance assertions are minimum evidence, not permission to ignore the obligation elsewhere.

The detailed verification cases in [verification-criteria.md](verification-criteria.md) are normative alongside the decision tables in section 11. Each planned verification has ID `VER-<requirement suffix>` (for example REQ-AUTH-001 → VER-AUTH-001). Evidence starts as **planned**, becomes **offline verified** or **live verified** only after execution, and becomes **accepted** only through human review. Every requirement below is currently **Draft** and all evidence **Not executed**. Verification uses applicable offline behavior tests, inspection, explicitly enabled live checks, model evaluation, or human walkthrough as stated by the acceptance text. No clause-level ISO/ASVS conformance is claimed: standards mapping is document-level guidance until actual clauses and applicability are reviewed.

STD-01 applies to the form and traceability of all requirements. A business rule need not originate from a standard: its source remains S1/S2/S4. STD-02 supplies quality-review guidance rather than business lifecycle rules. Tool choices are project constraints, not external security certifications.

## 5. Logical-state contract

These dimensions remain independent. Exact Jira statuses, field mappings, and business transition tables are gated decisions, not invented requirements.

| Dimension | Logical states/concepts | Transition rule |
| --- | --- | --- |
| Business | Order confirmation/fulfillment, returns/refunds, replacement links; application acknowledgment/progression/interview/rejection/offer; unknown/conflicting facts explicit | Accepted evidence and authorized corrections drive DEC-09 tables; late arrival alone cannot regress progress. Partial outcomes retain outstanding obligations. |
| Human review | Pending acknowledgment; acknowledged/open; resolved | Human action required for acknowledgment/resolution; acknowledgment alone need not discharge the obligation. |
| Approval | Pending; Approved; Changes Requested; Rejected; invalidated approval recorded | Only verified authorized decisions approve a current version. Protected changes invalidate approval and require a new decision. |
| Execution | Prepared/pending; in progress; confirmed; known failed; uncertain | Durable intent precedes external attempt. Uncertain cannot become retryable solely by timeout, restart, or lease expiry. |

The review and execution names are proposed logical vocabulary to make evidence testable, not claims that Jira supports identically named statuses. Their provider mappings require DEC-04/07; business transitions are now defined in ORD-01 and APP-01.

## 6. Numbered requirements

### GOV — Scope and authority

#### REQ-GOV-001

**Requirement:** The application shall run as one local Windows Python application with one bounded agent.

**Acceptance criteria:**

- **AC-GOV-001-01:** Inspect deployment: one application and agent.
- **AC-GOV-001-02:** no microservices, vector database, message broker, paid hosting, or mandatory tracing service.

**Source:** S1 §1,3,14; S2 §1–4. **References:** STD-01, STD-02. **Phase:** 0–7.

**Verification:** [VER-GOV-001](verification-criteria.md#ver-gov-001) — not executed.

#### REQ-GOV-002

**Requirement:** The application shall use LangChain orchestration for the initial accepted application.

**Acceptance criteria:**

- **AC-GOV-002-01:** Inspect dependencies and execution.
- **AC-GOV-002-02:** LangGraph migration starts only after user acceptance of the complete LangChain release.

**Source:** S1 §1,3,14; S2 §1–4. **References:** STD-01, STD-02. **Phase:** 0–7.

**Verification:** [VER-GOV-002](verification-criteria.md#ver-gov-002) — not executed.

#### REQ-GOV-003

**Requirement:** The application shall keep domain decisions independent of framework, HTTP-client, and persistence implementation details.

**Acceptance criteria:**

- **AC-GOV-003-01:** Domain tests execute without LangChain, external services, or a database.
- **AC-GOV-003-02:** adapters and workflows own those dependencies.

**Source:** S1 §1,3,14; S2 §1–4. **References:** STD-01, STD-02. **Phase:** 0–7.

**Verification:** [VER-GOV-003](verification-criteria.md#ver-gov-003) — not executed.

#### REQ-GOV-004

**Requirement:** The application shall use deterministic Python to validate proposals and execute external actions.

**Acceptance criteria:**

- **AC-GOV-004-01:** A model proposal alone cannot perform an external write.
- **AC-GOV-004-02:** invalid proposals fail before adapter execution.

**Source:** S1 §1,3,14; S2 §1–4. **References:** STD-01, STD-02. **Phase:** 0–7.

**Verification:** [VER-GOV-004](verification-criteria.md#ver-gov-004) — not executed.

#### REQ-GOV-005

**Requirement:** The application shall respect the defined data authorities.

**Acceptance criteria:**

- **AC-GOV-005-01:** Conflicting copies resolve according to the authority table.
- **AC-GOV-005-02:** Jira human notes are not overwritten by application reconciliation.

**Source:** S1 §1,3,14; S2 §1–4. **References:** STD-01, STD-02. **Phase:** 0–7.

**Verification:** [VER-GOV-005](verification-criteria.md#ver-gov-005) — not executed.

#### REQ-GOV-006

**Requirement:** The application shall create only modules and abstractions needed by delivered behavior.

**Acceptance criteria:**

- **AC-GOV-006-01:** Review finds no empty future modules or speculative framework.
- **AC-GOV-006-02:** folder names follow S3 when introduced.

**Source:** S1 §1,3,14; S2 §1–4. **References:** STD-01, STD-02. **Phase:** 0–7.

**Verification:** [VER-GOV-006](verification-criteria.md#ver-gov-006) — not executed.

### FND — Application foundation

#### REQ-FND-001

**Requirement:** The application shall validate configuration before dependent operations.

**Acceptance criteria:**

- **AC-FND-001-01:** Missing, malformed, incompatible, or unsafe settings produce actionable errors.
- **AC-FND-001-02:** unavailable features cannot appear enabled.

**Source:** S1 §2,5,6,8,9; S2 §5. **References:** STD-02, STD-04, REF-03, REF-04. **Phase:** 1.

**Verification:** [VER-FND-001](verification-criteria.md#ver-fnd-001) — not executed.

#### REQ-FND-002

**Requirement:** The application shall store runtime data under %LOCALAPPDATA%\MailJiraAgent\ outside Git.

**Acceptance criteria:**

- **AC-FND-002-01:** Fresh Windows startup resolves account-specific directories.
- **AC-FND-002-02:** unavailable or unsafe paths cause explicit failure without fallback into the repository.

**Source:** S1 §2,5,6,8,9; S2 §5. **References:** STD-02, STD-04, REF-03, REF-04. **Phase:** 1.

**Verification:** [VER-FND-002](verification-criteria.md#ver-fnd-002) — not executed.

#### REQ-FND-003

**Requirement:** The application shall provide a documented CLI with accurate startup and termination outcomes.

**Acceptance criteria:**

- **AC-FND-003-01:** Fresh installation initializes successfully.
- **AC-FND-003-02:** invalid configuration and operational failure return non-success outcomes with sanitized explanations.

**Source:** S1 §2,5,6,8,9; S2 §5. **References:** STD-02, STD-04, REF-03, REF-04. **Phase:** 1.

**Verification:** [VER-FND-003](verification-criteria.md#ver-fnd-003) — not executed.

#### REQ-FND-004

**Requirement:** The application shall prevent overlapping instances operating on the same runtime store.

**Acceptance criteria:**

- **AC-FND-004-01:** A second instance is rejected.
- **AC-FND-004-02:** after normal termination or process death, restart follows the documented recovery procedure without concurrent execution.

**Source:** S1 §2,5,6,8,9; S2 §5. **References:** STD-02, STD-04, REF-03, REF-04. **Phase:** 1.

**Verification:** [VER-FND-004](verification-criteria.md#ver-fnd-004) — not executed.

#### REQ-FND-005

**Requirement:** The application shall shut down without reporting unfinished external actions as confirmed.

**Acceptance criteria:**

- **AC-FND-005-01:** Interrupt at processing and write boundaries.
- **AC-FND-005-02:** committed work survives and unresolved external actions resume through recovery.

**Source:** S1 §2,5,6,8,9; S2 §5. **References:** STD-02, STD-04, REF-03, REF-04. **Phase:** 1.

**Verification:** [VER-FND-005](verification-criteria.md#ver-fnd-005) — not executed.

#### REQ-FND-006

**Requirement:** The application shall produce sanitized operational logs.

**Acceptance criteria:**

- **AC-FND-006-01:** Logs expose identifiers, decisions, durations, and outcomes.
- **AC-FND-006-02:** tokens, full configuration dumps, message bodies, and attachments are absent.
- **AC-FND-006-03:** sanitized newlines cannot forge records.
- **AC-FND-006-04:** names/subjects are excluded by default.

**Source:** S1 §2,5,6,8,9; S2 §5. **References:** STD-02, STD-04, REF-03, REF-04. **Phase:** 1.

**Verification:** [VER-FND-006](verification-criteria.md#ver-fnd-006) — not executed.

### AUTH — Gmail authorization

#### REQ-AUTH-001

**Requirement:** The application shall obtain Gmail access using installed-app authorization-code OAuth with PKCE and the system browser.

**Acceptance criteria:**

- **AC-AUTH-001-01:** Successful consent authorizes the intended account.
- **AC-AUTH-001-02:** cancelled or denied consent does not.
- **AC-AUTH-001-03:** missing or mismatched state is rejected.
- **AC-AUTH-001-04:** passwords are entered only at Google.

**Source:** S1 §8; S2 §6; accepted authorization discussion. **References:** STD-06, REF-01. **Phase:** 2; storage foundation in 1.

**Verification:** [VER-AUTH-001](verification-criteria.md#ver-auth-001) — not executed.

#### REQ-AUTH-002

**Requirement:** The application shall request only scopes justified by delivered enabled features.

**Acceptance criteria:**

- **AC-AUTH-002-01:** Initial reading requests no draft or sending scopes.
- **AC-AUTH-002-02:** each scope has a recorded purpose.
- **AC-AUTH-002-03:** denied permissions disable dependent features.
- **AC-AUTH-002-04:** scope expansion is reviewed.

**Source:** S1 §8; S2 §6; accepted authorization discussion. **References:** STD-06, REF-01. **Phase:** 2; storage foundation in 1.

**Verification:** [VER-AUTH-002](verification-criteria.md#ver-auth-002) — not executed.

#### REQ-AUTH-003

**Requirement:** The application shall verify the authorized Gmail account against configured account identity before mailbox processing.

**Acceptance criteria:**

- **AC-AUTH-003-01:** Matching identity permits processing.
- **AC-AUTH-003-02:** mismatched or unverified identity blocks it.
- **AC-AUTH-003-03:** account changes cannot silently reassign existing identities.

**Source:** S1 §8; S2 §6; accepted authorization discussion. **References:** STD-06, REF-01. **Phase:** 2; storage foundation in 1.

**Verification:** [VER-AUTH-003](verification-criteria.md#ver-auth-003) — not executed.

#### REQ-AUTH-004

**Requirement:** The application shall protect persisted OAuth credentials using Windows account access restrictions and the selected OS secret-protection mechanism.

**Acceptance criteria:**

- **AC-AUTH-004-01:** Tokens are encrypted at rest with user-scoped Windows DPAPI and protected by account-restricted file permissions.
- **AC-AUTH-004-02:** no machine-wide protection scope.
- **AC-AUTH-004-03:** missing, inaccessible, or undecryptable credentials fail explicitly.
- **AC-AUTH-004-04:** see DEC-15 in section 11.

**Source:** S1 §8; S2 §6; accepted authorization discussion. **References:** STD-04, REF-04. **Phase:** 1 storage mechanism; 2 OAuth persistence.

**Verification:** [VER-AUTH-004](verification-criteria.md#ver-auth-004) — not executed.

#### REQ-AUTH-005

**Requirement:** The application shall exclude OAuth secrets from diagnostics.

**Acceptance criteria:**

- **AC-AUTH-005-01:** Access and refresh tokens, authorization codes, PKCE verifiers, and secret-bearing responses are absent from captured normal and failure outputs.

**Source:** S1 §8; S2 §6; accepted authorization discussion. **References:** STD-04. **Phase:** 2; storage foundation in 1.

**Verification:** [VER-AUTH-005](verification-criteria.md#ver-auth-005) — not executed.

#### REQ-AUTH-006

**Requirement:** The application shall renew expired access tokens using valid refresh credentials when permitted.

**Acceptance criteria:**

- **AC-AUTH-006-01:** Successful renewal resumes within retry policy and securely persists returned updates.
- **AC-AUTH-006-02:** transient failure does not discard valid refresh credentials.
- **AC-AUTH-006-03:** failure cannot fabricate authorization.

**Source:** S1 §8; S2 §6; accepted authorization discussion. **References:** STD-06, REF-01. **Phase:** 2; storage foundation in 1.

**Verification:** [VER-AUTH-006](verification-criteria.md#ver-auth-006) — not executed.

#### REQ-AUTH-007

**Requirement:** The application shall block dependent Gmail operations after invalid, revoked, or nonrenewable authorization.

**Acceptance criteria:**

- **AC-AUTH-007-01:** Explicit reauthorization-required state is recorded.
- **AC-AUTH-007-02:** unattended runs do not repeatedly launch consent.
- **AC-AUTH-007-03:** pending local work survives reauthorization.

**Source:** S1 §8; S2 §6; accepted authorization discussion. **References:** STD-06, REF-01. **Phase:** 2; storage foundation in 1.

**Verification:** [VER-AUTH-007](verification-criteria.md#ver-auth-007) — not executed.

#### REQ-AUTH-008

**Requirement:** The application shall bound OAuth network operations and verify TLS certificates.

**Acceptance criteria:**

- **AC-AUTH-008-01:** Configured timeouts and retry limits terminate failures.
- **AC-AUTH-008-02:** denial and revoked credentials do not enter transient retry loops.
- **AC-AUTH-008-03:** invalid certificates are rejected.

**Source:** S1 §8; S2 §6; accepted authorization discussion. **References:** STD-06, REF-01. **Phase:** 2; storage foundation in 1.

**Verification:** [VER-AUTH-008](verification-criteria.md#ver-auth-008) — not executed.

### INT — Gmail intake and context

#### REQ-INT-001

**Requirement:** The application shall discover new mail only within the configured activation boundary and intake scope.

**Acceptance criteria:**

- **AC-INT-001-01:** Tests immediately before, at, and after the configured boundary follow DEC-02 semantics.
- **AC-INT-001-02:** selected-folder/label scope excludes unrelated messages.

**Source:** S2 §1,6,7,10. **References:** STD-07, REF-01. **Phase:** 2–3; full intake in 6.

**Verification:** [VER-INT-001](verification-criteria.md#ver-int-001) — not executed.

#### REQ-INT-002

**Requirement:** The application shall use a dedicated Gmail test label for the first working slice.

**Acceptance criteria:**

- **AC-INT-002-01:** Only eligible labeled test messages enter Phase 3.
- **AC-INT-002-02:** expansion beyond that label is explicit in Phase 6.

**Source:** S2 §1,6,7,10. **References:** STD-07, REF-01. **Phase:** 2–3; full intake in 6.

**Verification:** [VER-INT-002](verification-criteria.md#ver-int-002) — not executed.

#### REQ-INT-003

**Requirement:** The application shall make intake independent of read/unread status.

**Acceptance criteria:**

- **AC-INT-003-01:** Read and unread eligible messages are discovered.
- **AC-INT-003-02:** changing read state cannot create a second processing identity.

**Source:** S2 §1,6,7,10. **References:** STD-07, REF-01. **Phase:** 2–3; full intake in 6.

**Verification:** [VER-INT-003](verification-criteria.md#ver-int-003) — not executed.

#### REQ-INT-004

**Requirement:** The application shall preserve Gmail account, message, and thread identities.

**Acceptance criteria:**

- **AC-INT-004-01:** Retrieval, persisted processing state, proposals, and source links retain correct account context.
- **AC-INT-004-02:** thread identity alone never merges distinct business entities.

**Source:** S2 §1,6,7,10. **References:** STD-07, REF-01. **Phase:** 2–3; full intake in 6.

**Verification:** [VER-INT-004](verification-criteria.md#ver-int-004) — not executed.

#### REQ-INT-005

**Requirement:** The application shall traverse Gmail pagination without losing eligible messages.

**Acceptance criteria:**

- **AC-INT-005-01:** A multi-page mailbox is processed completely within per-run limits.
- **AC-INT-005-02:** interrupted traversal resumes or safely rescans without duplicates or omissions.

**Source:** S2 §1,6,7,10. **References:** STD-07, REF-01. **Phase:** 2–3; full intake in 6.

**Verification:** [VER-INT-005](verification-criteria.md#ver-int-005) — not executed.

#### REQ-INT-006

**Requirement:** The application shall persist discovery and processing progress durably.

**Acceptance criteria:**

- **AC-INT-006-01:** Crash before and after checkpoint persistence cannot permanently skip unfinished messages.
- **AC-INT-006-02:** replay is safe.

**Source:** S2 §1,6,7,10. **References:** STD-07, REF-01. **Phase:** 2–3; full intake in 6.

**Verification:** [VER-INT-006](verification-criteria.md#ver-int-006) — not executed.

#### REQ-INT-007

**Requirement:** The application shall decode message content safely without modifying messages during read-only verification.

**Acceptance criteria:**

- **AC-INT-007-01:** Representative multipart, charset, encoded-header, and malformed messages produce correct bounded content or explicit failure.
- **AC-INT-007-02:** read-only live check leaves source content and labels unchanged.

**Source:** S2 §1,6,7,10. **References:** STD-07, REF-01. **Phase:** 2–3; full intake in 6.

**Verification:** [VER-INT-007](verification-criteria.md#ver-int-007) — not executed.

#### REQ-INT-008

**Requirement:** The application shall keep historical context retrieval distinct from new-mail intake.

**Acceptance criteria:**

- **AC-INT-008-01:** Older messages may inform an eligible case through bounded investigation.
- **AC-INT-008-02:** retrieval alone creates no new processing obligation or independent write.

**Source:** S2 §1,6,7,10. **References:** STD-07, REF-01. **Phase:** 2–3; full intake in 6.

**Verification:** [VER-INT-008](verification-criteria.md#ver-int-008) — not executed.

#### REQ-INT-009

**Requirement:** The application shall support the manual Agent/Review label.

**Acceptance criteria:**

- **AC-INT-009-01:** Eligible manually labeled messages create or update review work without duplicate tasks.
- **AC-INT-009-02:** treatment of older labeled messages follows DEC-03.

**Source:** S2 §1,6,7,10. **References:** STD-07, REF-01. **Phase:** 6.

**Verification:** [VER-INT-009](verification-criteria.md#ver-int-009) — not executed.

#### REQ-INT-010

**Requirement:** The application shall recover intake after sleep, shutdown, or connectivity loss.

**Acceptance criteria:**

- **AC-INT-010-01:** Messages accumulated during downtime are processed under the activation boundary.
- **AC-INT-010-02:** read state does not affect catch-up.

**Source:** S2 §1,6,7,10. **References:** STD-07, REF-01. **Phase:** 3 bounded-label recovery; 6 full-scope catch-up.

**Verification:** [VER-INT-010](verification-criteria.md#ver-int-010) — not executed.

### AGT — Agent and model

#### REQ-AGT-001

**Requirement:** The application shall use LangChain with a local Ollama model, initially evaluating qwen3:8b.

**Acceptance criteria:**

- **AC-AGT-001-01:** Real invocation returns schema-validated results.
- **AC-AGT-001-02:** model is a candidate until evaluation passes.
- **AC-AGT-001-03:** unavailable Ollama produces explicit failure without simulated output.

**Source:** S1 §3,5,7,10; S2 §4,6–7. **References:** STD-05, REF-05. **Phase:** 2–7.

**Verification:** [VER-AGT-001](verification-criteria.md#ver-agt-001) — not executed.

#### REQ-AGT-002

**Requirement:** The application shall expose only allowlisted bounded investigation tools.

**Acceptance criteria:**

- **AC-AGT-002-01:** Agent has no send capability, unrestricted Gmail client, arbitrary HTTP, or shell.
- **AC-AGT-002-02:** forbidden calls fail without external effects.

**Source:** S1 §3,5,7,10; S2 §4,6–7. **References:** STD-05, REF-05. **Phase:** 2–7.

**Verification:** [VER-AGT-002](verification-criteria.md#ver-agt-002) — not executed.

#### REQ-AGT-003

**Requirement:** The application shall validate all model output against strict proposal schemas.

**Acceptance criteria:**

- **AC-AGT-003-01:** Malformed, extra-forbidden, unsupported-action, and invalid-reference output cannot reach execution.
- **AC-AGT-003-02:** safe failure or review is explicit.

**Source:** S1 §3,5,7,10; S2 §4,6–7. **References:** STD-05, REF-05. **Phase:** 2–7.

**Verification:** [VER-AGT-003](verification-criteria.md#ver-agt-003) — not executed.

#### REQ-AGT-004

**Requirement:** The application shall ground proposed facts and changes in retrievable evidence.

**Acceptance criteria:**

- **AC-AGT-004-01:** Unsupported references, invented dates, and unsupported claims are rejected or sent to review.
- **AC-AGT-004-02:** source evidence is retained for accepted facts.

**Source:** S1 §3,5,7,10; S2 §4,6–7. **References:** STD-05, REF-05. **Phase:** 2–7.

**Verification:** [VER-AGT-004](verification-criteria.md#ver-agt-004) — not executed.

#### REQ-AGT-005

**Requirement:** The application shall bound agent tool calls, execution time, retrieved messages, and context size.

**Acceptance criteria:**

- **AC-AGT-005-01:** At configured limits execution terminates explicitly without treating incomplete investigation as confident success.
- **AC-AGT-005-02:** values follow LIMIT-01 and EVAL-01.

**Source:** S1 §3,5,7,10; S2 §4,6–7. **References:** STD-05, REF-05. **Phase:** 2–7.

**Verification:** [VER-AGT-005](verification-criteria.md#ver-agt-005) — not executed.

#### REQ-AGT-006

**Requirement:** The application shall abstain or propose human review when consequential evidence is insufficient.

**Acceptance criteria:**

- **AC-AGT-006-01:** Ambiguous and missing-reference evaluation cases do not produce unverified consequential writes.

**Source:** S1 §3,5,7,10; S2 §4,6–7. **References:** STD-05, REF-05. **Phase:** 2–7.

**Verification:** [VER-AGT-006](verification-criteria.md#ver-agt-006) — not executed.

#### REQ-AGT-007

**Requirement:** The application shall evaluate model suitability before unattended model-driven business writes.

**Acceptance criteria:**

- **AC-AGT-007-01:** Pass the predeclared evaluation protocol EVAL-01.
- **AC-AGT-007-02:** metrics are calculated from frozen labels and serious errors separately.
- **AC-AGT-007-03:** no threshold is tuned after results.
- **AC-AGT-007-04:** failure blocks unattended model-driven business writes.

**Source:** S1 §3,5,7,10; S2 §4,6–7. **References:** STD-05, REF-05. **Phase:** 2–7.

**Verification:** [VER-AGT-007](verification-criteria.md#ver-agt-007) — not executed.

#### REQ-AGT-008

**Requirement:** The application shall record reproducibility identities for evaluations.

**Acceptance criteria:**

- **AC-AGT-008-01:** Report includes application, prompt, model settings, available artifact identity, dependency lock identity, evaluation-set version, and results.
- **AC-AGT-008-02:** unavailable identity is stated.

**Source:** S1 §3,5,7,10; S2 §4,6–7. **References:** STD-05, REF-05. **Phase:** 2–7.

**Verification:** [VER-AGT-008](verification-criteria.md#ver-agt-008) — not executed.

#### REQ-AGT-009

**Requirement:** The application shall treat retrieved instructions as evidence rather than application authority.

**Acceptance criteria:**

- **AC-AGT-009-01:** Hostile email requesting policy changes, sending, secret retrieval, or disallowed Jira content cannot authorize those actions regardless of model compliance.

**Source:** S1 §3,5,7,10; S2 §4,6–7. **References:** STD-05, REF-05. **Phase:** 2–7.

**Verification:** [VER-AGT-009](verification-criteria.md#ver-agt-009) — not executed.

### JIR — Jira integration

#### REQ-JIR-001

**Requirement:** The application shall verify Jira identity, project access, and required permissions before dependent writes.

**Acceptance criteria:**

- **AC-JIR-001-01:** Authentication, actual project restrictions, and permitted operations are checked against the selected edition.
- **AC-JIR-001-02:** unsupported restrictions block dependent use.

**Source:** S1 §5,8; S2 §4,6–8. **References:** STD-04, REF-02. **Phase:** 2–4.

**Verification:** [VER-JIR-001](verification-criteria.md#ver-jir-001) — not executed.

#### REQ-JIR-002

**Requirement:** The application shall support issue creation, retrieval, managed-field updates, comments, and links required by tracking and review.

**Acceptance criteria:**

- **AC-JIR-002-01:** Explicit live checks demonstrate each required operation on dedicated resources with confirmed external identities.

**Source:** S1 §5,8; S2 §4,6–8. **References:** STD-04, REF-02. **Phase:** 2–4.

**Verification:** [VER-JIR-002](verification-criteria.md#ver-jir-002) — not executed.

#### REQ-JIR-003

**Requirement:** The application shall restrict Jira writes to agreed application-managed fields and permitted email-derived content.

**Acceptance criteria:**

- **AC-JIR-003-01:** DEC-05 allowlist is enforced before every write.
- **AC-JIR-003-02:** unknown fields and sensitive content outside policy are rejected.
- **AC-JIR-003-03:** human-owned fields are preserved.

**Source:** S1 §5,8; S2 §4,6–8. **References:** STD-04, REF-02. **Phase:** 2–4.

**Verification:** [VER-JIR-003](verification-criteria.md#ver-jir-003) — not executed.

#### REQ-JIR-004

**Requirement:** The application shall attach durable correlation identities to application writes.

**Acceptance criteria:**

- **AC-JIR-004-01:** After timeout following accepted issue creation or comment creation, reconciliation locates the original operation rather than repeating it.
- **AC-JIR-004-02:** feasibility is demonstrated in Phase 2.

**Source:** S1 §5,8; S2 §4,6–8. **References:** STD-04, REF-02. **Phase:** 2–4.

**Verification:** [VER-JIR-004](verification-criteria.md#ver-jir-004) — not executed.

#### REQ-JIR-005

**Requirement:** The application shall verify the feasibility of human decisions independently from application activity.

**Acceptance criteria:**

- **AC-JIR-005-01:** Actual API evidence identifies actor, authorization, decision, and proposal version.
- **AC-JIR-005-02:** app-authored or unverifiable activity cannot count as human approval.

**Source:** S1 §5,8; S2 §4,6–8. **References:** STD-04, REF-02. **Phase:** 2–4.

**Verification:** [VER-JIR-005](verification-criteria.md#ver-jir-005) — not executed.

#### REQ-JIR-006

**Requirement:** The application shall handle provider rate limits and failures with explicit outcomes.

**Acceptance criteria:**

- **AC-JIR-006-01:** Retry guidance is honored within configured bounds.
- **AC-JIR-006-02:** permission and invalid-request failures are not blindly retried.
- **AC-JIR-006-03:** uncertain non-idempotent writes go to reconciliation.

**Source:** S1 §5,8; S2 §4,6–8. **References:** STD-04, REF-02. **Phase:** 2–4.

**Verification:** [VER-JIR-006](verification-criteria.md#ver-jir-006) — not executed.

#### REQ-JIR-007

**Requirement:** The application shall expose pending review, pending approval, deadlines, and failures through the Jira dashboard.

**Acceptance criteria:**

- **AC-JIR-007-01:** Configured views return representative records in each category and preserve project access restrictions.
- **AC-JIR-007-02:** no custom web dashboard is required.

**Source:** S1 §5,8; S2 §4,6–8. **References:** STD-04, REF-02. **Phase:** 2–4.

**Verification:** [VER-JIR-007](verification-criteria.md#ver-jir-007) — not executed.

### TRK — Matching and business lifecycle

#### REQ-TRK-001

**Requirement:** The application shall match entities using verified business references and account context.

**Acceptance criteria:**

- **AC-TRK-001-01:** Verified reference and account matches link correctly.
- **AC-TRK-001-02:** sender, subject, thread, or similarity alone cannot authorize a consequential merge.

**Source:** S1 §6; S2 §7–8. **References:** STD-02. **Phase:** 3–4.

**Verification:** [VER-TRK-001](verification-criteria.md#ver-trk-001) — not executed.

#### REQ-TRK-002

**Requirement:** The application shall keep distinct order and application references separate.

**Acceptance criteria:**

- **AC-TRK-002-01:** Repeat purchases and separate applications retain distinct entities even when sender, item, role, or thread matches.

**Source:** S1 §6; S2 §7–8. **References:** STD-02. **Phase:** 3–4.

**Verification:** [VER-TRK-002](verification-criteria.md#ver-trk-002) — not executed.

#### REQ-TRK-003

**Requirement:** The application shall associate shipment, return, and refund references only with supported links to their parent entities.

**Acceptance criteria:**

- **AC-TRK-003-01:** Explicit linked references associate correctly.
- **AC-TRK-003-02:** unsupported cross-links produce review without merging entities.

**Source:** S1 §6; S2 §7–8. **References:** STD-02. **Phase:** 3–4.

**Verification:** [VER-TRK-003](verification-criteria.md#ver-trk-003) — not executed.

#### REQ-TRK-004

**Requirement:** The application shall represent an established distinct replacement order as a linked entity.

**Acceptance criteria:**

- **AC-TRK-004-01:** Replacement with a distinct verified order reference retains its own identity and a traceable parent relationship.

**Source:** S1 §6; S2 §7–8. **References:** STD-02. **Phase:** 3–4.

**Verification:** [VER-TRK-004](verification-criteria.md#ver-trk-004) — not executed.

#### REQ-TRK-005

**Requirement:** The application shall record accepted business events with their evidence and event time separately from arrival time.

**Acceptance criteria:**

- **AC-TRK-005-01:** Late-arriving events preserve both times and source identity.
- **AC-TRK-005-02:** missing event time remains unknown rather than fabricated.

**Source:** S1 §6; S2 §7–8. **References:** STD-02. **Phase:** 3–4.

**Verification:** [VER-TRK-005](verification-criteria.md#ver-trk-005) — not executed.

#### REQ-TRK-006

**Requirement:** The application shall derive order progress from accepted confirmation, shipment, and delivery events.

**Acceptance criteria:**

- **AC-TRK-006-01:** Execute table ORD-01: confirmation, shipment, partial delivery, full delivery, and late-event rows produce the stated independent fulfillment outcome.
- **AC-TRK-006-02:** unknown/conflicting facts require review.

**Source:** S1 §6; S2 §7–8. **References:** STD-02. **Phase:** 3 confirmation/shipment subset in SLICE-01; 4 complete ORD-01.

**Verification:** [VER-TRK-006](verification-criteria.md#ver-trk-006) — not executed.

#### REQ-TRK-007

**Requirement:** The application shall represent returns and refunds without losing original fulfillment history.

**Acceptance criteria:**

- **AC-TRK-007-01:** Execute table ORD-01 return/refund rows.
- **AC-TRK-007-02:** return and refund dimensions retain fulfillment history.
- **AC-TRK-007-03:** requests alone cannot mark a refund completed.

**Source:** S1 §6; S2 §7–8. **References:** STD-02. **Phase:** 3–4.

**Verification:** [VER-TRK-007](verification-criteria.md#ver-trk-007) — not executed.

#### REQ-TRK-008

**Requirement:** The application shall represent partial deliveries and refunds without falsely marking the whole entity complete.

**Acceptance criteria:**

- **AC-TRK-008-01:** Table ORD-01 partial outcomes retain evidenced outstanding quantity/amount or unknown remainder.
- **AC-TRK-008-02:** a single delivered package or partial refund cannot complete an unverified whole order.

**Source:** S1 §6; S2 §7–8. **References:** STD-02. **Phase:** 3–4.

**Verification:** [VER-TRK-008](verification-criteria.md#ver-trk-008) — not executed.

#### REQ-TRK-009

**Requirement:** The application shall track application acknowledgment, progression, interviews, rejection, and offers.

**Acceptance criteria:**

- **AC-TRK-009-01:** Execute table APP-01.
- **AC-TRK-009-02:** offer, rejection, interview, and acknowledgement remain grounded in the same verified application.
- **AC-TRK-009-03:** contradictory terminal events require review.

**Source:** S1 §6; S2 §7–8. **References:** STD-02. **Phase:** 3–4.

**Verification:** [VER-TRK-009](verification-criteria.md#ver-trk-009) — not executed.

#### REQ-TRK-010

**Requirement:** The application shall handle interview scheduling and rescheduling using evidenced dates and times.

**Acceptance criteria:**

- **AC-TRK-010-01:** New confirmed schedule supersedes the prior schedule with history.
- **AC-TRK-010-02:** cancellation or ambiguity is explicit.
- **AC-TRK-010-03:** dates and deadlines are not invented.

**Source:** S1 §6; S2 §7–8. **References:** STD-02. **Phase:** 3–4.

**Verification:** [VER-TRK-010](verification-criteria.md#ver-trk-010) — not executed.

#### REQ-TRK-011

**Requirement:** The application shall prevent late notifications from incorrectly reversing established progress.

**Acceptance criteria:**

- **AC-TRK-011-01:** An older shipment after delivery and an older acknowledgment after interview do not regress state.
- **AC-TRK-011-02:** history still records accepted evidence.

**Source:** S1 §6; S2 §7–8. **References:** STD-02. **Phase:** 3–4.

**Verification:** [VER-TRK-011](verification-criteria.md#ver-trk-011) — not executed.

#### REQ-TRK-012

**Requirement:** The application shall allow legitimate new events to reopen tracking.

**Acceptance criteria:**

- **AC-TRK-012-01:** An evidenced return after delivery or authorized correction reopens relevant work according to DEC-09 without deleting completed history.

**Source:** S1 §6; S2 §7–8. **References:** STD-02. **Phase:** 3–4.

**Verification:** [VER-TRK-012](verification-criteria.md#ver-trk-012) — not executed.

#### REQ-TRK-013

**Requirement:** The application shall separate business progress, review, approval, and execution state.

**Acceptance criteria:**

- **AC-TRK-013-01:** An approval rejection does not imply job rejection.
- **AC-TRK-013-02:** technical failure does not change business stage.
- **AC-TRK-013-03:** state combinations follow the logical-state contract.

**Source:** S1 §6; S2 §7–8. **References:** STD-02. **Phase:** 3–4.

**Verification:** [VER-TRK-013](verification-criteria.md#ver-trk-013) — not executed.

### REV — Human review and corrections

#### REQ-REV-001

**Requirement:** The application shall create review work for important emails and consequential ambiguity.

**Acceptance criteria:**

- **AC-REV-001-01:** Missing references, conflicting matches, and agreed important-email cases produce a review task rather than unsupported business changes.
- **AC-REV-001-02:** criteria follow DEC-06.

**Source:** S2 §7–8. **References:** STD-02, STD-04, REF-02. **Phase:** 3–4.

**Verification:** [VER-REV-001](verification-criteria.md#ver-rev-001) — not executed.

#### REQ-REV-002

**Requirement:** The application shall include the reason, requested decision, source links, and evidenced deadline in review work.

**Acceptance criteria:**

- **AC-REV-002-01:** Reviewer can identify the uncertainty and requested action.
- **AC-REV-002-02:** absent deadlines are marked absent.
- **AC-REV-002-03:** no invented urgency appears.

**Source:** S2 §7–8. **References:** STD-02, STD-04, REF-02. **Phase:** 3–4.

**Verification:** [VER-REV-002](verification-criteria.md#ver-rev-002) — not executed.

#### REQ-REV-003

**Requirement:** The application shall group related follow-ups while preserving distinct obligations.

**Acceptance criteria:**

- **AC-REV-003-01:** Follow-ups for the same obligation update linked work.
- **AC-REV-003-02:** separate deadlines or decisions remain individually visible.

**Source:** S2 §7–8. **References:** STD-02, STD-04, REF-02. **Phase:** 3–4.

**Verification:** [VER-REV-003](verification-criteria.md#ver-rev-003) — not executed.

#### REQ-REV-004

**Requirement:** The application shall require explicit human acknowledgment or resolution of review work.

**Acceptance criteria:**

- **AC-REV-004-01:** Silence, elapsed time, app activity, and email instructions cannot resolve review.
- **AC-REV-004-02:** actor and decision are retained.

**Source:** S2 §7–8. **References:** STD-02, STD-04, REF-02. **Phase:** 3–4.

**Verification:** [VER-REV-004](verification-criteria.md#ver-rev-004) — not executed.

#### REQ-REV-005

**Requirement:** The application shall preserve human notes during automated updates.

**Acceptance criteria:**

- **AC-REV-005-01:** Updating managed fields or source evidence leaves reviewer-authored notes intact.

**Source:** S2 §7–8. **References:** STD-02, STD-04, REF-02. **Phase:** 3–4.

**Verification:** [VER-REV-005](verification-criteria.md#ver-rev-005) — not executed.

#### REQ-REV-006

**Requirement:** The application shall accept corrections only through an authorized, evidenced mechanism.

**Acceptance criteria:**

- **AC-REV-006-01:** Unauthorized or unverifiable corrections are blocked.
- **AC-REV-006-02:** authorized changes retain actor, reason, time, prior fact, and replacement fact.

**Source:** S2 §7–8. **References:** STD-02, STD-04, REF-02. **Phase:** 3–4.

**Verification:** [VER-REV-006](verification-criteria.md#ver-rev-006) — not executed.

#### REQ-REV-007

**Requirement:** The application shall recalculate affected business state and replay safely after corrections.

**Acceptance criteria:**

- **AC-REV-007-01:** Corrected matching or facts produce expected derived state without duplicating completed external actions or erasing execution history.

**Source:** S2 §7–8. **References:** STD-02, STD-04, REF-02. **Phase:** 3–4.

**Verification:** [VER-REV-007](verification-criteria.md#ver-rev-007) — not executed.

### APR — Drafts, approval, and sending

#### REQ-APR-001

**Requirement:** The application shall prepare reply proposals from verified evidence and validated recipients.

**Acceptance criteria:**

- **AC-APR-001-01:** Unsupported statements and recipient identities trigger review.
- **AC-APR-001-02:** From, To, CC, BCC, subject, body, and attachments are explicit before approval.

**Source:** S1 §7; S2 §6,9. **References:** STD-04, REF-01, REF-02. **Phase:** 5; feasibility in 2.

**Verification:** [VER-APR-001](verification-criteria.md#ver-apr-001) — not executed.

#### REQ-APR-002

**Requirement:** The application shall create Gmail drafts only through deterministic workflow code.

**Acceptance criteria:**

- **AC-APR-002-01:** Proposal validation precedes draft creation.
- **AC-APR-002-02:** draft identity and version are persisted.
- **AC-APR-002-03:** uncertain draft writes are represented and reconciled.

**Source:** S1 §7; S2 §6,9. **References:** STD-04, REF-01, REF-02. **Phase:** 5; feasibility in 2.

**Verification:** [VER-APR-002](verification-criteria.md#ver-apr-002) — not executed.

#### REQ-APR-003

**Requirement:** The application shall persist immutable approval snapshots with proposal versions and SHA-256 payload identities.

**Acceptance criteria:**

- **AC-APR-003-01:** Snapshot covers From, To, CC, BCC, subject, body, and attachment content identities.
- **AC-APR-003-02:** deterministic versioned serialization has test vectors under DEC-10.

**Source:** S1 §7; S2 §6,9. **References:** STD-04, STD-08, REF-01. **Phase:** 5; feasibility in 2.

**Verification:** [VER-APR-003](verification-criteria.md#ver-apr-003) — not executed.

#### REQ-APR-004

**Requirement:** The application shall create a reviewable approval task linked to the draft and exact proposal version.

**Acceptance criteria:**

- **AC-APR-004-01:** Reviewer can inspect the complete payload, attachment identities, source evidence, and requested decision before approval.

**Source:** S1 §7; S2 §6,9. **References:** STD-04, REF-01, REF-02. **Phase:** 5; feasibility in 2.

**Verification:** [VER-APR-004](verification-criteria.md#ver-apr-004) — not executed.

#### REQ-APR-005

**Requirement:** The application shall represent Pending, Approved, Changes Requested, and Rejected approval outcomes.

**Acceptance criteria:**

- **AC-APR-005-01:** Each decision has actor and version.
- **AC-APR-005-02:** silence is Pending.
- **AC-APR-005-03:** changes requested or rejection blocks execution.

**Source:** S1 §7; S2 §6,9. **References:** STD-04, REF-01, REF-02. **Phase:** 5; feasibility in 2.

**Verification:** [VER-APR-005](verification-criteria.md#ver-apr-005) — not executed.

#### REQ-APR-006

**Requirement:** The application shall verify reviewer identity and authority using provider evidence.

**Acceptance criteria:**

- **AC-APR-006-01:** Only an authorized human actor through the verified DEC-07 mechanism can approve.
- **AC-APR-006-02:** app-authored text, email assertions, and model output cannot approve.

**Source:** S1 §7; S2 §6,9. **References:** STD-04, REF-01, REF-02. **Phase:** 5; feasibility in 2.

**Verification:** [VER-APR-006](verification-criteria.md#ver-apr-006) — not executed.

#### REQ-APR-007

**Requirement:** The application shall invalidate approval when any protected payload component changes.

**Acceptance criteria:**

- **AC-APR-007-01:** Changing recipients, sender, subject, body, attachment membership, or attachment bytes blocks execution until fresh approval.
- **AC-APR-007-02:** same filename with different bytes is detected.

**Source:** S1 §7; S2 §6,9. **References:** STD-04, REF-01, REF-02. **Phase:** 5; feasibility in 2.

**Verification:** [VER-APR-007](verification-criteria.md#ver-apr-007) — not executed.

#### REQ-APR-008

**Requirement:** The application shall invalidate approval when defined material new information makes it no longer applicable.

**Acceptance criteria:**

- **AC-APR-008-01:** Table APR-01 invalidates approval on corrected relevant facts, changed schedule/deadline, contradicted recipient/action, or cancelled obligation.
- **AC-APR-008-02:** unrelated messages do not invalidate approval.

**Source:** S1 §7; S2 §6,9. **References:** STD-04, REF-01, REF-02. **Phase:** 5; feasibility in 2.

**Verification:** [VER-APR-008](verification-criteria.md#ver-apr-008) — not executed.

#### REQ-APR-009

**Requirement:** The application shall permit sending only through the guarded deterministic executor outside agent capabilities.

**Acceptance criteria:**

- **AC-APR-009-01:** Executor verifies reviewer, current version, payload integrity, relevance, prior execution, and send enablement.
- **AC-APR-009-02:** missing or uncertain checks block sending.

**Source:** S1 §7; S2 §6,9. **References:** STD-04, REF-01, REF-02. **Phase:** 5; feasibility in 2.

**Verification:** [VER-APR-009](verification-criteria.md#ver-apr-009) — not executed.

#### REQ-APR-010

**Requirement:** The application shall send only the payload whose exact version was approved.

**Acceptance criteria:**

- **AC-APR-010-01:** Execution evidence identifies the approved payload.
- **AC-APR-010-02:** edits to an editable Gmail draft cannot cause different content to be sent under old approval.
- **AC-APR-010-03:** no separate race workstream is required.

**Source:** S1 §7; S2 §6,9. **References:** STD-04, STD-07, REF-01. **Phase:** 5; feasibility in 2.

**Verification:** [VER-APR-010](verification-criteria.md#ver-apr-010) — not executed.

#### REQ-APR-011

**Requirement:** The application shall prevent concurrent or repeated sending of the same approved action.

**Acceptance criteria:**

- **AC-APR-011-01:** Concurrent requests and restart/replay cannot send a confirmed action again.
- **AC-APR-011-02:** uncertain actions remain blocked pending reconciliation.

**Source:** S1 §7; S2 §6,9. **References:** STD-04, REF-01, REF-02. **Phase:** 5; feasibility in 2.

**Verification:** [VER-APR-011](verification-criteria.md#ver-apr-011) — not executed.

#### REQ-APR-012

**Requirement:** The application shall record confirmed, failed, and uncertain sending results.

**Acceptance criteria:**

- **AC-APR-012-01:** A timeout after remote acceptance cannot be reported as confirmed failure or silently retried.
- **AC-APR-012-02:** provider evidence is retained for confirmed results.

**Source:** S1 §7; S2 §6,9. **References:** STD-04, REF-01, REF-02. **Phase:** 5; feasibility in 2.

**Verification:** [VER-APR-012](verification-criteria.md#ver-apr-012) — not executed.

#### REQ-APR-013

**Requirement:** The application shall reconcile uncertain sends before retrying.

**Acceptance criteria:**

- **AC-APR-013-01:** Located sent message is linked to the original action.
- **AC-APR-013-02:** unresolved uncertainty requires human review.
- **AC-APR-013-03:** absence of reliable evidence does not authorize blind retry.

**Source:** S1 §7; S2 §6,9. **References:** STD-04, REF-01, REF-02. **Phase:** 5; feasibility in 2.

**Verification:** [VER-APR-013](verification-criteria.md#ver-apr-013) — not executed.

#### REQ-APR-014

**Requirement:** The application shall keep live sending disabled until security acceptance passes and the user authorizes enablement.

**Acceptance criteria:**

- **AC-APR-014-01:** Forged and stale approval, changed fields and attachments, replay, concurrency, hostile input, and uncertain-send tests pass before explicit enablement is recorded.

**Source:** S1 §7; S2 §6,9. **References:** STD-04, REF-01, REF-02. **Phase:** 5; feasibility in 2.

**Verification:** [VER-APR-014](verification-criteria.md#ver-apr-014) — not executed.

### REC — Persistence and recovery

#### REQ-REC-001

**Requirement:** The application shall persist sufficient structured state for safe restart without copying the mailbox unnecessarily.

**Acceptance criteria:**

- **AC-REC-001-01:** Verified mappings, events, intended actions, approvals, execution records, and checkpoints survive restart.
- **AC-REC-001-02:** retained content follows policy.

**Source:** S1 §5,6,9; S2 §5–10. **References:** STD-02, REF-03. **Phase:** 1–7.

**Verification:** [VER-REC-001](verification-criteria.md#ver-rec-001) — not executed.

#### REQ-REC-002

**Requirement:** The application shall apply versioned SQLite migrations with required constraints enabled.

**Acceptance criteria:**

- **AC-REC-002-01:** Fresh creation and supported upgrades preserve data.
- **AC-REC-002-02:** foreign keys and uniqueness are verified.
- **AC-REC-002-03:** released migrations are not modified.

**Source:** S1 §5,6,9; S2 §5–10. **References:** REF-03. **Phase:** 1–7.

**Verification:** [VER-REC-002](verification-criteria.md#ver-rec-002) — not executed.

#### REQ-REC-003

**Requirement:** The application shall commit related local changes transactionally.

**Acceptance criteria:**

- **AC-REC-003-01:** Injected failure cannot leave half-accepted event/action state.
- **AC-REC-003-02:** no network request holds a long database transaction.

**Source:** S1 §5,6,9; S2 §5–10. **References:** STD-02, REF-03. **Phase:** 1–7.

**Verification:** [VER-REC-003](verification-criteria.md#ver-rec-003) — not executed.

#### REQ-REC-004

**Requirement:** The application shall enforce unique processing and action identities.

**Acceptance criteria:**

- **AC-REC-004-01:** Duplicate message discovery, event replay, and restart create no duplicate tracking issue or event comment.

**Source:** S1 §5,6,9; S2 §5–10. **References:** STD-02, REF-03. **Phase:** 1–7.

**Verification:** [VER-REC-004](verification-criteria.md#ver-rec-004) — not executed.

#### REQ-REC-005

**Requirement:** The application shall persist an intended external action before attempting its write.

**Acceptance criteria:**

- **AC-REC-005-01:** Crash before submission leaves recoverable intent.
- **AC-REC-005-02:** crash after remote acceptance enters reconciliation with the same correlation identity.

**Source:** S1 §5,6,9; S2 §5–10. **References:** STD-02, REF-03. **Phase:** 1–7.

**Verification:** [VER-REC-005](verification-criteria.md#ver-rec-005) — not executed.

#### REQ-REC-006

**Requirement:** The application shall distinguish confirmed success, known failure, and uncertain external outcomes.

**Acceptance criteria:**

- **AC-REC-006-01:** Network timeout after submission remains uncertain until evidence resolves it.
- **AC-REC-006-02:** no fabricated success or automatic reclassification to safe-to-retry.

**Source:** S1 §5,6,9; S2 §5–10. **References:** STD-02, REF-03. **Phase:** 1–7.

**Verification:** [VER-REC-006](verification-criteria.md#ver-rec-006) — not executed.

#### REQ-REC-007

**Requirement:** The application shall reconcile uncertain non-idempotent writes before repeating them.

**Acceptance criteria:**

- **AC-REC-007-01:** Injected interruptions after Jira issue and event-comment acceptance locate original writes.
- **AC-REC-007-02:** inconclusive lookup remains uncertain or goes to review.

**Source:** S1 §5,6,9; S2 §5–10. **References:** STD-02, REF-03. **Phase:** 1–7.

**Verification:** [VER-REC-007](verification-criteria.md#ver-rec-007) — not executed.

#### REQ-REC-008

**Requirement:** The application shall bound retries and preserve failure context without secrets.

**Acceptance criteria:**

- **AC-REC-008-01:** Transient, invalid-request, permission, and uncertain outcomes follow distinct policies.
- **AC-REC-008-02:** retry exhaustion exposes unfinished work.

**Source:** S1 §5,6,9; S2 §5–10. **References:** STD-02, REF-03. **Phase:** 1–7.

**Verification:** [VER-REC-008](verification-criteria.md#ver-rec-008) — not executed.

#### REQ-REC-009

**Requirement:** The migration process shall protect schema upgrades through backup and tested upgrade procedures.

**Acceptance criteria:**

- **AC-REC-009-01:** Back up before risky upgrades.
- **AC-REC-009-02:** an injected migration failure preserves recoverable data and reports failure.
- **AC-REC-009-03:** released migrations are immutable.
- **AC-REC-009-04:** destructive automatic rollback is not promised.

**Source:** S1 §5,6,9; S2 §5–10. **References:** STD-02, REF-03. **Phase:** 1; revalidated for each upgrade.

**Verification:** [VER-REC-009](verification-criteria.md#ver-rec-009) — not executed.

#### REQ-REC-010

**Requirement:** The application shall use timezone-aware instants and preserve date-only values.

**Acceptance criteria:**

- **AC-REC-010-01:** Instants store consistently in UTC.
- **AC-REC-010-02:** displays/schedules use Europe/Berlin.
- **AC-REC-010-03:** date-only evidence remains a date.
- **AC-REC-010-04:** unknown timezone is explicit.

**Source:** S1 §5,6,9; S2 §5–10. **References:** STD-02, REF-03. **Phase:** 1–7.

**Verification:** [VER-REC-010](verification-criteria.md#ver-rec-010) — not executed.

### DIG — Daily digest

#### REQ-DIG-001

**Requirement:** The application shall include every agreed digest category.

**Acceptance criteria:**

- **AC-DIG-001-01:** Digest covers important information/deadlines, pending reviews/approvals, order/application changes, newsletters/announcements, advertising, social activity, and processing failures.
- **AC-DIG-001-02:** zero-count categories are distinguishable from failed collection.

**Source:** S2 §10. **References:** STD-02. **Phase:** 6.

**Verification:** [VER-DIG-001](verification-criteria.md#ver-dig-001) — not executed.

#### REQ-DIG-002

**Requirement:** The application shall produce bounded factual summaries with counts and source links.

**Acceptance criteria:**

- **AC-DIG-002-01:** Summary claims and deadlines trace to evidence.
- **AC-DIG-002-02:** counts reconcile to the defined DEC-12 window and category rules.
- **AC-DIG-002-03:** unsupported claims are excluded or flagged.

**Source:** S2 §10. **References:** STD-02. **Phase:** 6.

**Verification:** [VER-DIG-002](verification-criteria.md#ver-dig-002) — not executed.

#### REQ-DIG-003

**Requirement:** The application shall carry unresolved human work across daily windows.

**Acceptance criteria:**

- **AC-DIG-003-01:** Unresolved reviews and approvals remain visible on later days until explicitly resolved.
- **AC-DIG-003-02:** older unresolved deadlines remain identifiable.

**Source:** S2 §10. **References:** STD-02. **Phase:** 6.

**Verification:** [VER-DIG-003](verification-criteria.md#ver-dig-003) — not executed.

#### REQ-DIG-004

**Requirement:** The application shall save digests locally with persistent window and outcome identities.

**Acceptance criteria:**

- **AC-DIG-004-01:** Restart and missed-run handling do not accidentally duplicate an already completed digest.
- **AC-DIG-004-02:** incomplete reports are not reported as complete.

**Source:** S2 §10. **References:** STD-02. **Phase:** 6.

**Verification:** [VER-DIG-004](verification-criteria.md#ver-dig-004) — not executed.

#### REQ-DIG-005

**Requirement:** The application shall expose partial collection or processing failures in the digest.

**Acceptance criteria:**

- **AC-DIG-005-01:** Unavailable services cannot produce a misleading all-clear report.
- **AC-DIG-005-02:** known failures and omitted data are explicit.

**Source:** S2 §10. **References:** STD-02. **Phase:** 6.

**Verification:** [VER-DIG-005](verification-criteria.md#ver-dig-005) — not executed.

### OPS — Windows operation and maintenance

#### REQ-OPS-001

**Requirement:** The application shall start through documented Windows Task Scheduler configuration and scripts/start.ps1.

**Acceptance criteria:**

- **AC-OPS-001-01:** Clean target-account setup starts the correct locked environment, uses account runtime paths, and reports failures without embedded credentials.

**Source:** S1 §8,9,13; S2 §10. **References:** STD-02, REF-04. **Phase:** 6.

**Verification:** [VER-OPS-001](verification-criteria.md#ver-ops-001) — not executed.

#### REQ-OPS-002

**Requirement:** The application shall schedule daily operation in Europe/Berlin with explicit daylight-saving and missed-run policies.

**Acceptance criteria:**

- **AC-OPS-002-01:** Spring gap, autumn overlap, sleep across scheduled time, and multiple missed days follow DEC-12 without accidental repeated windows.

**Source:** S1 §8,9,13; S2 §10. **References:** STD-02, REF-04. **Phase:** 6.

**Verification:** [VER-OPS-002](verification-criteria.md#ver-ops-002) — not executed.

#### REQ-OPS-003

**Requirement:** The application shall provide Windows notifications for agreed actionable outcomes.

**Acceptance criteria:**

- **AC-OPS-003-01:** DEC-13 scenarios notify the correct user without exposing unnecessary private content.
- **AC-OPS-003-02:** notification failure is visible and does not discard work.

**Source:** S1 §8,9,13; S2 §10. **References:** STD-02, REF-04. **Phase:** 6.

**Verification:** [VER-OPS-003](verification-criteria.md#ver-ops-003) — not executed.

#### REQ-OPS-004

**Requirement:** The application shall create consistent SQLite backups with a documented retention policy.

**Acceptance criteria:**

- **AC-OPS-004-01:** Backup during permitted operation restores to a valid database.
- **AC-OPS-004-02:** schedule, location, retention, and protection follow DEC-14.

**Source:** S1 §8,9,13; S2 §10. **References:** REF-03, REF-04. **Phase:** 6.

**Verification:** [VER-OPS-004](verification-criteria.md#ver-ops-004) — not executed.

#### REQ-OPS-005

**Requirement:** The application shall restore into a clean runtime environment with credentials handled separately.

**Acceptance criteria:**

- **AC-OPS-005-01:** Demonstration restores structured work and safely reconciles external effects.
- **AC-OPS-005-02:** unavailable account-bound credentials require documented reauthorization.

**Source:** S1 §8,9,13; S2 §10. **References:** STD-02, REF-04. **Phase:** 6.

**Verification:** [VER-OPS-005](verification-criteria.md#ver-ops-005) — not executed.

#### REQ-OPS-006

**Requirement:** The application shall apply agreed retention and deletion rules without destroying required pending-work evidence.

**Acceptance criteria:**

- **AC-OPS-006-01:** Expired records are removed under DEC-14.
- **AC-OPS-006-02:** pending approvals, uncertain actions, and required correction evidence remain protected until policy permits deletion.

**Source:** S1 §8,9,13; S2 §10. **References:** STD-02, REF-04. **Phase:** 6.

**Verification:** [VER-OPS-006](verification-criteria.md#ver-ops-006) — not executed.

#### REQ-OPS-007

**Requirement:** The application shall provide operational instructions for installation, upgrade, backup, restore, and incident recovery.

**Acceptance criteria:**

- **AC-OPS-007-01:** A clean-environment walkthrough succeeds.
- **AC-OPS-007-02:** steps cover stopping processing, disabling sending, rotating exposed credentials, and reviewing uncertain operations.

**Source:** S1 §8,9,13; S2 §10. **References:** STD-02, REF-04. **Phase:** 6.

**Verification:** [VER-OPS-007](verification-criteria.md#ver-ops-007) — not executed.

### SEC — Cross-cutting cybersecurity

#### REQ-SEC-001

**Requirement:** The application shall maintain a threat model covering protected assets, untrusted inputs, trust boundaries, and relevant abuse.

**Acceptance criteria:**

- **AC-SEC-001-01:** Model covers credentials, private content, business facts, human decisions, and execution history.
- **AC-SEC-001-02:** each material threat has a mitigation and verification link.

**Source:** S1 §5,7–10; S2 §4,6,9,11. **References:** STD-04. **Phase:** 0–7.

**Verification:** [VER-SEC-001](verification-criteria.md#ver-sec-001) — not executed.

#### REQ-SEC-002

**Requirement:** The application shall validate external and persisted data at trust boundaries.

**Acceptance criteria:**

- **AC-SEC-002-01:** Malformed configuration, API responses, database values, tool arguments, and model output fail explicitly without unauthorized effects.

**Source:** S1 §5,7–10; S2 §4,6,9,11. **References:** STD-04. **Phase:** 0–7.

**Verification:** [VER-SEC-002](verification-criteria.md#ver-sec-002) — not executed.

#### REQ-SEC-003

**Requirement:** The application shall prevent untrusted content from granting authority.

**Acceptance criteria:**

- **AC-SEC-003-01:** Direct and indirect prompt-injection cases cannot change policy, enable sending, approve actions, or bypass field restrictions.

**Source:** S1 §5,7–10; S2 §4,6,9,11. **References:** STD-04, STD-05. **Phase:** 0–7.

**Verification:** [VER-SEC-003](verification-criteria.md#ver-sec-003) — not executed.

#### REQ-SEC-004

**Requirement:** The application shall prevent disclosure to unauthorized destinations.

**Acceptance criteria:**

- **AC-SEC-004-01:** Agent cannot choose arbitrary network destinations.
- **AC-SEC-004-02:** Jira field allowlist and recipient approval checks reject exfiltration attempts through permitted tools.

**Source:** S1 §5,7–10; S2 §4,6,9,11. **References:** STD-04, STD-05. **Phase:** 0–7.

**Verification:** [VER-SEC-004](verification-criteria.md#ver-sec-004) — not executed.

#### REQ-SEC-005

**Requirement:** The application shall verify TLS and intended destinations for remote Gmail and Jira communications.

**Acceptance criteria:**

- **AC-SEC-005-01:** Invalid certificates and destinations are rejected.
- **AC-SEC-005-02:** tokens are not in URLs or logs.
- **AC-SEC-005-03:** loopback OAuth redirects and local Ollama may use HTTP only on loopback, never an untrusted remote interface.

**Source:** S1 §5,7–10; S2 §4,6,9,11. **References:** STD-04, STD-06, REF-01, REF-02. **Phase:** 0–7.

**Verification:** [VER-SEC-005](verification-criteria.md#ver-sec-005) — not executed.

#### REQ-SEC-006

**Requirement:** The application shall use parameterized SQL for variable data.

**Acceptance criteria:**

- **AC-SEC-006-01:** Injection strings supplied as values cannot alter query structure, retrieve unrelated rows, or execute additional statements.
- **AC-SEC-006-02:** permitted dynamic identifiers come only from fixed allowlists.

**Source:** S1 §5,7–10; S2 §4,6,9,11. **References:** STD-04, REF-03. **Phase:** 0–7.

**Verification:** [VER-SEC-006](verification-criteria.md#ver-sec-006) — not executed.

#### REQ-SEC-007

**Requirement:** The application shall constrain paths, filenames, and attachment handling.

**Acceptance criteria:**

- **AC-SEC-007-01:** Traversal, invalid filenames, oversized inputs, and malformed attachments fail safely without writing outside permitted locations.

**Source:** S1 §5,7–10; S2 §4,6,9,11. **References:** STD-04. **Phase:** 0–7.

**Verification:** [VER-SEC-007](verification-criteria.md#ver-sec-007) — not executed.

#### REQ-SEC-008

**Requirement:** The application shall render untrusted content safely and avoid unsolicited remote-content retrieval.

**Acceptance criteria:**

- **AC-SEC-008-01:** Malicious HTML/markup cannot execute in generated views or trigger unintended network requests.
- **AC-SEC-008-02:** output is encoded for its destination.

**Source:** S1 §5,7–10; S2 §4,6,9,11. **References:** STD-04. **Phase:** 0–7.

**Verification:** [VER-SEC-008](verification-criteria.md#ver-sec-008) — not executed.

#### REQ-SEC-009

**Requirement:** The application shall bound resource use and degrade explicitly under limits.

**Acceptance criteria:**

- **AC-SEC-009-01:** Oversized input, tool loops, service failure, and excessive retries terminate within agreed DEC-08 limits and preserve recoverable state.

**Source:** S1 §5,7–10; S2 §4,6,9,11. **References:** STD-04, STD-05. **Phase:** 0–7.

**Verification:** [VER-SEC-009](verification-criteria.md#ver-sec-009) — not executed.

#### REQ-SEC-010

**Requirement:** The application shall protect credentials and private operational artifacts from repository and diagnostic disclosure.

**Acceptance criteria:**

- **AC-SEC-010-01:** Secret scan and synthetic private-content tests cover code, fixtures, package metadata, logs, reports, and example configuration.
- **AC-SEC-010-02:** exposures trigger revocation/rotation procedures.

**Source:** S1 §5,7–10; S2 §4,6,9,11. **References:** STD-04. **Phase:** 0–7.

**Verification:** [VER-SEC-010](verification-criteria.md#ver-sec-010) — not executed.

#### REQ-SEC-011

**Requirement:** The application shall review dependency and model changes before accepted installation updates.

**Acceptance criteria:**

- **AC-SEC-011-01:** Locked dependency and recorded model changes receive relevant tests and security review.
- **AC-SEC-011-02:** no unverified automatic updates.

**Source:** S1 §5,7–10; S2 §4,6,9,11. **References:** STD-04. **Phase:** 0–7.

**Verification:** [VER-SEC-011](verification-criteria.md#ver-sec-011) — not executed.

#### REQ-SEC-012

**Requirement:** The application shall test security only against the application and authorized dedicated resources.

**Acceptance criteria:**

- **AC-SEC-012-01:** Test scope records permitted accounts/projects.
- **AC-SEC-012-02:** adversarial scenarios cannot target unrelated mailboxes, users, or third-party systems.

**Source:** S1 §5,7–10; S2 §4,6,9,11. **References:** STD-04. **Phase:** 0–7.

**Verification:** [VER-SEC-012](verification-criteria.md#ver-sec-012) — not executed.

### ENG — Development and delivery constraints

#### REQ-ENG-001

**Requirement:** The development process shall target Python 3.12 consistently in configuration, development, and CI.

**Acceptance criteria:**

- **AC-ENG-001-01:** requires-python is >=3.12,<3.13.
- **AC-ENG-001-02:** supported installs and CI use 3.12.
- **AC-ENG-001-03:** introduced dependencies are compatible.

**Source:** S1 §2–4,10–15; S3. **References:** REF-03, REF-05. **Phase:** 1–7.

**Verification:** [VER-ENG-001](verification-criteria.md#ver-eng-001) — not executed.

#### REQ-ENG-002

**Requirement:** The development process shall manage dependencies with uv, pyproject.toml, and a committed uv.lock.

**Acceptance criteria:**

- **AC-ENG-002-01:** Clean locked installation succeeds.
- **AC-ENG-002-02:** runtime and development dependencies are separated.
- **AC-ENG-002-03:** additions solve a present need and contain no secret-bearing URLs.

**Source:** S1 §2–4,10–15; S3. **References:** STD-03, REF-05. **Phase:** 1–7.

**Verification:** [VER-ENG-002](verification-criteria.md#ver-eng-002) — not executed.

#### REQ-ENG-003

**Requirement:** The development process shall enforce readable typed production code using Ruff and mypy.

**Acceptance criteria:**

- **AC-ENG-003-01:** Formatting, lint, and type checks pass.
- **AC-ENG-003-02:** functions have meaningful annotations.
- **AC-ENG-003-03:** unrestricted Any exceptions are justified.
- **AC-ENG-003-04:** public behavior is documented.

**Source:** S1 §2–4,10–15; S3. **References:** STD-09, REF-05. **Phase:** 1–7.

**Verification:** [VER-ENG-003](verification-criteria.md#ver-eng-003) — not executed.

#### REQ-ENG-004

**Requirement:** The development process shall avoid hidden side effects and misleading failure handling.

**Acceptance criteria:**

- **AC-ENG-004-01:** Imports perform no network calls or database writes.
- **AC-ENG-004-02:** specific exceptions preserve sanitized causes.
- **AC-ENG-004-03:** no broad swallowed failures or mutable-default defects.

**Source:** S1 §2–4,10–15; S3. **References:** STD-03, REF-05. **Phase:** 1–7.

**Verification:** [VER-ENG-004](verification-criteria.md#ver-eng-004) — not executed.

#### REQ-ENG-005

**Requirement:** The development process shall exclude unfinished and simulated production behavior.

**Acceptance criteria:**

- **AC-ENG-005-01:** Review finds no required behavior replaced by TODO, pass, ellipsis, NotImplementedError, fake responses, silent no-ops, or fallback simulations.
- **AC-ENG-005-02:** mocks remain in tests/evaluation tooling.

**Source:** S1 §2–4,10–15; S3. **References:** STD-03, REF-05. **Phase:** 1–7.

**Verification:** [VER-ENG-005](verification-criteria.md#ver-eng-005) — not executed.

#### REQ-ENG-006

**Requirement:** The development process shall use focused Git branches, reviewed diffs, and coherent commits while keeping main releasable.

**Acceptance criteria:**

- **AC-ENG-006-01:** Diff and checks are reviewed before merge.
- **AC-ENG-006-02:** remote PRs are used where available.
- **AC-ENG-006-03:** shared history is not rewritten without authorization.
- **AC-ENG-006-04:** no private runtime files are committed.

**Source:** S1 §2–4,10–15; S3. **References:** STD-03, REF-05. **Phase:** 1–7.

**Verification:** [VER-ENG-006](verification-criteria.md#ver-eng-006) — not executed.

#### REQ-ENG-007

**Requirement:** The development process shall obtain human review for security-sensitive changes.

**Acceptance criteria:**

- **AC-ENG-007-01:** Approval/sending, credentials, and migrations have recorded human review before acceptance.
- **AC-ENG-007-02:** automated checks do not substitute for that review.

**Source:** S1 §2–4,10–15; S3. **References:** STD-03, REF-05. **Phase:** 1–7.

**Verification:** [VER-ENG-007](verification-criteria.md#ver-eng-007) — not executed.

#### REQ-ENG-008

**Requirement:** The development process shall automate essential checks for pull requests and release candidates.

**Acceptance criteria:**

- **AC-ENG-008-01:** Locked install, Ruff format/lint, mypy, offline tests and coverage, secret scan, vulnerability check, and package build execute without production credentials.
- **AC-ENG-008-02:** Windows-specific behavior is tested on Windows.

**Source:** S1 §2–4,10–15; S3. **References:** STD-03, REF-05. **Phase:** 1–7.

**Verification:** [VER-ENG-008](verification-criteria.md#ver-eng-008) — not executed.

#### REQ-ENG-009

**Requirement:** The development process shall use one authoritative application version and deliberate releases.

**Acceptance criteria:**

- **AC-ENG-009-01:** Version follows agreed 0.x semantic progression and PEP 440.
- **AC-ENG-009-02:** changelog records user-visible changes and migration actions.
- **AC-ENG-009-03:** accepted releases are tagged.

**Source:** S1 §2–4,10–15; S3. **References:** STD-10. **Phase:** 1–7.

**Verification:** [VER-ENG-009](verification-criteria.md#ver-eng-009) — not executed.

#### REQ-ENG-010

**Requirement:** The development process shall maintain proportional project documentation alongside behavior.

**Acceptance criteria:**

- **AC-ENG-010-01:** README, AGENTS, SECURITY, requirements, architecture, test strategy, threat model, security tests, runbook, and changelog match delivered behavior.
- **AC-ENG-010-02:** SKILL.md appears only for an established reusable workflow.

**Source:** S1 §2–4,10–15; S3. **References:** STD-03, REF-05. **Phase:** 1–7.

**Verification:** [VER-ENG-010](verification-criteria.md#ver-eng-010) — not executed.

#### REQ-ENG-011

**Requirement:** The development process shall report delivery evidence honestly.

**Acceptance criteria:**

- **AC-ENG-011-01:** Each delivery identifies requirement/acceptance coverage, actual checks, limitations, and next phase step.
- **AC-ENG-011-02:** implemented, offline-tested, live-verified, and user-accepted states are distinct.

**Source:** S1 §2–4,10–15; S3. **References:** STD-03, REF-05. **Phase:** 1–7.

**Verification:** [VER-ENG-011](verification-criteria.md#ver-eng-011) — not executed.

### VAL — Verification and acceptance

#### REQ-VAL-001

**Requirement:** The verification process shall keep default pytest tests offline and deterministic.

**Acceptance criteria:**

- **AC-VAL-001-01:** No production credentials or model/API network calls are required.
- **AC-VAL-001-02:** synthetic fixtures and temporary real SQLite databases are used.
- **AC-VAL-001-03:** external boundaries rather than internal methods are mocked.

**Source:** S1 §10,12,13; S2 §6–11. **References:** STD-01, STD-03. **Phase:** 1–7.

**Verification:** [VER-VAL-001](verification-criteria.md#ver-val-001) — not executed.

#### REQ-VAL-002

**Requirement:** The verification process shall measure critical deterministic policies separately from other deterministic code.

**Acceptance criteria:**

- **AC-VAL-002-01:** Critical targets: 100% statements and branches.
- **AC-VAL-002-02:** other targets: 90% statements and 85% branches.
- **AC-VAL-002-03:** justified exclusions and any shortfall are visible and require resolution before acceptance.

**Source:** S1 §10,12,13; S2 §6–11. **References:** STD-01, STD-03. **Phase:** 1–7.

**Verification:** [VER-VAL-002](verification-criteria.md#ver-val-002) — not executed.

#### REQ-VAL-003

**Requirement:** The verification process shall maintain requirement-to-verification traceability.

**Acceptance criteria:**

- **AC-VAL-003-01:** Every requirement maps to planned evidence and later concrete test/report IDs.
- **AC-VAL-003-02:** critical recovery and security scenarios have named evidence.
- **AC-VAL-003-03:** documentation mapping is not reported as executed tests.

**Source:** S1 §10,12,13; S2 §6–11. **References:** STD-01, STD-03. **Phase:** 1–7.

**Verification:** [VER-VAL-003](verification-criteria.md#ver-val-003) — not executed.

#### REQ-VAL-004

**Requirement:** The verification process shall run live integration checks and model evaluations only when explicitly enabled.

**Acceptance criteria:**

- **AC-VAL-004-01:** Separate reports identify resource scope, identities, outcomes, and limitations.
- **AC-VAL-004-02:** mocked results cannot be represented as live proof.

**Source:** S1 §10,12,13; S2 §6–11. **References:** STD-01, STD-03. **Phase:** 1–7.

**Verification:** [VER-VAL-004](verification-criteria.md#ver-val-004) — not executed.

#### REQ-VAL-005

**Requirement:** The verification process shall exercise the complete first real-email-to-Jira slice.

**Acceptance criteria:**

- **AC-VAL-005-01:** Execute the Phase 3 slice in table SLICE-01: a verified order confirmation creates tracking, a follow-up updates it, ambiguity creates review, duplicate/restart replay adds nothing, and accepted issue/comment timeouts reconcile without duplicate writes.
- **AC-VAL-005-02:** sending unavailable.

**Source:** S1 §10,12,13; S2 §6–11. **References:** STD-01, STD-03. **Phase:** 3.

**Verification:** [VER-VAL-005](verification-criteria.md#ver-val-005) — not executed.

#### REQ-VAL-006

**Requirement:** The verification process shall perform authorized adversarial tests and add regressions for discovered defects.

**Acceptance criteria:**

- **AC-VAL-006-01:** Prompt injection, approval bypass/replay, exfiltration, SQL/command injection, traversal, unsafe rendering, exhaustion, leakage, and recovery abuse have recorded results and reviewed findings.

**Source:** S1 §10,12,13; S2 §6–11. **References:** STD-01, STD-03. **Phase:** 1–7.

**Verification:** [VER-VAL-006](verification-criteria.md#ver-val-006) — not executed.

#### REQ-VAL-007

**Requirement:** The verification process shall measure latency, throughput, memory use, and execution bounds.

**Acceptance criteria:**

- **AC-VAL-007-01:** Representative workload measurements are compared with DEC-08 limits.
- **AC-VAL-007-02:** no invented performance claim or unmeasured threshold is accepted.

**Source:** S1 §10,12,13; S2 §6–11. **References:** STD-01, STD-03. **Phase:** 1–7.

**Verification:** [VER-VAL-007](verification-criteria.md#ver-val-007) — not executed.

#### REQ-VAL-008

**Requirement:** The verification process shall require system evidence and user acceptance before release.

**Acceptance criteria:**

- **AC-VAL-008-01:** Offline unit/integration/system/acceptance checks, live checks, model results, security findings, and human workflow walkthrough are reviewed.
- **AC-VAL-008-02:** release-blocking defects resolved and limitations recorded before user acceptance/tagging.

**Source:** S1 §10,12,13; S2 §6–11. **References:** STD-01, STD-03. **Phase:** 1–7.

**Verification:** [VER-VAL-008](verification-criteria.md#ver-val-008) — not executed.

### MIG — Deferred LangGraph migration

#### REQ-MIG-001

**Requirement:** The migration process shall preserve the accepted LangChain release as the migration baseline.

**Acceptance criteria:**

- **AC-MIG-001-01:** No migration starts before complete LangChain acceptance.
- **AC-MIG-001-02:** accepted source, dependencies, prompts, data format, and tests remain recoverable.

**Source:** S2 §12. **References:** STD-02, REF-05. **Phase:** 8 only.

**Verification:** [VER-MIG-001](verification-criteria.md#ver-mig-001) — not executed.

#### REQ-MIG-002

**Requirement:** The migration process shall preserve domain rules, data ownership, and approval authority during orchestration migration.

**Acceptance criteria:**

- **AC-MIG-002-01:** Existing acceptance tests and live/security/model/recovery checks establish behavioral equivalence.
- **AC-MIG-002-02:** compatibility and rollback plan is reviewed.

**Source:** S2 §12. **References:** STD-02, REF-05. **Phase:** 8 only.

**Verification:** [VER-MIG-002](verification-criteria.md#ver-mig-002) — not executed.

#### REQ-MIG-003

**Requirement:** The migration process shall obtain separate acceptance for the LangGraph release.

**Acceptance criteria:**

- **AC-MIG-003-01:** Functional/resource comparison and migration limitations are reviewed before separate user acceptance and release.
- **AC-MIG-003-02:** optional tracing requires demonstrated need.

**Source:** S2 §12. **References:** STD-02, REF-05. **Phase:** 8 only.

**Verification:** [VER-MIG-003](verification-criteria.md#ver-mig-003) — not executed.


### Additional obligations from review

#### REQ-REC-011

**Requirement:** The application shall prevent concurrent execution of the same external action across all action types.

**Acceptance criteria:**

- **AC-REC-011-01:** Two workers racing to claim one Jira create/update/comment, draft-create, or send action result in at most one active submission.
- **AC-REC-011-02:** confirmed actions cannot be reclaimed.
- **AC-REC-011-03:** abandoned in-progress actions enter reconciliation, not blind resubmission.

**Source:** S1 §6; S2 §7,9. **References:** STD-04, REF-03. **Phase:** 1 execution foundation; 3 Jira; 5 drafts/sends.

**Verification:** [VER-REC-011](verification-criteria.md#ver-rec-011) — not executed.

#### REQ-REC-012

**Requirement:** The application shall reconcile external effects before resuming execution from a restored backup.

**Acceptance criteria:**

- **AC-REC-012-01:** Restore a snapshot older than a confirmed issue/comment/draft/send.
- **AC-REC-012-02:** no previously completed action is repeated without definitive reconciliation.
- **AC-REC-012-03:** inconclusive evidence blocks that action and creates review.

**Source:** S1 §9; S2 §10. **References:** STD-02, REF-03. **Phase:** 6.

**Verification:** [VER-REC-012](verification-criteria.md#ver-rec-012) — not executed.

#### REQ-FND-007

**Requirement:** The local runner shall coordinate intake, human-decision discovery, pending-action recovery, and due digests.

**Acceptance criteria:**

- **AC-FND-007-01:** Each enabled activity runs under section 11 intervals.
- **AC-FND-007-02:** one malformed message cannot indefinitely starve decision checking.
- **AC-FND-007-03:** restart discovers decisions made while offline and resumes only validated work.
- **AC-FND-007-04:** missing scopes disable dependent activities explicitly.

**Source:** S2 §2,7–10. **References:** STD-02. **Phase:** 1 runner lifecycle; 3 intake/recovery; 4 review; 5 approval; 6 digest.

**Verification:** [VER-FND-007](verification-criteria.md#ver-fnd-007) — not executed.

#### REQ-SEC-013

**Requirement:** The application shall never execute email bodies or attachments as code or commands.

**Acceptance criteria:**

- **AC-SEC-013-01:** Shell metacharacters, scripts, executable attachments, and instructions remain data.
- **AC-SEC-013-02:** no production handler invokes their contents.
- **AC-SEC-013-03:** extraction beyond supported limits stops explicitly.

**Source:** S1 §8; S2 §11. **References:** STD-04, STD-05. **Phase:** 2–7.

**Verification:** [VER-SEC-013](verification-criteria.md#ver-sec-013) — not executed.

#### REQ-SEC-014

**Requirement:** The application shall restrict local application services to loopback interfaces.

**Acceptance criteria:**

- **AC-SEC-014-01:** No application-created OAuth callback or Ollama integration requires LAN exposure.
- **AC-SEC-014-02:** remote endpoint configuration is rejected in this local-only scope.
- **AC-SEC-014-03:** runtime credentials are not exposed through local diagnostic endpoints.

**Source:** S1 §8. **References:** STD-04, REF-01, REF-05. **Phase:** 2–7.

**Verification:** [VER-SEC-014](verification-criteria.md#ver-sec-014) — not executed.

#### REQ-ENG-012

**Requirement:** The development process shall use explicit resource ownership and readable Python constructs.

**Acceptance criteria:**

- **AC-ENG-012-01:** Review verifies context managers for managed files/transactions/resources, no wildcard imports or hidden mutable global state, composition over unnecessary inheritance, and comments explaining intent without redundant narration.
- **AC-ENG-012-02:** no arbitrary function-size rules.

**Source:** S1 §4. **References:** STD-09. **Phase:** 1–7.

**Verification:** [VER-ENG-012](verification-criteria.md#ver-eng-012) — not executed.

#### REQ-ENG-013

**Requirement:** The development process shall inspect relevant existing code, tests, documentation, and AGENTS.md before changes.

**Acceptance criteria:**

- **AC-ENG-013-01:** Each task identifies its requirement and relevant existing artifacts.
- **AC-ENG-013-02:** edits remain focused.
- **AC-ENG-013-03:** focused checks precede applicable broader checks.
- **AC-ENG-013-04:** diff, recovery/security impact, and affected documentation are reviewed before delivery.

**Source:** S1 §1,11,15. **References:** STD-03. **Phase:** 0–7.

**Verification:** [VER-ENG-013](verification-criteria.md#ver-eng-013) — not executed.

#### REQ-VAL-009

**Requirement:** The verification process shall test observable domain behavior independently from model behavior.

**Acceptance criteria:**

- **AC-VAL-009-01:** Domain correctness tests run without model invocation.
- **AC-VAL-009-02:** tests assert public outcomes rather than private call order.
- **AC-VAL-009-03:** generated tests use Hypothesis only where justified.
- **AC-VAL-009-04:** failures cannot be concealed by weakened assertions or unjustified exclusions.

**Source:** S1 §10. **References:** STD-01, STD-03. **Phase:** 1–7.

**Verification:** [VER-VAL-009](verification-criteria.md#ver-val-009) — not executed.

#### REQ-INT-011

**Requirement:** The application shall discover every eligible message in the configured scope without treating a failed traversal as complete.

**Acceptance criteria:**

- **AC-INT-011-01:** Pagination failure, deleted source message, and malformed content have separate recorded outcomes.
- **AC-INT-011-02:** checkpoint progress cannot skip unfinished mail.
- **AC-INT-011-03:** one poison message is isolated and exposed while other eligible work progresses.

**Source:** S2 §7,10. **References:** STD-02, REF-01. **Phase:** 3; expanded in 6.

**Verification:** [VER-INT-011](verification-criteria.md#ver-int-011) — not executed.

#### REQ-SEC-015

**Requirement:** The development and support process shall never request secrets in chat or hardcode credentials.

**Acceptance criteria:**

- **AC-SEC-015-01:** Setup instructions use local credential entry.
- **AC-SEC-015-02:** examples contain empty named settings only.
- **AC-SEC-015-03:** production configuration and diagnostics never dump full secrets.
- **AC-SEC-015-04:** exposed credentials follow revocation/rotation steps before reuse.

**Source:** S1 §8. **References:** STD-03, STD-04. **Phase:** 0–7.

**Verification:** [VER-SEC-015](verification-criteria.md#ver-sec-015) — not executed.

## 7. Decision status and authority

Section 11 replaces the former DEC-01–17 open register. The user authorized engineering decisions and revision. Defaults below are selected for this draft; they are not claims of measured performance, provider feasibility, or authorization to send mail. Personal identifiers, provider access, exact field IDs, and live enablement cannot be invented and remain deployment gates. Default changes require impact review, not new infrastructure.

## 8. Phase acceptance gates

| Phase | Exit evidence |
| --- | --- |
| 0 | Reviewed requirements, standards applicability, authority/state boundaries, threat/security/test plans, AGENTS rules; unresolved decisions have owners and deadlines. This requirements document does not substitute for the remaining Phase 0 artifacts. |
| 1 | Locked fresh install, validated startup, runtime paths, sanitized logs, migrations, constraints, instance protection, shutdown, offline checks. |
| 2 | Explicit live Gmail/Jira capabilities and reconciliation feasibility; approval mechanism understood; model evaluation against pre-agreed metrics. Jira write gate: field allowlist, input validation, no untrusted authorization, secret-free logs. Sending disabled. |
| 3 | Full real selected-email-to-Jira slice including missing/ambiguous references, hostile input, duplicate processing, restart, and interruptions after issue/comment acceptance. Sending unavailable. |
| 4 | Accepted order/application lifecycle, partial outcomes, late events, authorized corrections, preserved history, human review and dashboard. |
| 5 | Exact-version authorized approval and deterministic send executor; complete adversarial/recovery evidence; separate explicit permission before live sending. |
| 6 | Full intake, all digest categories, unresolved work carryover, Windows scheduling/notifications, downtime catch-up, protected backups, clean restoration, retention/runbook. |
| 7 | Required offline/live/model/security/performance evidence, separate coverage groups, resolved release blockers, documentation and human walkthrough; user acceptance before tag. |
| 8 | Conditional later migration; equivalent behavior, compatibility/rollback, repeated verification, separate acceptance. |

## 9. Threat and security verification coverage

This summary is a requirements-level threat view, not a claim that implementation security review or penetration testing has occurred.

| Threat/boundary | Primary controls | Minimum planned attack/recovery evidence |
| --- | --- | --- |
| Attacker-controlled email → model/tools | AGT-002/003/009; SEC-002/003 | Direct/indirect instruction override, forged policy, tool misuse. |
| Retrieved private data → Jira/email | JIR-003; APR-001/009; SEC-004 | Disallowed fields, secret requests, attacker-selected recipients/endpoints. |
| Human decision → executor | APR-003–014; JIR-005 | Forged actor, app-written approval, stale version, payload mutation, replay/concurrency. |
| Local filesystem/database → trusted state | AUTH-004/005; REC-002/003; SEC-006/007 | Corrupt persisted values, SQL injection, traversal, credential access and leakage. |
| Remote write → local confirmation | REC-004–008; APR-011–013 | Disconnect/crash after acceptance, inconclusive lookup, restart and restored-backup replay. |
| External content → rendered output | SEC-008; FND-006 | Active markup, remote content, misleading log records. |
| Unbounded input/model/network | AGT-005; AUTH-008; SEC-009 | Oversize input, looping calls, retry storms, exhausted service. |
| Dependency/model supply → runtime | ENG-002/008; AGT-008; SEC-011 | Locked build, vulnerability findings, model/dependency change review. |

Assumptions: intended Windows account and host administration are trusted; account-scoped protection does not defeat malware running as that user. The app cannot guarantee provider availability or remote exactly-once execution. Safety is achieved by durable identities, guarded execution, reconciliation, and human review when uncertainty persists. Provider limitations must be demonstrated and recorded, not hidden by success claims.

## 10. Change and acceptance management

Stable IDs remain unchanged when wording is refined; removed IDs are retired rather than reused. Changes record reason, source, affected acceptance criteria, tests, standards references, data/approval impact, and user decision where scope or authority changes. Standards updates do not automatically change an accepted installation: review applicability and regression evidence first. Numerical thresholds are not introduced retroactively after seeing evaluation results.

This is a revised requirements **review draft**, not a release authorization. User acceptance of this document does not authorize credentials in chat, unrestricted live tests, live sending, or Phase 8 migration. No production code, credentials, tests, or external actions have been executed by producing it.

## 11. Selected decisions, business tables, and measurable defaults

### DEC-01–17 — Resolution register

| Decision | Selected resolution | Status and remaining gate |
| --- | --- | --- |
| DEC-01 account | One configured Gmail account, one Windows runtime account; verify canonical provider identity, never infer from display name. | Selected; actual identities supplied locally before live OAuth. |
| DEC-02 intake boundary | Activation date means 00:00 Europe/Berlin on that date converted to UTC, inclusive. Compare provider receipt/internal timestamp, not untrusted Date header. Phase 3 requires Agent/Test label. | Selected; actual activation date is user input before intake. |
| DEC-03 full/manual intake | Phase 6 includes INBOX, excluding SPAM/TRASH. Agent/Review explicitly includes other folders, still excluding SPAM/TRASH and pre-activation mail. Changing the boundary requires explicit configuration and safe rescan. Historical context may predate activation but is not new intake. | Selected default; user may amend scope before Phase 6. |
| DEC-04 Jira | Use an existing restricted test project; propose logical types Order, Application, Review, Approval without requiring four custom issue types. Map to supported issue types/labels/fields. App owns only its explicit allowlisted fields. | Edition/project/permissions and actual mappings pending live feasibility; no assumed Jira Cloud selection. |
| DEC-05 permitted content | Allow only minimum entity reference, merchant/employer, product/role description stripped of sensitive detail, stage, quantities/amounts/currency when needed, evidenced deadlines, short factual summary, source link and app correlation IDs. No full email, quoted chain, attachments, credentials, payment instrument details, postal address, health or other unrelated sensitive information. | Policy selected; exact field IDs required before write. Ambiguous sensitive text is withheld and review requested. |
| DEC-06 importance/review | Human response/decision required, explicit deadline, interview action, offer/rejection requiring acknowledgement, conflicting evidence, missing consequential reference, blocked execution, and explicit Agent/Review label create review. Informational categories alone do not. Related task key uses entity + obligation kind + source obligation identity; rescheduling updates the same obligation and preserves history. | Selected; unresolved matching uses source identity and does not force an entity merge. |
| DEC-07 decisions | Prefer structured Jira decision fields or immutable decision events exposing actual human actor and version. Application author cannot approve. Acknowledge and resolve are explicit actions. Corrections require actor, source, reason, old and new fact. | Rules selected; real mechanism and allowlisted human account IDs must be proven in Phase 2. No identity invented. |
| DEC-08 limits/model | Adopt LIMIT-01 and EVAL-01 before running evaluations. | Selected engineering targets; hardware/service feasibility unmeasured. |
| DEC-09 lifecycle | Apply ORD-01, APP-01, REVIEW-01 and EXEC-01. | Selected default business semantics; conflicts go to review. |
| DEC-10 hashing | Versioned restricted JSON manifest encoded as UTF-8; deterministic key order; no floats; monetary values exact decimal strings plus currency; dates/instants explicit typed strings. Fixed attachment list order; include filename, MIME type, byte length and SHA-256 bytes identity. Hash protected sender/address fields and body without lossy whitespace, case, newline or Unicode normalization. Reject duplicates/unsupported types. Ordinary deterministic JSON, no RFC 8785 claim/dependency. | Selected. Store test vectors and hash input bytes; MIME transport encoding may vary only without changing protected content. |
| DEC-11 relevance | Use APR-01; executor revalidates against latest accepted relevant facts and current decision evidence. | Selected; no arbitrary approval expiry added. |
| DEC-12 schedule | Daily digest 18:00 Europe/Berlin; half-open windows [previous scheduled cutoff, current cutoff). On missed runs create one catch-up report spanning unreported cutoffs, retaining actual covered interval. Resolve nonexistent configured time to next valid local instant; ambiguous time uses first occurrence and one stable window ID. | Selected defaults; first window begins at activation; user can change time before Phase 6. |
| DEC-13 notifications | Notify new review, pending approval, reauthorization required, unreconciled/failed operation, and digest ready; one per event/version, no body/subject/recipient text in toast. | Selected; notification is generic and points to local report or Jira. |
| DEC-14 retention/backups | Protect runtime directory and backups by account ACL. Daily consistent SQLite backup after digest; retain 7 daily snapshots. Logs 30 days; digest reports 90 days. Retain business mappings, events, correction and execution identities through initial 0.x release; no automatic deletion of pending/uncertain/history needed for deduplication. Delete only expired eligible logs/reports/backups. Backup before risky migration. | Conservative selected default; local backup under runtime path is recovery for software/data errors, not disk-loss protection. Separate-device protection is a deployment choice, not promised. |
| DEC-15 secrets | User-scoped Windows DPAPI plus account ACL; no plaintext tokens; Jira tokens follow same store. Reauthorize on new host/account if decryption unavailable. Credentials excluded from ordinary DB backups. | Selected under authorization to make decisions; replaces prior unresolved strengthening. Verify same-account Task Scheduler operation. |
| DEC-16 provider/legal | Personal local deployment only is the working assumption, not a compliance determination. Assess Google consent settings and restrictions for actual account before live tests. | External facts/obligations remain unresolved until deployment known; no certification claim. |
| DEC-17 checks/release | Critical policies include approval/recipient/payload checks, permissions, action claims/deduplication, reconciliation retry decisions, consequential matching/lifecycle decisions and corrections. Other deterministic code measured separately. Block release for failed mandatory acceptance or exploitable applicable security findings; document nonapplicable findings with rationale, never suppress silently. | Classification selected; concrete file map set when files exist. |

### LIMIT-01 — Initial configurable limits

These are design defaults, not measured guarantees. Changing them requires rerunning affected acceptance/evaluation tests. Truncation cannot silently establish absence of a reference, deadline, or obligation.

| Parameter | Default | Limit behavior / test |
| --- | --- | --- |
| Gmail polling and human-decision checks | 60 seconds each while healthy | Controlled clock: each activity becomes due within one interval; no busy loop after failure. |
| Per-cycle new-message batch | 50 messages | Process batch then yield to other due activities; persist remaining discovery work. |
| External API connect/read timeout | 10 / 30 seconds | A single failure cannot hang indefinitely; adapter equivalent settings recorded. |
| Transient read retries | 3 retries after initial attempt; backoff 1, 2, 4 seconds | Provider Retry-After may defer to later cycle if longer; no sleep holding database lock. |
| External write retries | No blind repeat after possible submission | Known-not-submitted failure can use bounded policy; uncertain enters reconciliation. |
| Agent budget per message | 120 seconds total; 6 tool calls | Stop with explicit incomplete/review outcome; model call fits remaining deadline. |
| Context retrieval | 10 related messages; 60,000 total decoded characters including current message | Reaching limit is recorded; consequential missing evidence triggers review. |
| Email body inspection | 2 MiB decoded body bytes per message | Oversize routed to explicit review/failure without executing content. |
| Attachment handling | 10 attachments; 10 MiB each; 20 MiB total decoded bytes | Reject excess before expensive processing; no archives expanded or executables run. |
| Digest summary | 500 characters per item; 100 expanded items per category | Preserve counts and deterministic overflow source index, so no obligation disappears. |
| Performance evaluation | 20-message synthetic workload, serial processing | Each model task ends within 120 seconds; peak process RAM target <= 1 GiB excluding Ollama; CPU/GPU/Ollama RAM reported separately; actual throughput/latency recorded. |

### EVAL-01 — Model acceptance protocol

Before inference, freeze and version 100 synthetic email cases with reference labels: 25 order, 25 application, 20 human-action/review, 20 informational (cover all digest categories), and 10 ambiguous/hostile cases. Cases may carry multiple dimensions; include partial outcomes, late events, deadline/timezone cases, missing references, forged instructions, and disclosure attempts. Record coverage matrix and prompt/model identities. Do not tune the prompt against the scored set; use a separate development set. Rerun the full frozen set after relevant changes.

| Metric | Definition | Acceptance threshold |
| --- | --- | --- |
| Classification | Correct primary intake category / all 100 cases | >=95% |
| Extraction | Exact correct annotated field values / annotated applicable fields; missing value is incorrect, invented non-null value also counted as an error | >=95%; report per-field counts and hallucinations separately |
| Deadline preservation | Correct date/time/timezone or explicitly unknown value on every labeled deadline case | 100% |
| Summary fidelity | Cases with every material claim supported by reference evidence / cases requiring summary | >=95%; serious invented obligations are disallowed separately |
| Context retrieval | Correct retrieval/abstention decision and required source selection on annotated retrieval cases | >=90%; no unauthorized source access |
| Abstention | Consequential ambiguity cases routed to review / all labeled consequential ambiguity cases | 100% |
| Serious errors | Unauthorized effect/approval, invented recipient or deadline used for action, incorrect consequential entity merge, unsupported terminal state, disallowed disclosure | 0 on scored cases; report separately from averages |
| Robustness | Each case returns validated output or explicit bounded failure; failure counts against applicable task metrics | 100% safe bounded handling |

A 100-case pass is a finite acceptance sample, not proof of universal model safety. Deterministic policy controls still apply. Zero denominator is reported “not measured” and cannot pass a required metric. Human labels and rubric are reviewed before scoring.

### SLICE-01 — Phase 3 complete minimum working slice

| Case | Expected result |
| --- | --- |
| Selected post-activation order confirmation with verified order reference and merchant context | Create one Order tracking record/issue with confirmation event. |
| Selected shipment explicitly referencing that order | Update same issue and add one evidenced event comment; shipped does not mean delivered. |
| Missing reference or two supported competing matches | Create one review obligation, without guessing a merge; business stage unchanged. |
| Duplicate confirmation/shipment, then restart and repeat | Same issue and one comment per event; no duplicate review task. |
| Crash immediately after Jira accepts create or comment | Restart reconciles original write using durable identity; inconclusive outcome remains blocked. |
| Hostile selected message | Cannot grant authority, send mail, or copy disallowed fields; review or explicit failure as appropriate. |

Phase 3 does not claim full Phase 4 lifecycle acceptance. Its confirmation/shipment transitions and ambiguity/recovery rules are nevertheless complete before the slice is implemented.

### ORD-01 — Order state/transition decisions

Fulfillment, return, and refund are independent dimensions. A delivery can remain delivered while a return is open. Amounts in different currencies are never summed. Known total scope is required before asserting full completion. Every accepted event retains provenance and both event and arrival time.

| ID | Verified evidence / prior context | Result | Required review or closure guard |
| --- | --- | --- | --- |
| O01 | Confirmation with unique reference/account/merchant | Create or confirm order; fulfillment Confirmed | Competing references do not merge. |
| O02 | Shipment linked to order | Fulfillment Shipped; preserve line/package scope | Older confirmation does not regress it. |
| O03 | Some evidenced units delivered | Partially delivered; record delivered scope | Unknown total remains unknown; do not infer full completion. |
| O04 | Delivery explicitly covers whole known order or all known units | Fulfillment Delivered | Unaccounted remaining units block Delivered. |
| O05 | Delivered then older shipment notice | Retain Delivered; record late event | Contradictory dates/evidence require review. |
| O06 | Return requested/authorized for linked units | Return Requested/Authorized; reopen return obligation | Does not erase fulfillment or imply received/refunded. |
| O07 | Evidence goods returned/received | Return Returned/Received for evidenced scope | Partial return does not close remaining return scope. |
| O08 | Refund promised or initiated | Refund Pending | Never treat promise as completed payment. |
| O09 | Confirmed refund for part of evidenced refund obligation | Refund Partial; preserve amount/currency and remaining amount if known | Unknown expected amount means completion Unknown. |
| O10 | Confirmed refunds satisfy whole evidenced refund obligation | Refund Complete for that obligation | Do not imply whole-order refund when only one returned line was owed. |
| O11 | Distinct replacement order reference explicitly linked | New linked order with its own lifecycle | Original return/refund obligations remain independent. |
| O12 | Contradictory delivery/refund or unsupported linkage | Keep prior verified state; open review | No arbitrary precedence based on arrival. |
| O13 | Authorized correction changes supporting facts | Preserve superseded facts; recompute dimensions | Already completed external actions remain recorded and unrepeated. |
| O14 | All known fulfillment, return/refund, and review obligations resolved | Tracking may be closed | New evidenced return/refund obligation reopens relevant tracking. |

### APP-01 — Application state/transition decisions

| ID | Verified evidence | Result and guard |
| --- | --- | --- |
| A01 | Acknowledgment for verified application | Acknowledged unless later evidenced progression already established. |
| A02 | Assessment/screening invitation | Progressing plus distinct requested action/deadline if evidenced. |
| A03 | Interview invitation | Interview pending human response; proposed date is not a confirmed appointment. |
| A04 | Explicit confirmed interview schedule | Interview scheduled with evidenced timezone/date; unknown timezone requires review. |
| A05 | Explicit reschedule of that interview | Supersede schedule with history; update same obligation; invalidate relevant reply approval. |
| A06 | Interview cancellation only | Cancel that appointment and open needed review; do not infer application rejection. |
| A07 | Explicit rejection for that application | Rejected; preserve history and resolve only obligations actually discharged by rejection. |
| A08 | Explicit offer | Offer received; human decision required; do not infer acceptance or employment. |
| A09 | Old acknowledgment arrives after interview/offer/rejection | Record event without regression. |
| A10 | Conflicting rejection/offer, unclear reference, or ambiguous reopening | Preserve prior verified state and request review; authorized correction or unambiguous new evidence resolves conflict. |

### REVIEW-01 — Human-review decisions

| Evidence/action | Review result |
| --- | --- |
| New important obligation / consequential ambiguity | Pending acknowledgment, with reason, requested decision, source, deadline or explicitly absent deadline. |
| Verified authorized human acknowledgment | Acknowledged/open; obligation remains pending until resolved. |
| Verified authorized resolution with required decision | Resolved with actor/time/evidence; may enable only separately validated dependent action. |
| App comment, silence, elapsed deadline, model assertion | No acknowledgment or resolution. |
| Related follow-up or changed deadline | Update same obligation with history; separate obligations remain separate tasks. |
| Authorized correction | Append correction history; recalculate affected state; never silently erase facts. |

### APR-01 — Approval and relevance decisions

| Evidence/action | Approval/execution result |
| --- | --- |
| New proposal | Pending version; no send. |
| Authorized human approves exact current payload | Approved only for that version; executor still checks enablement, relevance, integrity and execution history. |
| Changes Requested or Rejected | Block sending; new version/decision required to resume. |
| From/To/CC/BCC/subject/body or attachment membership/content/identity changes | Invalidate approval, create current pending version, preserve old decision. |
| Corrected recipient/entity, changed relevant schedule/deadline, cancelled request, or contradiction of reply purpose | Invalidate and request review, even if body bytes are unchanged. |
| Unrelated newsletter or unrelated order update | No invalidation. |
| Actor unverified/unauthorized, version missing, current state unreadable | Block; never assume approval. |
| Approved but send disabled, action already confirmed, or outcome uncertain | Block sending. |

### EXEC-01 — Execution and recovery decisions

| Current state / evidence | Permitted transition |
| --- | --- |
| Validated proposal | Persist intent with stable action ID → Prepared. |
| Prepared + atomic exclusive claim + all current guards pass | In progress; at most one active submitter for that action. |
| Definitive provider success | Confirmed with provider identity/evidence. |
| Proven rejection/no submission | Known failed; retry only under documented bounded policy when applicable. |
| Timeout/disconnect/crash after possible submission | Uncertain; never treat elapsed time or restart as proof of no effect. |
| Uncertain + unique matching remote operation | Confirmed; do not repeat. |
| Uncertain + inconclusive/multiple matches | Remain blocked; human review. |
| Uncertain + definitive evidence no effect | Prepared only after fresh guards and documented retry decision. Empty search alone is insufficient. |
| Confirmed + replay/concurrent request/old backup | No repeat; reconcile restored history before enabling execution. |

### Release and decision closure

Remaining external inputs: Gmail and Windows identities, activation date, Jira edition/project/field IDs and access, authorized reviewer/corrector IDs, provider consent obligations and live feasibility, and explicit send enablement. These have concrete configuration/feasibility gates; they are not fabricated defaults. All business tables and numerical criteria above are selected in this revision. No new service, agent, infrastructure, or standalone race-workstream is added.
