# W06-02 — Integration Test Design

## Status vocabulary

- `Planned`: interface contract และ expected result ชัดพอสำหรับเตรียม test แต่ยังไม่ได้ execute ใน Week 06
- `Not Ready`: interface/component ที่ requirement ต้องการยังไม่มีหรือ contract ยังไม่พร้อมให้ integration test
- `Not Executed`: test พร้อมและ environment พร้อม แต่ session นี้ยังไม่ได้รัน

## I01 — Mobile ↔ Scan API

| Test ID | Trace | Scenario / stimulus | Expected integration behavior | Technique | Status |
|---|---|---|---|---|---|
| W06-IT-01 | FR-SCAN-02 AC-1 | Mobile ส่ง JPG/PNG/WebP แบบ multipart ไป POST `/api/v1/scan/` | API รับ request, สร้าง scan และคืน HTTP 202 พร้อม id ที่ mobile ใช้เป็น task id ได้ | API contract + schema | Planned |
| W06-IT-02 | FR-SCAN-03 | หลังได้ id ให้ mobile poll GET `/api/v1/scan/{id}` | response deserialize ได้และ status/progress เปลี่ยนตาม state จน completed/failed | State transition + contract | Planned |
| W06-IT-03 | Access control | ผู้ใช้ B GET scan id ของผู้ใช้ A | API ปฏิเสธตาม ownership rule; mobile map 401/403 เป็น auth error | Negative authorization | Planned |
| W06-IT-04 | Mobile/backend contract | mobile เรียก `cancelScan()` → DELETE `/api/v1/scan/{id}` | ต้องมี endpoint/contract ที่สอดคล้อง หรือ client ต้องไม่เรียก feature ที่ backend ไม่มี | Consumer-driven contract | Not Ready |

## I02 — ScanService ↔ Redis Cache

| Test ID | Trace | Scenario / stimulus | Expected integration behavior | Technique | Status |
|---|---|---|---|---|---|
| W06-IT-05 | FR-SCAN-03 AC-1 | Redis มี key ของ SHA-256 เดิม | cache hit ไม่เรียก inference ซ้ำ, scan result ถูก persist และผลที่ client ใช้ได้ยังครบ | Stub inference + fake Redis | Planned |
| W06-IT-06 | FR-SCAN-03 AC-2 | Redis ไม่มี key | เรียก full analysis หนึ่งครั้งและเขียน cache TTL 30 วัน | Interaction test | Planned |
| W06-IT-07 | FR-SCAN-03, FR-XAI-01 | cache hit แต่ heatmap file ถูกลบ/ไม่มีใน filesystem | ระบบต้องไม่ส่ง media reference ที่ใช้ไม่ได้โดยไม่จัดการสถานะ; behavior ต้องถูกกำหนด/ตรวจพบอย่างชัดเจน | Cache/storage consistency | Planned |

## I03 — ScanService ↔ InferenceService ↔ ONNX/OCR

| Test ID | Trace | Scenario / stimulus | Expected integration behavior | Technique | Status |
|---|---|---|---|---|---|
| W06-IT-08 | FR-ANALYSIS-01/02 | inference stub คืน visual/OCR contract ที่ถูกต้อง | ScanService map output ไป text/visual fields, risk calculation และ completed state โดยไม่ทำ field หาย | Service integration with stub | Planned |
| W06-IT-09 | FR-SCAN-03 | ONNX worker timeout/no stdout/error | error ถูกส่งกลับจาก InferenceService และ scan ถูก mark `failed` โดยไม่ทำ server process ล่ม | Fault injection | Planned |
| W06-IT-10 | FR-ANALYSIS-02 | worker คืน visual contract ตาม implementation ปัจจุบัน | test ต้อง expose W05 visual dual-signal gap; ห้ามตีความค่าซ้ำเป็น independent AI-Gen evidence | Contract characterization | Planned |

## I04 — Scan Pipeline ↔ Source Verification

