# EmailJira — Verification criteria

Version 0.2.0 · 2026-10-22. Designed evidence only; no application tests executed. This is normative with requirements.md section 11.

## Execution rules

For each case, record requirement/AC IDs, fixture and tool versions, preconditions, measured observations, expected versus actual results, pass/fail, and evidence location. All listed AC assertions must pass; a partial pass is a failure. Inspect the requirement’s stated phase and source when setting the precondition. Live checks need dedicated authorized accounts/projects and explicit enablement; send checks additionally need the sending gate and approval. Use synthetic secrets and temporary real SQLite databases offline. Model-quality evidence never replaces deterministic authorization tests. For table references, every applicable row needs a named test with initial state, event, expected state/effects and forbidden effects.

## VER-GOV-001

**Requirement:** REQ-GOV-001. **Method:** Architecture/configuration inspection. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inspect a clean deployment, module imports, dependency lock and configured capabilities; attempt forbidden capabilities where relevant.

**Pass assertions:**

- AC-GOV-001-01: Inspect deployment: one application and agent.
- AC-GOV-001-02: no microservices, vector database, message broker, paid hosting, or mandatory tracing service.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-GOV-002

**Requirement:** REQ-GOV-002. **Method:** Architecture/configuration inspection. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inspect a clean deployment, module imports, dependency lock and configured capabilities; attempt forbidden capabilities where relevant.

**Pass assertions:**

- AC-GOV-002-01: Inspect dependencies and execution.
- AC-GOV-002-02: LangGraph migration starts only after user acceptance of the complete LangChain release.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-GOV-003

**Requirement:** REQ-GOV-003. **Method:** Architecture/configuration inspection. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inspect a clean deployment, module imports, dependency lock and configured capabilities; attempt forbidden capabilities where relevant.

**Pass assertions:**

- AC-GOV-003-01: Domain tests execute without LangChain, external services, or a database.
- AC-GOV-003-02: adapters and workflows own those dependencies.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-GOV-004

**Requirement:** REQ-GOV-004. **Method:** Architecture/configuration inspection. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inspect a clean deployment, module imports, dependency lock and configured capabilities; attempt forbidden capabilities where relevant.

**Pass assertions:**

- AC-GOV-004-01: A model proposal alone cannot perform an external write.
- AC-GOV-004-02: invalid proposals fail before adapter execution.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-GOV-005

**Requirement:** REQ-GOV-005. **Method:** Architecture/configuration inspection. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inspect a clean deployment, module imports, dependency lock and configured capabilities; attempt forbidden capabilities where relevant.

**Pass assertions:**

- AC-GOV-005-01: Conflicting copies resolve according to the authority table.
- AC-GOV-005-02: Jira human notes are not overwritten by application reconciliation.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-GOV-006

**Requirement:** REQ-GOV-006. **Method:** Architecture/configuration inspection. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inspect a clean deployment, module imports, dependency lock and configured capabilities; attempt forbidden capabilities where relevant.

**Pass assertions:**

- AC-GOV-006-01: Review finds no empty future modules or speculative framework.
- AC-GOV-006-02: folder names follow S3 when introduced.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-FND-001

**Requirement:** REQ-FND-001. **Method:** Offline integration + Windows walkthrough. **Delivery checkpoint:** 1.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Start clean, then invalid configuration; run two instances; inject shutdown and resource failures; advance a controlled scheduler clock.

**Pass assertions:**

- AC-FND-001-01: Missing, malformed, incompatible, or unsafe settings produce actionable errors.
- AC-FND-001-02: unavailable features cannot appear enabled.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-FND-002

**Requirement:** REQ-FND-002. **Method:** Offline integration + Windows walkthrough. **Delivery checkpoint:** 1.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Start clean, then invalid configuration; run two instances; inject shutdown and resource failures; advance a controlled scheduler clock.

**Pass assertions:**

- AC-FND-002-01: Fresh Windows startup resolves account-specific directories.
- AC-FND-002-02: unavailable or unsafe paths cause explicit failure without fallback into the repository.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-FND-003

**Requirement:** REQ-FND-003. **Method:** Offline integration + Windows walkthrough. **Delivery checkpoint:** 1.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Start clean, then invalid configuration; run two instances; inject shutdown and resource failures; advance a controlled scheduler clock.

**Pass assertions:**

- AC-FND-003-01: Fresh installation initializes successfully.
- AC-FND-003-02: invalid configuration and operational failure return non-success outcomes with sanitized explanations.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-FND-004

**Requirement:** REQ-FND-004. **Method:** Offline integration + Windows walkthrough. **Delivery checkpoint:** 1.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Start clean, then invalid configuration; run two instances; inject shutdown and resource failures; advance a controlled scheduler clock.

**Pass assertions:**

- AC-FND-004-01: A second instance is rejected.
- AC-FND-004-02: after normal termination or process death, restart follows the documented recovery procedure without concurrent execution.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-FND-005

**Requirement:** REQ-FND-005. **Method:** Offline integration + Windows walkthrough. **Delivery checkpoint:** 1.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Start clean, then invalid configuration; run two instances; inject shutdown and resource failures; advance a controlled scheduler clock.

**Pass assertions:**

- AC-FND-005-01: Interrupt at processing and write boundaries.
- AC-FND-005-02: committed work survives and unresolved external actions resume through recovery.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-FND-006

**Requirement:** REQ-FND-006. **Method:** Offline integration + Windows walkthrough. **Delivery checkpoint:** 1.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Start clean, then invalid configuration; run two instances; inject shutdown and resource failures; advance a controlled scheduler clock.

**Pass assertions:**

- AC-FND-006-01: Logs expose identifiers, decisions, durations, and outcomes.
- AC-FND-006-02: tokens, full configuration dumps, message bodies, and attachments are absent.
- AC-FND-006-03: sanitized newlines cannot forge records.
- AC-FND-006-04: names/subjects are excluded by default.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-AUTH-001

**Requirement:** REQ-AUTH-001. **Method:** Offline adapter security tests + explicitly enabled live OAuth check. **Delivery checkpoint:** 2; storage foundation in 1.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use synthetic normal, denied, malformed, expired/revoked and mismatched-account responses; run secret-capture checks; verify actual account/renewal separately on Windows.

**Pass assertions:**

- AC-AUTH-001-01: Successful consent authorizes the intended account.
- AC-AUTH-001-02: cancelled or denied consent does not.
- AC-AUTH-001-03: missing or mismatched state is rejected.
- AC-AUTH-001-04: passwords are entered only at Google.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-AUTH-002

**Requirement:** REQ-AUTH-002. **Method:** Offline adapter security tests + explicitly enabled live OAuth check. **Delivery checkpoint:** 2; storage foundation in 1.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use synthetic normal, denied, malformed, expired/revoked and mismatched-account responses; run secret-capture checks; verify actual account/renewal separately on Windows.

**Pass assertions:**

- AC-AUTH-002-01: Initial reading requests no draft or sending scopes.
- AC-AUTH-002-02: each scope has a recorded purpose.
- AC-AUTH-002-03: denied permissions disable dependent features.
- AC-AUTH-002-04: scope expansion is reviewed.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-AUTH-003

**Requirement:** REQ-AUTH-003. **Method:** Offline adapter security tests + explicitly enabled live OAuth check. **Delivery checkpoint:** 2; storage foundation in 1.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use synthetic normal, denied, malformed, expired/revoked and mismatched-account responses; run secret-capture checks; verify actual account/renewal separately on Windows.

**Pass assertions:**

- AC-AUTH-003-01: Matching identity permits processing.
- AC-AUTH-003-02: mismatched or unverified identity blocks it.
- AC-AUTH-003-03: account changes cannot silently reassign existing identities.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-AUTH-004

**Requirement:** REQ-AUTH-004. **Method:** Windows DPAPI/ACL integration. **Delivery checkpoint:** 1 storage mechanism; 2 OAuth persistence.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Persist synthetic token; inspect ciphertext and ACL; decrypt as intended account; fail decryption in wrong scope/account simulation; run Task Scheduler under intended account.

**Pass assertions:**

- AC-AUTH-004-01: Tokens are encrypted at rest with user-scoped Windows DPAPI and protected by account-restricted file permissions.
- AC-AUTH-004-02: no machine-wide protection scope.
- AC-AUTH-004-03: missing, inaccessible, or undecryptable credentials fail explicitly.
- AC-AUTH-004-04: see DEC-15 in section 11.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-AUTH-005

**Requirement:** REQ-AUTH-005. **Method:** Offline adapter security tests + explicitly enabled live OAuth check. **Delivery checkpoint:** 2; storage foundation in 1.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use synthetic normal, denied, malformed, expired/revoked and mismatched-account responses; run secret-capture checks; verify actual account/renewal separately on Windows.

**Pass assertions:**

- AC-AUTH-005-01: Access and refresh tokens, authorization codes, PKCE verifiers, and secret-bearing responses are absent from captured normal and failure outputs.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-AUTH-006

**Requirement:** REQ-AUTH-006. **Method:** Offline adapter security tests + explicitly enabled live OAuth check. **Delivery checkpoint:** 2; storage foundation in 1.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use synthetic normal, denied, malformed, expired/revoked and mismatched-account responses; run secret-capture checks; verify actual account/renewal separately on Windows.

**Pass assertions:**

- AC-AUTH-006-01: Successful renewal resumes within retry policy and securely persists returned updates.
- AC-AUTH-006-02: transient failure does not discard valid refresh credentials.
- AC-AUTH-006-03: failure cannot fabricate authorization.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-AUTH-007

