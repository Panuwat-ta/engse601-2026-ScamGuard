# W05-03 — Existing Test Evidence and Execution Record

## Evidence baseline

Requirement authority ของ Week 05 คือ SRS v1.1 จาก `Document/srs` บน ENGSE212 `main` ส่วน code acceptance ตรวจจาก `origin/main` commit `66bc9e4a` ใน isolated archive ที่ `/tmp/scamguard-w05-main` โดยไม่ checkout ทับ working tree ของโครงงานจริง

- Canonical SRS URL: https://github.com/Panuwat-ta/project/tree/main/Document/srs
- SRS: `05_Software_Requirement_Specification.md` v1.1, dated 2026-09-12
- Source-code URL: https://github.com/Panuwat-ta/project
- Branch: main
- Code commit inspected: `66bc9e4a`
- Date referenced: 2026-09-22

## E05-01 — Existing risk-calculator test suite

Command scope: `server/tests/utils/test_risk_calculator.py` บน isolated `origin/main` archive

Result actually executed:

```text
1 passed in 0.03s
```

Interpretation: มี existing unit test ของ Hybrid max+bonus implementation และ algorithm หลักตรงกับ FR-ANALYSIS-04 v1.1

## E05-02 — Boundary execution against main implementation

รัน `calculate_risk_score()` บน source ของ commit `66bc9e4a` ได้ผลจริงดังนี้:

```text
(0, 39, 0) -> total=39, grade=low
(0, 40, 0) -> total=40, grade=medium
(0, 69, 0) -> total=69, grade=medium
(70, 0, 0) -> total=70, grade=high
```

ผลตรงกับ band rule Low 0–39 / Medium 40–69 / High 70–100 ใน SRS v1.1

## E05-03 — Canonical FR-ANALYSIS-04 examples reproduced

หลังเปลี่ยน test basis จาก snapshot v1.0 มาเป็น canonical SRS v1.1 ได้รันตัวอย่าง AC-1/AC-2 จริง:

```text
(50, 85, 0) -> total=90, grade=high, primary=visual, multi=True
(100, 100, 100) -> total=100, grade=high, primary=visual, multi=True
```

Disposition: `Existing — aligned`. Finding เดิมที่กล่าวว่า code ควรได้ weighted score 80 ถูกยกเลิก เพราะ weighted formula เป็นข้อมูลจาก baseline เก่า ไม่ใช่ SRS v1.1 ปัจจุบัน

## E05-04 — System Consent validation static execution

รัน Pydantic schema จาก `origin/main` ด้วย `system_consent=False` จริง ได้ผล:

```text
RegisterRequest accepts system_consent=False: True
```

Code review ของ `/auth/register` ไม่พบ guard ที่ reject ก่อนสร้าง user/ConsentLog ดังนั้น FR-AUTH-01 AC-5 ยังไม่มี implementation evidence ที่ผ่าน

## E05-05 — Consent endpoint inventory

`git grep` บน `origin/main` พบ consent write ตอน registration แต่ไม่พบ `PUT /consent/research` และ `GET /consent/logs` ใน `server/app/api/v1`

Disposition: W05-CT-14/15 = `Not Ready` จนกว่าจะมี endpoint/model contract ตาม SRS v1.1

## E05-06 — Right-to-Access route inventory

SRS v1.1 FR-PDPA-01 AC-4 ระบุ `GET /users/me` แต่ main มี profile read ที่ `GET /api/v1/auth/me`; `users` router มี `DELETE /api/v1/users/me` สำหรับลบบัญชี

Disposition: W05-CT-16 = `Not Ready` และเปิด finding เพื่อ reconcile route/response contract

## E05-07 — Auth component test execution status

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
