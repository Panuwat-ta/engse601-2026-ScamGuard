# Week 07 - System Testing and UAT

สถานะ: Ready for Review (project-aligned design complete; execution pending)

## วัตถุประสงค์

Week 07 แปลง requirement, acceptance criteria และ findings จาก Week 05-06 เป็น System Test และ User Acceptance Test (UAT) scenarios ที่พร้อมให้ทีมมนุษย์นำไปรันบน build/environment จริง โดยแยกให้ชัดระหว่าง:

- ความครบของ test design และ traceability
- ความพร้อมของ environment/test data/ผู้ทดสอบ
- ผล execution ที่เกิดขึ้นจริง

เอกสารชุดนี้ไม่อ้างว่า System Test หรือ UAT ผ่านแล้ว เพราะ `develop/tests_all/tests_report/manual_tests/execution_log.md` ยังไม่มีผลรันจริง, ไม่มี approved deployed build และยังไม่มีผล peer review จริง ส่วนการวัด NFR-06 แบบผู้ใช้จริงยังขาด 100 valid participants

## Test basis

- Canonical Requirement/SRS: https://github.com/Panuwat-ta/project/tree/main/Document/srs
- SRS: `05_Software_Requirement_Specification.md` v1.1 ลงวันที่ 2026-09-12
- SRS SHA-256: `99bb8d5050fa54195b02869f1815e954fdd43ad0997e732b35426c70947cd40a`
- Frozen source baseline: https://github.com/Panuwat-ta/project, branch `main`, commit `66bc9e4a`
- Project test plan/cases/reports: https://github.com/Panuwat-ta/project/tree/develop/tests_all
- Test-design baseline: branch `develop`, commit `162e0249abb9e9940f014ba6d5182d38213bc771`
- Source facts: frozen Week 05-06 evidence is retained as historical risk input; current project test assets are taken from the pinned `develop` baseline
- Date referenced: 2026-09-23
- Course output currently announced in this repository: `System/UAT Scenarios`; official Week 07 template/file naming remains pending

## Scenario summary

| Type | Design complete | Not Executed | Not Ready | Pass/Fail claimed |
|---|---:|---:|---:|---:|
| System Test | 10 | 10 | 0 | 0 |
| UAT | 6 | 0 | 6 | 0 |
| Total | 16 | 10 | 6 | 0 |

System Test ทั้ง 10 รายการ map ตรงกับ `TC-E2E-SCAN-01` ถึง `TC-E2E-HIST-10` ใน project test suite. `Not Executed` หมายถึง scenario และ expected result พร้อม แต่ยังไม่มี manual run record บน pinned build. UAT ทั้ง 6 รายการยัง `Not Ready`; ทีมต้องเลือก UAT option และเตรียมผู้ใช้/consent ส่วน NFR-06 metric ต้องใช้ 100 valid participants ตาม SRS

## Work artifacts

- `work/01-system-scope-and-critical-journeys.md`
- `work/02-system-test-scenarios.md`
- `work/03-uat-protocol-and-questionnaire.md`
- `work/04-readiness-evidence-and-findings.md`
- `work/05-peer-review.md`
- `work/ai-use-declaration.md`
- `work/probes/system_readiness_probe.py`
- `work/evidence/E07-baseline.txt`
- `work/evidence/E07-readiness-basis.txt`
- `work/evidence/E07-tests-all-basis.txt`
- `work/evidence/E07-system-readiness-probe.txt`
- `work/evidence/E07-result-register.txt`
- `work/evidence/E07-pdf-check.txt`

## Submission artifact

- `submission/W07_ScamGuard_System-UAT-Scenarios_v1.pdf`

PDF เป็น submission candidate ที่ author-side complete. Independent peer review, official Week 07 template confirmation, environment provisioning, System Test execution และ UAT execution ยังต้องเกิดจริงก่อนเปลี่ยนเป็น `Submitted` หรือรายงานผล Pass/Fail/UAT metrics