**Requirement:** REQ-AUTH-007. **Method:** Offline adapter security tests + explicitly enabled live OAuth check. **Delivery checkpoint:** 2; storage foundation in 1.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use synthetic normal, denied, malformed, expired/revoked and mismatched-account responses; run secret-capture checks; verify actual account/renewal separately on Windows.

**Pass assertions:**

- AC-AUTH-007-01: Explicit reauthorization-required state is recorded.
- AC-AUTH-007-02: unattended runs do not repeatedly launch consent.
- AC-AUTH-007-03: pending local work survives reauthorization.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-AUTH-008

**Requirement:** REQ-AUTH-008. **Method:** Offline adapter security tests + explicitly enabled live OAuth check. **Delivery checkpoint:** 2; storage foundation in 1.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use synthetic normal, denied, malformed, expired/revoked and mismatched-account responses; run secret-capture checks; verify actual account/renewal separately on Windows.

**Pass assertions:**

- AC-AUTH-008-01: Configured timeouts and retry limits terminate failures.
- AC-AUTH-008-02: denial and revoked credentials do not enter transient retry loops.
- AC-AUTH-008-03: invalid certificates are rejected.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-INT-001

**Requirement:** REQ-INT-001. **Method:** Offline pagination/checkpoint integration + selected live mailbox check. **Delivery checkpoint:** 2–3; full intake in 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use messages before/at/after activation, read and unread, multiple pages, repeated IDs, older context and manual labels; inject crash, unavailable source and malformed message.

**Pass assertions:**

- AC-INT-001-01: Tests immediately before, at, and after the configured boundary follow DEC-02 semantics.
- AC-INT-001-02: selected-folder/label scope excludes unrelated messages.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-INT-002

**Requirement:** REQ-INT-002. **Method:** Offline pagination/checkpoint integration + selected live mailbox check. **Delivery checkpoint:** 2–3; full intake in 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use messages before/at/after activation, read and unread, multiple pages, repeated IDs, older context and manual labels; inject crash, unavailable source and malformed message.

**Pass assertions:**

- AC-INT-002-01: Only eligible labeled test messages enter Phase 3.
- AC-INT-002-02: expansion beyond that label is explicit in Phase 6.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-INT-003

**Requirement:** REQ-INT-003. **Method:** Offline pagination/checkpoint integration + selected live mailbox check. **Delivery checkpoint:** 2–3; full intake in 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use messages before/at/after activation, read and unread, multiple pages, repeated IDs, older context and manual labels; inject crash, unavailable source and malformed message.

**Pass assertions:**

- AC-INT-003-01: Read and unread eligible messages are discovered.
- AC-INT-003-02: changing read state cannot create a second processing identity.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-INT-004

**Requirement:** REQ-INT-004. **Method:** Offline pagination/checkpoint integration + selected live mailbox check. **Delivery checkpoint:** 2–3; full intake in 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use messages before/at/after activation, read and unread, multiple pages, repeated IDs, older context and manual labels; inject crash, unavailable source and malformed message.

**Pass assertions:**

- AC-INT-004-01: Retrieval, persisted processing state, proposals, and source links retain correct account context.
- AC-INT-004-02: thread identity alone never merges distinct business entities.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-INT-005

**Requirement:** REQ-INT-005. **Method:** Offline pagination/checkpoint integration + selected live mailbox check. **Delivery checkpoint:** 2–3; full intake in 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use messages before/at/after activation, read and unread, multiple pages, repeated IDs, older context and manual labels; inject crash, unavailable source and malformed message.

**Pass assertions:**

- AC-INT-005-01: A multi-page mailbox is processed completely within per-run limits.
- AC-INT-005-02: interrupted traversal resumes or safely rescans without duplicates or omissions.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-INT-006

**Requirement:** REQ-INT-006. **Method:** Offline pagination/checkpoint integration + selected live mailbox check. **Delivery checkpoint:** 2–3; full intake in 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use messages before/at/after activation, read and unread, multiple pages, repeated IDs, older context and manual labels; inject crash, unavailable source and malformed message.

**Pass assertions:**

- AC-INT-006-01: Crash before and after checkpoint persistence cannot permanently skip unfinished messages.
- AC-INT-006-02: replay is safe.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-INT-007

**Requirement:** REQ-INT-007. **Method:** Offline pagination/checkpoint integration + selected live mailbox check. **Delivery checkpoint:** 2–3; full intake in 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use messages before/at/after activation, read and unread, multiple pages, repeated IDs, older context and manual labels; inject crash, unavailable source and malformed message.

**Pass assertions:**

- AC-INT-007-01: Representative multipart, charset, encoded-header, and malformed messages produce correct bounded content or explicit failure.
- AC-INT-007-02: read-only live check leaves source content and labels unchanged.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-INT-008

**Requirement:** REQ-INT-008. **Method:** Offline pagination/checkpoint integration + selected live mailbox check. **Delivery checkpoint:** 2–3; full intake in 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use messages before/at/after activation, read and unread, multiple pages, repeated IDs, older context and manual labels; inject crash, unavailable source and malformed message.

**Pass assertions:**

- AC-INT-008-01: Older messages may inform an eligible case through bounded investigation.
- AC-INT-008-02: retrieval alone creates no new processing obligation or independent write.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-INT-009

**Requirement:** REQ-INT-009. **Method:** Offline pagination/checkpoint integration + selected live mailbox check. **Delivery checkpoint:** 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use messages before/at/after activation, read and unread, multiple pages, repeated IDs, older context and manual labels; inject crash, unavailable source and malformed message.

**Pass assertions:**

- AC-INT-009-01: Eligible manually labeled messages create or update review work without duplicate tasks.
- AC-INT-009-02: treatment of older labeled messages follows DEC-03.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-INT-010

**Requirement:** REQ-INT-010. **Method:** Offline pagination/checkpoint integration + selected live mailbox check. **Delivery checkpoint:** 3 bounded-label recovery; 6 full-scope catch-up.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use messages before/at/after activation, read and unread, multiple pages, repeated IDs, older context and manual labels; inject crash, unavailable source and malformed message.

**Pass assertions:**

- AC-INT-010-01: Messages accumulated during downtime are processed under the activation boundary.
- AC-INT-010-02: read state does not affect catch-up.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-AGT-001

**Requirement:** REQ-AGT-001. **Method:** Deterministic tool/schema security tests + separately enabled model evaluation. **Delivery checkpoint:** 2–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Invoke invalid outputs, forbidden tools, oversized context and a tool loop; execute frozen EVAL-01 cases with recorded identities and deadline/resource counters.

**Pass assertions:**

- AC-AGT-001-01: Real invocation returns schema-validated results.
- AC-AGT-001-02: model is a candidate until evaluation passes.
- AC-AGT-001-03: unavailable Ollama produces explicit failure without simulated output.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-AGT-002

**Requirement:** REQ-AGT-002. **Method:** Deterministic tool/schema security tests + separately enabled model evaluation. **Delivery checkpoint:** 2–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Invoke invalid outputs, forbidden tools, oversized context and a tool loop; execute frozen EVAL-01 cases with recorded identities and deadline/resource counters.

**Pass assertions:**

- AC-AGT-002-01: Agent has no send capability, unrestricted Gmail client, arbitrary HTTP, or shell.
- AC-AGT-002-02: forbidden calls fail without external effects.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-AGT-003

**Requirement:** REQ-AGT-003. **Method:** Deterministic tool/schema security tests + separately enabled model evaluation. **Delivery checkpoint:** 2–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Invoke invalid outputs, forbidden tools, oversized context and a tool loop; execute frozen EVAL-01 cases with recorded identities and deadline/resource counters.

**Pass assertions:**

- AC-AGT-003-01: Malformed, extra-forbidden, unsupported-action, and invalid-reference output cannot reach execution.
- AC-AGT-003-02: safe failure or review is explicit.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-AGT-004

**Requirement:** REQ-AGT-004. **Method:** Deterministic tool/schema security tests + separately enabled model evaluation. **Delivery checkpoint:** 2–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Invoke invalid outputs, forbidden tools, oversized context and a tool loop; execute frozen EVAL-01 cases with recorded identities and deadline/resource counters.

**Pass assertions:**

- AC-AGT-004-01: Unsupported references, invented dates, and unsupported claims are rejected or sent to review.
- AC-AGT-004-02: source evidence is retained for accepted facts.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-AGT-005

**Requirement:** REQ-AGT-005. **Method:** Deterministic tool/schema security tests + separately enabled model evaluation. **Delivery checkpoint:** 2–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Invoke invalid outputs, forbidden tools, oversized context and a tool loop; execute frozen EVAL-01 cases with recorded identities and deadline/resource counters.

**Pass assertions:**

- AC-AGT-005-01: At configured limits execution terminates explicitly without treating incomplete investigation as confident success.
- AC-AGT-005-02: values follow LIMIT-01 and EVAL-01.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-AGT-006

**Requirement:** REQ-AGT-006. **Method:** Deterministic tool/schema security tests + separately enabled model evaluation. **Delivery checkpoint:** 2–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Invoke invalid outputs, forbidden tools, oversized context and a tool loop; execute frozen EVAL-01 cases with recorded identities and deadline/resource counters.

**Pass assertions:**

- AC-AGT-006-01: Ambiguous and missing-reference evaluation cases do not produce unverified consequential writes.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-AGT-007

