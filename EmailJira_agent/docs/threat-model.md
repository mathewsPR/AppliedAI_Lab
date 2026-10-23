# EmailJira threat model

Version 0.1.0 · 2026-10-22 · Design analysis, not penetration-test evidence. Boundaries derive from [architecture](architecture.md); controls from [requirements](requirements.md); planned evidence from [security test plan](security-test-plan.md).

## Assets, actors and assumptions

| Asset | Harm if compromised |
| --- | --- |
| OAuth/Jira credentials | Unauthorized mailbox/project access and writes |
| Private mail/evidence/attachments | Disclosure to Jira, recipients, logs or malicious endpoints |
| Verified mapping/events/corrections | Wrong entity merges, deadlines, lifecycle decisions and obligations |
| Human notes/decisions/approved version | Forged authorization or unintended outgoing content |
| Execution/checkpoint/backup history | Duplicate writes/sends, skipped work or replay after restore |
| Local resource/service availability | Unbounded processing, unavailable reviews/digests, lost recovery |

Actors include external sender/attachment author, hostile quoted/forwarded content author, compromised dependency/model artifact, unauthorized Jira participant, another local user, and accidental operator/network/process failure. Trusted components include reviewed deterministic app code, intended Windows account/administration and authenticated provider interfaces within their demonstrated capabilities. Provider content remains untrusted input. Local administrator/same-user malware compromise is outside account-scoped protection guarantees; record this limitation, not a promise of isolation.

## Trust boundaries

| Boundary | Crossing | Enforced invariant |
| --- | --- | --- |
| B1 | Gmail/attachments → decoder/agent | Bounded safe data; no execution, no policy authority |
| B2 | Agent/tools/proposal → deterministic workflow | Allowlisted read capabilities and validated structured proposals; no unrestricted clients |
| B3 | Workflow → Jira | Per-project/field/content policy and stable correlated write; human fields preserved |
| B4 | Jira decision → executor | Verified authorized human actor and exact version, not app text |
| B5 | Approved snapshot/editable draft → Gmail send | Approved protected content only, current relevance, exclusive claim, no previous/uncertain execution |
| B6 | Files/SQLite/backup → trusted runtime state | ACL/DPAPI, validation, constraints, migrations, safe restore/reconciliation |
| B7 | External/local HTTP endpoints → runtime | Remote TLS verification and configured provider endpoints; loopback-only local services |
| B8 | Logs/reports/notifications/build → user or repository | Minimal sanitized output; no secrets/private source copy |

## Threat/control matrix

Likelihood is qualitative design prioritization, not a measured probability. H/M indicate high/medium potential risk based on exposure and consequence. Requirement and test IDs connect each mitigation to designed evidence; residual risk remains until executed checks and feasibility review.

