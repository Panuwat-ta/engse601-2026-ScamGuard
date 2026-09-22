# W05-02 — Component Test Case Set

## Status vocabulary

- `Existing`: มี test/execution evidence จริงที่ตรวจได้แล้ว
- `Planned`: ออกแบบ test ได้ แต่ยังไม่ได้รันหรือยังไม่อยู่ใน automated suite
- `Not Ready`: ยังมี blocker ด้าน requirement, implementation หรือ environment

## Test cases: Visual analysis and risk logic

| TC ID | Trace | Component | Input / condition | Expected result from SRS/W03 | Method | Status |
|---|---|---|---|---|---|---|
| W05-CT-01 | REQ-01 / AC-R1-01 | ONNX worker output contract | probability map จาก visual model | score ที่ส่งออกอยู่ 0–100 และ contract ระบุสัญญาณที่ใช้คำนวณ `visual_score` อย่างตรวจย้อนกลับได้ | Adapter/component test | Planned |
| W05-CT-02 | REQ-01 / AC-R1-01 | Visual score calculation | forgery=85, AI-gen=90 | `visual_score = round(85×0.6 + 90×0.4) = 87` | Pure unit test เมื่อมี dual-signal calculator | Not Ready |
| W05-CT-03 | REQ-01 / AC-R1-02/03 | Detection threshold | confidence รอบ threshold | ต่ำกว่า threshold = ไม่พบ, ที่/เหนือ threshold = พบ ตาม Q-01 | Boundary test | Not Ready |
| W05-CT-04 | FR-ANALYSIS-04 AC-1 | Overall risk calculator | text=75, visual=87, source=75 | `risk_score=80` ตาม weighted formula 0.25/0.45/0.30 | Pure unit test | Existing — mismatch found |
| W05-CT-05 | FR-ANALYSIS-04 AC-2 | Overall risk calculator | 100/100/100 | `risk_score=100` | Pure unit test | Existing |
| W05-CT-06 | FR-ANALYSIS-04 AC-3 | Risk grade | score basis ให้ผลรวม 39 | grade=`low` | Boundary unit test | Existing |
| W05-CT-07 | FR-ANALYSIS-04 AC-4 | Risk grade | score basis ให้ผลรวม 40 | grade=`medium` | Boundary unit test | Existing |
| W05-CT-08 | FR-ANALYSIS-04 AC-4 | Risk grade | score basis ให้ผลรวม 69 | grade=`medium` | Boundary unit test | Existing |
| W05-CT-09 | FR-ANALYSIS-04 AC-5 | Risk grade | score basis ให้ผลรวม 70 | grade=`high` | Boundary unit test | Existing |
| W05-CT-10 | FR-ANALYSIS-04 AC-6 | Visual Override | `risk_score=65`, `visual_score=85` | grade=`high` แม้ final score <70 | Unit test ของ grade rule หลังคำนวณ final score | Not Ready — algorithm mismatch |

## Test cases: Consent management

| TC ID | Trace | Component | Input / condition | Expected result from SRS/W03 | Method | Status |
|---|---|---|---|---|---|---|
| W05-CT-11 | REQ-05 / AC-R5-01 | `/auth/register` + ConsentLog | system=true, research=false | สมัครสำเร็จและมีหลักฐาน consent ที่ตรวจย้อนกลับได้ | FastAPI component/API test | Planned |
| W05-CT-12 | REQ-05 / AC-R5-02 | Register validation | system=false | HTTP 400 `System consent is required`; ต้องไม่สร้างบัญชี | Negative API test | Not Ready — implementation gap |
| W05-CT-13 | REQ-05 / AC-R5-01 | Registration | system=true, research=false | Research Consent เป็น optional; การไม่ยินยอมต้องไม่ block registration | API test + persisted consent check | Planned |
| W05-CT-14 | REQ-05 / AC-R5-03 | Research-consent update | grant แล้ว revoke ผ่าน consent endpoint | HTTP 200, research=false, มี audit timestamp | Component/API test | Not Ready — endpoint absent |
| W05-CT-15 | REQ-05 / AC-R5-04 | Consent audit trail | grant → revoke แล้วอ่าน logs | history ครบตามเวลา ไม่มี event หาย | Component/API + DB assertion | Not Ready — endpoint/audit model absent |
| W05-CT-16 | REQ-05 / AC-R5-05 | System-consent withdrawal | พยายามถอนโดยไม่ลบบัญชี | server reject / ไม่มี endpoint ที่อนุญาต | Negative API test | Not Ready — canonical behavior ยังไม่ implement |
| W05-CT-17 | REQ-05 / Q-06 | Research dataset handling | revoke หลังข้อมูลเคย approved/exported | ต้องเป็นไปตาม decision Q-06 เท่านั้น | Review + later integration test | Not Ready — decision open |

## Interpretation rules

- `Existing` หมายถึงมี execution evidence เฉพาะ behavior นั้น ไม่ได้แปลว่า requirement ทั้งข้อผ่านแล้ว
- W05-CT-02/03 ห้ามตั้ง threshold ใหม่เอง เพราะ Q-01 ยังเปิดอยู่
- W05-CT-17 ห้ามสรุป delete-vs-going-forward แทน owner/advisor เพราะ Q-06 ยังเปิดอยู่
- Requirement-code mismatch ต้องเปิด finding และให้ owner ตัดสินว่าจะปรับ requirement, design หรือ implementation ก่อน re-test

## Source-code reference

- URL: https://github.com/Panuwat-ta/project
- Branch: main
- Commit: `66bc9e4a`
- Date: 2026-09-22