**Requirement:** REQ-AGT-007. **Method:** Frozen model evaluation. **Delivery checkpoint:** 2–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Freeze labels, prompts and 100 scored cases before inference; calculate each EVAL-01 numerator/denominator, unknown denominators and serious errors; any required failed metric blocks enablement.

**Pass assertions:**

- AC-AGT-007-01: Pass the predeclared evaluation protocol EVAL-01.
- AC-AGT-007-02: metrics are calculated from frozen labels and serious errors separately.
- AC-AGT-007-03: no threshold is tuned after results.
- AC-AGT-007-04: failure blocks unattended model-driven business writes.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-AGT-008

**Requirement:** REQ-AGT-008. **Method:** Deterministic tool/schema security tests + separately enabled model evaluation. **Delivery checkpoint:** 2–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Invoke invalid outputs, forbidden tools, oversized context and a tool loop; execute frozen EVAL-01 cases with recorded identities and deadline/resource counters.

**Pass assertions:**

- AC-AGT-008-01: Report includes application, prompt, model settings, available artifact identity, dependency lock identity, evaluation-set version, and results.
- AC-AGT-008-02: unavailable identity is stated.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-AGT-009

**Requirement:** REQ-AGT-009. **Method:** Deterministic tool/schema security tests + separately enabled model evaluation. **Delivery checkpoint:** 2–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Invoke invalid outputs, forbidden tools, oversized context and a tool loop; execute frozen EVAL-01 cases with recorded identities and deadline/resource counters.

**Pass assertions:**

- AC-AGT-009-01: Hostile email requesting policy changes, sending, secret retrieval, or disallowed Jira content cannot authorize those actions regardless of model compliance.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-JIR-001

**Requirement:** REQ-JIR-001. **Method:** Offline adapter/recovery tests + explicitly enabled dedicated-project check. **Delivery checkpoint:** 2–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inject denied permission, invalid field, rate limit and post-acceptance timeout; verify real actor/correlation evidence and issue/comment/link operations on test resources.

**Pass assertions:**

- AC-JIR-001-01: Authentication, actual project restrictions, and permitted operations are checked against the selected edition.
- AC-JIR-001-02: unsupported restrictions block dependent use.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-JIR-002

**Requirement:** REQ-JIR-002. **Method:** Offline adapter/recovery tests + explicitly enabled dedicated-project check. **Delivery checkpoint:** 2–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inject denied permission, invalid field, rate limit and post-acceptance timeout; verify real actor/correlation evidence and issue/comment/link operations on test resources.

**Pass assertions:**

- AC-JIR-002-01: Explicit live checks demonstrate each required operation on dedicated resources with confirmed external identities.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-JIR-003

**Requirement:** REQ-JIR-003. **Method:** Offline adapter/recovery tests + explicitly enabled dedicated-project check. **Delivery checkpoint:** 2–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inject denied permission, invalid field, rate limit and post-acceptance timeout; verify real actor/correlation evidence and issue/comment/link operations on test resources.

**Pass assertions:**

- AC-JIR-003-01: DEC-05 allowlist is enforced before every write.
- AC-JIR-003-02: unknown fields and sensitive content outside policy are rejected.
- AC-JIR-003-03: human-owned fields are preserved.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-JIR-004

**Requirement:** REQ-JIR-004. **Method:** Offline adapter/recovery tests + explicitly enabled dedicated-project check. **Delivery checkpoint:** 2–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inject denied permission, invalid field, rate limit and post-acceptance timeout; verify real actor/correlation evidence and issue/comment/link operations on test resources.

**Pass assertions:**

- AC-JIR-004-01: After timeout following accepted issue creation or comment creation, reconciliation locates the original operation rather than repeating it.
- AC-JIR-004-02: feasibility is demonstrated in Phase 2.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-JIR-005

**Requirement:** REQ-JIR-005. **Method:** Offline adapter/recovery tests + explicitly enabled dedicated-project check. **Delivery checkpoint:** 2–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inject denied permission, invalid field, rate limit and post-acceptance timeout; verify real actor/correlation evidence and issue/comment/link operations on test resources.

**Pass assertions:**

- AC-JIR-005-01: Actual API evidence identifies actor, authorization, decision, and proposal version.
- AC-JIR-005-02: app-authored or unverifiable activity cannot count as human approval.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-JIR-006

**Requirement:** REQ-JIR-006. **Method:** Offline adapter/recovery tests + explicitly enabled dedicated-project check. **Delivery checkpoint:** 2–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inject denied permission, invalid field, rate limit and post-acceptance timeout; verify real actor/correlation evidence and issue/comment/link operations on test resources.

**Pass assertions:**

- AC-JIR-006-01: Retry guidance is honored within configured bounds.
- AC-JIR-006-02: permission and invalid-request failures are not blindly retried.
- AC-JIR-006-03: uncertain non-idempotent writes go to reconciliation.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-JIR-007

**Requirement:** REQ-JIR-007. **Method:** Offline adapter/recovery tests + explicitly enabled dedicated-project check. **Delivery checkpoint:** 2–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inject denied permission, invalid field, rate limit and post-acceptance timeout; verify real actor/correlation evidence and issue/comment/link operations on test resources.

**Pass assertions:**

- AC-JIR-007-01: Configured views return representative records in each category and preserve project access restrictions.
- AC-JIR-007-02: no custom web dashboard is required.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-TRK-001

**Requirement:** REQ-TRK-001. **Method:** Offline table-driven domain tests. **Delivery checkpoint:** 3–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Parameterize every applicable ORD-01 and APP-01 row; include same reference under different accounts/merchants, repeated purchases, late arrival, partial quantities/currencies and contradictory evidence.

**Pass assertions:**

- AC-TRK-001-01: Verified reference and account matches link correctly.
- AC-TRK-001-02: sender, subject, thread, or similarity alone cannot authorize a consequential merge.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-TRK-002

**Requirement:** REQ-TRK-002. **Method:** Offline table-driven domain tests. **Delivery checkpoint:** 3–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Parameterize every applicable ORD-01 and APP-01 row; include same reference under different accounts/merchants, repeated purchases, late arrival, partial quantities/currencies and contradictory evidence.

**Pass assertions:**

- AC-TRK-002-01: Repeat purchases and separate applications retain distinct entities even when sender, item, role, or thread matches.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-TRK-003

**Requirement:** REQ-TRK-003. **Method:** Offline table-driven domain tests. **Delivery checkpoint:** 3–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Parameterize every applicable ORD-01 and APP-01 row; include same reference under different accounts/merchants, repeated purchases, late arrival, partial quantities/currencies and contradictory evidence.

**Pass assertions:**

- AC-TRK-003-01: Explicit linked references associate correctly.
- AC-TRK-003-02: unsupported cross-links produce review without merging entities.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-TRK-004

**Requirement:** REQ-TRK-004. **Method:** Offline table-driven domain tests. **Delivery checkpoint:** 3–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Parameterize every applicable ORD-01 and APP-01 row; include same reference under different accounts/merchants, repeated purchases, late arrival, partial quantities/currencies and contradictory evidence.

**Pass assertions:**

- AC-TRK-004-01: Replacement with a distinct verified order reference retains its own identity and a traceable parent relationship.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-TRK-005

**Requirement:** REQ-TRK-005. **Method:** Offline table-driven domain tests. **Delivery checkpoint:** 3–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Parameterize every applicable ORD-01 and APP-01 row; include same reference under different accounts/merchants, repeated purchases, late arrival, partial quantities/currencies and contradictory evidence.

**Pass assertions:**

- AC-TRK-005-01: Late-arriving events preserve both times and source identity.
- AC-TRK-005-02: missing event time remains unknown rather than fabricated.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-TRK-006

**Requirement:** REQ-TRK-006. **Method:** Offline table-driven domain tests. **Delivery checkpoint:** 3 confirmation/shipment subset in SLICE-01; 4 complete ORD-01.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Parameterize every applicable ORD-01 and APP-01 row; include same reference under different accounts/merchants, repeated purchases, late arrival, partial quantities/currencies and contradictory evidence.

**Pass assertions:**

- AC-TRK-006-01: Execute table ORD-01: confirmation, shipment, partial delivery, full delivery, and late-event rows produce the stated independent fulfillment outcome.
- AC-TRK-006-02: unknown/conflicting facts require review.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-TRK-007

**Requirement:** REQ-TRK-007. **Method:** Offline table-driven domain tests. **Delivery checkpoint:** 3–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Parameterize every applicable ORD-01 and APP-01 row; include same reference under different accounts/merchants, repeated purchases, late arrival, partial quantities/currencies and contradictory evidence.

**Pass assertions:**

- AC-TRK-007-01: Execute table ORD-01 return/refund rows.
- AC-TRK-007-02: return and refund dimensions retain fulfillment history.
- AC-TRK-007-03: requests alone cannot mark a refund completed.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-TRK-008

**Requirement:** REQ-TRK-008. **Method:** Offline table-driven domain tests. **Delivery checkpoint:** 3–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Parameterize every applicable ORD-01 and APP-01 row; include same reference under different accounts/merchants, repeated purchases, late arrival, partial quantities/currencies and contradictory evidence.

**Pass assertions:**

- AC-TRK-008-01: Table ORD-01 partial outcomes retain evidenced outstanding quantity/amount or unknown remainder.
- AC-TRK-008-02: a single delivered package or partial refund cannot complete an unverified whole order.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-TRK-009

**Requirement:** REQ-TRK-009. **Method:** Offline table-driven domain tests. **Delivery checkpoint:** 3–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Parameterize every applicable ORD-01 and APP-01 row; include same reference under different accounts/merchants, repeated purchases, late arrival, partial quantities/currencies and contradictory evidence.

