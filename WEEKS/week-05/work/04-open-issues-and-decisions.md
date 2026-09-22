# W05-04 — Open Issues, Findings and Decisions Needed

## Findings from Code & Logic Reading Clinic

| ID | Finding | Trace / evidence | Impact | Status | Owner | Next action |
|---|---|---|---|---|---|---|
| W05-F01 | Visual Analysis contract ยังไม่ตรง SRS v1.1: baseline แยก SegFormer forgery confidence แบบ `Normalize(Confidence×Coverage)` และ AI-Gen detector แต่ main ใช้ max SegFormer probability เป็นทั้ง `visual_risk_score` และ `ai_gen_probability` | FR-ANALYSIS-02 AC-1/2/3; `server/app/services/onnx_worker.py` | W05-CT-01 ถึง 03 ยังใช้เป็น requirement pass ไม่ได้ | Not Ready | ภานุวัฒน์ | กำหนด/implement output contract ให้ตรง canonical SRS หรือแก้ baseline ผ่าน change process แล้ว re-test |
| W05-F02 | Finding เดิมเรื่อง weighted Overall Risk Score ถูกยกเลิกหลังยืนยัน canonical SRS v1.1; Hybrid max+bonus ใน main ตรง AC-1/2 แต่ AC-7 Visual Override ใช้ตัวอย่าง `risk_score=65, visual=85` ซึ่งเกิดจาก calculator เดียวกันไม่ได้เพราะ total ต้องไม่น้อยกว่า visual | FR-ANALYSIS-04 AC-1/2/7; E05-03 | Algorithm หลักผ่านการ align แต่ AC-7 ควร clarify ว่าเป็น grade-rule unit test แยกหรือ legacy example | Needs Clarification | ภานุวัฒน์ | เก็บ Hybrid max+bonus เป็น baseline; review AC-7 wording โดยไม่เปลี่ยน algorithm จากการเดา |
| W05-F03 | `system_consent=False` ผ่าน `RegisterRequest` และ route ไม่มี explicit reject | FR-AUTH-01 AC-5; E05-04 | ขัดข้อกำหนด System Consent บังคับ | Not Ready | ภานุวัฒน์ | เพิ่ม validation/route guard แล้วเพิ่ม negative API test |
| W05-F04 | Consent storage contract ไม่ตรง SRS v1.1: SRS ระบุ consent log event fields (`consent_type`, `is_granted`, timestamps) แต่ main เก็บหนึ่ง row สอง boolean และไม่มี `updated_at` | FR-PDPA-01 AC-2/3/5 | revoke/audit trail ตาม baseline ยังยืนยันไม่ได้ | Not Ready | ภานุวัฒน์ | Reconcile canonical consent schema กับ implementation/migration ก่อน re-test |
| W05-F05 | ไม่พบ `PUT /consent/research` และ `GET /consent/logs` บน main | FR-PDPA-01 AC-3/5; E05-05 | ถอน Research Consent และอ่าน audit logs ยังทดสอบไม่ได้ | Not Ready | ภานุวัฒน์ | Implement endpoint ตาม baseline หลัง schema decision แล้วเพิ่ม API component tests |
| W05-F06 | Right-to-Access route contract ไม่ตรง: SRS ระบุ `GET /users/me` แต่ main ใช้ `GET /api/v1/auth/me`; `/api/v1/users/me` เป็น DELETE | FR-PDPA-01 AC-4; E05-06 | Client/API contract และ test path ไม่ตรง baseline | Not Ready | ภานุวัฒน์ | ตัดสิน canonical route แล้วปรับ SRS หรือ code ผ่าน controlled change จากนั้นเพิ่ม contract test |
| W05-F07 | W03/W04 handoff อ้าง SRS v1.0 แต่ canonical source ปัจจุบันเป็น SRS v1.1; บาง finding/decision เช่น weighted score 0.25/0.45/0.30 ถูกแก้ใน baseline ใหม่แล้ว | IN-02, SRS v1.1, W03/W04 artifacts | ถ้าใช้ handoff เก่าโดยไม่ re-check จะสร้าง test case ผิด baseline | Open | ภานุวัฒน์ | อัปเดต Input Register และใช้ SRS v1.1 เป็น authority สำหรับ W05 เป็นต้น; เก็บ W03/W04 เป็น historical evidence |

## Week 05 working decision

Week 05 เดินหน้าต่อด้วย canonical SRS v1.1 โดยรับ Hybrid max+bonus เป็น current requirement และใช้ existing risk-calculator evidence ได้ ส่วน Visual Analysis contract และ consent flows ยังเป็น `Not Ready` ตาม findings ด้านบน

W03/W04 ยังคงเป็นหลักฐานการทบทวนย้อนหลัง ไม่แก้ไฟล์ submission เก่าเพื่อซ่อนประวัติ แต่จะไม่ยก wording จาก v1.0 มา override SRS v1.1

Behavior ที่ SRS v1.1 ไม่ได้กำหนด เช่น retroactive deletion ของข้อมูล research หลังถอน consent จะไม่ถูกสร้าง expected result ขึ้นเอง และไม่ถือเป็น Week 05 acceptance criterion

## Re-check criteria

- W05-F01 ปิดได้เมื่อ main มี visual output contract ที่ trace ได้ถึง FR-ANALYSIS-02 AC-1/2/3 หรือมี baseline revision ที่อนุมัติแล้ว
- W05-F02 ปิดได้เมื่อ AC-7 ถูกทำให้ testable โดยไม่ขัดกับ Hybrid max+bonus หรือมีคำอธิบายว่าเป็น isolated grading rule
- W05-F03 ปิดได้เมื่อ `system_consent=false` ได้ HTTP 400 และไม่มี user/consent data ถูกสร้าง
- W05-F04/F05 ปิดได้เมื่อ consent schema/API รองรับ revoke + audit trail ตาม SRS v1.1 และ component tests ผ่าน
- W05-F06 ปิดได้เมื่อ profile route/response contract ตรงกันระหว่าง SRS และ main
- W05-F07 ปิดได้เมื่อ source/version register และ Week 05 trace ใช้ canonical v1.1 ครบ โดยไม่แก้ประวัติ submission เก่า

## Canonical SRS reference

- URL: https://github.com/Panuwat-ta/project/tree/main/Document/srs
- Branch: main
- SRS version: 1.1

## Source-code reference

- URL: https://github.com/Panuwat-ta/project
- Branch: main
- Commit: `66bc9e4a`
- Date: 2026-09-22
