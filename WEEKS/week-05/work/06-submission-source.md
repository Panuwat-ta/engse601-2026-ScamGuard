<style>
@page { size: A4; margin: 15mm 14mm 16mm 14mm; }
body { font-family: Arial, "Noto Sans Thai", sans-serif; font-size: 9.7pt; line-height: 1.42; color: #20242a; }
h1 { font-size: 22pt; margin: 0 0 6px; line-height: 1.15; color: #17253b; }
h2 { font-size: 14.5pt; margin: 16px 0 7px; padding-bottom: 4px; border-bottom: 1.5px solid #394b64; color: #17253b; }
h3 { font-size: 11.5pt; margin: 12px 0 5px; color: #26384f; }
p { margin: 5px 0 8px; }
table { width: 100%; border-collapse: collapse; margin: 7px 0 11px; font-size: 8.1pt; table-layout: fixed; }
thead { display: table-header-group; }
tr { break-inside: avoid; page-break-inside: avoid; }
th, td { border: 1px solid #b9c1cc; padding: 4px 5px; vertical-align: top; overflow-wrap: break-word; }
th { background: #eef1f5; font-weight: 700; color: #17253b; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.4pt; background: #f5f6f7; padding: 0 2px; }
a { color: #274d7d; text-decoration: none; }
.cover { padding-top: 34mm; page-break-after: always; }
.kicker { font-size: 10pt; text-transform: uppercase; letter-spacing: .06em; color: #53657d; margin-bottom: 10px; }
.subtitle { font-size: 12pt; color: #394b64; margin: 0 0 24px; }
.meta { width: 86%; font-size: 9.5pt; }
.meta td { border: 0; border-bottom: 1px solid #d5dae1; padding: 6px 4px; }
.meta td:first-child { width: 31%; font-weight: 700; color: #394b64; }
.callout { border-left: 4px solid #546b89; background: #f5f7fa; padding: 8px 10px; margin: 10px 0; }
.small { font-size: 8.4pt; color: #4d5968; }
.center { text-align: center; }
.right { text-align: right; }
.status-pass { font-weight: 700; }
.page-break { page-break-before: always; }
</style>

<div class="cover">
<div class="kicker">ENGSE601 - Software Verification and Validation</div>

# Week 05 - Component Test Case Set

<div class="subtitle">ScamGuard - Component / Unit Testing (Documentation Revision v2 Final)</div>
<table class="meta">
<tr><td>Project</td><td>ScamGuard - Scam Image Detection Application</td></tr>
<tr><td>Activity</td><td>Code & Logic Reading Clinic</td></tr>
<tr><td>Primary author</td><td>ภานุวัฒน์ ต๋าคำ</td></tr>
<tr><td>Date</td><td>22 September 2026</td></tr>
<tr><td>Requirement baseline</td><td>SRS v1.1, branch <code>main</code>, 2026-09-12</td></tr>
<tr><td>Code baseline</td><td><code>main</code> at <code>66bc9e4a</code></td></tr>
<tr><td>Document status</td><td>Revision Candidate v2 Final</td></tr>
<tr><td>Original submission</td><td>v1, tag <code>w05-submission-v1</code>, merge <code>ca354a8</code></td></tr>
</table>

<div class="callout"><strong>Revision note.</strong> v2 Final improves structure, traceability, terminology and readability only. It does not rewrite the original v1 submission history and does not change the frozen test basis, raw evidence or the 18 recorded test results.</div>

<p class="small">Canonical requirement source: <a href="https://github.com/Panuwat-ta/project/tree/main/Document/srs">Panuwat-ta/project - Document/srs</a><br>
Source-code repository: <a href="https://github.com/Panuwat-ta/project">Panuwat-ta/project</a></p>
</div>

## 1. Executive Summary

Week 05 verifies selected high-risk components of ScamGuard against the current canonical SRS v1.1. The scope covers Visual Analysis, Risk Score Calculation, Registration and Consent Management. Verification uses deterministic unit/component execution, a reproducible handler probe with fake DB, and explicit static contract inspection where an endpoint or output contract is absent.

The result set contains 18 cases: 7 Pass, 9 Fail, 1 Not Ready and 1 Needs Clarification. A failed case is retained as valid V&V evidence; no missing implementation is converted to Pass.

| Result | Count | Interpretation |
|---|---:|---|
| Pass | 7 | Verified behavior aligns with the baseline |
| Fail | 9 | Current implementation does not align with the baseline |
| Not Ready | 1 | Required component contract is not available for a valid acceptance test |
| Needs Clarification | 1 | Requirement example conflicts with the same baseline's algorithm semantics |
| **Total** | **18** | Selected Week 05 component cases |
## 2. Test Basis, Scope and Strategy

### 2.1 Frozen test basis

- Canonical SRS: v1.1 dated 2026-09-12, from `Document/srs` on `main`
- SRS SHA-256: `99bb8d5050fa54195b02869f1815e954fdd43ad0997e732b35426c70947cd40a`
- Code baseline: `Panuwat-ta/project`, branch `main`, commit `66bc9e4a`
- W03/W04 are historical v1.0 evidence only and do not override SRS v1.1

### 2.2 Selected scope

| Scope | Requirement | Component | Verification focus |
|---|---|---|---|
| C01 | FR-ANALYSIS-02 | `onnx_worker.py` | forgery / AI-Gen / visual output contract |
| C02 | FR-ANALYSIS-04 | `risk_calculator.py` | Hybrid max+bonus and grade boundaries |
| C03 | FR-AUTH-01 | auth schema + handler | registration response and mandatory System Consent |
| C04 | FR-PDPA-01 | consent model + route inventory | consent lifecycle and profile/API contracts |

### 2.3 Verification techniques

- Example-based tests for SRS-provided risk-score examples
- Boundary checks around Low/Medium/High transitions
- Negative handler probe for mandatory System Consent
- Static source/schema/route inspection for explicit output/API contracts
- Test-only fake DB and environment values; no production secret or database is used

<div class="callout"><strong>Out of scope:</strong> model Accuracy/F1/mDice, GPU performance, full System/UAT journeys, production-service availability and unstated retroactive research-data rules. These concerns are handed to later V&V activities instead of being inferred in Week 05.</div>

## 3. Component Test Cases

### 3.1 Visual Analysis - FR-ANALYSIS-02
| ID | AC | Verification | Expected | Actual evidence | Result |
|---|---|---|---|---|---|
| CT-01 | AC-1 | Contract inspection | Separate `forgery_confidence` 0-100 traceable to forgery signal | No `forgery_confidence`; worker exposes `visual_risk_score` from SegFormer max probability | Fail |
| CT-02 | AC-2 | Contract inspection | Separate `ai_gen_confidence` from an AI-Gen detector | `ai_gen_prob` is the same SegFormer max probability; no separate AI-Gen output | Fail |
| CT-03 | AC-3 | Readiness check | Visual-score behavior can be tested from canonical independent signals | Required separate signal contracts are not available on main | Not Ready |

FR-ANALYSIS-02 AC-5 (GPU inference <= 10 seconds) is deferred to NFR testing because no valid performance evidence is produced by this component activity.

### 3.2 Risk Calculation - FR-ANALYSIS-04

| ID | AC | Input / technique | Expected | Actual evidence | Result |
|---|---|---|---|---|---|
| CT-04 | AC-1 | `(50,85,0)` example | 90, High, primary=visual | `90 high visual True` | Pass |
| CT-05 | AC-2 | `(100,100,100)` example | capped 100, High | `100 high visual True` | Pass |
| CT-06 | AC-3 | `(10,0,0)` | 10, Low | `10 low textual False` | Pass |
| CT-07 | AC-4 | `(30,0,0)` | 30, Low | `30 low textual False` | Pass |
| CT-08 | AC-5 | `(55,0,0)` | 55, Medium | `55 medium textual False` | Pass |
| CT-09 | AC-6 | `(80,0,0)` | 80, High | `80 high textual False` | Pass |
| CT-10 | AC-7 | consistency analysis of stated 65 total / 85 visual | High by Visual Override | Hybrid max uses visual in base, so total cannot be 65 when visual is 85 | Needs Clarification |

Supporting boundary probe: 39 -> Low, 40 -> Medium, 69 -> Medium, 70 -> High.

### 3.3 Registration - FR-AUTH-01
| ID | AC | Verification | Expected | Actual evidence | Result |
|---|---|---|---|---|---|
| CT-11 | AC-1 | Handler probe + schema inspection | Response includes `id, full_name, email, role, status, created_at`; no password/hash | Keys are `email, full_name, id, message, role`; `status` and `created_at` absent | Fail |
| CT-12 | AC-5 | Negative handler probe: System Consent=false | HTTP 400 and no user/consent persistence | Handler returns `UserResponse` and fake DB receives User + ConsentLog(false,false) | Fail |
| CT-13 | AC-1 subcondition | Handler probe: system=true, research=false | Optional Research Consent must not block registration | Registration succeeds and persists research=false | Pass |

### 3.4 Consent Management - FR-PDPA-01

| ID | AC | Verification | Expected | Actual evidence | Result |
|---|---|---|---|---|---|
| CT-14 | AC-2 | Model contract inspection | Event/log model supports `consent_type`, `is_granted` and separate records | Current model stores one row with two booleans | Fail |
| CT-15 | AC-3 | Route inventory | `PUT /consent/research` updates research consent and records update | Endpoint not present on main | Fail |
| CT-16 | AC-4 | Route contract inspection | GET `/users/me` returns current-user profile | Profile GET is `/api/v1/auth/me`; `/api/v1/users/me` is DELETE | Fail |
| CT-17 | AC-5 | Route inventory | GET `/consent/logs` returns consent history | Endpoint not present on main | Fail |
| CT-18 | AC-3/5 | Model contract inspection | Consent history/update supports `updated_at` | Current `ConsentLog` has `created_at` only | Fail |

## 4. Evidence and Reproducibility

### 4.1 Evidence types

This artifact distinguishes executed tests, executed component probes and static contract inspection. Static inspection is used only where the SRS defines an explicit field/endpoint and the implementation contract can be verified directly; it is not presented as an end-to-end runtime test.

| Evidence | Description | Supports |
|---|---|---|
| `E05-baseline.txt` | Code commit, SRS version and SRS SHA-256 | Frozen test basis |
| `E05-pytest-component.txt` | Existing risk-calculator unit execution: `1 passed in 0.03s` | Risk logic supporting evidence |
| `E05-component-probe.txt` | Risk examples/boundaries, auth handler behavior, route and visual contract inventory | CT-01 to CT-18 as mapped in work evidence |
| `component_probe.py` | Reproducible probe source using fake DB and test-only environment | Re-execution / audit |
### 4.2 Evidence integrity

The test/probe execution used an isolated `origin/main` archive rather than the active product working branch. No `.env`, API key, token, production password or production database content is included in this artifact.

No claim is made for model Accuracy/F1/mDice, GPU inference time, end-to-end system pass, stakeholder approval or independent peer-review approval because those claims are not supported by Week 05 evidence.

<h2 style="page-break-before: always;">5. Findings and Handoff</h2>

| ID | Finding | Status | Next action / handoff |
|---|---|---|---|
| F01 | Visual forgery/AI-Gen signals are not separated as required | Open | Fix output contract/detector then re-test before System/UAT |
| F02 | AC-7 example 65 total / 85 visual is inconsistent with Hybrid max+bonus semantics | Needs Clarification | Clarify SRS through controlled change; do not guess algorithm intent |
| F03 | Registration response misses `status` and `created_at` | Open | Fix response schema/handler and add contract test |
| F04 | System Consent=false is accepted and persisted | Open | Add guard before persistence and re-test negative case |
| F05 | Consent persistence differs from event/log SRS contract | Open | Reconcile schema/migration before integration testing |
| F06 | Research-consent update/log endpoints are missing | Open | Implement endpoints and component/API tests |
| F07 | `/users/me` profile route contract differs between SRS and code | Open | Select canonical route then synchronize SRS/code/test |
| F08 | W03/W04 used SRS v1.0 | Closed for W05 | Preserve as history; use v1.1 as current authority |

<div class="callout"><strong>Handoff.</strong> F01/F05/F06/F07 feed Week 06 integration risk; F01/F03/F04/F06/F07 feed Week 07 System/UAT after fixes; performance/model-quality concerns feed Week 11; unresolved product findings may become formal defects in Week 14.</div>

## 6. AI Use and Review Integrity

AI was used to organize test cases, compare source contracts with the canonical SRS, execute local read-only verification through Remote Desktop Commander, and draft/report findings. Expected results were checked against SRS v1.1; actual results come from stored execution output or explicit source/schema/route inspection.

No test result, screenshot, stakeholder decision, peer-review approval or product metric was fabricated.

### Review status

The original v1 artifact was merged through PR #5 at commit `ca354a8` and tagged `w05-submission-v1`. GitHub showed no recorded independent PR review at verification time, and the reviewer decision fields remain pending in `work/05-peer-review.md`.

Therefore this v2 Final document is a <strong>Revision Candidate</strong>. It may improve the quality of the Week 05 documentation without claiming that the independent peer-review gate has already passed.

<div class="callout"><strong>Evidence package.</strong> Detailed scope, 18 test cases, raw evidence, findings, peer-review record and AI declaration are stored under <code>WEEKS/week-05/work/</code>. Canonical requirement and source repositories are linked on the cover page.</div>