| ID | Boundary / scenario | Impact; priority | Controls | Planned evidence | Residual/assumption |
| --- | --- | --- | --- | --- | --- |
| TH-01 | B1/B2 email instructs model to override policy or send | Unauthorized action; H | REQ-AGT-002/003/009; REQ-SEC-003 | SEC-TC-001,002 | Model may obey text; deterministic guards must still deny authority. |
| TH-02 | B2/B3 private context exfiltrated through allowed Jira fields | Privacy loss; H | REQ-JIR-003; REQ-SEC-004 | SEC-TC-003 | Redaction/allowlist must inspect actual payload, not trust prompt. |
| TH-03 | B4 forged/unauthorized/app-authored approval | Unwanted send; H | REQ-JIR-005; REQ-APR-006/009 | SEC-TC-004,005 | Provider actor evidence must be feasible in selected Jira. |
| TH-04 | B5 stale version or changed draft/attachment | Different content sent; H | REQ-APR-003/007/010 | SEC-TC-006,007 | No invented remote atomicity; execution must use approved protected content. |
| TH-05 | B5 changed schedule/cancelled obligation after approval | Obsolete harmful reply; H | REQ-APR-008/009 | SEC-TC-008 | Relevance based on latest accepted verified facts. |
| TH-06 | B5/B6 concurrent/replayed execution | Duplicate write/send; H | REQ-REC-004/011; REQ-APR-011 | SEC-TC-009 | Process lock alone insufficient; atomic per-action claim required. |
| TH-07 | B3/B5 timeout after remote acceptance | Blind retry duplicates; H | REQ-REC-005–007; REQ-APR-012/013 | SEC-TC-010,011 | Inconclusive lookup remains blocked. |
| TH-08 | B6 old backup revives completed action | Duplicate send/write; H | REQ-REC-012; REQ-OPS-005 | SEC-TC-012 | Local snapshot may omit new remote effects. |
| TH-09 | B6/B8 token/config disclosure | Account compromise; H | REQ-AUTH-004/005; REQ-SEC-010/015 | SEC-TC-013,014 | DPAPI is not same-user malware protection. |
| TH-10 | B6 SQL/command/path payload from source data | Corruption/execution; H | REQ-SEC-006/007/013 | SEC-TC-015,016 | Inspect all paths and identifiers, not only body text. |
| TH-11 | B1/B8 active HTML and remote image retrieval | Execution/tracking/disclosure; M | REQ-SEC-008 | SEC-TC-017 | Rendering destination must escape content correctly. |
| TH-12 | B1/B2 resource exhaustion/retry storm | Denial of service; M | REQ-AGT-005; REQ-SEC-009 | SEC-TC-018 | Hardware targets unmeasured until evaluation. |
| TH-13 | B7 invalid TLS/endpoint/local LAN exposure | Credential interception; H | REQ-AUTH-008; REQ-SEC-005/014 | SEC-TC-019 | Loopback trust limited to intended host account model. |
| TH-14 | B6 migration/crash/constraint failure | Lost or inconsistent facts; H | REQ-REC-002/003/009 | SEC-TC-020 | No automatic destructive rollback promise. |
| TH-15 | B2/B3 invented reference/deadline, bad merge or late event | Wrong tracking/action; H | REQ-AGT-004/006/007; REQ-TRK-001/008/011 | SEC-TC-021 | Finite model metrics do not replace deterministic validation/review. |
| TH-16 | B4 unauthorized correction or lost human notes | Integrity loss; H | REQ-REV-005–007; REQ-GOV-005 | SEC-TC-022 | Verify correction actor and retain superseded facts. |
| TH-17 | B8 malicious dependency/model artifact | Trusted-code compromise; H | REQ-SEC-011; REQ-ENG-002/008 | SEC-TC-023 | Lock/scanning reduce risk, do not certify supply chain. |
| TH-18 | B8 forged log or notification leakage | Misleading audit/privacy loss; M | REQ-FND-006; REQ-OPS-003 | SEC-TC-024 | Generic notification retains no private body/subject. |

## Security invariants and negative outcomes

No agent tool grants send/write authority; no untrusted text approves actions. No unsafe merge or completion without verified evidence. No field-content policy bypass. No send on missing/invalid/stale/unverifiable approval, disabled send, changed payload, obsolete purpose, prior confirmation or uncertain outcome. No timeout/restart/backup authorizes blind replay. If safety cannot be established, preserve evidence and produce explicit failure/uncertainty/review rather than invented success.

## Risk treatment and review triggers

Accept only the documented local-account trust assumption, finite evaluation limitation, provider outage and account-bound recovery limitations; these are design assumptions, not user approval of exploitable defects. Reduce other threats with mapped controls; demonstrate feasibility before dependent writes. Review this model after new capabilities/scopes, Jira decision mechanism, dependency/model updates, payload schema, migrations, endpoint exposure or restore changes. Exploitable applicable findings block release until resolved; human review verifies residual risk and proposed scope changes. Detailed operational recovery commands arrive with implemented operation in Phase 6.