**Pass assertions:**

- AC-TRK-009-01: Execute table APP-01.
- AC-TRK-009-02: offer, rejection, interview, and acknowledgement remain grounded in the same verified application.
- AC-TRK-009-03: contradictory terminal events require review.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-TRK-010

**Requirement:** REQ-TRK-010. **Method:** Offline table-driven domain tests. **Delivery checkpoint:** 3–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Parameterize every applicable ORD-01 and APP-01 row; include same reference under different accounts/merchants, repeated purchases, late arrival, partial quantities/currencies and contradictory evidence.

**Pass assertions:**

- AC-TRK-010-01: New confirmed schedule supersedes the prior schedule with history.
- AC-TRK-010-02: cancellation or ambiguity is explicit.
- AC-TRK-010-03: dates and deadlines are not invented.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-TRK-011

**Requirement:** REQ-TRK-011. **Method:** Offline table-driven domain tests. **Delivery checkpoint:** 3–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Parameterize every applicable ORD-01 and APP-01 row; include same reference under different accounts/merchants, repeated purchases, late arrival, partial quantities/currencies and contradictory evidence.

**Pass assertions:**

- AC-TRK-011-01: An older shipment after delivery and an older acknowledgment after interview do not regress state.
- AC-TRK-011-02: history still records accepted evidence.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-TRK-012

**Requirement:** REQ-TRK-012. **Method:** Offline table-driven domain tests. **Delivery checkpoint:** 3–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Parameterize every applicable ORD-01 and APP-01 row; include same reference under different accounts/merchants, repeated purchases, late arrival, partial quantities/currencies and contradictory evidence.

**Pass assertions:**

- AC-TRK-012-01: An evidenced return after delivery or authorized correction reopens relevant work according to DEC-09 without deleting completed history.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-TRK-013

**Requirement:** REQ-TRK-013. **Method:** Offline table-driven domain tests. **Delivery checkpoint:** 3–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Parameterize every applicable ORD-01 and APP-01 row; include same reference under different accounts/merchants, repeated purchases, late arrival, partial quantities/currencies and contradictory evidence.

**Pass assertions:**

- AC-TRK-013-01: An approval rejection does not imply job rejection.
- AC-TRK-013-02: technical failure does not change business stage.
- AC-TRK-013-03: state combinations follow the logical-state contract.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-REV-001

**Requirement:** REQ-REV-001. **Method:** Offline workflow tests + dedicated Jira human walkthrough. **Delivery checkpoint:** 3–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Create important/ambiguous obligations; acknowledge, follow up, resolve and correct with allowed and forbidden actors; compare preserved human notes and event history.

**Pass assertions:**

- AC-REV-001-01: Missing references, conflicting matches, and agreed important-email cases produce a review task rather than unsupported business changes.
- AC-REV-001-02: criteria follow DEC-06.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-REV-002

**Requirement:** REQ-REV-002. **Method:** Offline workflow tests + dedicated Jira human walkthrough. **Delivery checkpoint:** 3–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Create important/ambiguous obligations; acknowledge, follow up, resolve and correct with allowed and forbidden actors; compare preserved human notes and event history.

**Pass assertions:**

- AC-REV-002-01: Reviewer can identify the uncertainty and requested action.
- AC-REV-002-02: absent deadlines are marked absent.
- AC-REV-002-03: no invented urgency appears.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-REV-003

**Requirement:** REQ-REV-003. **Method:** Offline workflow tests + dedicated Jira human walkthrough. **Delivery checkpoint:** 3–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Create important/ambiguous obligations; acknowledge, follow up, resolve and correct with allowed and forbidden actors; compare preserved human notes and event history.

**Pass assertions:**

- AC-REV-003-01: Follow-ups for the same obligation update linked work.
- AC-REV-003-02: separate deadlines or decisions remain individually visible.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-REV-004

**Requirement:** REQ-REV-004. **Method:** Offline workflow tests + dedicated Jira human walkthrough. **Delivery checkpoint:** 3–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Create important/ambiguous obligations; acknowledge, follow up, resolve and correct with allowed and forbidden actors; compare preserved human notes and event history.

**Pass assertions:**

- AC-REV-004-01: Silence, elapsed time, app activity, and email instructions cannot resolve review.
- AC-REV-004-02: actor and decision are retained.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-REV-005

**Requirement:** REQ-REV-005. **Method:** Offline workflow tests + dedicated Jira human walkthrough. **Delivery checkpoint:** 3–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Create important/ambiguous obligations; acknowledge, follow up, resolve and correct with allowed and forbidden actors; compare preserved human notes and event history.

**Pass assertions:**

- AC-REV-005-01: Updating managed fields or source evidence leaves reviewer-authored notes intact.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-REV-006

**Requirement:** REQ-REV-006. **Method:** Offline workflow tests + dedicated Jira human walkthrough. **Delivery checkpoint:** 3–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Create important/ambiguous obligations; acknowledge, follow up, resolve and correct with allowed and forbidden actors; compare preserved human notes and event history.

**Pass assertions:**

- AC-REV-006-01: Unauthorized or unverifiable corrections are blocked.
- AC-REV-006-02: authorized changes retain actor, reason, time, prior fact, and replacement fact.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-REV-007

**Requirement:** REQ-REV-007. **Method:** Offline workflow tests + dedicated Jira human walkthrough. **Delivery checkpoint:** 3–4.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Create important/ambiguous obligations; acknowledge, follow up, resolve and correct with allowed and forbidden actors; compare preserved human notes and event history.

**Pass assertions:**

- AC-REV-007-01: Corrected matching or facts produce expected derived state without duplicating completed external actions or erasing execution history.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-APR-001

**Requirement:** REQ-APR-001. **Method:** Offline security/recovery integration + explicitly authorized live draft/send checks. **Delivery checkpoint:** 5; feasibility in 2.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Exercise every APR-01 guard and protected field individually, same-name changed attachment, forged actor, stale version, concurrent workers and timeout after acceptance; live sending remains separately gated.

**Pass assertions:**

- AC-APR-001-01: Unsupported statements and recipient identities trigger review.
- AC-APR-001-02: From, To, CC, BCC, subject, body, and attachments are explicit before approval.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-APR-002

**Requirement:** REQ-APR-002. **Method:** Offline security/recovery integration + explicitly authorized live draft/send checks. **Delivery checkpoint:** 5; feasibility in 2.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Exercise every APR-01 guard and protected field individually, same-name changed attachment, forged actor, stale version, concurrent workers and timeout after acceptance; live sending remains separately gated.

**Pass assertions:**

- AC-APR-002-01: Proposal validation precedes draft creation.
- AC-APR-002-02: draft identity and version are persisted.
- AC-APR-002-03: uncertain draft writes are represented and reconciled.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-APR-003

**Requirement:** REQ-APR-003. **Method:** Hash manifest test vectors. **Delivery checkpoint:** 5; feasibility in 2.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Run fixed payload byte vectors twice; vary every protected field and attachment filename/MIME/length/content/order; include Unicode, CRLF, whitespace and duplicate keys; compare input bytes and digest.

**Pass assertions:**

- AC-APR-003-01: Snapshot covers From, To, CC, BCC, subject, body, and attachment content identities.
- AC-APR-003-02: deterministic versioned serialization has test vectors under DEC-10.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-APR-004

**Requirement:** REQ-APR-004. **Method:** Offline security/recovery integration + explicitly authorized live draft/send checks. **Delivery checkpoint:** 5; feasibility in 2.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Exercise every APR-01 guard and protected field individually, same-name changed attachment, forged actor, stale version, concurrent workers and timeout after acceptance; live sending remains separately gated.

**Pass assertions:**

- AC-APR-004-01: Reviewer can inspect the complete payload, attachment identities, source evidence, and requested decision before approval.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-APR-005

**Requirement:** REQ-APR-005. **Method:** Offline security/recovery integration + explicitly authorized live draft/send checks. **Delivery checkpoint:** 5; feasibility in 2.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Exercise every APR-01 guard and protected field individually, same-name changed attachment, forged actor, stale version, concurrent workers and timeout after acceptance; live sending remains separately gated.

**Pass assertions:**

- AC-APR-005-01: Each decision has actor and version.
- AC-APR-005-02: silence is Pending.
- AC-APR-005-03: changes requested or rejection blocks execution.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-APR-006

**Requirement:** REQ-APR-006. **Method:** Offline security/recovery integration + explicitly authorized live draft/send checks. **Delivery checkpoint:** 5; feasibility in 2.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Exercise every APR-01 guard and protected field individually, same-name changed attachment, forged actor, stale version, concurrent workers and timeout after acceptance; live sending remains separately gated.

**Pass assertions:**

- AC-APR-006-01: Only an authorized human actor through the verified DEC-07 mechanism can approve.
- AC-APR-006-02: app-authored text, email assertions, and model output cannot approve.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-APR-007

**Requirement:** REQ-APR-007. **Method:** Offline security/recovery integration + explicitly authorized live draft/send checks. **Delivery checkpoint:** 5; feasibility in 2.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Exercise every APR-01 guard and protected field individually, same-name changed attachment, forged actor, stale version, concurrent workers and timeout after acceptance; live sending remains separately gated.

**Pass assertions:**

- AC-APR-007-01: Changing recipients, sender, subject, body, attachment membership, or attachment bytes blocks execution until fresh approval.
- AC-APR-007-02: same filename with different bytes is detected.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-APR-008

