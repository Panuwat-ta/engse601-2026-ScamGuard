# W07-01 - System Scope and Critical Journeys

## 1. Baseline and authority

| Field | Team record |
|---|---|
| Project/team | ScamGuard - Scam Image Detection Application |
| Requirement authority | `Document/srs/05_Software_Requirement_Specification.md` v1.1, 2026-09-12 |
| Requirement URL | https://github.com/Panuwat-ta/project/tree/main/Document/srs |
| Requirement hash | `99bb8d5050fa54195b02869f1815e954fdd43ad0997e732b35426c70947cd40a` |
| Frozen source baseline | https://github.com/Panuwat-ta/project, branch `main`, commit `66bc9e4a` |
| Source date referenced | 2026-09-22 |
| Primary Author | ภานุวัฒน์ |
| Assigned Peer Reviewer | เอกพันธ์ |
| Artifact status | Ready for Review; no System/UAT execution result claimed |

The local ENGSE212 working tree was observed on `develop`; it was read only and is not used as the `main` acceptance baseline. Week 07 reuses the frozen `main` source snapshots already captured in Week 05-06 so that the baseline remains reproducible without issuing Git commands in the ENGSE212 repository.

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

## 3. Critical user journeys

| Journey | User goal | Requirement trace | Main risk | W05/W06 handoff |
|---|---|---|---|---|
| J01 First use and access | consent, register, login, logout | FR-AUTH-01-04, FR-PDPA-01 | invalid consent or token behavior | W05-F03/F04/F05 |
| J02 Submit image | select, optionally crop, validate and upload | FR-SCAN-01/02 | unsupported/oversize images accepted or wrong HTTP contract | W06-F01 |
| J03 Receive trustworthy result | poll, analyze, calculate and explain | FR-SCAN-03, FR-ANALYSIS-01-04 | incomplete source/visual evidence presented as complete | W05-F01/F02, W06-F03/F05/F06 |
| J04 Understand heatmap | view, toggle, adjust opacity, zoom/pan | FR-XAI-01, NFR-06 | heatmap missing, inaccessible or misunderstood | W06-F04/F07 |
| J05 Manage evidence | view/filter/delete history and report scam | FR-HISTORY-01/02 | response/filter/report contract mismatch | W06-F08/F09 |
| J06 Exercise privacy rights | manage consent, inspect/delete data/account | FR-PDPA-01 | consent logs or deletion unavailable | W05-F04/F05 |

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
- UAT recruitment, consent/privacy notice, facilitator script and 100 real participants
- rollback and incident contact for any shared environment

## 5. Exit criteria

Design exit is reached when every scenario has trace, preconditions, steps, oracle, evidence path, owner and status. Execution exit is separate and requires raw logs/screenshots/measurements, defect disposition, peer review and reconciled result counts. Submission/acceptance must not be inferred from document generation or a repository merge event.
