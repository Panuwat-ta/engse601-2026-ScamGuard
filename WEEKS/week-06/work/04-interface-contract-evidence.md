# W06-04 - Interface Contract and Execution Evidence

## 1. Evidence classification

- `Baseline record`: version/commit/hash ที่ใช้ freeze test basis
- `Source snapshot`: source excerpt/route/schema ที่ดึงจาก `/home/panuwat/project` ด้วย `git show origin/main:<path>` พร้อม commit/path/hash
- `Executed integration probe`: pytest/ASGI/service orchestration ที่ execute จริง
- `Executed contract probe`: source/signature contract ถูกตรวจด้วย test harness และ assertion
- `Static design source`: code/SRS reading ที่ใช้สร้าง expected result หรืออธิบาย blocker

## 2. Evidence register

| Evidence ID | Source | Observed fact / result | Used by |
|---|---|---|---|
| E06-01 | `work/evidence/E06-baseline.txt` | ENGSE212 main `66bc9e4a`; SRS v1.1 hash `99bb8d...d40a`; Python 3.10.21 | all cases |
| E06-S01 | `work/evidence/E06-source-contract-snapshot.txt` | exact origin/main excerpts + SHA-256 for scan/cache/source/heatmap/history/report/mobile contracts | IT-01, IT-04..07, IT-12..18 |
| E06-S02 | `work/evidence/E06-route-inventory.txt` | backend route decorators + mobile consumer calls captured from origin/main | IT-01..04, IT-15..18 |
| E06-S03 | `work/evidence/E06-schema-contract.txt` | exact Scan/History/Report schema fields from origin/main | IT-02, IT-13..18 |
| E06-02 | `work/probes/integration_probe_test.py` | reproducible ASGI/service integration harness with explicit test doubles | IT-01..10, IT-12..18 |
| E06-03 | `work/evidence/E06-integration-probe.txt` | final pytest execution: 11 failed / 6 passed; exit code 1 due expected product contract failures | IT-01..10, IT-12..18 |
| E06-04 | `work/evidence/E06-result-register.txt` | per-case result/observed contract summary including IT-11 Not Ready | all cases |
| E06-05 | canonical SRS FR-SCAN-02/03 | upload HTTP 202; cache hit/miss and TTL 30 days | I01/I02 |
| E06-06 | mobile `scan_remote_datasource.dart` + backend `scan.py` | mobile calls DELETE scan; backend route exposes POST/GET only | IT-04 / F02 |
| E06-07 | `scan_service.py` | Redis cache orchestration, heatmap file lifecycle, `DEFAULT_SOURCE_SCORE` | I02/I04/I05 |
| E06-08 | `onnx_worker.py` + W05 evidence | no separate `forgery_confidence`/`ai_gen_confidence` | IT-10 / F05 |
| E06-09 | canonical SRS FR-ANALYSIS-03 | API-down fallback must set unavailable and exclude source | IT-11/12 |
| E06-10 | canonical SRS FR-XAI-01 + `main.py` | expected `/uploads/{filename}`; server has `/uploads` static mount | IT-13/14 |
| E06-11 | canonical SRS FR-HISTORY-01 + `history.py`/schema | SRS `scans/risk_grade/start_date/end_date`; code `items/risk_level/keyword/risk_level` | IT-15/16 |
| E06-12 | canonical SRS FR-HISTORY-02 + report schema/service | HTTP 201/409 work, but `report_id`/duplicate message contract drifts | IT-17/18 |

## 3. Source evidence chain

Source-derived evidence ใช้ข้อมูลจริงจาก `/home/panuwat/project` แต่ freeze ที่ ENGSE212 `origin/main` commit `66bc9e4a` เพื่อไม่ให้ local `develop` หรือ uncommitted changes เปลี่ยนผลย้อนหลัง

```text
Canonical SRS v1.1
  -> ENGSE212 origin/main source snapshot / route inventory / schema snapshot
  -> integration_probe_test.py
  -> E06-integration-probe.txt
  -> E06-result-register.txt
  -> Week 06 PDF
```

ทุก source snapshot ระบุ URL `https://github.com/Panuwat-ta/project`, branch `main`, pinned commit, วันที่อ้างอิง, source path, line number และ SHA-256 ที่เกี่ยวข้อง โดยไม่เก็บ `.env`, secret หรือ production data

## 4. Execution command

```text
cd /tmp/scamguard-w06-main/server
PYTHONPATH=/tmp/scamguard-w06-main/server \
W06_BASELINE_ROOT=/tmp/scamguard-w06-main \
/home/panuwat/project/server/venv/bin/python -m pytest -q \
  /home/panuwat/work/engse601-2026-ScamGuard/WEEKS/week-06/work/probes/integration_probe_test.py
```

Test-only environment variables for DB/Redis/model paths were set to non-production dummy values. The harness does not connect to those external services; dependencies are replaced at the seam under test.

## 5. Final execution result

```text
11 failed, 6 passed in 0.88s
pytest_exit_code=1
```

The non-zero exit code represents deliberately asserted canonical contracts that the current implementation violates; it is not hidden as an infrastructure failure. W06-IT-11 is separately `Not Ready` because the production Google Vision adapter does not exist.

## 6. Claims not made

Week 06 does not claim:

- real PostgreSQL or Redis production availability
- real Google Vision success/failure behavior
- GPU/model inference performance or model accuracy
- full mobile-device UAT pass
- stakeholder approval
- independent peer-review approval