**Requirement:** REQ-APR-008. **Method:** Offline security/recovery integration + explicitly authorized live draft/send checks. **Delivery checkpoint:** 5; feasibility in 2.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Exercise every APR-01 guard and protected field individually, same-name changed attachment, forged actor, stale version, concurrent workers and timeout after acceptance; live sending remains separately gated.

**Pass assertions:**

- AC-APR-008-01: Table APR-01 invalidates approval on corrected relevant facts, changed schedule/deadline, contradicted recipient/action, or cancelled obligation.
- AC-APR-008-02: unrelated messages do not invalidate approval.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-APR-009

**Requirement:** REQ-APR-009. **Method:** Offline security/recovery integration + explicitly authorized live draft/send checks. **Delivery checkpoint:** 5; feasibility in 2.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Exercise every APR-01 guard and protected field individually, same-name changed attachment, forged actor, stale version, concurrent workers and timeout after acceptance; live sending remains separately gated.

**Pass assertions:**

- AC-APR-009-01: Executor verifies reviewer, current version, payload integrity, relevance, prior execution, and send enablement.
- AC-APR-009-02: missing or uncertain checks block sending.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-APR-010

**Requirement:** REQ-APR-010. **Method:** Offline security/recovery integration + explicitly authorized live draft/send checks. **Delivery checkpoint:** 5; feasibility in 2.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Exercise every APR-01 guard and protected field individually, same-name changed attachment, forged actor, stale version, concurrent workers and timeout after acceptance; live sending remains separately gated.

**Pass assertions:**

- AC-APR-010-01: Execution evidence identifies the approved payload.
- AC-APR-010-02: edits to an editable Gmail draft cannot cause different content to be sent under old approval.
- AC-APR-010-03: no separate race workstream is required.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-APR-011

**Requirement:** REQ-APR-011. **Method:** Offline security/recovery integration + explicitly authorized live draft/send checks. **Delivery checkpoint:** 5; feasibility in 2.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Exercise every APR-01 guard and protected field individually, same-name changed attachment, forged actor, stale version, concurrent workers and timeout after acceptance; live sending remains separately gated.

**Pass assertions:**

- AC-APR-011-01: Concurrent requests and restart/replay cannot send a confirmed action again.
- AC-APR-011-02: uncertain actions remain blocked pending reconciliation.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-APR-012

**Requirement:** REQ-APR-012. **Method:** Offline security/recovery integration + explicitly authorized live draft/send checks. **Delivery checkpoint:** 5; feasibility in 2.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Exercise every APR-01 guard and protected field individually, same-name changed attachment, forged actor, stale version, concurrent workers and timeout after acceptance; live sending remains separately gated.

**Pass assertions:**

- AC-APR-012-01: A timeout after remote acceptance cannot be reported as confirmed failure or silently retried.
- AC-APR-012-02: provider evidence is retained for confirmed results.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-APR-013

**Requirement:** REQ-APR-013. **Method:** Offline security/recovery integration + explicitly authorized live draft/send checks. **Delivery checkpoint:** 5; feasibility in 2.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Exercise every APR-01 guard and protected field individually, same-name changed attachment, forged actor, stale version, concurrent workers and timeout after acceptance; live sending remains separately gated.

**Pass assertions:**

- AC-APR-013-01: Located sent message is linked to the original action.
- AC-APR-013-02: unresolved uncertainty requires human review.
- AC-APR-013-03: absence of reliable evidence does not authorize blind retry.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-APR-014

**Requirement:** REQ-APR-014. **Method:** Offline security/recovery integration + explicitly authorized live draft/send checks. **Delivery checkpoint:** 5; feasibility in 2.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Exercise every APR-01 guard and protected field individually, same-name changed attachment, forged actor, stale version, concurrent workers and timeout after acceptance; live sending remains separately gated.

**Pass assertions:**

- AC-APR-014-01: Forged and stale approval, changed fields and attachments, replay, concurrency, hostile input, and uncertain-send tests pass before explicit enablement is recorded.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-REC-001

**Requirement:** REQ-REC-001. **Method:** Real temporary SQLite crash/concurrency/recovery tests. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Run fresh/upgrade stores with constraints; fail before/after commit and before/after remote acceptance; race two claims; restore an older backup and reconcile original operations.

**Pass assertions:**

- AC-REC-001-01: Verified mappings, events, intended actions, approvals, execution records, and checkpoints survive restart.
- AC-REC-001-02: retained content follows policy.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-REC-002

**Requirement:** REQ-REC-002. **Method:** Real temporary SQLite crash/concurrency/recovery tests. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Run fresh/upgrade stores with constraints; fail before/after commit and before/after remote acceptance; race two claims; restore an older backup and reconcile original operations.

**Pass assertions:**

- AC-REC-002-01: Fresh creation and supported upgrades preserve data.
- AC-REC-002-02: foreign keys and uniqueness are verified.
- AC-REC-002-03: released migrations are not modified.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-REC-003

**Requirement:** REQ-REC-003. **Method:** Real temporary SQLite crash/concurrency/recovery tests. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Run fresh/upgrade stores with constraints; fail before/after commit and before/after remote acceptance; race two claims; restore an older backup and reconcile original operations.

**Pass assertions:**

- AC-REC-003-01: Injected failure cannot leave half-accepted event/action state.
- AC-REC-003-02: no network request holds a long database transaction.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-REC-004

**Requirement:** REQ-REC-004. **Method:** Real temporary SQLite crash/concurrency/recovery tests. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Run fresh/upgrade stores with constraints; fail before/after commit and before/after remote acceptance; race two claims; restore an older backup and reconcile original operations.

**Pass assertions:**

- AC-REC-004-01: Duplicate message discovery, event replay, and restart create no duplicate tracking issue or event comment.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-REC-005

**Requirement:** REQ-REC-005. **Method:** Real temporary SQLite crash/concurrency/recovery tests. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Run fresh/upgrade stores with constraints; fail before/after commit and before/after remote acceptance; race two claims; restore an older backup and reconcile original operations.

**Pass assertions:**

- AC-REC-005-01: Crash before submission leaves recoverable intent.
- AC-REC-005-02: crash after remote acceptance enters reconciliation with the same correlation identity.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-REC-006

**Requirement:** REQ-REC-006. **Method:** Real temporary SQLite crash/concurrency/recovery tests. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Run fresh/upgrade stores with constraints; fail before/after commit and before/after remote acceptance; race two claims; restore an older backup and reconcile original operations.

**Pass assertions:**

- AC-REC-006-01: Network timeout after submission remains uncertain until evidence resolves it.
- AC-REC-006-02: no fabricated success or automatic reclassification to safe-to-retry.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-REC-007

**Requirement:** REQ-REC-007. **Method:** Real temporary SQLite crash/concurrency/recovery tests. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Run fresh/upgrade stores with constraints; fail before/after commit and before/after remote acceptance; race two claims; restore an older backup and reconcile original operations.

**Pass assertions:**

- AC-REC-007-01: Injected interruptions after Jira issue and event-comment acceptance locate original writes.
- AC-REC-007-02: inconclusive lookup remains uncertain or goes to review.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-REC-008

**Requirement:** REQ-REC-008. **Method:** Real temporary SQLite crash/concurrency/recovery tests. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Run fresh/upgrade stores with constraints; fail before/after commit and before/after remote acceptance; race two claims; restore an older backup and reconcile original operations.

**Pass assertions:**

- AC-REC-008-01: Transient, invalid-request, permission, and uncertain outcomes follow distinct policies.
- AC-REC-008-02: retry exhaustion exposes unfinished work.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-REC-009

**Requirement:** REQ-REC-009. **Method:** Real temporary SQLite crash/concurrency/recovery tests. **Delivery checkpoint:** 1; revalidated for each upgrade.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Run fresh/upgrade stores with constraints; fail before/after commit and before/after remote acceptance; race two claims; restore an older backup and reconcile original operations.

**Pass assertions:**

- AC-REC-009-01: Back up before risky upgrades.
- AC-REC-009-02: an injected migration failure preserves recoverable data and reports failure.
- AC-REC-009-03: released migrations are immutable.
- AC-REC-009-04: destructive automatic rollback is not promised.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-REC-010

**Requirement:** REQ-REC-010. **Method:** Real temporary SQLite crash/concurrency/recovery tests. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Run fresh/upgrade stores with constraints; fail before/after commit and before/after remote acceptance; race two claims; restore an older backup and reconcile original operations.

**Pass assertions:**

- AC-REC-010-01: Instants store consistently in UTC.
- AC-REC-010-02: displays/schedules use Europe/Berlin.
- AC-REC-010-03: date-only evidence remains a date.
- AC-REC-010-04: unknown timezone is explicit.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-DIG-001

**Requirement:** REQ-DIG-001. **Method:** Offline controlled-clock and report-content tests. **Delivery checkpoint:** 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use known items in all categories, zero and unavailable categories, overlapping windows, unresolved work, overflow and repeated/restarted generation; reconcile report index and counts to fixtures.

**Pass assertions:**

- AC-DIG-001-01: Digest covers important information/deadlines, pending reviews/approvals, order/application changes, newsletters/announcements, advertising, social activity, and processing failures.
- AC-DIG-001-02: zero-count categories are distinguishable from failed collection.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-DIG-002

**Requirement:** REQ-DIG-002. **Method:** Offline controlled-clock and report-content tests. **Delivery checkpoint:** 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use known items in all categories, zero and unavailable categories, overlapping windows, unresolved work, overflow and repeated/restarted generation; reconcile report index and counts to fixtures.

