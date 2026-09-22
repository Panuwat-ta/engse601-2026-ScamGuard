# Week 06 — Integration / API Testing

สถานะ: In Progress

## เป้าหมาย

ทำ Interface Risk Mapping และออกแบบ Integration Test Design จาก requirement, interface contract และ code จริงของ ScamGuard โดยเน้นจุดเชื่อมต่อที่ความผิดพลาดของ component หนึ่งสามารถส่งผลต่ออีก component ได้

## Test basis

- Canonical Requirement/SRS: https://github.com/Panuwat-ta/project/tree/main/Document/srs
- Branch: `main`
- SRS: `05_Software_Requirement_Specification.md` v1.1 (2026-09-12)
- Source code: https://github.com/Panuwat-ta/project
- Code baseline: branch `main`, commit `66bc9e4a`
- Week 05 handoff: `WEEKS/week-05/work/04-open-issues-and-decisions.md`
- Course activity: Interface Risk Mapping

## Initial integration scope

- Mobile client ↔ Scan API
- ScanService ↔ Redis cache
- ScanService ↔ InferenceService ↔ ONNX/OCR worker
- ScanService ↔ Source Verification / Google Vision fallback
- ScanService ↔ Heatmap storage ↔ API/Mobile result rendering
- Scan ↔ History ↔ Report flow

## Work artifacts

- `work/01-interface-scope-and-risk-map.md`
- `work/02-integration-test-design.md`
- `work/03-open-issues-and-entry-criteria.md`
- `work/04-interface-contract-evidence.md`
- `work/ai-use-declaration.md`

## Status rule

Week 06 เป็นงานออกแบบ integration testing จึงไม่สร้างผล Pass/Fail ให้ case ที่ยังไม่ได้ execute จริง ใช้ `Planned`, `Not Ready` หรือ `Not Executed` ตามหลักฐานและ entry criteria ที่มีอยู่

## Current handoff constraint

ผล Fail/Not Ready จาก Week 05 ไม่ถูกซ่อนหรือแปลงเป็น Pass แต่ถูกใช้เป็น interface risk และ dependency ของ Integration Test Design โดยเฉพาะ visual contract, source verification, scan cancel และ cross-API contract gaps ที่เกี่ยวข้อง