| Test ID | Trace | Scenario / stimulus | Expected integration behavior | Technique | Status |
|---|---|---|---|---|---|
| W06-IT-11 | FR-ANALYSIS-03 AC-1/2/3 | Google Vision คืน similar URLs | source URLs/count ถูก map เป็น source score ตาม canonical formula และส่งต่อ risk pipeline | Adapter integration | Not Ready |
| W06-IT-12 | FR-ANALYSIS-03 AC-4 | Google Vision down/ยังไม่เชื่อมต่อ | `source_status="unavailable"`, `source_urls=[]`, แจ้งผู้ใช้ และตัด source dimension ออกจาก total score | Failure/fallback integration | Not Ready |

เหตุผลของ `Not Ready`: baseline `scan_service.py` ยังไม่เรียก Google Vision adapter และใช้ `settings.DEFAULT_SOURCE_SCORE` เป็น source score แทน จึงไม่มี production interface ให้ positive/fallback test เชื่อมต่ออย่างตรง SRS ได้ในตอนนี้

## I05 — Heatmap Storage ↔ API ↔ Mobile

| Test ID | Trace | Scenario / stimulus | Expected integration behavior | Technique | Status |
|---|---|---|---|---|---|
| W06-IT-13 | FR-XAI-01 AC-1 | inference คืน `heatmap_bytes` | ScanService บันทึกไฟล์ใน `LOCAL_UPLOAD_DIR/heatmaps`, API expose reference ที่ mobile แปลง/โหลดเป็น `/uploads/{filename}` ได้ | Temp filesystem + API contract | Planned |
| W06-IT-14 | FR-XAI-01 AC-1/2 | GET completed scan ที่มี heatmap | URL/reference จาก API ต้องชี้ไฟล์ที่ HTTP client เปิดได้จริงและ result model parse ได้ | Cross-layer media contract | Planned |

## I06 — Scan ↔ History ↔ Report

| Test ID | Trace | Scenario / stimulus | Expected integration behavior | Technique | Status |
|---|---|---|---|---|---|
| W06-IT-15 | FR-HISTORY-01 AC-1 | scan ของผู้ใช้ completed แล้วเรียก GET `/api/v1/history` | รายการของผู้ใช้มี scan ล่าสุด, risk score/grade และ thumbnail reference โดยไม่รั่วข้อมูลผู้ใช้อื่น | DB/API integration | Planned |
| W06-IT-16 | FR-HISTORY-01 AC-2/3 | เรียก history ด้วย date range และ risk grade ตาม SRS | server filter ตาม `created_at` และ risk grade contract เดียวกับ client | Consumer/API contract | Not Ready |
| W06-IT-17 | FR-HISTORY-02 AC-1 | ผู้ใช้ POST `/api/v1/reports` ด้วย scan ของตน | report เชื่อมกับ scan owner เดิม, บันทึก pending และคืน response ที่ตรง schema | DB/API integration | Planned |
| W06-IT-18 | FR-HISTORY-02 AC-2 | report scan เดิมซ้ำ | integration layer ปฏิเสธ HTTP 409 และไม่สร้าง duplicate report | Negative DB/API | Planned |

เหตุผลของ W06-IT-16 `Not Ready`: SRS ระบุ `start_date`, `end_date`, `risk_grade` แต่ history route baseline รับ `keyword` และ `risk_level` และยังไม่พบ date-range parameters จึงต้อง reconcile contract ก่อนทดสอบ acceptance ตาม SRS

## Planned execution order

1. I01 Mobile/API และ I03 Scan/Inference ก่อน เพราะเป็นเส้นทางหลักของ scan journey
2. I02 Cache และ I05 Heatmap เพื่อทดสอบ shared state/media contract
3. I06 History/Report หลังมี completed scan fixture ที่เสถียร
4. I04 Source Verification เมื่อ implementation/adapter ตรง FR-ANALYSIS-03 แล้ว

## Evidence rule

ไฟล์นี้เป็น test design ไม่ใช่ผล execution การมี test case ในตารางจึงไม่ถือว่า Pass จนกว่าจะมีคำสั่ง, environment, output และ evidence ที่รันจริงรองรับ