**Pass assertions:**

- AC-DIG-002-01: Summary claims and deadlines trace to evidence.
- AC-DIG-002-02: counts reconcile to the defined DEC-12 window and category rules.
- AC-DIG-002-03: unsupported claims are excluded or flagged.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-DIG-003

**Requirement:** REQ-DIG-003. **Method:** Offline controlled-clock and report-content tests. **Delivery checkpoint:** 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use known items in all categories, zero and unavailable categories, overlapping windows, unresolved work, overflow and repeated/restarted generation; reconcile report index and counts to fixtures.

**Pass assertions:**

- AC-DIG-003-01: Unresolved reviews and approvals remain visible on later days until explicitly resolved.
- AC-DIG-003-02: older unresolved deadlines remain identifiable.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-DIG-004

**Requirement:** REQ-DIG-004. **Method:** Offline controlled-clock and report-content tests. **Delivery checkpoint:** 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use known items in all categories, zero and unavailable categories, overlapping windows, unresolved work, overflow and repeated/restarted generation; reconcile report index and counts to fixtures.

**Pass assertions:**

- AC-DIG-004-01: Restart and missed-run handling do not accidentally duplicate an already completed digest.
- AC-DIG-004-02: incomplete reports are not reported as complete.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-DIG-005

**Requirement:** REQ-DIG-005. **Method:** Offline controlled-clock and report-content tests. **Delivery checkpoint:** 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use known items in all categories, zero and unavailable categories, overlapping windows, unresolved work, overflow and repeated/restarted generation; reconcile report index and counts to fixtures.

**Pass assertions:**

- AC-DIG-005-01: Unavailable services cannot produce a misleading all-clear report.
- AC-DIG-005-02: known failures and omitted data are explicit.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-OPS-001

**Requirement:** REQ-OPS-001. **Method:** Offline time/storage tests + Windows clean-environment walkthrough. **Delivery checkpoint:** 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Advance clocks across DST gap/overlap and downtime; verify Task Scheduler under intended account, toast failures, retention boundaries, backup during use and clean restore.

**Pass assertions:**

- AC-OPS-001-01: Clean target-account setup starts the correct locked environment, uses account runtime paths, and reports failures without embedded credentials.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-OPS-002

**Requirement:** REQ-OPS-002. **Method:** Deterministic scheduling table tests. **Delivery checkpoint:** 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use Europe/Berlin spring gap and autumn overlap fixtures plus multi-day sleep and changed configured time; assert exact UTC window endpoints and stable one-report identity.

**Pass assertions:**

- AC-OPS-002-01: Spring gap, autumn overlap, sleep across scheduled time, and multiple missed days follow DEC-12 without accidental repeated windows.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-OPS-003

**Requirement:** REQ-OPS-003. **Method:** Offline time/storage tests + Windows clean-environment walkthrough. **Delivery checkpoint:** 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Advance clocks across DST gap/overlap and downtime; verify Task Scheduler under intended account, toast failures, retention boundaries, backup during use and clean restore.

**Pass assertions:**

- AC-OPS-003-01: DEC-13 scenarios notify the correct user without exposing unnecessary private content.
- AC-OPS-003-02: notification failure is visible and does not discard work.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-OPS-004

**Requirement:** REQ-OPS-004. **Method:** Offline time/storage tests + Windows clean-environment walkthrough. **Delivery checkpoint:** 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Advance clocks across DST gap/overlap and downtime; verify Task Scheduler under intended account, toast failures, retention boundaries, backup during use and clean restore.

**Pass assertions:**

- AC-OPS-004-01: Backup during permitted operation restores to a valid database.
- AC-OPS-004-02: schedule, location, retention, and protection follow DEC-14.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-OPS-005

**Requirement:** REQ-OPS-005. **Method:** Offline time/storage tests + Windows clean-environment walkthrough. **Delivery checkpoint:** 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Advance clocks across DST gap/overlap and downtime; verify Task Scheduler under intended account, toast failures, retention boundaries, backup during use and clean restore.

**Pass assertions:**

- AC-OPS-005-01: Demonstration restores structured work and safely reconciles external effects.
- AC-OPS-005-02: unavailable account-bound credentials require documented reauthorization.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-OPS-006

**Requirement:** REQ-OPS-006. **Method:** Offline time/storage tests + Windows clean-environment walkthrough. **Delivery checkpoint:** 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Advance clocks across DST gap/overlap and downtime; verify Task Scheduler under intended account, toast failures, retention boundaries, backup during use and clean restore.

**Pass assertions:**

- AC-OPS-006-01: Expired records are removed under DEC-14.
- AC-OPS-006-02: pending approvals, uncertain actions, and required correction evidence remain protected until policy permits deletion.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-OPS-007

**Requirement:** REQ-OPS-007. **Method:** Offline time/storage tests + Windows clean-environment walkthrough. **Delivery checkpoint:** 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Advance clocks across DST gap/overlap and downtime; verify Task Scheduler under intended account, toast failures, retention boundaries, backup during use and clean restore.

**Pass assertions:**

- AC-OPS-007-01: A clean-environment walkthrough succeeds.
- AC-OPS-007-02: steps cover stopping processing, disabling sending, rotating exposed credentials, and reviewing uncertain operations.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-SEC-001

**Requirement:** REQ-SEC-001. **Method:** Adversarial offline boundary tests + scoped configuration inspection. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Submit hostile instructions, disclosure attempts, SQL/command strings, traversal, malformed/oversized content and active markup; capture network calls, outputs, storage access and side effects.

**Pass assertions:**

- AC-SEC-001-01: Model covers credentials, private content, business facts, human decisions, and execution history.
- AC-SEC-001-02: each material threat has a mitigation and verification link.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-SEC-002

**Requirement:** REQ-SEC-002. **Method:** Adversarial offline boundary tests + scoped configuration inspection. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Submit hostile instructions, disclosure attempts, SQL/command strings, traversal, malformed/oversized content and active markup; capture network calls, outputs, storage access and side effects.

**Pass assertions:**

- AC-SEC-002-01: Malformed configuration, API responses, database values, tool arguments, and model output fail explicitly without unauthorized effects.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-SEC-003

**Requirement:** REQ-SEC-003. **Method:** Adversarial offline boundary tests + scoped configuration inspection. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Submit hostile instructions, disclosure attempts, SQL/command strings, traversal, malformed/oversized content and active markup; capture network calls, outputs, storage access and side effects.

**Pass assertions:**

- AC-SEC-003-01: Direct and indirect prompt-injection cases cannot change policy, enable sending, approve actions, or bypass field restrictions.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-SEC-004

**Requirement:** REQ-SEC-004. **Method:** Adversarial offline boundary tests + scoped configuration inspection. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Submit hostile instructions, disclosure attempts, SQL/command strings, traversal, malformed/oversized content and active markup; capture network calls, outputs, storage access and side effects.

**Pass assertions:**

- AC-SEC-004-01: Agent cannot choose arbitrary network destinations.
- AC-SEC-004-02: Jira field allowlist and recipient approval checks reject exfiltration attempts through permitted tools.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-SEC-005

**Requirement:** REQ-SEC-005. **Method:** Adversarial offline boundary tests + scoped configuration inspection. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Submit hostile instructions, disclosure attempts, SQL/command strings, traversal, malformed/oversized content and active markup; capture network calls, outputs, storage access and side effects.

**Pass assertions:**

- AC-SEC-005-01: Invalid certificates and destinations are rejected.
- AC-SEC-005-02: tokens are not in URLs or logs.
- AC-SEC-005-03: loopback OAuth redirects and local Ollama may use HTTP only on loopback, never an untrusted remote interface.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-SEC-006

**Requirement:** REQ-SEC-006. **Method:** Adversarial offline boundary tests + scoped configuration inspection. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Submit hostile instructions, disclosure attempts, SQL/command strings, traversal, malformed/oversized content and active markup; capture network calls, outputs, storage access and side effects.

**Pass assertions:**

- AC-SEC-006-01: Injection strings supplied as values cannot alter query structure, retrieve unrelated rows, or execute additional statements.
- AC-SEC-006-02: permitted dynamic identifiers come only from fixed allowlists.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-SEC-007

**Requirement:** REQ-SEC-007. **Method:** Adversarial offline boundary tests + scoped configuration inspection. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Submit hostile instructions, disclosure attempts, SQL/command strings, traversal, malformed/oversized content and active markup; capture network calls, outputs, storage access and side effects.

**Pass assertions:**

- AC-SEC-007-01: Traversal, invalid filenames, oversized inputs, and malformed attachments fail safely without writing outside permitted locations.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-SEC-008

**Requirement:** REQ-SEC-008. **Method:** Adversarial offline boundary tests + scoped configuration inspection. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Submit hostile instructions, disclosure attempts, SQL/command strings, traversal, malformed/oversized content and active markup; capture network calls, outputs, storage access and side effects.

**Pass assertions:**

- AC-SEC-008-01: Malicious HTML/markup cannot execute in generated views or trigger unintended network requests.
- AC-SEC-008-02: output is encoded for its destination.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-SEC-009

**Requirement:** REQ-SEC-009. **Method:** Adversarial offline boundary tests + scoped configuration inspection. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Submit hostile instructions, disclosure attempts, SQL/command strings, traversal, malformed/oversized content and active markup; capture network calls, outputs, storage access and side effects.

**Pass assertions:**

- AC-SEC-009-01: Oversized input, tool loops, service failure, and excessive retries terminate within agreed DEC-08 limits and preserve recoverable state.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-SEC-010

