# W06-02 - Integration Test Design and Results

## 1. Test basis

- Canonical SRS: https://github.com/Panuwat-ta/project/tree/main/Document/srs
- SRS: `05_Software_Requirement_Specification.md` v1.1, 2026-09-12
- Code: https://github.com/Panuwat-ta/project
- Branch / commit: `main` / `66bc9e4a`
- Execution date: 2026-09-22
- Raw evidence: `work/evidence/E06-integration-probe.txt`
- Result register: `work/evidence/E06-result-register.txt`

## 2. Result vocabulary

| Result | Definition |
|---|---|
| Pass | Executed integration/contract evidence ตรง expected result ของ selected behavior |
| Fail | Executed evidence ยืนยันว่า current implementation ไม่ตรง canonical contract/expected behavior |
| Not Ready | Requirement ต้องใช้ production interface ที่ยังไม่มีจริง จึงไม่สร้าง mock contract ใหม่แล้วนับเป็นผล acceptance |
| Not Executed | Test พร้อมแต่ไม่ได้ execute; ไม่มี case สถานะนี้ใน final Week 06 set |

ผล Pass ของ test case หนึ่งยืนยันเฉพาะ behavior ที่ case นั้นตรวจ ไม่ได้หมายความว่า requirement ทั้งข้อผ่านทั้งหมด

## 3. I01 - Mobile <-> Scan API

| Test ID | Trace | Scenario / stimulus | Expected integration behavior | Actual / evidence | Result |
|---|---|---|---|---|---|
| W06-IT-01 | FR-SCAN-02 AC-1 | multipart JPG ไป POST `/api/v1/scan/` | HTTP 202 และคืน `scan_id`/identifier | ASGI execution คืน HTTP 200 พร้อม `id`; status code ไม่ตรง SRS | Fail |
| W06-IT-02 | Scan polling contract | GET `/api/v1/scan/{id}` ที่ status=`processing_visual`, progress=50 | client ได้ id/status/progress สำหรับ poll state | HTTP 200; `id`, `status=processing_visual`, `progress=50` ตรง fixture | Pass |
| W06-IT-03 | Ownership rule | User B GET scan ของ User A | HTTP 403 | HTTP 403 จาก route จริง | Pass |
| W06-IT-04 | Mobile consumer contract | mobile เรียก DELETE `/api/v1/scan/{id}` | backend มี cancel contract หรือ consumer ไม่เรียก endpoint ที่ไม่มี | route จริงคืน HTTP 405 Method Not Allowed | Fail |

## 4. I02 - ScanService <-> Redis Cache

| Test ID | Trace | Scenario / stimulus | Expected integration behavior | Actual / evidence | Result |
|---|---|---|---|---|---|
| W06-IT-05 | FR-SCAN-03 AC-1 | Redis มี SHA-256 key เดิม | ใช้ cached result และไม่เรียก inference ซ้ำ | probe ยืนยัน scan completed, inference call=0, ไม่มี cache rewrite | Pass |
| W06-IT-06 | FR-SCAN-03 AC-2 | Cache miss | run analysis แล้ว `SETEX` TTL 30 วัน | `json.dumps(inference_result)` ล้มเมื่อ `heatmap_bytes=b''` ยังเป็น bytes; `SETEX` ไม่ถูกเรียก | Fail |
| W06-IT-07 | FR-SCAN-03 AC-1 + FR-XAI-01 | cache record มี `has_heatmap=true` แต่ไฟล์ heatmap หาย | cached result ต้องมี usable heatmap reference หรือ explicit degraded/recovery behavior | scan completed แต่ `heatmap_image_url=None`; ไม่มี recovery/degraded state | Fail |

## 5. I03 - ScanService <-> InferenceService / ONNX / OCR

| Test ID | Trace | Scenario / stimulus | Expected integration behavior | Actual / evidence | Result |
|---|---|---|---|---|---|
| W06-IT-08 | FR-ANALYSIS-01/02 | deterministic inference stub คืน visual=80, ai=0.8, OCR=`ด่วน` | map output ไป scan fields, keyword/text score และ completed state | `visual_score=80`, `text_score=25`, AI=0.8, keyword `ด่วน`, status completed | Pass |
| W06-IT-09 | scan failure boundary | inference seam raise exception | exception ถูก contain และ scan เปลี่ยนเป็น failed โดย process ไม่ crash ออกนอก boundary | status=`failed`, progress=0 | Pass |
| W06-IT-10 | FR-ANALYSIS-02 AC-1/2 | ตรวจ output contract ของ ONNX worker | มี separate `forgery_confidence` และ `ai_gen_confidence` ตาม SRS | executed contract probe ไม่พบทั้งสอง field; current worker ใช้ SegFormer max probability ร่วมกัน | Fail |

## 6. I04 - Scan Pipeline <-> Source Verification

