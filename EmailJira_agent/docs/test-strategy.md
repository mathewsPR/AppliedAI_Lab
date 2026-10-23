# EmailJira test strategy

Version 0.1.0 · 2026-10-22 · Applies to [requirements](requirements.md), [verification criteria](verification-criteria.md) and [Phase 1 cases](phase-1-test-cases.md). Designed evidence is not executed evidence.

## Objectives and method

Demonstrate agreed user outcomes, policy enforcement, data integrity, recovery and bounded operation. Use risk-based design with equivalence partitions, boundary values, decision tables, state transitions, adversarial cases and meaningful structural coverage. ISTQB CTFL terminology/techniques are guidance, not product certification; [official syllabus](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf) is supplementary to the accepted standards baseline. No wholesale ISO 29119 adoption or new testing platform is required.

Trace source → REQ → AC → VER → detailed case/variant → implemented pytest/check/report → result/defect. Each mapping states full current-phase or partial evidence. One case may support related criteria; one requirement may need many cases. Reviewing a sentence, inventing a VER ID or passing a model evaluation cannot prove deterministic system behavior.

## Levels and types

| Level | What is exercised | Introduced |
| --- | --- | --- |
| Unit | Public deterministic config/domain/policy/hash/time behavior, without model | With delivered rule, Phase 1 onward |
| Component integration | Collaborating workflows/adapters, real temporary SQLite, actual resource management | Phase 1 onward |
| System | Whole delivered installed app via public runner/CLI, failure/restart/concurrency | Foundation in Phase 1; full SLICE-01 in Phase 3 |
| System integration | Actual authorized Gmail/Jira/Ollama interactions and Windows capabilities | Explicitly enabled Phase 2; Windows foundation checks in Phase 1 |
| Acceptance | User outcome walkthrough against phase gates | Each phase; complete application in Phase 7 |

Security, reliability/recovery, performance, usability of review/approval, platform compatibility and regression are cross-cutting test types. Offline/live are environments, not distinct test levels. Static inspection/build/process checks are recorded separately from dynamic tests. Model quality is evaluated separately from code tests using EVAL-01, never treated as a policy permission system.

## Environments and isolation

- Default pytest runs offline, no production credentials, external APIs or local model required. Synthetic sanitized fixtures; controlled clocks; real temporary SQLite; real subprocesses for lifecycle/instance behavior. Mock only appropriate external boundaries.
- Windows-specific DPAPI/ACL/Task Scheduler/notification/process behavior executes on Windows under isolated authorized account/runtime. Linux tests/mocks are insufficient platform evidence.
- Live checks use dedicated explicitly selected Gmail/Jira resources, bounded actions and recorded account/project scope; consent/credentials entered locally. Sending remains separately gated. Use real provider evidence for actor/correlation feasibility.
- Build/install/advisory tooling may require approved downloads; this does not authorize runtime integration calls. Locked environments, recorded tool/OS/commit/prompt/model/test-set identities support repeatability.
- Never add production fakes, unused schemas/modules or simulation switches just to satisfy tests. Unsupported feature remains unavailable. Fault injection belongs to tests/evaluation tooling.

## Responsibilities and review

Developer implements behavior and relevant tests together. Test designer derives oracles independently from requirements and reviews negative/recovery coverage. Assistant can perform both but must identify self-review honestly. User is acceptance owner and human reviewer for security-sensitive changes; no fictional independent assurance. CI automates checks and evidence collection without granting user authority or release acceptance.

## Gates and evidence

| Gate | Required evidence |
| --- | --- |
| Phase 0 entry to development | Complete requirements/authority/decision/threat/test documentation; critical planned mappings; external unknowns have owners and gates |
| Phase 1 | Relevant TC-P1 cases and variants, locked build/tool checks, Windows foundation evidence and human sensitive-change review |
| Before first Jira write | Permitted fields, validation, no untrusted authorization and sanitized diagnostics verified; actual access/correlation feasibility |
| Before unattended model-driven writes | Frozen EVAL-01 set/labels/thresholds scored and passed; no retrospective threshold tuning |
| Before live sending | Complete protected-field/actor/version/relevance/concurrency/uncertainty security checks and explicit enablement plus per-message human approval |
| Operational release | Scheduling/DST, downtime, backup restoration/replay protection, retention, notifications, full offline/live/model/security/performance and human walkthrough |

Before a case executes, bind concrete public command/config/schema/version to its specification; record preconditions and expected observations. Statuses: Planned, Implemented/not run, Pass, Fail, Blocked, Not applicable with rationale. Missing required evidence cannot pass. Store sanitized inputs, observations, IDs, expected/actual, environment and defect links. A test result belongs to a revision/environment, not all future versions.

Critical deterministic policies target 100% statements and branches; other deterministic code 90% statements/85% branches. Classify only existing files; separately report group denominators and justified exclusions. No future empty policy group reported as 100% proven. No weakened assertions or unjustified exclusions to meet a number. Thresholds are targets adopted as acceptance gates; shortfalls require resolution before dependent acceptance.

Required PR/release-candidate checks: locked install, Ruff format/lint, mypy, offline tests/coverage, secret scan, dependency vulnerability audit and package build; Python 3.12 with actual Windows jobs where needed. Current cases are in [phase-1-test-cases.md](phase-1-test-cases.md). Full critical security case inventory is in [security-test-plan.md](security-test-plan.md).

## Regression and defects

Fixes receive reproducing regression tests. Requirement/decision changes trigger impact analysis of cases, fixtures, migration, approval snapshots and operations. Run focused checks first, then applicable broader gates; do not repeat unrelated suites without cause. Triage actual impact/exploitability, retain findings/rationale and block release for applicable exploitable vulnerabilities or failed mandatory acceptance. No unsupported global security guarantee from finite tests.

## Phase discipline and remaining work

Implement executable tests alongside each feature; no complete unused test suite now. Use planned tests/unit, tests/integration, tests/acceptance, tests/security and evaluations directories incrementally with clear markers. Detailed Phase 2+ cases are elaborated before dependent implementation using current VER/security scenarios. No tests, coverage, integrations or model evaluations have been executed at Phase 0 closeout. Exact reference-only AC wording is interpreted in the Phase 0 validation report, not counted as a passing behavior.
