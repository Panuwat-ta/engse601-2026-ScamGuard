# W07-02 - System Test Scenarios

## 1. Basis and status vocabulary

The project System/E2E design authority is `https://github.com/Panuwat-ta/project/tree/develop/tests_all`, pinned to `develop` commit `162e0249abb9e9940f014ba6d5182d38213bc771`. The ten scenarios below map one-to-one to the baseline matrix in `tests_all/manual_tests/test_cases_e2e.md`.

- `Not Executed`: project test design exists, but no real row exists in `tests_all/tests_report/manual_tests/execution_log.md` for the pinned build
- `Not Ready`: a required environment, dataset or decision prevents a valid run
- `Pass` / `Fail`: may be used only after build/env/tester/raw evidence are recorded

All ten scenarios are `Not Executed`. Historical automated reports are supporting evidence only: they lack the Commit/Build/Env metadata required to claim an execution on the Week 07 baseline. The current generated JUnit file reports `tests=0`.

## 2. Project-aligned System Test scenarios

| W07 ID / Project TC | Canonical SRS trace | Project scenario and execution focus | Acceptance oracle | Required evidence | Status |
|---|---|---|---|---|---|
| W07-ST-01 / TC-E2E-SCAN-01 | FR-SCAN-01-03, FR-ANALYSIS-01-04, FR-XAI-01, FR-HISTORY-01 | Full detection journey: mobile selection/upload, async processing, multi-layer analysis, heatmap/result and history | terminal result is owned, internally consistent and honest about unavailable analysis; risk/heatmap/history match SRS contracts | build IDs, device/API recording, input hash, result JSON, DB/media trace | Not Executed |
| W07-ST-02 / TC-E2E-CACHE-02 | FR-SCAN-03, NFR-01, NFR-07 | Repeat the identical image and distinguish cache miss from cache hit | reusable result and heatmap remain valid; cache hit P95 <=3s; TTL/hit state are observable | image hash, timing samples, Redis-safe evidence, both API bodies | Not Executed |
| W07-ST-03 / TC-E2E-REPORT-03 | FR-HISTORY-02, FR-ADMIN-02, FR-ADMIN-04 | User submits incident report; admin reviews it; audit trail records decision | valid report enters pending queue, authorization is enforced, decision and audit state remain consistent | user/admin recordings, request/response logs, report/audit extracts | Not Executed |
| W07-ST-04 / TC-E2E-MODEL-04 | FR-ADMIN-03, NFR-05 | Dry-run, deploy model version, observe active model and live inference, then rollback if required | invalid model cannot become active; successful deployment changes the active version with audit evidence and no broken scan contract | model/build IDs, dry-run/deploy responses, worker log, audit record | Not Executed |
| W07-ST-05 / TC-E2E-BAN-05 | FR-ADMIN-01, NFR-04 | Admin suspends a user during an active mobile session | protected calls are rejected without data leakage; client clears/blocks access according to the approved contract | two-role session log, 403 responses, device recording, admin audit | Not Executed |
| W07-ST-06 / TC-E2E-OFFLINE-06 | Canonical trace unresolved; project case uses legacy `NFR-PERF-03` | Open cached history/result offline, restore network and refresh | no crash; cached data remains viewable; reconnect refresh does not duplicate/lose items | requirement disposition, airplane-mode recording, local/remote before-after data | Not Executed |
| W07-ST-07 / TC-E2E-FULL-07 | FR-AUTH-01-02, FR-SCAN-02-03, FR-HISTORY-01-02, FR-ADMIN-02/04, FR-PDPA-01 | Register through scan, history, report, admin review and audit | one traceable user journey preserves ownership, consent, status/version and audit continuity | sanitized end-to-end correlation record, DB extracts, user/admin recordings | Not Executed |
| W07-ST-08 / TC-E2E-AUTH-08 | FR-AUTH-03, NFR-04 | Access token expires during polling/history; refresh and resume | expired access is rejected; valid refresh resumes the same journey; invalid refresh clears access | controlled token clock, HTTP transcript, device state recording | Not Executed |
| W07-ST-09 / TC-E2E-REG-09 | FR-ADMIN-03, NFR-05 | Re-scan an immutable reference image after model deployment | response schema remains stable, scores remain 0-100, model identity/audit are recorded; any grade change is explained | file hash, before/after JSON, model versions, audit log | Not Executed |
| W07-ST-10 / TC-E2E-HIST-10 | FR-HISTORY-01, FR-PDPA-01 | Delete owned history, refresh list and request the deleted detail | deleted item is absent/404, shared media is not incorrectly removed, required audit/consent retention is preserved | before/after API/UI/DB/media evidence, deletion/audit record | Not Executed |

## 3. Known design and traceability warnings

- `tests_all/manual_tests/test_cases_e2e.md` uses legacy aliases such as `FR-INPUT-*`, `FR-SYS-*`, `FR-HIST-*` and `NFR-PERF-*`; Week 07 maps expected behavior to canonical SRS v1.1 IDs without silently rewriting the project file.
- `TC-E2E-BAN-05` contains a source-inspection defect note, but the manual execution log has no real run; Week 07 therefore records `Not Executed`, not an E2E `Fail`.
- `TC-E2E-OFFLINE-06` has no direct canonical SRS v1.1 requirement located. The scenario remains in the project baseline, but requirement disposition is required before acceptance.
- Historical `automate_test_ci.md` records one automated E2E journey passing, but its original Commit/Build/Env is unrecorded and it does not cover all ten System scenarios.

## 4. Execution record rule

For each actual run, append a real row to the project manual execution log and reference it here with pinned commit/build/model/environment, tester, input checksums, expected/actual result, raw evidence and defect ID. Do not overwrite this design table with unsupported Pass/Fail values.
