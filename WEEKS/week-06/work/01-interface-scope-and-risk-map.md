# W06-01 — Interface Scope and Risk Map

## Baseline

- Requirement authority: ScamGuard SRS v1.1, canonical `Document/srs` on ENGSE212 `main`
- Requirement URL: https://github.com/Panuwat-ta/project/tree/main/Document/srs
- Implementation URL: https://github.com/Panuwat-ta/project
- Implementation branch: `main`
- Implementation commit inspected: `66bc9e4a`
- Date referenced: 2026-09-22

## Interface map

| ID | Producer / caller | Consumer / dependency | Contract under test | Requirement trace | Risk | Entry status |
|---|---|---|---|---|---|---|
| I01 | Mobile Scan feature | FastAPI `/api/v1/scan/` | multipart upload, returned scan id, polling GET, ownership/error mapping | FR-SCAN-02, FR-SCAN-03 | client/server path or schema drift breaks scan journey | Ready to design |
| I02 | `scan_service.py` | Redis cache | SHA-256 cache key, hit/miss behavior, TTL, reusable result | FR-SCAN-03 | cache result can diverge from DB/filesystem state | Ready to design |
| I03 | `scan_service.py` | `inference_service.py` → ONNX worker/OCR | subprocess JSON/result contract, timeout/error propagation, visual/OCR fields | FR-ANALYSIS-01/02 | worker/OCR failure can fail whole scan or return incomplete result | Ready to design with W05 constraint |
| I04 | Scan analysis pipeline | Google Vision / Source Verification | source URLs, source score, API-down fallback and exclusion from total score | FR-ANALYSIS-03 | current code may inject a default source score instead of marking unavailable | Not Ready for positive integration |
| I05 | Inference/ScanService | local heatmap storage → API → Mobile | persisted heatmap path must become usable `/uploads/...` URL | FR-XAI-01 | path/URL mismatch or missing file prevents XAI display | Ready to design |
| I06 | Completed scan | History API → Report API | completed scan visibility, ownership, filters, report reference | FR-HISTORY-01/02 | cross-module contract drift breaks trace from scan to history/report | Ready to design |

## Code-reading observations

1. Mobile และ backend ใช้ scan path เดียวกันแล้ว: mobile `ApiEndpoints.scans = '/scan/'`, backend router prefix `/scan` + POST `/`; polling ใช้ GET `/scan/{id}`.
2. Mobile มี `cancelScan()` ที่เรียก DELETE `/scan/{id}` แต่ backend `scan.py` บน baseline มีเฉพาะ POST และ GET จึงเป็น interface mismatch ที่ต้องออก negative/contract test.
3. Cache hit อ่านผลจาก Redis แต่ heatmap bytes ถูกถอดออกก่อน cache; ต้องทดสอบว่าผลจาก cache ยังชี้ไปยังไฟล์ heatmap ที่มีอยู่และ client เปิดได้.
4. `inference_service.py` เชื่อม ONNX worker ผ่าน subprocess stdin/stdout และรวม OCR ใน `predict()` เดียว; timeout/no-output/error จึงเป็น failure boundary ระหว่าง service กับ worker.
5. FR-ANALYSIS-03 AC-4 กำหนด API-down fallback เป็น `source_status="unavailable"` และตัด source ออกจากคะแนนรวม แต่ `scan_service.py` ปัจจุบันใช้ `settings.DEFAULT_SOURCE_SCORE` แล้วส่งเข้า `calculate_risk_score()`.
6. FR-XAI-01 AC-1 คาด `heatmap_url: "/uploads/{filename}"`; backend เก็บ filesystem path ใน `heatmap_image_url` ขณะที่ mobile มี logic แปลง relative path เป็น `/uploads/...`. ต้องยืนยัน contract ข้าม storage/API/mobile.
7. History SRS กำหนด date/risk filters แต่ implementation ปัจจุบันใช้ `keyword` และ `risk_level` และยังไม่เห็น `start_date/end_date`; เป็น integration contract gap สำหรับ I06.

## Test-double strategy

- Redis: fake/in-memory Redis หรือ dependency replacement เพื่อบังคับ cache hit/miss โดยไม่พึ่ง shared environment
- Inference: stub `inference_service.predict()` สำหรับ success/timeout/error และตรวจ ScanService orchestration แยกจาก model accuracy
- Source Verification: stub Google Vision adapter เมื่อ implementation มี contract จริง; จนกว่านั้น positive cases เป็น `Not Ready`
- Database: isolated test DB/transaction เพื่อยืนยัน ownership, persistence และ scan→history→report relation
- Filesystem: temporary upload directory เพื่อยืนยัน raw image/heatmap lifecycle โดยไม่แตะ production uploads
