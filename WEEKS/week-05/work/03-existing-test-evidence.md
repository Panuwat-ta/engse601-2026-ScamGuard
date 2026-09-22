# W05-03 — Existing Test Evidence and Execution Record

## Evidence baseline

หลักฐาน acceptance ของ Week 05 ต้องผูกกับ ENGSE212 `main` ตาม IN-04 จึงตรวจจาก `origin/main` commit `66bc9e4a` ใน isolated archive ที่ `/tmp/scamguard-w05-main` โดยไม่ checkout ทับ working tree ของโครงงานจริง

- URL: https://github.com/Panuwat-ta/project
- Branch: main
- Commit: `66bc9e4a`
- Date: 2026-09-22

## E05-01 — Existing risk-calculator test suite

Command scope: `server/tests/utils/test_risk_calculator.py` บน isolated `origin/main` archive

Result actually executed:

```text
1 passed in 0.03s
```

Interpretation: มี existing unit test ของ Hybrid Worst-Case implementation แต่ test เดิมไม่ได้ตรวจว่า algorithm ตรงกับ weighted formula ใน SRS FR-ANALYSIS-04 AC-1

## E05-02 — Boundary execution against main implementation

รัน `calculate_risk_score()` บน source ของ commit `66bc9e4a` ได้ผลจริงดังนี้:

```text
(0, 39, 0) -> total=39, grade=low
(0, 40, 0) -> total=40, grade=medium
(0, 69, 0) -> total=69, grade=medium
(70, 0, 0) -> total=70, grade=high
```

## E05-03 — SRS weighted-score mismatch reproduced

SRS FR-ANALYSIS-04 AC-1 กำหนด input `text=75, visual=87, source=75` และ expected `risk_score=80` จากสูตร 0.25/0.45/0.30

Execution against `origin/main` returned:

```text
(75, 87, 75) -> total=97, grade=high, primary=visual, multi=True
```

Disposition: `Existing — mismatch found`. ห้ามนับเป็น requirement pass; เปิด finding W05-F02 เพื่อ reconcile source of truth กับ implementation

## E05-04 — System Consent validation static execution

รัน Pydantic schema จาก `origin/main` ด้วย `system_consent=False` จริง ได้ผล:

```text
RegisterRequest accepts system_consent=False: True
```

Code review ของ `/auth/register` ไม่พบ guard ที่ reject ก่อนสร้าง user/ConsentLog ดังนั้น AC-R5-02 ยังไม่มี implementation evidence ที่ผ่าน

## E05-05 — Consent endpoint inventory

`git grep` บน `origin/main` พบ consent API logic เฉพาะ registration ใน `server/app/api/v1/auth.py`; ไม่พบ GET/PUT consent-management route ใน `server/app/api/v1`

Disposition: W05-CT-14 ถึง W05-CT-16 = `Not Ready` จนกว่าจะมี canonical endpoint/behavior

## E05-06 — Auth component test execution status

พยายามรัน `server/tests/api/test_auth.py` จาก isolated `origin/main` archive แต่ test collection หยุดก่อน execute เพราะ archive ไม่รวม runtime `.env` และ `Settings` ต้องการ `ALLOWED_ORIGINS`, `DATABASE_URL`, `JWT_SECRET_KEY`, `REDIS_URL`, `ONNX_MODEL_PATH`, `XAI_MODEL_PATH`

Disposition: `Not Executed` ไม่ใช่ `Fail`. จะรันใหม่เมื่อมี test environment ที่กำหนดค่าอย่างปลอดภัยโดยไม่ copy secret เข้า evidence repo

## Supplementary run — not baseline acceptance evidence

บน working tree `/home/panuwat/project` branch `refactoring-admin` มีการรัน read-only test scope:

```text
server/tests/utils/test_risk_calculator.py
server/tests/utils/test_onnx_runner.py
server/tests/api/test_auth.py
10 passed, 2 warnings in 0.12s
```

ผลนี้ใช้เพื่อดูความพร้อมของ test harness เท่านั้น ไม่ใช้ตัดสิน Week 05 baseline เพราะ IN-04 ระบุ branch `main` และ working tree มีการเปลี่ยนแปลงที่ยังไม่ merge

## Evidence rule

ไม่มีการสร้าง screenshot, log, pass/fail หรือ stakeholder approval ที่ไม่ได้เกิดขึ้นจริง ทุก execution ที่บันทึกด้านบนมาจากคำสั่งที่รันจริงใน session วันที่ 2026-09-22
