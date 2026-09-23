# W07-04 - Readiness Evidence and Findings

## 1. Evidence map

| Evidence | Purpose | Classification |
|---|---|---|
| `E07-baseline.txt` | separate SRS, historical code and current project-testing baselines | Existing |
| `E07-readiness-basis.txt` | carry Week 05-06 risks forward without treating them as current execution | Existing/derived |
| `E07-tests-all-basis.txt` | pin Master Test Plan, 10 E2E scenarios, manual log, JUnit and historical-report limits | Existing/derived |
| `system_readiness_probe.py` | verify hashes, develop ref, scenario count and execution-record state without running the product | Existing executable probe |
| `E07-system-readiness-probe.txt` | raw readiness output | Existing raw output |
| `E07-result-register.txt` | reconcile 10 System + 6 UAT statuses | Existing summary |
| `E07-pdf-check.txt` | record final PDF structure/render checks | Existing after generation |
| Pinned-build System/UAT runtime evidence | prove current end-to-end behavior and user metrics | Not Ready |
| Human peer-review decision | independently verify content and Definition of Done | Not Ready |

## 2. Readiness findings

| ID | Finding | Basis | Status | Owner | Next action |
|---|---|---|---|---|---|
| W07-F01 | official Week 07 template and final naming rule are not yet present in the course scaffold | Week 07 course scaffold | Open dependency | ภานุวัฒน์ | compare candidate with official template; issue v2 if required |
| W07-F02 | no approved deployed build/environment identifier is recorded | PROJECT current truth and Week 07 evidence | Not Ready | ภานุวัฒน์ | record app/API/model/DB/Redis build and isolated environment |
| W07-F03 | Week 05-06 findings use historical `main` commit `66bc9e4a`; later `develop` reports cannot close them without equivalent re-test metadata | E05/E06 result registers; IN-06 | Open verification gap | ภานุวัฒน์ | rerun mapped tests on a pinned `develop` build and reconcile each finding |
| W07-F04 | project manual execution log contains template rows only and explicitly states no real manual run exists | `tests_all/tests_report/manual_tests/execution_log.md` | Not Executed | ภานุวัฒน์ | execute selected E2E cases and append real rows with tester/build/evidence |
| W07-F05 | project E2E cases use legacy requirement aliases; offline scenario has no direct canonical SRS v1.1 trace located | `tests_all/manual_tests/test_cases_e2e.md` vs SRS v1.1 | Needs controlled reconciliation | ภานุวัฒน์ | update project RTM/test-case trace through the ENGSE212 process; do not invent IDs here |
| W07-F06 | current generated JUnit artifact reports zero tests; historical automated pass reports omit commit/build/env | `junit.xml`, `api_suite_verification.md`, `automate_test_ci.md` | Insufficient current execution evidence | ภานุวัฒน์ | run current suites on pinned build and retain JUnit plus metadata |
| W07-F07 | UAT option has not been selected and no real participant sessions exist | Master Test Plan sections 3.5-3.6; no response dataset/log | Not Ready | เอกพันธ์ | choose internal beta/external UAT, approve privacy protocol and execute real sessions |
| W07-F08 | NFR-06 100-participant satisfaction/heatmap metric has not been measured | SRS NFR-06; no response dataset | Not Ready | เอกพันธ์ | recruit 100 valid participants and report denominators/distributions without fabricated values |
| W07-F09 | independent peer-review and release sign-off decisions are absent | `05-peer-review.md`; blank `tests_all/release_signoff.md` | Pending human review | เอกพันธ์ | perform independent review; Dev/QA/PM complete sign-off only after gates pass |

## 3. Definition of Done assessment

Author-side design is complete when:

- [x] canonical SRS/version/hash are pinned
- [x] project test plan/cases/reports are pinned to `develop` commit/hash evidence
- [x] ten project E2E journeys are mapped one-to-one
- [x] ten System Test scenarios include canonical trace, oracle and evidence requirement
- [x] six UAT scenarios and NFR-06 questionnaire/metrics are defined
- [x] all 16 statuses reconcile without fabricated Pass/Fail
- [x] historical reports, zero-test JUnit and empty manual log are classified honestly
- [x] findings have owner and next action
- [x] AI use is disclosed
- [ ] official Week 07 template has been confirmed
- [ ] independent peer review has occurred
- [ ] pinned system environment/data are ready and System Tests have executed
- [ ] UAT option has been selected and real sessions have executed
- [ ] 100 valid participants have been measured before claiming NFR-06 metrics
- [ ] release sign-off, merge/tag and LMS submission have occurred

Therefore the correct state is `Ready for Review`, not `Submitted`, `Accepted` or `Passed`.

## 4. Change control

When the official template, SRS, project test baseline or code/build baseline changes, create a new document version. Preserve the current PDF and update hashes, scenario mappings, evidence paths and revision history; never silently transfer a result between baselines.
