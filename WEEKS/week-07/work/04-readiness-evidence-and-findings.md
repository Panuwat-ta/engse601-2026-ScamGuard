# W07-04 - Readiness Evidence and Findings

## 1. Evidence map

| Evidence | Purpose | Classification |
|---|---|---|
| `E07-baseline.txt` | pin SRS hash, source baseline and authoring context | Existing |
| `E07-readiness-basis.txt` | map Week 05-06 frozen source facts into Week 07 entry risk | Existing/derived |
| `system_readiness_probe.py` | reproducibly verify hashes/metadata/contract facts | Existing executable probe |
| `E07-system-readiness-probe.txt` | raw output from the readiness probe | Existing raw output |
| `E07-result-register.txt` | reconcile 18 design/execution statuses | Existing summary |
| `E07-pdf-check.txt` | record PDF structure/render checks | Existing after generation |
| System/UAT runtime logs | prove end-to-end behavior and user metrics | Not Ready |
| Human peer-review decision | verify content and DoD independently | Not Ready |

## 2. Readiness findings

| ID | Finding | Basis | Status | Owner | Next action |
|---|---|---|---|---|---|
| W07-F01 | official Week 07 template and final naming rule are not yet present in the course scaffold | Week 07 README originally states template/details will be announced | Open dependency | ภานุวัฒน์ | compare candidate against official template when released; issue v2 if structure changes |
| W07-F02 | no approved deployed build/environment identifier is recorded for system execution | PROJECT current build is Not Ready; no deployment URL/build id in Week 07 evidence | Not Ready | ภานุวัฒน์ | provision isolated environment and record app/API/model/DB/Redis versions |
| W07-F03 | frozen baseline has critical scan/cache/source/heatmap/history/report gaps | W06-F01-F09 and E06 raw evidence | Open product gaps | ภานุวัฒน์ | fix or approve known-defect execution, then rerun affected integration tests before System Test |
| W07-F04 | consent and PDPA journey is not acceptance-ready on the frozen baseline | W05-F03-F05 and component evidence | Open product gaps | ภานุวัฒน์ | implement/retest consent enforcement, research withdrawal and log access |
| W07-F05 | controlled system-test data and ground truth are absent | no approved manifest/checksums/expected outputs in repository | Not Ready | ภานุวัฒน์ | create licensed/synthetic data pack with privacy review and oracle |
| W07-F06 | UAT recruitment/consent and 100 participant responses do not exist | NFR-06 requires 100; no response dataset/log | Not Ready | เอกพันธ์ | prepare recruitment and privacy protocol; run real facilitated sessions |
| W07-F07 | independent peer-review decision is absent | `05-peer-review.md` fields pending | Pending human review | เอกพันธ์ | review traceability, status honesty, PDF and execution gate |

## 3. Definition of Done assessment

Author-side design is complete when:

- [x] canonical SRS/version/hash are pinned
- [x] frozen source baseline and inherited source evidence are identified
- [x] six critical journeys are mapped
- [x] twelve System Test scenarios include trace, precondition, procedure, oracle and evidence
- [x] six UAT scenarios and the NFR-06 questionnaire/metrics are defined
- [x] all 18 statuses reconcile without fabricated Pass/Fail
- [x] readiness findings have owner and next action
- [x] AI use is disclosed
- [x] PDF candidate and render QA evidence exist
- [ ] official Week 07 template has been confirmed
- [ ] independent peer review has occurred
- [ ] system environment/data are ready and tests have executed
- [ ] 100 real UAT sessions and analysis have occurred
- [ ] merge/tag/LMS submission has occurred

Therefore the correct state is `Ready for Review`, not `Submitted`, `Accepted` or `Passed`.

## 4. Change control

When an official Week 07 template, new SRS or new code baseline is adopted, create a new document version. Preserve v1 and update requirement/source hashes, impacted scenarios, evidence paths and revision history; do not silently replace the baseline or past results.
