# Week 05 - Component / Unit Testing

สถานะหลักของสัปดาห์: Submitted (v1)
สถานะเอกสารปรับปรุง: Revision Candidate (v2 Final)

## วัตถุประสงค์

Week 05 ใช้กิจกรรม Code & Logic Reading Clinic เพื่อออกแบบและตรวจสอบ Component Test Case Set จาก requirement, acceptance criteria และ code/logic จริงของ ScamGuard โดยเน้นความสามารถในการตรวจสอบย้อนกลับจาก Requirement -> Test -> Evidence -> Finding

เอกสารฉบับปรับปรุง v2 Final ไม่เปลี่ยนผลทดสอบเดิม แต่ปรับโครงสร้าง การอธิบาย test basis, verification technique, evidence และ handoff ให้ชัดเจนขึ้นสำหรับการตรวจงานและใช้ต่อใน Week 06 เป็นต้นไป

## Test basis

- Canonical Requirement/SRS: https://github.com/Panuwat-ta/project/tree/main/Document/srs
- Branch: `main`
- SRS: `05_Software_Requirement_Specification.md` v1.1 ลงวันที่ 2026-09-12
- Source code: https://github.com/Panuwat-ta/project
- Code baseline: branch `main`, commit `66bc9e4a`
- Date referenced: 2026-09-22
- Primary scope: FR-ANALYSIS-02, FR-ANALYSIS-04, FR-AUTH-01, FR-PDPA-01

## ผลการตรวจสอบ

| Result | Count |
|---|---:|
| Pass | 7 |
| Fail | 9 |
| Not Ready | 1 |
| Needs Clarification | 1 |
| Total | 18 |

ผลทั้งหมดอ้างอิงหลักฐานจริงเท่านั้น: test/probe ที่ execute แล้ว, route/schema/source contract ที่ตรวจจริง และสถานะ `Not Ready`/`Needs Clarification` เมื่อยังไม่สามารถสร้างผล acceptance ที่ถูกต้องได้

## Work artifacts

- `work/01-component-scope.md` - scope, baseline และ test strategy
- `work/02-component-test-cases.md` - Component Test Case Set จำนวน 18 cases
- `work/03-existing-test-evidence.md` - execution/static-inspection evidence
- `work/04-open-issues-and-decisions.md` - findings, disposition และ handoff
- `work/05-peer-review.md` - peer-review record และ repository event
- `work/06-submission-source.md` - source สำหรับเอกสารฉบับปรับปรุง
- `work/ai-use-declaration.md` - AI Use Declaration
- `work/probes/component_probe.py` - reproducible component probe
- `work/evidence/` - raw evidence ที่ใช้รองรับผลทดสอบ

## Submission / revision record

- Original submitted artifact: `submission/W05_ScamGuard_Component-Test-Case-Set_v1.pdf`
- Original submission tag: `w05-submission-v1`
- Merge commit: `ca354a8`
- Revised documentation candidate: `submission/W05_ScamGuard_Component-Test-Case-Set_v2-final.pdf`

v1 ยังคงเป็นหลักฐานการส่งงานเดิมและไม่ถูกเขียนทับ ส่วน v2 Final เป็นการปรับคุณภาพเอกสารโดยคง test basis, raw evidence และผล 18 cases เดิมไว้ ตรวจพบว่า GitHub ไม่มี recorded PR review สำหรับการส่ง v1 ดังนั้นเอกสารต้องไม่อ้างว่าได้รับ independent peer-review แล้วจนกว่าจะมีหลักฐานจริง
