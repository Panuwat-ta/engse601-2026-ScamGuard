# W06-03 - Findings, Entry Criteria and Handoff

## 1. Integration findings register

| ID | Finding | Evidence / trace | Status | Owner | Next action |
|---|---|---|---|---|---|
| W06-F01 | Scan upload API คืน HTTP 200 แต่ FR-SCAN-02 AC-1 กำหนด HTTP 202 | W06-IT-01; E06 integration probe | Open | ภานุวัฒน์ | ปรับ route status contract หรือ controlled SRS change แล้ว re-test mobile/API |
| W06-F02 | Mobile มี DELETE `/scan/{id}` แต่ backend ไม่มี cancel route | W06-IT-04; mobile datasource + scan router | Open | ภานุวัฒน์ | implement cancel endpoint หรือถอด/disable consumer action แล้วเพิ่ม contract test |
| W06-F03 | Cache miss อาจเขียน Redis ไม่ได้เมื่อ `heatmap_bytes=b''` คงอยู่ใน result และ `json.dumps` serialize bytes ไม่ได้ | W06-IT-06; raw stdout `Redis cache write error` | Open | ภานุวัฒน์ | sanitize/remove binary field ก่อน cache serialization และ re-test TTL 30 วัน |
| W06-F04 | Cache record อ้างว่ามี heatmap แต่ไฟล์หายแล้ว scan ยัง completed โดยไม่มี media reference/recovery state | W06-IT-07 | Open | ภานุวัฒน์ | กำหนด cache/media lifecycle และ recovery/degraded behavior |
| W06-F05 | Visual worker ยังไม่มี separate forgery/AI-Gen outputs ตาม SRS | W06-IT-10; W05-F01 | Open dependency | ภานุวัฒน์ | แก้ component contract แล้ว re-run I03/System-UAT |
| W06-F06 | Source Verification production adapter ยังไม่มี และ fallback ปัจจุบันใช้ `DEFAULT_SOURCE_SCORE` แทน unavailable/exclusion | W06-IT-11/12; FR-ANALYSIS-03 | Open / Not Ready | ภานุวัฒน์ | implement Google Vision adapter + canonical fallback แล้ว re-test success/down paths |
| W06-F07 | Heatmap ถูก persist เป็น filesystem path ใน API field แทน canonical `/uploads/{filename}` | W06-IT-13/14; FR-XAI-01 | Open | ภานุวัฒน์ | normalize media reference ที่ server contract และเพิ่ม cross-client test |
| W06-F08 | History API schema/filter contract ไม่ตรง SRS: `items/risk_level`, ไม่มี `start_date/end_date/risk_grade` | W06-IT-15/16; FR-HISTORY-01 | Open | ภานุวัฒน์ | reconcile response/query schema แล้วเพิ่ม API integration regression tests |
| W06-F09 | Report API contract ไม่ตรง SRS บาง field/message: `id` vs `report_id`, duplicate detail ต่างข้อความ | W06-IT-17/18; FR-HISTORY-02 | Open | ภานุวัฒน์ | sync SRS/code response contract ผ่าน controlled change แล้ว re-test |

## 2. Entry criteria used for execution

- Canonical SRS/version/hash และ ENGSE212 code commit ถูก pin ก่อนรัน
- ใช้ isolated source archive ไม่ checkout ทับ working branch ของ ENGSE212
- Test database/Redis/model dependencies ถูกแทนด้วย deterministic doubles เฉพาะ seam ที่มี contract จริง
- Test filesystem แยกจาก production uploads
- External Google Vision positive case ไม่ถูกสร้าง mock contract ใหม่เมื่อ production adapter ยังไม่มี
- ไม่อ่านหรือคัดลอก `.env`, production credential หรือ production data ลง evidence

## 3. Exit criteria status

| Exit criterion | Status | Evidence |
|---|---|---|
| Interface map ครอบคลุม critical producer/consumer | Met | `01-interface-scope-and-risk-map.md` I01-I06 |
| ทุก test มี requirement trace + expected + actual/result | Met | `02-integration-test-design.md` 18 cases |
| Executed cases มี raw reproducible evidence | Met | `integration_probe_test.py`, `E06-integration-probe.txt` |
| Not Ready มี blocker/owner/next action | Met | W06-IT-11 / W06-F06 |
| Fail ไม่ถูกแปลงเป็น Pass | Met | 11 Fail ถูกเก็บตาม evidence |
| AI Use Declaration ครบ | Met | `ai-use-declaration.md` |
| PDF submission candidate สร้างและตรวจ layout | Met | `submission/W06_ScamGuard_Integration-Test-Design_v1.pdf` + `E06-pdf-check.txt` |
| Independent peer review | Pending | `05-peer-review.md` |

## 4. Handoff to later work

- Week 07 System/UAT: F01, F02, F05, F06, F07, F08, F09 กระทบ end-to-end user journeys และต้องไม่ถูกซ่อนด้วย mock
- Week 10 Test Data: cache/media/source scenarios ต้องมี deterministic fixtures ที่อ้าง requirement ได้
- Week 11 NFR: latency, real Redis/PostgreSQL, GPU inference และ model-quality metrics ต้องใช้ dedicated environment
- Week 14 Defect Management: promote W06-F01-F09 ที่ยัง unresolved เป็น formal defect records พร้อม severity/status/history
- ENGSE212 implementation: แก้ contract ที่ reproduce ได้จาก W06 แล้ว re-run test IDs เดิมเพื่อเก็บ regression evidence

## 5. Review gate

Author-side Integration Test Design และ execution evidence ครบแล้ว แต่ Team Working Agreement กำหนด independent peer review ก่อน merge/tag submission. จึงตั้งสถานะ Week 06 เป็น `Ready for Review` และไม่สร้าง reviewer decision/sign-off ขึ้นเอง