| Test ID | Trace | Scenario / stimulus | Expected integration behavior | Actual / evidence | Result |
|---|---|---|---|---|---|
| W06-IT-11 | FR-ANALYSIS-03 AC-1/2/3 | Google Vision Web Detection คืน similar URLs | map URLs/count/context เป็น source score ตามสูตร canonical | baseline ไม่มี production Google Vision source-verification adapter ให้เชื่อมต่อ | Not Ready |
| W06-IT-12 | FR-ANALYSIS-03 AC-4 | source service down/ยังไม่เชื่อมต่อ | `source_status="unavailable"`, URLs ว่าง และตัด source dimension ออกจาก total score | current scan pipeline ไม่มี `source_status`; ใช้ `DEFAULT_SOURCE_SCORE` ต่อไป | Fail |

## 7. I05 - Heatmap Storage <-> API <-> Mobile

| Test ID | Trace | Scenario / stimulus | Expected integration behavior | Actual / evidence | Result |
|---|---|---|---|---|---|
| W06-IT-13 | FR-XAI-01 AC-1 | inference คืน `heatmap_bytes` | persist media และ response/reference เป็น `/uploads/{filename}` | file ถูกสร้าง แต่ `heatmap_image_url` เป็น absolute filesystem path | Fail |
| W06-IT-14 | FR-XAI-01 AC-1 | วาง test media ใต้ mounted upload directory แล้ว GET `/uploads/heatmaps/w06.jpg` | static media route เปิดไฟล์ canonical URL ได้ | HTTP 200 และ bytes ตรง test fixture | Pass |

## 8. I06 - Scan <-> History <-> Report

| Test ID | Trace | Scenario / stimulus | Expected integration behavior | Actual / evidence | Result |
|---|---|---|---|---|---|
| W06-IT-15 | FR-HISTORY-01 AC-1 | completed scan ของ user แล้ว GET `/api/v1/history` | HTTP 200 body ใช้ collection `scans` และ field `risk_grade` ตาม SRS | HTTP 200 แต่ body ใช้ `items` และ item ใช้ `risk_level` | Fail |
| W06-IT-16 | FR-HISTORY-01 AC-2/3 | filter `start_date`, `end_date`, `risk_grade` | route รองรับ query contract ทั้งสาม | function signature มี `keyword`, `risk_level`; ไม่มี date range/risk_grade | Fail |
| W06-IT-17 | FR-HISTORY-02 AC-1 | POST report ของ scan ตนเอง description >=10 | HTTP 201, status pending และ response มี `report_id` | persist pending และ HTTP 201 สำเร็จ แต่ response ใช้ `id` ไม่ใช่ `report_id` | Fail |
| W06-IT-18 | FR-HISTORY-02 AC-2 | report scan เดิมซ้ำ | HTTP 409, ไม่สร้าง duplicate, detail `You have already reported this scan` | HTTP 409 และไม่ add record แต่ detail=`This scan has already been reported` | Fail |

## 9. Execution summary

| Result | Count | Interpretation |
|---|---:|---|
| Pass | 6 | selected integration behavior มี execution evidence ตรง expected |
| Fail | 11 | API/data/service contract ปัจจุบันไม่ตรง expected baseline |
| Not Ready | 1 | production adapter ที่ requirement ต้องการยังไม่มีให้ execute |
| Total | 18 | Week 06 integration cases |

Pytest harness summary: `11 failed, 6 passed in 0.88s`; case W06-IT-11 ถูกเก็บ `Not Ready` นอก pytest เพราะการสร้าง fake Google Vision adapter ขึ้นเองจะทำให้เกิด contract ที่ production ยังไม่มี

## 10. Execution method and integrity

- ใช้ isolated archive ของ ENGSE212 `origin/main` commit `66bc9e4a`
- FastAPI route tests ใช้ ASGI transport โดยไม่เปิด network port
- DB/Redis/Inference ใช้ deterministic test doubles เฉพาะ seam ที่มี production interface อยู่แล้ว
- ไม่อ่าน `.env`, production token, API key, password หรือ production database data
- Source Verification positive case ไม่ถูก mock แล้วนับ Pass เพราะ production adapter ยังไม่มี
- Failure จาก product mismatch เก็บเป็น Fail; failure ที่เกิดจาก missing production interface ใช้ Not Ready

## 11. Evidence chain

- Source contract snapshot: `work/evidence/E06-source-contract-snapshot.txt`
- API/consumer route inventory: `work/evidence/E06-route-inventory.txt`
- Schema contract snapshot: `work/evidence/E06-schema-contract.txt`
- Executable integration probe: `work/probes/integration_probe_test.py`
- Raw pytest output: `work/evidence/E06-integration-probe.txt`
- Per-case result register: `work/evidence/E06-result-register.txt`

Source-derived files above ถูกสร้างจาก `/home/panuwat/project` โดย freeze ที่ ENGSE212 `origin/main` commit `66bc9e4a`; local `develop`/uncommitted changes ไม่ถูกใช้เป็น test basis
