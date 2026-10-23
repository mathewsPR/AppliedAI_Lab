# EmailJira — Phase 1 detailed test cases

Version: 0.1.0 · Requirements baseline: 0.2.0 · Date: 2026-10-22.
Status: designed, reviewed structurally, **not implemented and not executed**.

## 1. Purpose and professional approach

This document turns Phase 1 foundation requirements into concrete test conditions, inputs, procedures and observable oracles. It uses risk-based selection and ISTQB CTFL test-analysis/design terminology, not an ISTQB certification or formal ISO 29119 conformance claim. Testing is adapted to the project; a real company normally maintains traceability proportionate to risk, not one arbitrary unit test per sentence.

Official guidance: [ISTQB CTFL syllabus v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf), particularly test analysis/design, traceability, levels/types and black-box techniques. This is a supplementary test-design reference, not an unapproved change to the accepted STD-01–10 baseline. Project authority remains [requirements.md](requirements.md), [verification-criteria.md](verification-criteria.md), and the three original source documents.

Traceability chain: source requirement → AC → VER scenario → TC-P1 case/variant → future pytest/report identifier → actual result/defect. Multiple cases can support one AC, and one case can exercise several related ACs; a link alone is not evidence of full coverage.

## 2. Phase 1 scope and levels

| Level/method | Phase 1 scope | Evidence boundary |
| --- | --- | --- |
| Unit | Configuration validation and delivered path/time helpers | Public observable behavior, no future business-policy modules. |
| Component integration | Real temporary SQLite, migration runner, logging and Windows secret-store adapter | No provider mocks chosen by production. |
| System | Installed foundation CLI/runner, two-process exclusion, shutdown, restart, invalid startup | Entire delivered foundation application; not full email-to-Jira workflow. |
| Platform integration | Windows DPAPI, account ACL, process lifecycle | Must execute on Windows; Linux/mock results cannot satisfy this evidence. |
| Build/static/process | Packaging, dependencies, type/lint/security checks, Git/doc/review controls | Record inspection and build evidence separately from runtime test results. |
| Acceptance | Target Windows foundation walkthrough with user | Phase 1 acceptance only; no complete-project acceptance implied. |

Later system integration with Gmail/Jira/Ollama begins in Phase 2; real email-to-Jira system acceptance in Phase 3; lifecycle in Phase 4; exact approval/sending in Phase 5; digest/scheduling/backup restoration in Phase 6. These cases do not create their code early. All externally writing/live/model tests remain explicitly gated.

## 3. Responsibilities, environment and execution controls

- Developer implements feature and relevant tests together; test author derives conditions and independently checks expected outcomes from requirements. In this project the assistant may fill both roles, so self-review is identified as such.
- User/human reviewer accepts security-sensitive migration/credential changes and Phase 1 walkthrough. No fictional team members or independent audit are implied.
- CI runs repeatable locked checks and stores reports; it does not grant release or live-send authority.
- Use Python 3.12.x, locked development dependencies and current delivered schema. Record Windows edition/build, interpreter/tool versions, commit/lock identity and config identity with each run.
- Offline runtime tests use no production tokens, model or provider network; approved package/advisory downloads during setup/audit are distinct from application integration access.
- Allocate a test-owned runtime root outside the repository, temporary real SQLite, synthetic sentinels and real child processes where process behavior matters. Do not touch the normal user runtime. Inject faults only through test harness/boundaries, never production simulation switches.
- Default filesystem fixture parent is an isolated account-owned temporary directory; use an injected LOCALAPPDATA root in child test environment when supported. Real Windows path/ACL checks run on an isolated user profile/VM. No case changes system HOME or real account data.
- Planned automation folders: unit → tests/unit; component/platform integration → tests/integration; system/acceptance → tests/acceptance; security → tests/security. Use markers to indicate level/platform/type without duplicating cases. No test files are created by this specification.
- P1 = mandatory phase gate due to safety, data integrity, security or essential operation. P2 = mandatory normal-quality evidence. Priority orders execution, not permission to omit. Every parameterized variant is separately reported.

## 4. Entry and exit gates

**Entry:** reviewed foundation configuration/CLI/storage contracts and Phase 0 prerequisites; relevant feature implemented; migration and critical-code classification defined for delivered files; authorized isolated Windows environment available. Before code exists a case is Planned, not failed for lack of code. Exact CLI spelling/config keys are bound to documented public contract at implementation time; semantic outcomes below do not change silently.

**Exit:** all applicable P1/P2 variants pass; all mandatory Windows evidence exists; required build/lint/type/secret/audit checks pass; critical delivered policies meet 100% statement/branch targets, other deterministic code meets 90%/85%; actual coverage classification/exclusions reviewed; no applicable release-blocking defects; human review recorded. A mandatory Blocked or Not run is not a pass. Later-phase evidence is explicitly deferred and cannot close its parent requirement.

**Conditional variants:** no feature/schema is added purely to satisfy a test. When a contract-dependent variant lacks a justified Phase 1 behavior, record N/A-to-Phase-1 with exact rationale, retained future gate and reviewer approval. This cannot waive an actual Phase 1 obligation such as fresh migrations, transaction safety, DPAPI storage mechanism or instance protection.

## 5. Shared result and evidence rules

Pass requires every stated expected outcome. Fail records actual versus expected, reproducer, environment, requirement/AC/case/variant IDs and severity. Blocked identifies prerequisite/owner. Not applicable needs rationale and reviewer decision. No fabricated execution date, code coverage or live verification.

Common evidence: sanitized invocation/result, captured stdout/stderr/logs, before/after test-owned DB/schema/version, process IDs and synchronization events where relevant, ACL/protection inspection on Windows, relevant tool reports, revision identity, actual duration and defect links. Cleanup runs after evidence capture even on failure; cleanup must never hide the failure. Secret fixtures are synthetic and may exist only in tests, never normal production execution.

## 6. Detailed cases

### TC-P1-001 — Clean Python 3.12 locked installation

**Level:** Build/integration. **Priority:** P1. **Technique:** Checklist and valid partition.

