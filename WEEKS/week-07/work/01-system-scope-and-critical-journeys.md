# W07-01 - System Scope and Critical Journeys

## 1. Baseline and authority

| Field | Team record |
|---|---|
| Project/team | ScamGuard - Scam Image Detection Application |
| Requirement authority | `Document/srs/05_Software_Requirement_Specification.md` v1.1, 2026-09-12 |
| Requirement URL | https://github.com/Panuwat-ta/project/tree/main/Document/srs |
| Requirement hash | `99bb8d5050fa54195b02869f1815e954fdd43ad0997e732b35426c70947cd40a` |
| Historical source baseline | https://github.com/Panuwat-ta/project, branch `main`, commit `66bc9e4a` (Week 05-06 risk evidence) |
| Project testing authority | https://github.com/Panuwat-ta/project/tree/develop/tests_all |
| Test-design branch/commit | `develop` / `162e0249abb9e9940f014ba6d5182d38213bc771` |
| Source date referenced | 2026-09-23 |
| Primary Author | ภานุวัฒน์ |
| Assigned Peer Reviewer | เอกพันธ์ |
| Artifact status | Ready for Review; no System/UAT execution result claimed |

Week 07 separates authorities: requirement IDs/Acceptance Criteria come from SRS v1.1 on `main`, while the project's Master Test Plan, manual/E2E cases, RTM and execution reports come from the pinned `develop/tests_all` baseline. Frozen `main` evidence from Week 05-06 remains historical risk input only. `/home/panuwat/project` was inspected read-only without Git commands.

## 2. System boundary

In scope for System Test design:

1. Mobile onboarding, registration, login and logout
2. Gallery selection, optional crop/skip and client-side validation
3. Upload, asynchronous processing/polling and ownership control
4. OCR, visual analysis, source-verification state and risk calculation
5. Result explanation and heatmap controls
6. History, deletion and report submission
7. Consent/account deletion and protected-resource behavior
8. Error recovery and honest degraded-state messaging

Out of scope for a Week 07 Pass claim until separate evidence exists:

- 1,000-image model accuracy/mDice evaluation
- 100-concurrent-user performance test
- one-month uptime measurement
- production Google Vision behavior
- production Redis/PostgreSQL/GPU availability
- security penetration testing
- stakeholder approval or independent peer-review sign-off

## 3. Project E2E journeys used by Week 07

| Project TC | Journey | Priority | Main Week 07 risk |
|---|---|---:|---|
| TC-E2E-SCAN-01 | Full User Scam Detection Journey | P0 | integrated upload, AI, heatmap and history behavior |
| TC-E2E-CACHE-02 | High-Speed Cache Hit Workflow | P0 | Redis/media consistency and latency |
| TC-E2E-REPORT-03 | User Incident Reporting to Admin Review | P1 | report/audit contract across user and admin |
| TC-E2E-MODEL-04 | AI Model Deployment to Live Inference | P1 | deploy/rollback and live worker behavior |
| TC-E2E-BAN-05 | Malicious Actor Ban and Session Revocation | P1 | 403 handling and session revocation |
| TC-E2E-OFFLINE-06 | Offline Storage and Reconnection Sync | P2 | local cache/recovery and requirement-trace gap |
| TC-E2E-FULL-07 | Full Lifecycle Register to Audit Verification | P1 | register-to-audit data continuity |
| TC-E2E-AUTH-08 | Mid Journey Access Expiry With Refresh Resume | P1 | token refresh without losing journey state |
| TC-E2E-REG-09 | Post Deploy Scan Regression Stability | P1 | result-contract stability after model deployment |
| TC-E2E-HIST-10 | History Delete Then Detail Not Found | P2 | DB/media deletion consistency and audit retention |

## 4. Entry criteria for real execution

All items below require objective evidence before execution status can move from `Not Executed`/`Not Ready`:

- approved mobile build identifier and API deployment URL
- code/build baseline mapped to the frozen requirement baseline or an approved change record
- isolated test database, Redis, object/media storage and model dependencies
- controlled test accounts for at least two users and one admin where relevant
- licensed/consented image test-data package with expected ground truth
- production-adapter disposition for source verification
- fixed or explicitly accepted known gaps from Week 05-06
- logging/timing capture that does not expose secrets or personal data
- selected UAT option, recruitment, consent/privacy notice and facilitator script
- 100 valid participants only when claiming the NFR-06 population metric
- rollback and incident contact for any shared environment

## 5. Exit criteria

Design exit is reached when every scenario has trace, preconditions, steps, oracle, evidence path, owner and status. Execution exit is separate and requires raw logs/screenshots/measurements, defect disposition, peer review and reconciled result counts. Submission/acceptance must not be inferred from document generation or a repository merge event.