**Requirement:** REQ-SEC-010. **Method:** Adversarial offline boundary tests + scoped configuration inspection. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Submit hostile instructions, disclosure attempts, SQL/command strings, traversal, malformed/oversized content and active markup; capture network calls, outputs, storage access and side effects.

**Pass assertions:**

- AC-SEC-010-01: Secret scan and synthetic private-content tests cover code, fixtures, package metadata, logs, reports, and example configuration.
- AC-SEC-010-02: exposures trigger revocation/rotation procedures.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-SEC-011

**Requirement:** REQ-SEC-011. **Method:** Adversarial offline boundary tests + scoped configuration inspection. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Submit hostile instructions, disclosure attempts, SQL/command strings, traversal, malformed/oversized content and active markup; capture network calls, outputs, storage access and side effects.

**Pass assertions:**

- AC-SEC-011-01: Locked dependency and recorded model changes receive relevant tests and security review.
- AC-SEC-011-02: no unverified automatic updates.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-SEC-012

**Requirement:** REQ-SEC-012. **Method:** Adversarial offline boundary tests + scoped configuration inspection. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Submit hostile instructions, disclosure attempts, SQL/command strings, traversal, malformed/oversized content and active markup; capture network calls, outputs, storage access and side effects.

**Pass assertions:**

- AC-SEC-012-01: Test scope records permitted accounts/projects.
- AC-SEC-012-02: adversarial scenarios cannot target unrelated mailboxes, users, or third-party systems.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-ENG-001

**Requirement:** REQ-ENG-001. **Method:** Development/release evidence inspection + clean locked checks. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Review source/diff/instructions/configuration; run locked install, lint/format/type/offline coverage/security/build checks as applicable; record actual tool results and human security review.

**Pass assertions:**

- AC-ENG-001-01: requires-python is >=3.12,<3.13.
- AC-ENG-001-02: supported installs and CI use 3.12.
- AC-ENG-001-03: introduced dependencies are compatible.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-ENG-002

**Requirement:** REQ-ENG-002. **Method:** Development/release evidence inspection + clean locked checks. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Review source/diff/instructions/configuration; run locked install, lint/format/type/offline coverage/security/build checks as applicable; record actual tool results and human security review.

**Pass assertions:**

- AC-ENG-002-01: Clean locked installation succeeds.
- AC-ENG-002-02: runtime and development dependencies are separated.
- AC-ENG-002-03: additions solve a present need and contain no secret-bearing URLs.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-ENG-003

**Requirement:** REQ-ENG-003. **Method:** Development/release evidence inspection + clean locked checks. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Review source/diff/instructions/configuration; run locked install, lint/format/type/offline coverage/security/build checks as applicable; record actual tool results and human security review.

**Pass assertions:**

- AC-ENG-003-01: Formatting, lint, and type checks pass.
- AC-ENG-003-02: functions have meaningful annotations.
- AC-ENG-003-03: unrestricted Any exceptions are justified.
- AC-ENG-003-04: public behavior is documented.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-ENG-004

**Requirement:** REQ-ENG-004. **Method:** Development/release evidence inspection + clean locked checks. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Review source/diff/instructions/configuration; run locked install, lint/format/type/offline coverage/security/build checks as applicable; record actual tool results and human security review.

**Pass assertions:**

- AC-ENG-004-01: Imports perform no network calls or database writes.
- AC-ENG-004-02: specific exceptions preserve sanitized causes.
- AC-ENG-004-03: no broad swallowed failures or mutable-default defects.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-ENG-005

**Requirement:** REQ-ENG-005. **Method:** Development/release evidence inspection + clean locked checks. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Review source/diff/instructions/configuration; run locked install, lint/format/type/offline coverage/security/build checks as applicable; record actual tool results and human security review.

**Pass assertions:**

- AC-ENG-005-01: Review finds no required behavior replaced by TODO, pass, ellipsis, NotImplementedError, fake responses, silent no-ops, or fallback simulations.
- AC-ENG-005-02: mocks remain in tests/evaluation tooling.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-ENG-006

**Requirement:** REQ-ENG-006. **Method:** Development/release evidence inspection + clean locked checks. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Review source/diff/instructions/configuration; run locked install, lint/format/type/offline coverage/security/build checks as applicable; record actual tool results and human security review.

**Pass assertions:**

- AC-ENG-006-01: Diff and checks are reviewed before merge.
- AC-ENG-006-02: remote PRs are used where available.
- AC-ENG-006-03: shared history is not rewritten without authorization.
- AC-ENG-006-04: no private runtime files are committed.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-ENG-007

**Requirement:** REQ-ENG-007. **Method:** Development/release evidence inspection + clean locked checks. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Review source/diff/instructions/configuration; run locked install, lint/format/type/offline coverage/security/build checks as applicable; record actual tool results and human security review.

**Pass assertions:**

- AC-ENG-007-01: Approval/sending, credentials, and migrations have recorded human review before acceptance.
- AC-ENG-007-02: automated checks do not substitute for that review.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-ENG-008

**Requirement:** REQ-ENG-008. **Method:** Development/release evidence inspection + clean locked checks. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Review source/diff/instructions/configuration; run locked install, lint/format/type/offline coverage/security/build checks as applicable; record actual tool results and human security review.

**Pass assertions:**

- AC-ENG-008-01: Locked install, Ruff format/lint, mypy, offline tests and coverage, secret scan, vulnerability check, and package build execute without production credentials.
- AC-ENG-008-02: Windows-specific behavior is tested on Windows.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-ENG-009

**Requirement:** REQ-ENG-009. **Method:** Development/release evidence inspection + clean locked checks. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Review source/diff/instructions/configuration; run locked install, lint/format/type/offline coverage/security/build checks as applicable; record actual tool results and human security review.

**Pass assertions:**

- AC-ENG-009-01: Version follows agreed 0.x semantic progression and PEP 440.
- AC-ENG-009-02: changelog records user-visible changes and migration actions.
- AC-ENG-009-03: accepted releases are tagged.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-ENG-010

**Requirement:** REQ-ENG-010. **Method:** Development/release evidence inspection + clean locked checks. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Review source/diff/instructions/configuration; run locked install, lint/format/type/offline coverage/security/build checks as applicable; record actual tool results and human security review.

**Pass assertions:**

- AC-ENG-010-01: README, AGENTS, SECURITY, requirements, architecture, test strategy, threat model, security tests, runbook, and changelog match delivered behavior.
- AC-ENG-010-02: SKILL.md appears only for an established reusable workflow.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-ENG-011

**Requirement:** REQ-ENG-011. **Method:** Development/release evidence inspection + clean locked checks. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Review source/diff/instructions/configuration; run locked install, lint/format/type/offline coverage/security/build checks as applicable; record actual tool results and human security review.

**Pass assertions:**

- AC-ENG-011-01: Each delivery identifies requirement/acceptance coverage, actual checks, limitations, and next phase step.
- AC-ENG-011-02: implemented, offline-tested, live-verified, and user-accepted states are distinct.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-VAL-001

**Requirement:** REQ-VAL-001. **Method:** Verification evidence audit. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inspect test configuration, separate coverage groups, frozen model evaluation, scoped live reports and acceptance ledger; deliberately missing/failed evidence must prevent a pass.

**Pass assertions:**

- AC-VAL-001-01: No production credentials or model/API network calls are required.
- AC-VAL-001-02: synthetic fixtures and temporary real SQLite databases are used.
- AC-VAL-001-03: external boundaries rather than internal methods are mocked.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-VAL-002

**Requirement:** REQ-VAL-002. **Method:** Verification evidence audit. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inspect test configuration, separate coverage groups, frozen model evaluation, scoped live reports and acceptance ledger; deliberately missing/failed evidence must prevent a pass.

**Pass assertions:**

- AC-VAL-002-01: Critical targets: 100% statements and branches.
- AC-VAL-002-02: other targets: 90% statements and 85% branches.
- AC-VAL-002-03: justified exclusions and any shortfall are visible and require resolution before acceptance.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-VAL-003

**Requirement:** REQ-VAL-003. **Method:** Verification evidence audit. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inspect test configuration, separate coverage groups, frozen model evaluation, scoped live reports and acceptance ledger; deliberately missing/failed evidence must prevent a pass.

**Pass assertions:**

- AC-VAL-003-01: Every requirement maps to planned evidence and later concrete test/report IDs.
- AC-VAL-003-02: critical recovery and security scenarios have named evidence.
- AC-VAL-003-03: documentation mapping is not reported as executed tests.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-VAL-004

**Requirement:** REQ-VAL-004. **Method:** Verification evidence audit. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inspect test configuration, separate coverage groups, frozen model evaluation, scoped live reports and acceptance ledger; deliberately missing/failed evidence must prevent a pass.

**Pass assertions:**

- AC-VAL-004-01: Separate reports identify resource scope, identities, outcomes, and limitations.
- AC-VAL-004-02: mocked results cannot be represented as live proof.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-VAL-005

**Requirement:** REQ-VAL-005. **Method:** Live first-slice acceptance. **Delivery checkpoint:** 3.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Execute each SLICE-01 row on dedicated real Gmail/Jira resources, recording message/action/remote IDs; inspect restart and post-acceptance interruption outcomes.

**Pass assertions:**

- AC-VAL-005-01: Execute the Phase 3 slice in table SLICE-01: a verified order confirmation creates tracking, a follow-up updates it, ambiguity creates review, duplicate/restart replay adds nothing, and accepted issue/comment timeouts reconcile without duplicate writes.
- AC-VAL-005-02: sending unavailable.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-VAL-006

