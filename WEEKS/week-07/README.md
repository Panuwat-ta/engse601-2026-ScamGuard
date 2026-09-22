# Week 07 - System Testing and UAT

สถานะ: Ready for Review (author-side design complete; execution pending)

## วัตถุประสงค์

Week 07 แปลง requirement, acceptance criteria และ findings จาก Week 05-06 เป็น System Test และ User Acceptance Test (UAT) scenarios ที่พร้อมให้ทีมมนุษย์นำไปรันบน build/environment จริง โดยแยกให้ชัดระหว่าง:

- ความครบของ test design และ traceability
- ความพร้อมของ environment/test data/ผู้ทดสอบ
- ผล execution ที่เกิดขึ้นจริง

เอกสารชุดนี้ไม่อ้างว่า System Test หรือ UAT ผ่านแล้ว เพราะยังไม่มี deployed baseline, test-data package, execution log, ผู้ทดสอบ UAT 100 คน หรือผล peer review จริง

## Test basis

- Canonical Requirement/SRS: https://github.com/Panuwat-ta/project/tree/main/Document/srs
- SRS: `05_Software_Requirement_Specification.md` v1.1 ลงวันที่ 2026-09-12
- SRS SHA-256: `99bb8d5050fa54195b02869f1815e954fdd43ad0997e732b35426c70947cd40a`
- Frozen source baseline: https://github.com/Panuwat-ta/project, branch `main`, commit `66bc9e4a`
- Source facts: frozen snapshots and executed probes from Week 05-06
- Date referenced: 2026-09-22
- Course output currently announced in this repository: `System/UAT Scenarios`; official Week 07 template/file naming remains pending

## Scenario summary

| Type | Design complete | Not Executed | Not Ready | Pass/Fail claimed |
|---|---:|---:|---:|---:|
| System Test | 12 | 12 | 0 | 0 |
| UAT | 6 | 0 | 6 | 0 |
| Total | 18 | 12 | 6 | 0 |

`Not Executed` หมายถึง scenario และ expected result พร้อม แต่ยังไม่ได้รันบน integrated build จริง ส่วน `Not Ready` ใช้กับ UAT ที่ยังขาด approved build, recruitment/consent และผู้ทดสอบจริงตาม sample size ใน SRS

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
- `work/evidence/E07-system-readiness-probe.txt`
- `work/evidence/E07-result-register.txt`
- `work/evidence/E07-pdf-check.txt`

## Submission artifact

- `submission/W07_ScamGuard_System-UAT-Scenarios_v1.pdf`

PDF เป็น submission candidate ที่ author-side complete. Independent peer review, official Week 07 template confirmation, environment provisioning, System Test execution และ UAT execution ยังต้องเกิดจริงก่อนเปลี่ยนเป็น `Submitted` หรือรายงานผล Pass/Fail/UAT metrics
