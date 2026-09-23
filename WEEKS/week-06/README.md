# Week 06 - Integration / API Testing

สถานะ: Ready for Review

## วัตถุประสงค์

Week 06 ใช้กิจกรรม Interface/API Risk Mapping เพื่อระบุจุดเชื่อมต่อระหว่าง Mobile, API, service, Redis, inference, media storage, history และ report แล้วออกแบบและ execute integration probes บน baseline ที่ตรึงไว้ โดยแยก test double ออกจาก production dependency อย่างชัดเจน

## Test basis

- Canonical Requirement/SRS: https://github.com/Panuwat-ta/project/tree/main/Document/srs
- Branch: `main`
- SRS: `05_Software_Requirement_Specification.md` v1.1 ลงวันที่ 2026-09-12
- SRS latest commit in `Document/srs`: `2b8a1fb0`
- Source code: https://github.com/Panuwat-ta/project
- Code baseline: branch `main`, commit `66bc9e4a`
- Project test assets: https://github.com/Panuwat-ta/project/tree/develop/tests_all
- Test-document baseline: branch `develop`, commit `162e0249abb9e9940f014ba6d5182d38213bc771`
- Week 05 handoff: `WEEKS/week-05/work/04-open-issues-and-decisions.md`
- Course activity: Workshop 3 - Interface/API Risk Mapping

## Integration scope

1. Mobile client <-> Scan API
2. ScanService <-> Redis cache
3. ScanService <-> InferenceService / ONNX / OCR
4. Scan pipeline <-> Source Verification
5. Heatmap storage <-> API <-> Mobile
6. Scan <-> History <-> Report

## Execution summary

| Result | Count |
|---|---:|
| Pass | 6 |
| Fail | 11 |
| Not Ready | 1 |
| Total | 18 |

`Fail` เป็นผล V&V ที่เกิดจาก contract/behavior ไม่ตรง baseline และไม่ถูกแปลงเป็น Pass เพื่อให้เอกสารดูสมบูรณ์ ส่วน `Not Ready` ใช้เฉพาะกรณีที่ production interface ที่ requirement ต้องการยังไม่มีให้ทดสอบจริง

ผล 6 Pass / 11 Fail / 1 Not Ready เป็นผลของ harness บน frozen `main` commit `66bc9e4a` เท่านั้น การตรวจ `develop/tests_all` เมื่อ 2026-09-23 พบทั้ง automated API/E2E design และ historical pass reports แต่รายงานเดิมไม่มี commit/build/env ครบ จึงใช้เป็น supporting evidence และ re-test target ไม่ใช่เหตุผลเปลี่ยนผล Week 06 ย้อนหลัง

## Work artifacts

- `work/01-interface-scope-and-risk-map.md`
- `work/02-integration-test-design.md`
- `work/03-open-issues-and-entry-criteria.md`
- `work/04-interface-contract-evidence.md`
- `work/05-peer-review.md`
- `work/ai-use-declaration.md`
- `work/probes/integration_probe_test.py`
- `work/evidence/E06-baseline.txt`
- `work/evidence/E06-source-contract-snapshot.txt`
- `work/evidence/E06-route-inventory.txt`
- `work/evidence/E06-schema-contract.txt`
- `work/evidence/E06-integration-probe.txt`
- `work/evidence/E06-result-register.txt`
- `work/evidence/E06-pdf-check.txt`
- `work/evidence/E06-tests-all-basis.txt`

## Submission artifact

- `submission/W06_ScamGuard_Integration-Test-Design_v1.pdf`

Author-side artifact preparation is complete and the PDF/result evidence is reproducible. Independent peer-review fields remain pending, so Week 06 is `Ready for Review` rather than `Submitted` until a real reviewer decision is recorded.