**Requirement:** REQ-VAL-006. **Method:** Verification evidence audit. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inspect test configuration, separate coverage groups, frozen model evaluation, scoped live reports and acceptance ledger; deliberately missing/failed evidence must prevent a pass.

**Pass assertions:**

- AC-VAL-006-01: Prompt injection, approval bypass/replay, exfiltration, SQL/command injection, traversal, unsafe rendering, exhaustion, leakage, and recovery abuse have recorded results and reviewed findings.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-VAL-007

**Requirement:** REQ-VAL-007. **Method:** Verification evidence audit. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inspect test configuration, separate coverage groups, frozen model evaluation, scoped live reports and acceptance ledger; deliberately missing/failed evidence must prevent a pass.

**Pass assertions:**

- AC-VAL-007-01: Representative workload measurements are compared with DEC-08 limits.
- AC-VAL-007-02: no invented performance claim or unmeasured threshold is accepted.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-VAL-008

**Requirement:** REQ-VAL-008. **Method:** Verification evidence audit. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inspect test configuration, separate coverage groups, frozen model evaluation, scoped live reports and acceptance ledger; deliberately missing/failed evidence must prevent a pass.

**Pass assertions:**

- AC-VAL-008-01: Offline unit/integration/system/acceptance checks, live checks, model results, security findings, and human workflow walkthrough are reviewed.
- AC-VAL-008-02: release-blocking defects resolved and limitations recorded before user acceptance/tagging.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-MIG-001

**Requirement:** REQ-MIG-001. **Method:** Deferred baseline-comparison audit + regression suite. **Delivery checkpoint:** 8 only.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Only after initial user acceptance, compare LangChain baseline and migration under the same functional/security/recovery/model/live cases and data compatibility procedures.

**Pass assertions:**

- AC-MIG-001-01: No migration starts before complete LangChain acceptance.
- AC-MIG-001-02: accepted source, dependencies, prompts, data format, and tests remain recoverable.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-MIG-002

**Requirement:** REQ-MIG-002. **Method:** Deferred baseline-comparison audit + regression suite. **Delivery checkpoint:** 8 only.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Only after initial user acceptance, compare LangChain baseline and migration under the same functional/security/recovery/model/live cases and data compatibility procedures.

**Pass assertions:**

- AC-MIG-002-01: Existing acceptance tests and live/security/model/recovery checks establish behavioral equivalence.
- AC-MIG-002-02: compatibility and rollback plan is reviewed.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-MIG-003

**Requirement:** REQ-MIG-003. **Method:** Deferred baseline-comparison audit + regression suite. **Delivery checkpoint:** 8 only.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Only after initial user acceptance, compare LangChain baseline and migration under the same functional/security/recovery/model/live cases and data compatibility procedures.

**Pass assertions:**

- AC-MIG-003-01: Functional/resource comparison and migration limitations are reviewed before separate user acceptance and release.
- AC-MIG-003-02: optional tracing requires demonstrated need.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-REC-011

**Requirement:** REQ-REC-011. **Method:** Two-worker race, every external action type. **Delivery checkpoint:** 1 execution foundation; 3 Jira; 5 drafts/sends.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Release two workers simultaneously against one durable action; observe adapter call count, claim ownership and final state; kill owner after submission and restart.

**Pass assertions:**

- AC-REC-011-01: Two workers racing to claim one Jira create/update/comment, draft-create, or send action result in at most one active submission.
- AC-REC-011-02: confirmed actions cannot be reclaimed.
- AC-REC-011-03: abandoned in-progress actions enter reconciliation, not blind resubmission.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-REC-012

**Requirement:** REQ-REC-012. **Method:** Real temporary SQLite crash/concurrency/recovery tests. **Delivery checkpoint:** 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Run fresh/upgrade stores with constraints; fail before/after commit and before/after remote acceptance; race two claims; restore an older backup and reconcile original operations.

**Pass assertions:**

- AC-REC-012-01: Restore a snapshot older than a confirmed issue/comment/draft/send.
- AC-REC-012-02: no previously completed action is repeated without definitive reconciliation.
- AC-REC-012-03: inconclusive evidence blocks that action and creates review.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-FND-007

**Requirement:** REQ-FND-007. **Method:** Controlled-clock runner integration. **Delivery checkpoint:** 1 runner lifecycle; 3 intake/recovery; 4 review; 5 approval; 6 digest.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Make one message fail while a verified human decision and digest become due; advance 60 seconds; restart after a decision was made offline; inspect all queues and guarded resumption.

**Pass assertions:**

- AC-FND-007-01: Each enabled activity runs under section 11 intervals.
- AC-FND-007-02: one malformed message cannot indefinitely starve decision checking.
- AC-FND-007-03: restart discovers decisions made while offline and resumes only validated work.
- AC-FND-007-04: missing scopes disable dependent activities explicitly.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-SEC-013

**Requirement:** REQ-SEC-013. **Method:** Adversarial offline boundary tests + scoped configuration inspection. **Delivery checkpoint:** 2–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Submit hostile instructions, disclosure attempts, SQL/command strings, traversal, malformed/oversized content and active markup; capture network calls, outputs, storage access and side effects.

**Pass assertions:**

- AC-SEC-013-01: Shell metacharacters, scripts, executable attachments, and instructions remain data.
- AC-SEC-013-02: no production handler invokes their contents.
- AC-SEC-013-03: extraction beyond supported limits stops explicitly.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-SEC-014

**Requirement:** REQ-SEC-014. **Method:** Adversarial offline boundary tests + scoped configuration inspection. **Delivery checkpoint:** 2–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Submit hostile instructions, disclosure attempts, SQL/command strings, traversal, malformed/oversized content and active markup; capture network calls, outputs, storage access and side effects.

**Pass assertions:**

- AC-SEC-014-01: No application-created OAuth callback or Ollama integration requires LAN exposure.
- AC-SEC-014-02: remote endpoint configuration is rejected in this local-only scope.
- AC-SEC-014-03: runtime credentials are not exposed through local diagnostic endpoints.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-ENG-012

**Requirement:** REQ-ENG-012. **Method:** Development/release evidence inspection + clean locked checks. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Review source/diff/instructions/configuration; run locked install, lint/format/type/offline coverage/security/build checks as applicable; record actual tool results and human security review.

**Pass assertions:**

- AC-ENG-012-01: Review verifies context managers for managed files/transactions/resources, no wildcard imports or hidden mutable global state, composition over unnecessary inheritance, and comments explaining intent without redundant narration.
- AC-ENG-012-02: no arbitrary function-size rules.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-ENG-013

**Requirement:** REQ-ENG-013. **Method:** Development/release evidence inspection + clean locked checks. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Review source/diff/instructions/configuration; run locked install, lint/format/type/offline coverage/security/build checks as applicable; record actual tool results and human security review.

**Pass assertions:**

- AC-ENG-013-01: Each task identifies its requirement and relevant existing artifacts.
- AC-ENG-013-02: edits remain focused.
- AC-ENG-013-03: focused checks precede applicable broader checks.
- AC-ENG-013-04: diff, recovery/security impact, and affected documentation are reviewed before delivery.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-VAL-009

**Requirement:** REQ-VAL-009. **Method:** Verification evidence audit. **Delivery checkpoint:** 1–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Inspect test configuration, separate coverage groups, frozen model evaluation, scoped live reports and acceptance ledger; deliberately missing/failed evidence must prevent a pass.

**Pass assertions:**

- AC-VAL-009-01: Domain correctness tests run without model invocation.
- AC-VAL-009-02: tests assert public outcomes rather than private call order.
- AC-VAL-009-03: generated tests use Hypothesis only where justified.
- AC-VAL-009-04: failures cannot be concealed by weakened assertions or unjustified exclusions.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-INT-011

**Requirement:** REQ-INT-011. **Method:** Offline pagination/checkpoint integration + selected live mailbox check. **Delivery checkpoint:** 3; expanded in 6.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Use messages before/at/after activation, read and unread, multiple pages, repeated IDs, older context and manual labels; inject crash, unavailable source and malformed message.

**Pass assertions:**

- AC-INT-011-01: Pagination failure, deleted source message, and malformed content have separate recorded outcomes.
- AC-INT-011-02: checkpoint progress cannot skip unfinished mail.
- AC-INT-011-03: one poison message is isolated and exposed while other eligible work progresses.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

## VER-SEC-015

**Requirement:** REQ-SEC-015. **Method:** Adversarial offline boundary tests + scoped configuration inspection. **Delivery checkpoint:** 0–7.

**Preconditions:** Relevant feature/configuration is present; known expected inputs and initial state are fixed; external effects are captured offline or explicitly enabled on dedicated live resources.

**Procedure:** Submit hostile instructions, disclosure attempts, SQL/command strings, traversal, malformed/oversized content and active markup; capture network calls, outputs, storage access and side effects.

**Pass assertions:**

- AC-SEC-015-01: Setup instructions use local credential entry.
- AC-SEC-015-02: examples contain empty named settings only.
- AC-SEC-015-03: production configuration and diagnostics never dump full secrets.
- AC-SEC-015-04: exposed credentials follow revocation/rotation steps before reuse.

**Fail rule:** Any unmet assertion, unauthorized side effect, missing mandatory observation, or unresolved result fails this case. No invented success.

**Evidence required:** Case inputs, initial/final state or inspection checklist, observed effects, relevant identifiers and sanitized output; separate offline/live/model/human results. **Status:** Not executed.

