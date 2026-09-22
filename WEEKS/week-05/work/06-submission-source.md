<style>
body { font-family: sans-serif; font-size: 10.5pt; line-height: 1.35; }
h1 { font-size: 21pt; margin-bottom: 4px; }
h2 { font-size: 15pt; margin-top: 18px; border-bottom: 1px solid #bbb; padding-bottom: 3px; }
h3 { font-size: 12pt; margin-top: 14px; }
table { width: 100%; border-collapse: collapse; margin: 8px 0 12px; font-size: 8.3pt; table-layout: fixed; }
th, td { border: 1px solid #aaa; padding: 4px 5px; vertical-align: top; overflow-wrap: anywhere; }
th { font-weight: 700; }
code { font-size: 9pt; }
.small { font-size: 8.5pt; }
</style>

# ENGSE601 Week 05 - Component Test Case Set v1

**Project:** ScamGuard - Scam Image Detection Application  
**Activity:** Code & Logic Reading Clinic  
**Author:** ภานุวัฒน์ ต๋าคำ  
**Date:** 22 September 2026  
**Artifact status:** Ready for Review

## 1. Test Basis and Scope

Canonical Requirement/SRS: `https://github.com/Panuwat-ta/project/tree/main/Document/srs`, branch `main`, SRS v1.1 dated 2026-09-12. Source-code baseline: `https://github.com/Panuwat-ta/project`, branch `main`, commit `66bc9e4a`.
Scope covers four current requirements/components: FR-ANALYSIS-02 (`onnx_worker.py`), FR-ANALYSIS-04 (`risk_calculator.py`), FR-AUTH-01 (`auth.py` + schema), and FR-PDPA-01 (`ConsentLog` + user/consent routes). W03/W04 are used only as historical handoff when consistent with SRS v1.1.

Out of scope: dataset-level Accuracy/F1/mDice, GPU performance, full System/UAT journey, and unstated retroactive research-data rules.

## 2. Execution Summary

| Result | Count | Meaning |
|---|---:|---|
| Pass | 7 | Executed/inspected result aligns with SRS v1.1 |
| Fail | 9 | Executed/inspected implementation does not align with SRS v1.1 |
| Not Ready | 1 | Required component contract is not yet available for an independent test |
| Needs Clarification | 1 | Requirement example conflicts with its own algorithm semantics |
| **Total** | **18** | Component test cases in this artifact |

Evidence is stored as plain text under `WEEKS/week-05/work/evidence/`; the reproducible probe is `work/probes/component_probe.py`.

## 3. Component Test Cases

### 3.1 Visual Analysis - FR-ANALYSIS-02

| ID | AC | Expected | Actual | Result |
|---|---|---|---|---|
| CT-01 | AC-1 | Separate `forgery_confidence` 0-100 traceable to forgery signal | Worker exposes `visual_risk_score`; no `forgery_confidence` key | Fail |
| CT-02 | AC-2 | Separate `ai_gen_confidence` from AI-Gen detector | `ai_gen_prob` is max SegFormer probability; no separate AI-Gen field | Fail |
| CT-03 | AC-3 | Visual-score calculation can be tested from canonical signals | Separate signals/contract required by SRS are not available on main | Not Ready |
### 3.2 Risk Calculation - FR-ANALYSIS-04

| ID | AC | Input | Expected | Actual | Result |
|---|---|---|---|---|---|
| CT-04 | AC-1 | 50/85/0 | 90, High, primary visual | `90 high visual True` | Pass |
| CT-05 | AC-2 | 100/100/100 | cap at 100, High | `100 high visual True` | Pass |
| CT-06 | AC-3 | score basis 10 | Low | `10 low` | Pass |
| CT-07 | AC-4 | score basis 30 | Low | `30 low` | Pass |
| CT-08 | AC-5 | score basis 55 | Medium | `55 medium` | Pass |
| CT-09 | AC-6 | score basis 80 | High | `80 high` | Pass |
| CT-10 | AC-7 | stated 65 total / 85 visual | High by visual override | Hybrid max uses visual in base; same calculator cannot produce total 65 when visual is 85 | Needs Clarification |

### 3.3 Registration - FR-AUTH-01

| ID | AC | Expected | Actual | Result |
|---|---|---|---|---|
| CT-11 | AC-1 | successful response has `id, full_name, email, role, status, created_at` | response keys: `email, full_name, id, message, role` | Fail |
| CT-12 | AC-5 | System Consent=false -> HTTP 400, create nothing | handler returns `UserResponse` and adds User + ConsentLog(false,false) | Fail |
| CT-13 | AC-1 subcondition | Research Consent=false must not block registration | handler succeeds and persists research=false | Pass |

### 3.4 Consent Management - FR-PDPA-01
| ID | AC | Expected | Actual | Result |
|---|---|---|---|---|
| CT-14 | AC-2 | event/log model supports `consent_type`, `is_granted`, timestamp and 2 records | current model stores one row with two booleans | Fail |
| CT-15 | AC-3 | `PUT /consent/research` revokes research consent and records update | endpoint not present on main | Fail |
| CT-16 | AC-4 | GET `/users/me` returns current-user profile | profile GET is `/api/v1/auth/me`; `/api/v1/users/me` is DELETE | Fail |
| CT-17 | AC-5 | GET `/consent/logs` returns consent history | endpoint not present on main | Fail |
| CT-18 | AC-3/5 | consent history supports `updated_at` | current ConsentLog has `created_at` only | Fail |

## 4. Evidence

### E05-01 Existing automated test

`server/tests/utils/test_risk_calculator.py` on the isolated main baseline:

```text
.                                                                        [100%]
1 passed in 0.03s
```

### E05-02 Reproducible component probe

The probe confirms Hybrid max+bonus examples/boundaries, registration handler behavior, route inventory, and the Visual Analysis output contract. Raw evidence: `work/evidence/E05-component-probe.txt`.

### E05-03 Baseline record

`work/evidence/E05-baseline.txt` records the ENGSE212 main commit and the SHA-256/version of canonical SRS v1.1 used for this artifact.
## 5. Findings and Handoff

| Finding | Disposition / next action |
|---|---|
| F01 Visual dual-signal contract absent | Accepted implementation gap; fix ENGSE212 visual/AI-Gen output contract, then re-test |
| F02 AC-7 example is not producible by Hybrid max+bonus | Clarify canonical SRS wording; does not invalidate AC-1/2 algorithm evidence |
| F03 Register response misses `status`/`created_at` | Fix response schema/handler and add contract test |
| F04 System Consent=false is accepted | Add validation/guard before persistence and re-test |
| F05 Consent storage differs from event-log SRS contract | Reconcile schema/migration before integration testing |
| F06 Research-consent update/log routes missing | Implement endpoints and component tests |
| F07 `/users/me` route contract mismatch | Select canonical route and sync SRS/code via controlled change |
| F08 W03/W04 used v1.0 | Closed for W05; SRS v1.1 is current authority |

These product defects do not invalidate the Week 05 V&V artifact: failed tests are preserved as evidence and handed off to W06/W07/W14 rather than converted to Pass.

## 6. AI Use and Integrity

AI was used to organize test cases, run read-only/local verification through Remote Desktop Commander, compare code with SRS, and draft the report. All expected results were checked against SRS v1.1; all actual results come from executed probes/tests or direct source-contract inspection. No test result, stakeholder decision, screenshot, or approval was fabricated.

No `.env`, token, API key, production password, or production database content is included. The component probe uses test-only configuration and an in-memory fake DB.

## 7. Review Gate

Author-side Definition of Done is complete: canonical source/version is pinned, 18 test cases are traceable, raw evidence is stored, findings have owner/next action, and AI use is disclosed.

Per `TEAM.md`, independent human peer review by **เอกพันธ์** is still required before merge/tag as `Submitted`. Until that sign-off exists, this artifact is **Ready for Review** and must not be represented as peer-reviewed or Submitted.
