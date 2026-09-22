# W06-01 - Interface Scope and Risk Map

## 1. Baseline

- Requirement authority: ScamGuard SRS v1.1 in canonical `Document/srs`
- Requirement URL: https://github.com/Panuwat-ta/project/tree/main/Document/srs
- Implementation URL: https://github.com/Panuwat-ta/project
- Implementation branch: `main`
- Implementation commit: `66bc9e4a`
- SRS commit: `2b8a1fb0`
- Verification date: 2026-09-22

## 2. Interface map

| ID | Producer / caller | Consumer / dependency | Contract under test | Requirement trace | Execution outcome |
|---|---|---|---|---|---|
| I01 | Mobile Scan feature | FastAPI Scan API | multipart upload, HTTP status, scan id, polling, ownership, cancel | FR-SCAN-02, FR-SCAN-03 | Mixed: IT-02/03 Pass; IT-01/04 Fail |
| I02 | `scan_service.py` | Redis cache | SHA-256 key, hit/miss, TTL, cached media consistency | FR-SCAN-03, FR-XAI-01 | Mixed: IT-05 Pass; IT-06/07 Fail |
| I03 | `scan_service.py` | `inference_service.py` / ONNX / OCR | result mapping, failure propagation, visual output contract | FR-ANALYSIS-01/02 | Mixed: IT-08/09 Pass; IT-10 Fail |
| I04 | Scan pipeline | Source Verification / Google Vision | similar URLs, source score, API-down fallback | FR-ANALYSIS-03 | IT-11 Not Ready; IT-12 Fail |
| I05 | Inference / ScanService | heatmap storage / `/uploads` / Mobile | file persistence and public media reference | FR-XAI-01 | IT-13 Fail; IT-14 Pass |
| I06 | Completed scan | History API / Report API | history schema/filters, report create/duplicate contracts | FR-HISTORY-01/02 | IT-15/16/17/18 Fail |

## 3. Risk rationale

Week 06 เลือก interface ที่มีผลกระทบข้าม component มากกว่าทดสอบ function เดี่ยว ได้แก่ state transition ของ scan, cache/media lifecycle, worker failure propagation, fallback ของ external source service, media URL contract และ trace จาก scan ไป history/report

## 4. Test-double strategy

- Database: fake async session เฉพาะ transaction/query seam ที่ test ต้องควบคุม
- Redis: in-memory fake ที่บันทึก `get`/`setex` interaction และ TTL
- Inference: deterministic stub ที่คืนผลสำเร็จหรือบังคับ exception ตาม scenario
- Filesystem: `tmp_path`/test upload directory แยกจาก production uploads
- HTTP/API: FastAPI ASGI transport เรียก route จริงโดยไม่เปิด network port
- External Google Vision: ไม่สร้าง mock production contract ขึ้นเองเมื่อ adapter จริงยังไม่มี; positive case คง `Not Ready`

## 5. Scope boundary

การใช้ stub/fake มีเป้าหมาย isolate interface boundary ไม่ใช่ยืนยัน model accuracy, GPU performance, production Redis/PostgreSQL availability หรือ external Google Vision behavior จริง ประเด็นเหล่านั้นต้องมีหลักฐานคนละระดับใน Week 07/11 หรือหลัง implementation พร้อม
