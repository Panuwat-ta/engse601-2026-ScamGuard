# W06-04 — Interface Contract Evidence

หลักฐานนี้เป็นผลจาก code/SRS reading สำหรับออกแบบ Week 06 ยังไม่ใช่ execution result ของ integration tests

| Evidence ID | Source | Observed contract / fact | Used by |
|---|---|---|---|
| E06-01 | canonical SRS v1.1 FR-SCAN-02/03 | upload เป็น multipart; cache hit/miss ใช้ SHA-256 และ Redis TTL 30 วัน | I01, I02 |
| E06-02 | `scam_image_mobile/lib/core/network/api_endpoints.dart` | mobile ใช้ `/scan/` และ GET `/scan/{id}` | I01 |
| E06-03 | `scan_remote_datasource.dart` | submit scan ส่ง file + consent/clientRequestId/title; poll GET; cancel เรียก DELETE `/scan/{id}` | I01 |
| E06-04 | `server/app/api/v1/scan.py` | baseline มี POST `/` และ GET `/{scan_id}`; ไม่พบ DELETE scan route | I01, W06-F01 |
| E06-05 | `server/app/services/scan_service.py` | orchestration เชื่อม file validation, Redis, inference, scoring, DB, XAI และ websocket | I02–I05 |
| E06-06 | `server/app/services/inference_service.py` | ONNX worker ถูกเรียกเป็น subprocess JSON ผ่าน stdin/stdout แล้วรวม OCR result | I03 |
| E06-07 | canonical SRS v1.1 FR-ANALYSIS-03 AC-4 | source API down ต้อง `source_status="unavailable"` และตัด source จาก total score | I04 |
| E06-08 | `scan_service.py` | baseline ใช้ `settings.DEFAULT_SOURCE_SCORE` และส่ง source score เข้า risk calculator | I04, W06-F03 |
| E06-09 | canonical SRS v1.1 FR-XAI-01 AC-1 | heatmap expected URL คือ `/uploads/{filename}` | I05 |
| E06-10 | `server/app/main.py` + mobile `AnalysisResultModel` | server mount `/uploads`; mobile normalize relative path เป็น `/uploads/...` | I05 |
| E06-11 | canonical SRS v1.1 FR-HISTORY-01 | history กำหนด date range และ risk-grade filters | I06 |
| E06-12 | `server/app/api/v1/history.py` | baseline รับ `page, limit, keyword, risk_level`; ยังไม่พบ `start_date/end_date` | I06, W06-F05 |

## Baseline verification

- ENGSE212 main: `66bc9e4af3747808ef45273d31b50dbc59ad91ab`
- SRS latest commit touching file on main: `2b8a1fb095cea3e0fea28892f52d52a182840519`
- SRS SHA-256 verified equal between working canonical file and `origin/main`: `99bb8d5050fa54195b02869f1815e954fdd43ad0997e732b35426c70947cd40a`
- Date verified: 2026-09-22