**Links:** [REQ-ENG-001](requirements.md#req-eng-001) / AC-ENG-001-01; [REQ-ENG-001](requirements.md#req-eng-001) / AC-ENG-001-02; [REQ-ENG-001](requirements.md#req-eng-001) / AC-ENG-001-03; [REQ-ENG-002](requirements.md#req-eng-002) / AC-ENG-002-01; [REQ-ENG-002](requirements.md#req-eng-002) / AC-ENG-002-02; [REQ-ENG-002](requirements.md#req-eng-002) / AC-ENG-002-03.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** A fresh checkout of the delivered Phase 1 revision; no existing virtual environment; dependency download access permitted only during installation.

**Data/variants:** Committed pyproject.toml and uv.lock; Python 3.12.x; development and runtime dependency groups.

**Steps:**

1. Install from the unchanged lock into a fresh environment using the documented uv procedure.
2. Record interpreter version and installed dependency identities.
3. Compare the lock bytes before/after; inspect runtime/development groups and dependency URL configuration.

**Expected outcomes / pass oracle:**

- Installation succeeds with Python 3.12 and does not rewrite the lock.
- Declared Python range is >=3.12,<3.13; runtime installation does not require development-only tools.
- Every dependency has a documented present use; no secret-bearing index or dependency URL.

**Cleanup:** Delete the isolated environment; retain sanitized install report.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-002 — Unsupported interpreter is rejected

**Level:** Build/integration. **Priority:** P1. **Technique:** Equivalence partitioning.

**Links:** [REQ-ENG-001](requirements.md#req-eng-001) / AC-ENG-001-01; [REQ-ENG-001](requirements.md#req-eng-001) / AC-ENG-001-02.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Same checkout; supported installer configured to respect requires-python.

**Data/variants:** Interpreters 3.11.x and 3.13.x; separate environment per variant.

**Steps:**

1. Attempt installation under each unsupported version.
2. Inspect installer result and repository changes.

**Expected outcomes / pass oracle:**

- Both unsupported versions are rejected with an interpreter-compatibility explanation.
- No usable falsely supported application installation is reported; project files are unchanged.

**Cleanup:** Remove failed isolated environments.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-003 — Help/version are side-effect free

**Level:** System — local CLI. **Priority:** P1. **Technique:** Use-case and negative side-effect checks.

**Links:** [REQ-FND-003](requirements.md#req-fnd-003) / AC-FND-003-01; [REQ-FND-003](requirements.md#req-fnd-003) / AC-FND-003-02; [REQ-ENG-004](requirements.md#req-eng-004) / AC-ENG-004-01; [REQ-ENG-009](requirements.md#req-eng-009) / AC-ENG-009-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Phase 1 installed; runtime directory does not exist; all credentials absent; external network denied.

**Data/variants:** Documented help and version invocations; clean account-local temporary runtime root.

**Steps:**

1. Invoke help, then version, through the documented CLI.
2. Capture exit status/stdout/stderr and file/network effects.

**Expected outcomes / pass oracle:**

- Both return successful diagnostic output without requiring Gmail/Jira/Ollama.
- Version matches the authoritative package version; no runtime DB, credentials, lock, or service call is created.

**Cleanup:** Remove any test-owned capture directory.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-004 — First valid foundation startup

**Level:** System — local CLI. **Priority:** P1. **Technique:** Happy path.

**Links:** [REQ-FND-001](requirements.md#req-fnd-001) / AC-FND-001-01; [REQ-FND-001](requirements.md#req-fnd-001) / AC-FND-001-02; [REQ-FND-002](requirements.md#req-fnd-002) / AC-FND-002-01; [REQ-FND-003](requirements.md#req-fnd-003) / AC-FND-003-01; [REQ-REC-002](requirements.md#req-rec-002) / AC-REC-002-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Fresh installed package; clean writable Windows runtime location; no live integrations configured; process capture enabled.

**Data/variants:** Minimum documented Phase 1 configuration; sending false; fake-looking values are not required because integrations are unavailable.

**Steps:**

1. Run the documented foundation startup command.
2. Wait for documented ready signal, then request normal shutdown.
3. Inspect runtime tree, migration version, output and network attempts.

**Expected outcomes / pass oracle:**

- Startup reaches foundation-ready state and shutdown succeeds.
- DB/schema and sanitized logs are created under the account runtime path.
- Gmail/Jira/Ollama/drafting/sending are explicitly unavailable; no remote operations or fabricated integration success.

**Cleanup:** Stop child process; delete only test-owned runtime tree.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-005 — Missing/malformed configuration fails before dependent writes

**Level:** Unit + CLI integration. **Priority:** P1. **Technique:** Equivalence partitioning.

**Links:** [REQ-FND-001](requirements.md#req-fnd-001) / AC-FND-001-01; [REQ-FND-003](requirements.md#req-fnd-003) / AC-FND-003-02.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Configuration contract has been documented with actual field names; a clean runtime tree is allocated per variant.

**Data/variants:** Missing required Phase 1 setting; malformed syntax; wrong type for each typed setting; unreadable config file. Do not treat future OAuth credentials as Phase 1 required settings.

**Steps:**

1. Run each variant through public configuration loading.
2. For one missing and one malformed variant, run the CLI and record effects.

**Expected outcomes / pass oracle:**

- Each variant raises a specific actionable validation error without dumping config or secrets.
- CLI returns nonzero; no migrations or runner work execute after failed validation.

**Cleanup:** Restore file access and remove fixtures.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-006 — Invalid intervals and configured limits

**Level:** Unit. **Priority:** P1. **Technique:** Boundary-value analysis.

**Links:** [REQ-FND-001](requirements.md#req-fnd-001) / AC-FND-001-01; [REQ-SEC-002](requirements.md#req-sec-002) / AC-SEC-002-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Only the numeric settings actually delivered in Phase 1 are tested; valid ranges are documented before implementation.

**Data/variants:** For a positive integer interval: -1, 0, 1, selected default 60, boolean true, string bad, and fraction 1.5. For any declared maximum M: M-1, M, M+1.

**Steps:**

1. Parameterize the public config loader for each applicable setting.
2. Compare normalized settings/error against its documented range.

**Expected outcomes / pass oracle:**

- Positive valid values retain their documented units; invalid type/value rejected before runner startup.
- Boolean/fraction values cannot silently become a positive integer; maximum boundary is enforced if defined.

**Cleanup:** No persistent effects.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-007 — Unavailable future features cannot appear enabled

**Level:** Unit + system. **Priority:** P1. **Technique:** Decision table.

**Links:** [REQ-FND-001](requirements.md#req-fnd-001) / AC-FND-001-02; [REQ-ENG-005](requirements.md#req-eng-005) / AC-ENG-005-01; [REQ-ENG-005](requirements.md#req-eng-005) / AC-ENG-005-02.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Phase 1 package with integration features not implemented; network denied.

**Data/variants:** Configurations: integration off; request Gmail/Jira feature; request sending enabled.

**Steps:**

1. Start off variant.
2. Attempt each unavailable feature through its documented configuration/command.

**Expected outcomes / pass oracle:**

- Foundation-only variant can start.
- Unavailable requested feature fails explicitly or is explicitly marked unavailable according to documented CLI contract; it never reports functional success.
- Sending remains impossible; no fake adapters, fixtures or hardcoded responses selected by production.

**Cleanup:** Stop processes and remove runtime fixtures.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-008 — Account runtime-path resolution

**Level:** Unit + Windows integration. **Priority:** P1. **Technique:** Equivalence partitioning.

**Links:** [REQ-FND-002](requirements.md#req-fnd-002) / AC-FND-002-01; [REQ-SEC-007](requirements.md#req-sec-007) / AC-SEC-007-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Dedicated test-owned Windows account-local path; application contract fixes %LOCALAPPDATA% root.

**Data/variants:** LOCALAPPDATA test roots with spaces and Unicode; two different account-root fixtures.

**Steps:**

1. Resolve and initialize runtime paths for each root.
2. Observe DB/log/credential paths and compare resolved containment.

**Expected outcomes / pass oracle:**

- Paths are descendants of the selected account root/MailJiraAgent and outside checkout.
- Spaces/Unicode preserve identity; changing working directory does not relocate runtime data.

**Cleanup:** Delete test-owned paths only.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-009 — Unsafe or inaccessible runtime path fails closed

**Level:** Windows integration + system. **Priority:** P1. **Technique:** Negative partitions and error guessing.

**Links:** [REQ-FND-002](requirements.md#req-fnd-002) / AC-FND-002-02; [REQ-FND-003](requirements.md#req-fnd-003) / AC-FND-003-02; [REQ-SEC-007](requirements.md#req-sec-007) / AC-SEC-007-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Isolated runtime roots with controlled permissions and an untouched sentinel outside the allowed tree.

**Data/variants:** Missing LOCALAPPDATA; root is file; access denied; attempted repository-root override if override exists; traversal/junction escape if app accepts a configurable subpath.

**Steps:**

1. Run startup for each applicable variant.
2. Inspect error, exit code, checkout and sentinel.

**Expected outcomes / pass oracle:**

- Clear failure with no fallback to cwd, checkout, or global writable directory.
- No outside sentinel modified; app must not weaken ACLs to proceed.
- Unsupported configuration keys are rejected rather than becoming unreviewed path overrides.

**Cleanup:** Restore ACLs/junctions safely, then remove fixtures.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-010 — Normal logs contain actionable operational metadata

**Level:** Integration. **Priority:** P2. **Technique:** Checklist.

**Links:** [REQ-FND-006](requirements.md#req-fnd-006) / AC-FND-006-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Capture every configured logger destination; isolated healthy foundation execution.

**Data/variants:** Known synthetic run identifier and controlled clock/duration source.

**Steps:**

1. Start and stop foundation; trigger one recoverable validation/storage failure.
2. Inspect emitted records.

**Expected outcomes / pass oracle:**

- Records identify operation/outcome and useful identifiers; durations where applicable are nonnegative.
- Failure record has useful sanitized context, not only an unexplained failure or fabricated success.

**Cleanup:** Remove captured logs.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-011 — Secret/private data excluded from all output

**Level:** Security integration. **Priority:** P1. **Technique:** Adversarial data partitioning.

**Links:** [REQ-FND-006](requirements.md#req-fnd-006) / AC-FND-006-02; [REQ-FND-006](requirements.md#req-fnd-006) / AC-FND-006-04; [REQ-AUTH-005](requirements.md#req-auth-005) / AC-AUTH-005-01; [REQ-SEC-010](requirements.md#req-sec-010) / AC-SEC-010-01; [REQ-SEC-015](requirements.md#req-sec-015) / AC-SEC-015-03.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Capture stdout, stderr, every log handler, exception formatting and debug diagnostics supported by Phase 1.

**Data/variants:** Unique synthetic sentinels for access token, refresh token, auth code, PKCE verifier, Jira token, full config blob, subject, personal name, body and attachment bytes.

**Steps:**

1. Pass sentinels only through delivered config/error/log boundaries, using external-boundary response fixtures solely in tests.
2. Trigger normal and failure paths, including exception causes.
3. Search all captures for each sentinel and full-config representation.

**Expected outcomes / pass oracle:**

- No secret/private sentinel appears in any capture, including debug and chained exceptions.
- Necessary field/error identifiers remain useful without printing raw values.
- No claim of live OAuth error coverage: provider-specific cases remain Phase 2.

**Cleanup:** Destroy synthetic captures; never use real secrets.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-012 — Untrusted newlines cannot forge log records

**Level:** Security integration. **Priority:** P1. **Technique:** Error guessing.

**Links:** [REQ-FND-006](requirements.md#req-fnd-006) / AC-FND-006-03.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Logger exposed through a delivered public path; capture parser uses configured record format.

**Data/variants:** Untrusted identifier with CR, LF, tabs, quotation marks, Unicode and fake second-record prefix.

**Steps:**

1. Emit one operation with hostile value.
2. Parse output records and inspect displayed text.

**Expected outcomes / pass oracle:**

- One logical event remains one event; hostile bytes are escaped or safely encoded.
- No fake approved/success record is created; valid identifiers remain distinguishable.

**Cleanup:** Remove capture.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-013 — Imports have no runtime side effects

**Level:** Integration. **Priority:** P1. **Technique:** Isolation and observation.

**Links:** [REQ-ENG-004](requirements.md#req-eng-004) / AC-ENG-004-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Fresh subprocess; no runtime store; network calls denied at boundary; delivered modules enumerable.

**Data/variants:** Each production module introduced in Phase 1.

**Steps:**

1. Import each delivered module in a fresh subprocess.
2. Observe network, filesystem and DB creation, process startup, and exit.

**Expected outcomes / pass oracle:**

- Import completes without network, DB writes, runtime creation or spawned worker.
- Explicit startup entry point, rather than import, owns initialization.

**Cleanup:** Stop any unexpected process and fail; remove test captures.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-014 — Fresh SQLite migration and repeated initialization

**Level:** Database integration. **Priority:** P1. **Technique:** State transitions.

**Links:** [REQ-REC-002](requirements.md#req-rec-002) / AC-REC-002-01; [REQ-FND-003](requirements.md#req-fnd-003) / AC-FND-003-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Temporary real SQLite file and delivered initial migration.

**Data/variants:** Empty directory; then same initialized file.

**Steps:**

1. Initialize once through production migration entry point.
2. Record schema/version/data; initialize again.

**Expected outcomes / pass oracle:**

- Initial schema and migration history exist exactly once and are consistent.
- Second invocation applies nothing twice and preserves data; no destructive recreation.

**Cleanup:** Close connections; remove temporary DB.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-015 — Foreign keys enforced on every production connection

**Level:** Database integration. **Priority:** P1. **Technique:** Constraint negative testing.

**Links:** [REQ-REC-002](requirements.md#req-rec-002) / AC-REC-002-02.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Initial schema includes a legitimate parent/child constraint required by delivered migration bookkeeping or other delivered behavior.

**Data/variants:** Existing parent, valid child, orphan child; two independently opened production connections.

**Steps:**

1. Verify foreign-key setting on each connection.
2. Insert valid pair and then attempt orphan insert; rollback expected failure.

**Expected outcomes / pass oracle:**

- Foreign-key enforcement is active on both connections.
- Valid pair survives; orphan insert fails with a specific constraint error and leaves no orphan.
- If no justified parent/child table exists yet, inspect enforcement setting and mark insert variant deferred rather than creating speculative tables.

**Cleanup:** Close and delete DB.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-016 — Uniqueness and rollback leave migration ledger consistent

**Level:** Database integration. **Priority:** P1. **Technique:** Constraint boundaries.

**Links:** [REQ-REC-002](requirements.md#req-rec-002) / AC-REC-002-02; [REQ-REC-002](requirements.md#req-rec-002) / AC-REC-002-03; [REQ-REC-003](requirements.md#req-rec-003) / AC-REC-003-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Real temporary store with delivered migration ledger unique version identity.

**Data/variants:** Same migration version twice, plus one distinct version in a test migration resource.

**Steps:**

1. Attempt duplicate ledger identity in a transaction.
2. Reopen database and inspect migration history.

**Expected outcomes / pass oracle:**

- Duplicate is rejected; ledger contains one entry per applied version.
- Failure cannot mark an unapplied migration applied or corrupt prior entries.

**Cleanup:** Delete temporary DB/test migration resources.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-017 — Local transaction commit and rollback

**Level:** Database integration. **Priority:** P1. **Technique:** State transitions and fault injection.

**Links:** [REQ-REC-003](requirements.md#req-rec-003) / AC-REC-003-01; [REQ-REC-001](requirements.md#req-rec-001) / AC-REC-001-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Use only related writes exposed by delivered foundation persistence, such as migration DDL and version record.

**Data/variants:** Success variant; exception between related writes; distinct known baseline row/schema.

**Steps:**

1. Perform related writes successfully and reopen.
2. Reset baseline; inject failure after first related write and reopen.

**Expected outcomes / pass oracle:**

- Successful transaction persists all related changes.
- Failed transaction persists none of that transaction; prior committed baseline remains.
- No future event/action schema is added merely to execute this case.

**Cleanup:** Remove DB and test failure injection.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-018 — Migration statement failure is recoverable

**Level:** Database integration. **Priority:** P1. **Technique:** Fault injection.

**Links:** [REQ-REC-009](requirements.md#req-rec-009) / AC-REC-009-02; [REQ-REC-002](requirements.md#req-rec-002) / AC-REC-002-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Temporary database with baseline migration; test-only next migration deliberately fails mid-transaction.

**Data/variants:** Create test-owned table or row, then invalid SQL before migration ledger completion.

**Steps:**

1. Snapshot baseline; execute failing test migration through migration runner.
2. Reopen file; inspect schema/data/version; retry with corrected test migration only.

**Expected outcomes / pass oracle:**

- First run fails explicitly and cannot mark version applied; baseline remains recoverable.
- Corrected test resource applies once; no partial schema silently reported successful.
- Never edit a released production migration to arrange the fixture.

**Cleanup:** Delete DB and isolated migration resources.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-019 — Released migration immutability is verified

**Level:** Static review/build check. **Priority:** P1. **Technique:** Configuration comparison.

**Links:** [REQ-REC-002](requirements.md#req-rec-002) / AC-REC-002-03; [REQ-REC-009](requirements.md#req-rec-009) / AC-REC-009-03.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** First baseline retained; for first-ever release, no released migration exists.

**Data/variants:** Released migration files compared against baseline/tag; added migration in current change.

**Steps:**

1. Compare existing migration contents with accepted baseline.
2. Inspect whether schema changes use a new version rather than modifying old migration.

**Expected outcomes / pass oracle:**

- Released migration contents unchanged; new change has a new unique version.
- First-ever release records an initial baseline and does not fabricate a previous tag.

**Cleanup:** Restore any deliberately altered copy; never change baseline.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-020 — Upgrade backup gate protects risky changes

**Level:** Migration integration + review. **Priority:** P1. **Technique:** Decision table.

**Links:** [REQ-REC-009](requirements.md#req-rec-009) / AC-REC-009-01; [REQ-REC-009](requirements.md#req-rec-009) / AC-REC-009-02; [REQ-REC-009](requirements.md#req-rec-009) / AC-REC-009-04.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Risk classification documented; isolated DB with known data; backup-capable migration workflow exists if a risky migration is delivered.

**Data/variants:** Risky migration with writable backup destination, then denied backup destination; no risky production upgrade need be invented.

**Steps:**

1. Inspect risky-upgrade procedure and its gate.
2. When supported, attempt upgrade with backup success and then backup failure; inspect original and backup stores.

**Expected outcomes / pass oracle:**

- Risky upgrade cannot start without a verified recoverable pre-upgrade backup.
- Backup failure blocks mutation; failure is explicit.
- No promise of automatic reversal of destructive migrations. If Phase 1 contains only initial creation, operational upgrade variant is explicitly deferred to first risky upgrade and checklist remains applicable.

**Cleanup:** Remove backup and temporary stores.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-021 — SQLite error causes explicit startup failure

**Level:** Database integration + system. **Priority:** P1. **Technique:** Failure partitions.

**Links:** [REQ-FND-003](requirements.md#req-fnd-003) / AC-FND-003-02; [REQ-FND-005](requirements.md#req-fnd-005) / AC-FND-005-02; [REQ-ENG-004](requirements.md#req-eng-004) / AC-ENG-004-02; [REQ-ENG-004](requirements.md#req-eng-004) / AC-ENG-004-03.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Separate isolated runtime per failure; no real user DB.

**Data/variants:** DB path is directory; read-only file; invalid/corrupt SQLite bytes; injected write failure representing disk-full.

**Steps:**

1. Start with each variant.
2. Inspect process outcome and original bytes; reopen healthy baseline where applicable.

**Expected outcomes / pass oracle:**

- No ready/success signal after failed initialization; nonzero exit and sanitized specific cause.
- Existing corrupt/readonly store is not silently replaced, truncated or reinitialized.
- Committed healthy baseline remains intact after injected write failure.

**Cleanup:** Restore permissions; remove fixtures.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-022 — Normal single-instance exclusion

**Level:** Windows process/system. **Priority:** P1. **Technique:** State transitions.

**Links:** [REQ-FND-004](requirements.md#req-fnd-004) / AC-FND-004-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Two real app subprocesses target the same normalized runtime store; first process reports ready.

**Data/variants:** Process A holds active instance protection; process B uses same store.

**Steps:**

1. Start A and wait on observable readiness.
2. Start B; capture result and store activity; keep A alive.

**Expected outcomes / pass oracle:**

- B exits nonzero with already-running explanation before DB migration/runner work.
- A remains healthy and owns the store; no concurrent writers created by B.

**Cleanup:** Stop A gracefully and remove runtime.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-023 — Simultaneous startup race has one winner

**Level:** Windows process/system. **Priority:** P1. **Technique:** Concurrency and error guessing.

**Links:** [REQ-FND-004](requirements.md#req-fnd-004) / AC-FND-004-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Two real processes share a clean test runtime; synchronization barrier in test harness, not production fake mode.

**Data/variants:** Start A/B simultaneously; repeat controlled race 10 times with isolated stores.

**Steps:**

1. Release both processes together and observe readiness/exit.
2. Inspect migration history and active processes.

**Expected outcomes / pass oracle:**

- Exactly one process becomes ready in each run; loser rejects safely.
- No duplicated initialization or damaged DB; test uses bounded waits, not timing-only sleeps.

**Cleanup:** Stop winner each round and remove stores.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-024 — Graceful stop releases instance ownership

**Level:** Windows process/system. **Priority:** P1. **Technique:** State transitions.

**Links:** [REQ-FND-004](requirements.md#req-fnd-004) / AC-FND-004-02; [REQ-FND-005](requirements.md#req-fnd-005) / AC-FND-005-02.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Running instance A, test-owned runtime.

**Data/variants:** Documented stop signal/control method for Windows; process B for restart.

**Steps:**

1. Request graceful stop and wait for process exit.
2. Start B on same store.

**Expected outcomes / pass oracle:**

- A terminates under documented shutdown bound (execution watchdog 10 seconds in harness).
- B obtains ownership and resumes healthy state; no permanent stale-lock failure.
- If 10-second bound is unmet, report a design/performance finding rather than silently kill and mark pass.

**Cleanup:** Stop B; remove runtime.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-025 — Abrupt process death does not leave permanent ownership

**Level:** Windows process/system. **Priority:** P1. **Technique:** Recovery transitions.

**Links:** [REQ-FND-004](requirements.md#req-fnd-004) / AC-FND-004-02; [REQ-FND-005](requirements.md#req-fnd-005) / AC-FND-005-02.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Process A ready with committed migration/state; test harness has permission to terminate its own child only.

**Data/variants:** Forced child termination; new process B.

**Steps:**

1. Terminate A without cleanup.
2. Start B and inspect recovery and DB integrity.

**Expected outcomes / pass oracle:**

- B obtains valid ownership after A is confirmed dead, using documented safe lock semantics.
- Committed store survives; active unrelated owner would never be overridden solely because a file is old.

**Cleanup:** Stop B; remove runtime.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-026 — Restart preserves commits and rejects incomplete work

**Level:** Database integration + system. **Priority:** P1. **Technique:** Crash-boundary analysis.

**Links:** [REQ-REC-003](requirements.md#req-rec-003) / AC-REC-003-01; [REQ-REC-001](requirements.md#req-rec-001) / AC-REC-001-01; [REQ-FND-005](requirements.md#req-fnd-005) / AC-FND-005-01; [REQ-FND-005](requirements.md#req-fnd-005) / AC-FND-005-02.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Only delivered local persistence operations; real child process and temporary SQLite.

**Data/variants:** Kill before transaction commit; kill after commit; use ledger/schema or another legitimate delivered record.

**Steps:**

1. For each boundary run operation and terminate child at test-observed boundary.
2. Reopen through normal initialization.

**Expected outcomes / pass oracle:**

- Before commit: incomplete related change absent and migration not falsely marked applied.
- After commit: change and corresponding version/state retained.
- No unfinished operation appears as confirmed; remote-write variants explicitly deferred.

**Cleanup:** Delete test stores and synchronization fixtures.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-027 — Signal handling stops idle runner cleanly

**Level:** System — local runner. **Priority:** P1. **Technique:** State transitions.

**Links:** [REQ-FND-005](requirements.md#req-fnd-005) / AC-FND-005-01; [REQ-FND-005](requirements.md#req-fnd-005) / AC-FND-005-02; [REQ-FND-007](requirements.md#req-fnd-007) / AC-FND-007-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Foundation runner idle; integration modules unavailable; subprocess observed through public signals/output.

**Data/variants:** Documented user interrupt and stop pathway; first signal plus repeated signal variant.

**Steps:**

1. Send supported stop request while idle.
2. Repeat in independent run with second request during stopping.
3. Inspect handles, logs and exit outcome.

**Expected outcomes / pass oracle:**

- No new work starts after stop accepted; store handles and instance ownership released.
- User-requested clean termination uses documented successful outcome; interruption/error distinction is explicit.
- No fictitious pending email or external-write success.

**Cleanup:** Terminate only test child if hung and report failure; remove runtime.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-028 — Windows account credential-store round trip

**Level:** Windows security integration. **Priority:** P1. **Technique:** Valid partition.

**Links:** [REQ-AUTH-004](requirements.md#req-auth-004) / AC-AUTH-004-01; [REQ-AUTH-004](requirements.md#req-auth-004) / AC-AUTH-004-02; [REQ-SEC-010](requirements.md#req-sec-010) / AC-SEC-010-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Delivered foundation secret-store interface using real user-scoped Windows DPAPI; current account test scope; no OAuth flow.

**Data/variants:** Synthetic token byte string P1-SYNTHETIC-TOKEN; expected account ACL.

**Steps:**

1. Store and retrieve via production secret-store API.
2. Inspect file bytes, effective ACL, protection flags/configuration, logs and Git paths.

**Expected outcomes / pass oracle:**

- Same account retrieves original value; on-disk bytes do not contain plaintext token.
- User-scoped protection selected, not machine-wide; broad unrelated-user access absent.
- Only allowed account and necessary OS principals have access; token absent from output/repository.

**Cleanup:** Delete encrypted synthetic file; never alter user credentials.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-029 — Missing/inaccessible/corrupt secret produces explicit result

**Level:** Windows security integration. **Priority:** P1. **Technique:** Negative partitions.

**Links:** [REQ-AUTH-004](requirements.md#req-auth-004) / AC-AUTH-004-03; [REQ-AUTH-005](requirements.md#req-auth-005) / AC-AUTH-005-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Real delivered secret store; separate fixture per variant.

**Data/variants:** Missing credential file; access denied; empty file; modified ciphertext; truncated ciphertext.

**Steps:**

1. Attempt retrieval for each variant.
2. Inspect typed unavailable/error result, logging, and whether original file was changed.

**Expected outcomes / pass oracle:**

- No token or authenticated-success result is fabricated.
- Failure identifies missing/permission/decryption class without token or raw ciphertext dump; permissions are not relaxed.
- Original fixture is not overwritten with blank/default token.

**Cleanup:** Restore test ACL; delete fixtures.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-030 — Different Windows user cannot recover token

**Level:** Windows security integration/manual. **Priority:** P1. **Technique:** Authorization negative testing.

**Links:** [REQ-AUTH-004](requirements.md#req-auth-004) / AC-AUTH-004-01; [REQ-AUTH-004](requirements.md#req-auth-004) / AC-AUTH-004-02; [REQ-AUTH-004](requirements.md#req-auth-004) / AC-AUTH-004-03.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Two explicitly authorized isolated Windows test accounts or controlled test VM; no real credentials.

**Data/variants:** Synthetic user-A DPAPI blob; user B has read access only to an isolated copied blob so decryption is tested independently of filesystem denial.

**Steps:**

1. Protect under A.
2. Verify B cannot read original restricted location.
3. Give B the test copy, attempt unprotect, then recheck A original round trip.

**Expected outcomes / pass oracle:**

- Original ACL denies B; isolated copied blob cannot be decrypted as B.
- A original remains recoverable; B failure leaks no token.
- If second account unavailable, mark Blocked; same-account mocked failure is not proof of cross-user protection.

**Cleanup:** Delete copies under both accounts; restore no production ACLs.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-031 — Resources close and exceptions preserve useful causes

**Level:** Unit/integration + static review. **Priority:** P1. **Technique:** Fault injection and checklist.

**Links:** [REQ-ENG-004](requirements.md#req-eng-004) / AC-ENG-004-02; [REQ-ENG-004](requirements.md#req-eng-004) / AC-ENG-004-03; [REQ-ENG-012](requirements.md#req-eng-012) / AC-ENG-012-01; [REQ-ENG-012](requirements.md#req-eng-012) / AC-ENG-012-02.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Delivered file, DB and secret-store operations; test-owned resources.

**Data/variants:** Raise a specific exception inside managed operation; sentinel secret in low-level error; repeated calls.

**Steps:**

1. Exercise failing operation twice; inspect resource release and exception chain.
2. Review context-manager use and remaining coding constraints.

**Expected outcomes / pass oracle:**

- File/DB resources released on success and failure; no resource exhaustion or unintended shared mutable state.
- Sanitized cause retained without broad swallowed errors; no wildcard imports/hidden mutable globals/unnecessary inheritance or arbitrary size rules.

**Cleanup:** Close leaked handles only after recording failure; remove fixtures.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-032 — SQL injection strings remain data

**Level:** Database security integration. **Priority:** P1. **Technique:** Adversarial input.

**Links:** [REQ-SEC-006](requirements.md#req-sec-006) / AC-SEC-006-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** A delivered persistence method accepts a legitimate variable value; otherwise inspect parameter binding and defer data-path assertion until such method exists.

**Data/variants:** Value: x'; DROP TABLE migrations; -- ; quotes, Unicode and SQL comment syntax; known unrelated row.

**Steps:**

1. Insert/query hostile value using public persistence API.
2. Check matched value and unrelated table/rows.

**Expected outcomes / pass oracle:**

- Value stored/retrieved literally where valid, or rejected by documented validation.
- No extra statement executes and unrelated data unchanged; dynamic SQL identifiers originate from fixed allowlist.

**Cleanup:** Delete temporary DB.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-033 — Time representations preserve instants and dates

**Level:** Unit/database integration. **Priority:** P2. **Technique:** Boundary and equivalence partitions.

**Links:** [REQ-REC-010](requirements.md#req-rec-010) / AC-REC-010-01; [REQ-REC-010](requirements.md#req-rec-010) / AC-REC-010-02; [REQ-REC-010](requirements.md#req-rec-010) / AC-REC-010-03; [REQ-REC-010](requirements.md#req-rec-010) / AC-REC-010-04.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Only timestamp/date behavior actually introduced in foundation; fixed clock; no model.

**Data/variants:** 2026-10-25T00:30:00Z and 2026-10-25T01:30:00Z; date-only 2026-10-25; naive timestamp with no timezone.

**Steps:**

1. Store/format supported instants and reopen if persisted.
2. Check display and date handling; submit naive timestamp.

**Expected outcomes / pass oracle:**

- UTC instants remain distinct although both display local 02:30 with different offsets in Europe/Berlin.
- Date-only remains date; no invented midnight. Naive instant rejected or explicitly unknown per public contract, never silently assigned local timezone.
- Business date-only variant deferred until date type exists; fixture checks do not add unused domain code.

**Cleanup:** Remove DB/captures.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-034 — Style, typing and public documentation checks

**Level:** Static/build. **Priority:** P2. **Technique:** Checklist.

**Links:** [REQ-ENG-003](requirements.md#req-eng-003) / AC-ENG-003-01; [REQ-ENG-003](requirements.md#req-eng-003) / AC-ENG-003-02; [REQ-ENG-003](requirements.md#req-eng-003) / AC-ENG-003-03; [REQ-ENG-003](requirements.md#req-eng-003) / AC-ENG-003-04.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Delivered Phase 1 source, locked dev tools, agreed Ruff/mypy configuration.

**Data/variants:** All current production modules and public CLI/persistence/config interfaces.

**Steps:**

1. Run formatter check, lint and mypy.
2. Review annotations, justified Any exceptions and public-interface docstrings.

**Expected outcomes / pass oracle:**

- Configured checks succeed and do not exclude relevant production code without rationale.
- Public behavior and non-obvious constraints documented; meaningful annotations exist; no blanket Any escape.

**Cleanup:** Keep reports; do not autoformat unrelated code.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-035 — Production contains no simulation or placeholder behavior

**Level:** Static review + system. **Priority:** P1. **Technique:** Checklist and negative capability testing.

**Links:** [REQ-ENG-005](requirements.md#req-eng-005) / AC-ENG-005-01; [REQ-ENG-005](requirements.md#req-eng-005) / AC-ENG-005-02; [REQ-GOV-006](requirements.md#req-gov-006) / AC-GOV-006-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Delivered production source and built artifact.

**Data/variants:** No placeholder integration modules; future feature invocation from TC-P1-007.

**Steps:**

1. Inspect production paths for unfinished required behavior and test-fixture imports.
2. Exercise documented available behavior and unsupported future commands.

**Expected outcomes / pass oracle:**

- No required production behavior uses dummy results, silent no-ops or fake adapters.
- Future features explicitly unavailable; no empty scaffolding merely mirroring full planned tree.
- Keyword search findings are reviewed semantically: a valid empty exception class is not automatically a fake feature.

**Cleanup:** Retain review checklist.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-036 — Repository excludes private runtime artifacts

**Level:** Static/Git verification. **Priority:** P1. **Technique:** Checklist.

**Links:** [REQ-ENG-006](requirements.md#req-eng-006) / AC-ENG-006-04; [REQ-SEC-010](requirements.md#req-sec-010) / AC-SEC-010-01; [REQ-SEC-015](requirements.md#req-sec-015) / AC-SEC-015-01; [REQ-SEC-015](requirements.md#req-sec-015) / AC-SEC-015-02.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Local checkout; disposable private-runtime sentinel files; no real token.

**Data/variants:** Synthetic log/DB/token/email files outside repository; .env.example empty secret fields; .gitignore rules.

**Steps:**

1. Inspect tracked files and package input tree.
2. Check ignore behavior for runtime/secrets patterns; inspect setup documentation.

**Expected outcomes / pass oracle:**

- No credentials, runtime databases/logs/private email tracked or packaged.
- Examples use named empty secret settings; setup requests local entry rather than chat disclosure.
- Ignore checks do not substitute for inspecting already tracked files.

**Cleanup:** Delete synthetic sentinels; do not stage them.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-037 — Secret scanner catches a controlled fixture

**Level:** Security tooling verification. **Priority:** P1. **Technique:** Tool sensitivity check.

**Links:** [REQ-ENG-008](requirements.md#req-eng-008) / AC-ENG-008-01; [REQ-SEC-010](requirements.md#req-sec-010) / AC-SEC-010-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Locked/configured scanner and isolated untracked fixture; no real secrets.

**Data/variants:** Scanner-supported published synthetic detection fixture, plus clean repository variant.

**Steps:**

1. Run scan on isolated known-positive fixture.
2. Run required repository scan and inspect exclusions.

**Expected outcomes / pass oracle:**

- Known-positive fixture produces finding and failing gate; clean repo report assessed.
- Broad exclusions cannot conceal current production sources; diagnostics do not print live secrets.
- Scanner pass is not proof that logs/DPAPI are secure.

**Cleanup:** Delete fixture before normal scan; retain sanitized reports.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-038 — Dependency audit reports and dispositions are visible

**Level:** Security/build verification. **Priority:** P1. **Technique:** Tool integration checklist.

**Links:** [REQ-ENG-008](requirements.md#req-eng-008) / AC-ENG-008-01; [REQ-SEC-011](requirements.md#req-sec-011) / AC-SEC-011-01; [REQ-SEC-011](requirements.md#req-sec-011) / AC-SEC-011-02.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Committed lock; approved audit access to current vulnerability data; no production credentials.

**Data/variants:** Current locked dependency graph; separate tool-supported known-positive advisory fixture when practical.

**Steps:**

1. Run configured vulnerability audit against locked dependencies.
2. Inspect graph identity, findings, exceptions and gate result.

**Expected outcomes / pass oracle:**

- Report matches tested lock and source/date; applicable exploitable findings block release or phase acceptance per policy.
- Unavailable audit feed is Blocked/error, not a clean pass; justified nonapplicable dispositions retained.
- Feed access is tooling network, not live Gmail/Jira/Ollama access.

**Cleanup:** Remove isolated advisory fixture; keep report.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-039 — Package build and install represent delivered features

**Level:** Build/system. **Priority:** P1. **Technique:** Artifact verification.

**Links:** [REQ-ENG-008](requirements.md#req-eng-008) / AC-ENG-008-01; [REQ-ENG-009](requirements.md#req-eng-009) / AC-ENG-009-01; [REQ-FND-003](requirements.md#req-fnd-003) / AC-FND-003-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Clean Phase 1 checkout; locked build tools; isolated install destination.

**Data/variants:** Wheel/source artifact if project packaging supports both; no runtime private files.

**Steps:**

1. Build distributable; inspect contents/version metadata.
2. Install built artifact into fresh Python 3.12 environment; execute help and foundation startup.

**Expected outcomes / pass oracle:**

- Build succeeds; metadata version matches authoritative version; installed CLI initializes foundation.
- Artifact includes required migrations/resources and excludes credentials, test captures and runtime store.

**Cleanup:** Remove isolated environment/artifacts after retaining build identity.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-040 — Default tests are offline and deterministic

**Level:** Verification-system check. **Priority:** P1. **Technique:** Isolation and repeatability.

**Links:** [REQ-VAL-001](requirements.md#req-val-001) / AC-VAL-001-01; [REQ-VAL-001](requirements.md#req-val-001) / AC-VAL-001-02; [REQ-VAL-001](requirements.md#req-val-001) / AC-VAL-001-03; [REQ-VAL-009](requirements.md#req-val-009) / AC-VAL-009-01; [REQ-VAL-009](requirements.md#req-val-009) / AC-VAL-009-02; [REQ-VAL-009](requirements.md#req-val-009) / AC-VAL-009-03; [REQ-VAL-009](requirements.md#req-val-009) / AC-VAL-009-04; [REQ-VAL-004](requirements.md#req-val-004) / AC-VAL-004-02.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Implemented Phase 1 tests only; deny external socket access; remove credentials.

**Data/variants:** Two consecutive full offline runs; temporary real SQLite; controlled clock and subprocess synchronization.

**Steps:**

1. Execute default test selection twice.
2. Inspect collection, fixture lifetimes and mocked boundaries.

**Expected outcomes / pass oracle:**

- Same expected results without Gmail/Jira/Ollama calls or production credentials.
- No tests require execution-order dependency; no mocking private internal methods merely to mirror implementation.
- Windows tests are visibly not selected/blocked on unsupported host, never counted as Windows proof; Hypothesis used only with justification.

**Cleanup:** Remove temp files; keep separate run reports.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-041 — Separate coverage gates apply to delivered code

**Level:** Verification/build. **Priority:** P1. **Technique:** Structural coverage audit.

**Links:** [REQ-VAL-002](requirements.md#req-val-002) / AC-VAL-002-01; [REQ-VAL-002](requirements.md#req-val-002) / AC-VAL-002-02; [REQ-VAL-002](requirements.md#req-val-002) / AC-VAL-002-03.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Current source classified critical/other deterministically; executed tests instrumented for statement and branch coverage.

**Data/variants:** Critical foundation policy files if present; other foundation code; reviewed exclusion list.

**Steps:**

1. Run coverage for delivered code with separate group reports.
2. Inspect uncovered branches and exclusion rationale.

**Expected outcomes / pass oracle:**

- Critical group meets 100% statement and branch targets; other group meets 90%/85%.
- An empty future approval/lifecycle group is Not applicable—not 100% proven.
- Shortfalls remain visible and block relevant gate; no weakened assertions or fake modules to inflate coverage.

**Cleanup:** Retain reports keyed to revision.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-042 — Essential CI checks fail rather than hide errors

**Level:** CI/build verification. **Priority:** P1. **Technique:** Negative gate injection.

**Links:** [REQ-ENG-008](requirements.md#req-eng-008) / AC-ENG-008-01; [REQ-ENG-008](requirements.md#req-eng-008) / AC-ENG-008-02; [REQ-ENG-001](requirements.md#req-eng-001) / AC-ENG-001-02.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Disposable branch/copy with Python 3.12 CI; no production credentials; Windows runner available for platform checks.

**Data/variants:** Independent variants: formatter/lint violation, mypy error, failing assertion, secret fixture, audit failure, build failure.

**Steps:**

1. Execute clean required checks.
2. Introduce each controlled failure in isolated copy and rerun relevant gate.
3. Inspect result propagation and OS job selection.

**Expected outcomes / pass oracle:**

- Each injected required failure causes non-success gate; no continue-on-error masking.
- Windows-specific checks actually execute on Windows; required missing platform job is incomplete evidence.
- Install/audit jobs may access approved package/advisory services; application tests remain offline.

**Cleanup:** Discard disposable copy/failures.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-043 — Human review and focused Git delivery evidence

**Level:** Static/process review. **Priority:** P1. **Technique:** Checklist.

**Links:** [REQ-ENG-006](requirements.md#req-eng-006) / AC-ENG-006-01; [REQ-ENG-006](requirements.md#req-eng-006) / AC-ENG-006-02; [REQ-ENG-006](requirements.md#req-eng-006) / AC-ENG-006-03; [REQ-ENG-007](requirements.md#req-eng-007) / AC-ENG-007-01; [REQ-ENG-007](requirements.md#req-eng-007) / AC-ENG-007-02; [REQ-ENG-013](requirements.md#req-eng-013) / AC-ENG-013-01; [REQ-ENG-013](requirements.md#req-eng-013) / AC-ENG-013-02; [REQ-ENG-013](requirements.md#req-eng-013) / AC-ENG-013-03; [REQ-ENG-013](requirements.md#req-eng-013) / AC-ENG-013-04.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Phase 1 change ready for review; relevant source docs/AGENTS read; human reviewer available.

**Data/variants:** Diff, focused/broader check reports, migration and credential changes, remote PR if remote exists.

**Steps:**

1. Review scope, correctness, failures, privacy/recovery, compatibility, tests and affected docs.
2. Record human decision on credential/migration changes; inspect history.

**Expected outcomes / pass oracle:**

- Focused coherent change and no unauthorized shared-history rewrite.
- Security-sensitive changes retain actual human review; same assistant self-review not mislabeled independent/human acceptance.
- Local-only work uses recorded diff/check review; remote PR only when workflow exists.

**Cleanup:** Keep review evidence; do not merge/tag without applicable authorization.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-044 — Documentation and delivery report match foundation reality

**Level:** Static/process acceptance. **Priority:** P1. **Technique:** Checklist.

**Links:** [REQ-ENG-009](requirements.md#req-eng-009) / AC-ENG-009-02; [REQ-ENG-009](requirements.md#req-eng-009) / AC-ENG-009-03; [REQ-ENG-010](requirements.md#req-eng-010) / AC-ENG-010-01; [REQ-ENG-010](requirements.md#req-eng-010) / AC-ENG-010-02; [REQ-ENG-011](requirements.md#req-eng-011) / AC-ENG-011-01; [REQ-ENG-011](requirements.md#req-eng-011) / AC-ENG-011-02; [REQ-VAL-003](requirements.md#req-val-003) / AC-VAL-003-01; [REQ-VAL-003](requirements.md#req-val-003) / AC-VAL-003-02; [REQ-VAL-003](requirements.md#req-val-003) / AC-VAL-003-03.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Phase 1 delivered artifacts and actual reports available.

**Data/variants:** README, AGENTS, SECURITY, architecture/testing/security/runbook docs at applicable maturity, changelog, result ledger.

**Steps:**

1. Follow README setup in fresh environment; compare stated commands/features with installed artifact.
2. Inspect traceability and delivery report, acceptance and release claims.

**Expected outcomes / pass oracle:**

- Documents accurately mark future integrations unavailable; changelog records actual foundation changes.
- Each case maps to REQ/AC and actual result; planned/not-run never recorded pass.
- No unnecessary SKILL.md; release tag only when a release is accepted, not automatically on Phase 1 test completion.

**Cleanup:** Keep checklist and actual result report.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-045 — Phase 1 user walkthrough

**Level:** Acceptance — foundation only. **Priority:** P1. **Technique:** Scenario walkthrough.

**Links:** [REQ-FND-001](requirements.md#req-fnd-001) / AC-FND-001-01; [REQ-FND-001](requirements.md#req-fnd-001) / AC-FND-001-02; [REQ-FND-002](requirements.md#req-fnd-002) / AC-FND-002-01; [REQ-FND-002](requirements.md#req-fnd-002) / AC-FND-002-02; [REQ-FND-003](requirements.md#req-fnd-003) / AC-FND-003-01; [REQ-FND-003](requirements.md#req-fnd-003) / AC-FND-003-02; [REQ-FND-004](requirements.md#req-fnd-004) / AC-FND-004-01; [REQ-FND-004](requirements.md#req-fnd-004) / AC-FND-004-02; [REQ-FND-005](requirements.md#req-fnd-005) / AC-FND-005-02.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** User/reviewer on target Windows account; actual installed Phase 1 package; no live credentials.

**Data/variants:** Valid config, invalid config copy, two CLI windows and test-owned clean runtime.

**Steps:**

1. Install/start valid foundation and inspect runtime location.
2. Attempt second instance; request shutdown and restart.
3. Attempt invalid startup; review outputs and evidence.

**Expected outcomes / pass oracle:**

- User observes healthy startup, explicit rejection/error behavior and safe restart.
- No monitoring/tracking/sending is falsely claimed; foundation acceptance recorded separately from complete application acceptance.

**Cleanup:** Stop test instances and remove walkthrough runtime.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-046 — Traceability and phase boundary audit

**Level:** Static verification. **Priority:** P1. **Technique:** Coverage/impact analysis.

**Links:** [REQ-VAL-003](requirements.md#req-val-003) / AC-VAL-003-01; [REQ-VAL-003](requirements.md#req-val-003) / AC-VAL-003-02; [REQ-VAL-003](requirements.md#req-val-003) / AC-VAL-003-03; [REQ-VAL-004](requirements.md#req-val-004) / AC-VAL-004-01; [REQ-VAL-004](requirements.md#req-val-004) / AC-VAL-004-02; [REQ-ENG-010](requirements.md#req-eng-010) / AC-ENG-010-01.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Requirements v0.2.0, this specification, implemented tests and results for current phase.

**Data/variants:** Full/partial/deferred disposition matrix below; changed requirement diff.

**Steps:**

1. Resolve every linked REQ/AC/VER ID.
2. Compare executed IDs/results to designed cases and disposition matrix.
3. Inspect later-phase requirements are not silently marked complete.

**Expected outcomes / pass oracle:**

- No dangling IDs; every Phase 1 obligation has concrete evidence or explicit blocker.
- Partial foundation evidence cannot close full multi-phase requirement; future live/model reports separate.
- Requirement changes trigger review of mapped tests before claiming ongoing acceptance.

**Cleanup:** Retain audit and defect links.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-047 — External writes cannot occur in Phase 1

**Level:** System/security — foundation. **Priority:** P1. **Technique:** Negative capability testing.

**Links:** [REQ-GOV-004](requirements.md#req-gov-004) / AC-GOV-004-01; [REQ-GOV-004](requirements.md#req-gov-004) / AC-GOV-004-02; [REQ-APR-014](requirements.md#req-apr-014) / AC-APR-014-01; [REQ-ENG-005](requirements.md#req-eng-005) / AC-ENG-005-01; [REQ-ENG-005](requirements.md#req-eng-005) / AC-ENG-005-02.

**Phase boundary:** Early safety guard only; REQ-APR-014 full security/send enablement remains Phase 5..

**Preconditions:** Phase 1 package and foundation CLI; external network denied and attempts captured.

**Data/variants:** Normal start, invalid config, future-feature request, shutdown/restart.

**Steps:**

1. Execute each path with no integration configuration.
2. Inspect attempted external operations and reported feature state.

**Expected outcomes / pass oracle:**

- Zero Gmail/Jira/Ollama external operations; no send executor or fake external result.
- This is boundary evidence only: exact approval and remote uncertain-write rules remain deferred to their phases.

**Cleanup:** Stop processes; delete runtime/captures.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

### TC-P1-048 — File/resource pressure produces honest failure

**Level:** Integration/system. **Priority:** P1. **Technique:** Fault injection.

**Links:** [REQ-FND-003](requirements.md#req-fnd-003) / AC-FND-003-02; [REQ-FND-005](requirements.md#req-fnd-005) / AC-FND-005-02; [REQ-SEC-009](requirements.md#req-sec-009) / AC-SEC-009-01; [REQ-ENG-004](requirements.md#req-eng-004) / AC-ENG-004-02; [REQ-ENG-004](requirements.md#req-eng-004) / AC-ENG-004-03.

**Phase boundary:** Phase 1 behavior; not proof of later integration behavior.

**Preconditions:** Temporary runtime with delivered logger/database operations; test-only filesystem boundary injection.

**Data/variants:** Permission loss on log write; disk-full on DB commit; file open failure; existing committed baseline.

**Steps:**

1. Inject each fault where delivered behavior opens/writes resource.
2. Observe application state and outputs; reopen baseline after fault removed.

**Expected outcomes / pass oracle:**

- No false ready/commit/success result; failure is visible through available sanitized output.
- Resources released and committed baseline preserved.
- No unbounded retry; no machine-wide disk exhaustion used to arrange test.

**Cleanup:** Remove injected faults, close handles, delete runtime.

**Evidence:** shared section 5 plus the case-specific observations above. **Execution:** Not implemented / Not run.

## 7. Requirement/AC → case traceability

Every row is designed coverage only. “Full current scope” means the complete Phase 1 obligation is designed for verification, never that it has passed. Detailed requirements remain at version 0.2.0 unchanged.

| Requirement | Phase 1 disposition | Acceptance-criterion → cases | Remaining evidence |
| --- | --- | --- | --- |
| [REQ-APR-014](requirements.md#req-apr-014) | Partial current-phase evidence | AC-APR-014-01 → TC-P1-047 | Sending unavailable now; full exact-version security gate and user enablement Phase 5. |
| [REQ-AUTH-004](requirements.md#req-auth-004) | Partial current-phase evidence | AC-AUTH-004-01 → TC-P1-028, TC-P1-030; AC-AUTH-004-02 → TC-P1-028, TC-P1-030; AC-AUTH-004-03 → TC-P1-029, TC-P1-030; AC-AUTH-004-04 → later phase / checklist context; not independently exercised here | Real DPAPI/ACL mechanism now with synthetic bytes; real OAuth persistence/renewal in Phase 2. |
| [REQ-AUTH-005](requirements.md#req-auth-005) | Partial current-phase evidence | AC-AUTH-005-01 → TC-P1-011, TC-P1-029 | Delivered diagnostic boundaries now; OAuth provider response paths Phase 2. |
| [REQ-ENG-001](requirements.md#req-eng-001) | Full current scope designed | AC-ENG-001-01 → TC-P1-001, TC-P1-002; AC-ENG-001-02 → TC-P1-001, TC-P1-002, TC-P1-042; AC-ENG-001-03 → TC-P1-001 | Recheck when behavior or requirements change. |
| [REQ-ENG-002](requirements.md#req-eng-002) | Full current scope designed | AC-ENG-002-01 → TC-P1-001; AC-ENG-002-02 → TC-P1-001; AC-ENG-002-03 → TC-P1-001 | Recheck when behavior or requirements change. |
| [REQ-ENG-003](requirements.md#req-eng-003) | Full current scope designed | AC-ENG-003-01 → TC-P1-034; AC-ENG-003-02 → TC-P1-034; AC-ENG-003-03 → TC-P1-034; AC-ENG-003-04 → TC-P1-034 | Recheck when behavior or requirements change. |
| [REQ-ENG-004](requirements.md#req-eng-004) | Full current scope designed | AC-ENG-004-01 → TC-P1-003, TC-P1-013; AC-ENG-004-02 → TC-P1-021, TC-P1-031, TC-P1-048; AC-ENG-004-03 → TC-P1-021, TC-P1-031, TC-P1-048 | Recheck when behavior or requirements change. |
| [REQ-ENG-005](requirements.md#req-eng-005) | Full current scope designed | AC-ENG-005-01 → TC-P1-007, TC-P1-035, TC-P1-047; AC-ENG-005-02 → TC-P1-007, TC-P1-035, TC-P1-047 | Recheck when behavior or requirements change. |
| [REQ-ENG-006](requirements.md#req-eng-006) | Full current scope designed | AC-ENG-006-01 → TC-P1-043; AC-ENG-006-02 → TC-P1-043; AC-ENG-006-03 → TC-P1-043; AC-ENG-006-04 → TC-P1-036 | Recheck when behavior or requirements change. |
| [REQ-ENG-007](requirements.md#req-eng-007) | Full current scope designed | AC-ENG-007-01 → TC-P1-043; AC-ENG-007-02 → TC-P1-043 | Recheck when behavior or requirements change. |
| [REQ-ENG-008](requirements.md#req-eng-008) | Full current scope designed | AC-ENG-008-01 → TC-P1-037, TC-P1-038, TC-P1-039, TC-P1-042; AC-ENG-008-02 → TC-P1-042 | Recheck when behavior or requirements change. |
| [REQ-ENG-009](requirements.md#req-eng-009) | Partial current-phase evidence | AC-ENG-009-01 → TC-P1-003, TC-P1-039; AC-ENG-009-02 → TC-P1-044; AC-ENG-009-03 → TC-P1-044 | Single version/changelog now; tagging only at accepted release. |
| [REQ-ENG-010](requirements.md#req-eng-010) | Partial current-phase evidence | AC-ENG-010-01 → TC-P1-044, TC-P1-046; AC-ENG-010-02 → TC-P1-044 | Current documentation accuracy now; runbook and feature docs evolve with delivered behavior. |
| [REQ-ENG-011](requirements.md#req-eng-011) | Partial current-phase evidence | AC-ENG-011-01 → TC-P1-044; AC-ENG-011-02 → TC-P1-044 | Phase 1 report now; every subsequent delivery rechecked. |
| [REQ-ENG-012](requirements.md#req-eng-012) | Full current scope designed | AC-ENG-012-01 → TC-P1-031; AC-ENG-012-02 → TC-P1-031 | Recheck when behavior or requirements change. |
| [REQ-ENG-013](requirements.md#req-eng-013) | Full current scope designed | AC-ENG-013-01 → TC-P1-043; AC-ENG-013-02 → TC-P1-043; AC-ENG-013-03 → TC-P1-043; AC-ENG-013-04 → TC-P1-043 | Recheck when behavior or requirements change. |
| [REQ-FND-001](requirements.md#req-fnd-001) | Full current scope designed | AC-FND-001-01 → TC-P1-004, TC-P1-005, TC-P1-006, TC-P1-045; AC-FND-001-02 → TC-P1-004, TC-P1-007, TC-P1-045 | Recheck when behavior or requirements change. |
| [REQ-FND-002](requirements.md#req-fnd-002) | Full current scope designed | AC-FND-002-01 → TC-P1-004, TC-P1-008, TC-P1-045; AC-FND-002-02 → TC-P1-009, TC-P1-045 | Recheck when behavior or requirements change. |
| [REQ-FND-003](requirements.md#req-fnd-003) | Full current scope designed | AC-FND-003-01 → TC-P1-003, TC-P1-004, TC-P1-014, TC-P1-039, TC-P1-045; AC-FND-003-02 → TC-P1-003, TC-P1-005, TC-P1-009, TC-P1-021, TC-P1-045, TC-P1-048 | Recheck when behavior or requirements change. |
| [REQ-FND-004](requirements.md#req-fnd-004) | Full current scope designed | AC-FND-004-01 → TC-P1-022, TC-P1-023, TC-P1-045; AC-FND-004-02 → TC-P1-024, TC-P1-025, TC-P1-045 | Recheck when behavior or requirements change. |
| [REQ-FND-005](requirements.md#req-fnd-005) | Partial current-phase evidence | AC-FND-005-01 → TC-P1-026, TC-P1-027; AC-FND-005-02 → TC-P1-021, TC-P1-024, TC-P1-025, TC-P1-026, TC-P1-027, TC-P1-045, TC-P1-048 | Local commit/shutdown evidence now; interruptions around actual external writes in Phase 3/5. |
| [REQ-FND-006](requirements.md#req-fnd-006) | Full current scope designed | AC-FND-006-01 → TC-P1-010; AC-FND-006-02 → TC-P1-011; AC-FND-006-03 → TC-P1-012; AC-FND-006-04 → TC-P1-011 | Recheck when behavior or requirements change. |
| [REQ-FND-007](requirements.md#req-fnd-007) | Partial current-phase evidence | AC-FND-007-01 → TC-P1-027; AC-FND-007-02 → later phase / checklist context; not independently exercised here; AC-FND-007-03 → later phase / checklist context; not independently exercised here; AC-FND-007-04 → later phase / checklist context; not independently exercised here | Runner lifecycle/idle stop now; coordination of real intake/review/approval/digest in Phases 3–6. |
| [REQ-GOV-004](requirements.md#req-gov-004) | Partial current-phase evidence | AC-GOV-004-01 → TC-P1-047; AC-GOV-004-02 → TC-P1-047 | No external-write capability in foundation; actual proposal/executor boundary Phase 3 onward. |
| [REQ-GOV-006](requirements.md#req-gov-006) | Partial current-phase evidence | AC-GOV-006-01 → TC-P1-035; AC-GOV-006-02 → later phase / checklist context; not independently exercised here | No empty modules in Phase 1; reevaluate each phase. |
| [REQ-REC-001](requirements.md#req-rec-001) | Partial current-phase evidence | AC-REC-001-01 → TC-P1-017, TC-P1-026; AC-REC-001-02 → later phase / checklist context; not independently exercised here | Only delivered local state/ledger now; business events, approvals and external history in later phases. |
| [REQ-REC-002](requirements.md#req-rec-002) | Partial current-phase evidence | AC-REC-002-01 → TC-P1-004, TC-P1-014, TC-P1-018; AC-REC-002-02 → TC-P1-015, TC-P1-016; AC-REC-002-03 → TC-P1-016, TC-P1-019 | Initial schema, constraints and current version now; upgrades rechecked whenever introduced. |
| [REQ-REC-003](requirements.md#req-rec-003) | Partial current-phase evidence | AC-REC-003-01 → TC-P1-016, TC-P1-017, TC-P1-026; AC-REC-003-02 → later phase / checklist context; not independently exercised here | Delivered local transactions now; event/action atomicity and absence of network-held transactions Phase 3 onward. |
| [REQ-REC-009](requirements.md#req-rec-009) | Partial current-phase evidence | AC-REC-009-01 → TC-P1-020; AC-REC-009-02 → TC-P1-018, TC-P1-020; AC-REC-009-03 → TC-P1-019; AC-REC-009-04 → TC-P1-020 | Initial/released migration rules now; actual risky-upgrade backup behavior on first justified risky migration. |
| [REQ-REC-010](requirements.md#req-rec-010) | Partial current-phase evidence | AC-REC-010-01 → TC-P1-033; AC-REC-010-02 → TC-P1-033; AC-REC-010-03 → TC-P1-033; AC-REC-010-04 → TC-P1-033 | Delivered timestamp/path/log representation now; business dates and digest scheduling in later phases. |
| [REQ-SEC-002](requirements.md#req-sec-002) | Partial current-phase evidence | AC-SEC-002-01 → TC-P1-006 | Configuration/persisted foundation inputs now; API/model boundaries Phase 2 onward. |
| [REQ-SEC-006](requirements.md#req-sec-006) | Full current scope designed | AC-SEC-006-01 → TC-P1-032; AC-SEC-006-02 → later phase / checklist context; not independently exercised here | Recheck when behavior or requirements change. |
| [REQ-SEC-007](requirements.md#req-sec-007) | Partial current-phase evidence | AC-SEC-007-01 → TC-P1-008, TC-P1-009 | Runtime path boundaries now; real attachment handling later. |
| [REQ-SEC-009](requirements.md#req-sec-009) | Partial current-phase evidence | AC-SEC-009-01 → TC-P1-048 | Bounded foundation failure behavior now; model/input/retry budgets later. |
| [REQ-SEC-010](requirements.md#req-sec-010) | Partial current-phase evidence | AC-SEC-010-01 → TC-P1-011, TC-P1-028, TC-P1-036, TC-P1-037; AC-SEC-010-02 → later phase / checklist context; not independently exercised here | Current code, logs and secret store now; all later artifacts remain in scope. |
| [REQ-SEC-011](requirements.md#req-sec-011) | Partial current-phase evidence | AC-SEC-011-01 → TC-P1-038; AC-SEC-011-02 → TC-P1-038 | Current dependency/audit controls now; model identity/update tests Phase 2 onward. |
| [REQ-SEC-015](requirements.md#req-sec-015) | Partial current-phase evidence | AC-SEC-015-01 → TC-P1-036; AC-SEC-015-02 → TC-P1-036; AC-SEC-015-03 → TC-P1-011; AC-SEC-015-04 → later phase / checklist context; not independently exercised here | Setup/support/config behavior now; rotation walkthrough when credential integration exists. |
| [REQ-VAL-001](requirements.md#req-val-001) | Full current scope designed | AC-VAL-001-01 → TC-P1-040; AC-VAL-001-02 → TC-P1-040; AC-VAL-001-03 → TC-P1-040 | Recheck when behavior or requirements change. |
| [REQ-VAL-002](requirements.md#req-val-002) | Full current scope designed | AC-VAL-002-01 → TC-P1-041; AC-VAL-002-02 → TC-P1-041; AC-VAL-002-03 → TC-P1-041 | Recheck when behavior or requirements change. |
| [REQ-VAL-003](requirements.md#req-val-003) | Full current scope designed | AC-VAL-003-01 → TC-P1-044, TC-P1-046; AC-VAL-003-02 → TC-P1-044, TC-P1-046; AC-VAL-003-03 → TC-P1-044, TC-P1-046 | Recheck when behavior or requirements change. |
| [REQ-VAL-004](requirements.md#req-val-004) | Partial current-phase evidence | AC-VAL-004-01 → TC-P1-046; AC-VAL-004-02 → TC-P1-040, TC-P1-046 | Offline selection and no misleading live claims now; actual live/model checks later. |
| [REQ-VAL-009](requirements.md#req-val-009) | Full current scope designed | AC-VAL-009-01 → TC-P1-040; AC-VAL-009-02 → TC-P1-040; AC-VAL-009-03 → TC-P1-040; AC-VAL-009-04 → TC-P1-040 | Recheck when behavior or requirements change. |

## 8. Deferred requirements and findings from test derivation

| Requirement / topic | Disposition |
| --- | --- |
| REQ-REC-004–008 | Message/action deduplication, durable external intent, remote-outcome taxonomy, reconciliation and provider retry tests begin with actual integration/Phase 3; no empty action modules in Phase 1. Local schema/transaction basis is tested above. |
| REQ-REC-011 | Atomic external-action claim/concurrency belongs to first real action executor in Phase 3, repeated for drafts/sends in Phase 5. Phase 1 process lock is tested independently; it is not substitute evidence. |
| REQ-REC-012 | Restored-backup external-effect reconciliation remains Phase 6; migration recoverability is Phase 1. |
| REQ-SEC-003–005,013–014 | No exposure or external operations in Phase 1; active email/model/remote communication/local-service capability tests start when delivered in Phase 2 onward. |
| REQ-VAL-005–008 | Full real-email slice, full adversarial coverage, performance/model workloads and complete-release acceptance remain later phase gates. Foundation security/CI and walkthrough evidence does not close them. |
| Lifecycle/approval decision tables | ORD-01, APP-01, APR-01 and external EXEC-01 transitions are not implemented as Phase 1 business tests. Migration/lock/shutdown states get foundation transition tests now. |
| AC-AUTH-004-04 | “See DEC-15” is a reference, not independent observable behavior; use DEC-15 and AC-AUTH-004-01–03 as oracle. Source wording improvement recommended for next requirements edit; no silent baseline edit. |
| AC-FND-005-01 | “Interrupt at processing/write boundaries” is a test instruction rather than an outcome; TC-P1-026/027 assert preserved committed state and no false confirmation. External boundaries remain deferred. |
| Broad phase ranges | Requirement text includes broad 1–7 ranges. This document explicitly allocates only meaningful delivered foundation evidence. Do not close whole multi-phase requirements by passing a local subset. |
| Shutdown timeout | 10-second subprocess watchdog in TC-P1-024 is a test design threshold, not an existing production service-level promise. A failure raises a requirement/design decision; it is never silently waived. |
| Public contract binding | Exact config names, command syntax, exceptions, schema tables and Windows-supported stop mechanism must be recorded during implementation before case execution. This avoids inventing code interfaces in requirements test design. |

## 9. Foundation state-transition coverage

| Start | Stimulus | Expected state | Cases |
| --- | --- | --- | --- |
| Uninitialized | Valid startup | Initialized + ready + ownership acquired | 004,014 |
| Uninitialized | Invalid config/storage/migration | Explicit non-success, no false ready | 005–009,018,021 |
| Ready/owned | Second/concurrent start | One owner; loser rejected | 022,023 |
| Ready/owned | Normal stop | Committed state retained; ownership released | 024,027 |
| Ready/owned | Forced process death | Subsequent safe restart, no permanent stale owner | 025,026 |
| Local transaction pending | Exception/kill before commit | Uncommitted writes absent | 017,018,026 |
| Transaction committed | Stop/kill and restart | Committed writes retained | 017,025,026 |
| Secret encrypted under user A | User B read/decrypt attempt | ACL denial; copied ciphertext cannot decrypt | 028–030 |

## 10. Self-review and next implementation order

Review checks: positive/negative/boundary cases; security/data-integrity priorities; real SQLite rather than in-memory mocks; real subprocess races; Windows DPAPI evidence; complete REQ/AC link validity; cleanup and error paths; partial/deferred requirement boundaries; no live integration authorization or production scaffolding. This is an author self-review, not external independent assurance.

Implementation sequence: (1) Python package, locked tools and minimal CLI; (2) validated config/runtime paths; (3) sanitized logging; (4) initial migration/transactions; (5) instance protection and shutdown; (6) DPAPI/ACL mechanism; (7) integrated foundation walkthrough and checks. Implement each relevant test when its behavior is introduced. Reuse fixtures and parameterization rather than copying test logic or creating a separate framework.

A fresh-start system test does not replace component failure tests; many unit tests do not replace the installed Windows system check. Successful documentation validation only proves case links/structure, not correct software.
