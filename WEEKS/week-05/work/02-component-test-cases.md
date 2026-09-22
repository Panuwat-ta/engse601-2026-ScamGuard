# W05-02 — Component Test Case Set

## Status vocabulary

- `Existing`: มี test/execution evidence จริงที่ตรวจได้แล้ว
- `Planned`: ออกแบบ test ได้ แต่ยังไม่ได้รันหรือยังไม่อยู่ใน automated suite
- `Not Ready`: ยังมี blocker ด้าน requirement, implementation หรือ environment
- `Needs Clarification`: wording ใน baseline ทำให้สร้าง pass/fail ที่มีความหมายไม่ได้โดยไม่ตีความเพิ่ม
- `Deferred`: ไม่ใช่ acceptance basis ของ Week 05 baseline ปัจจุบัน

## Test cases: Visual analysis and risk logic

| TC ID | Trace | Component | Input / condition | Expected result from SRS v1.1 | Method | Status |
|---|---|---|---|---|---|---|
| W05-CT-01 | FR-ANALYSIS-02 AC-1 | SegFormer/ONNX output contract | probability map ของภาพ forgery | `forgery_confidence` อยู่ 0–100 และมีวิธีคำนวณที่ trace ได้ถึง `Normalize(Confidence×Coverage)` | Adapter/component test | Not Ready — main ยัง expose max probability เป็น visual score โดยตรง |
| W05-CT-02 | FR-ANALYSIS-02 AC-2 | AI-Gen detector contract | ภาพ Stable Diffusion | มี `ai_gen_confidence` 0–100 จาก AI-Gen Detection Model แยกจาก forgery signal | Component/model-adapter test | Not Ready — ไม่พบ separate detector contract บน main |
| W05-CT-03 | FR-ANALYSIS-02 AC-3/4 | Visual score contract | output จาก visual pipeline | `visual_score` อยู่ 0–100 และภาพจริงตาม AC-4 ให้ค่าต่ำตามตัวอย่าง baseline โดยไม่ alias signal คนละชนิดเป็นค่าเดียวกัน | Component contract test | Not Ready — implementation contract ยังไม่ตรง wording |
| W05-CT-04 | FR-ANALYSIS-04 AC-1 | Overall risk calculator | text=50, visual=85, source=0 | `risk_score=90`, grade=`high`, primary=`visual` ตาม Hybrid max+bonus | Pure unit execution | Existing |
| W05-CT-05 | FR-ANALYSIS-04 AC-2 | Overall risk calculator | 100/100/100 | `risk_score=100`, grade=`high` | Pure unit execution | Existing |
| W05-CT-06 | FR-ANALYSIS-04 AC-3–6 band rule | Risk grade boundary | total basis = 39 | grade=`low` | Boundary unit execution | Existing |
| W05-CT-07 | FR-ANALYSIS-04 AC-3–6 band rule | Risk grade boundary | total basis = 40 | grade=`medium` | Boundary unit execution | Existing |
| W05-CT-08 | FR-ANALYSIS-04 AC-3–6 band rule | Risk grade boundary | total basis = 69 | grade=`medium` | Boundary unit execution | Existing |
| W05-CT-09 | FR-ANALYSIS-04 AC-3–6 band rule | Risk grade boundary | total basis = 70 | grade=`high` | Boundary unit execution | Existing |
| W05-CT-10 | FR-ANALYSIS-04 AC-7 | Visual Override | SRS ยกตัวอย่าง risk_score=65, visual_score=85 | grade=`high` | Rule-level test หลังแยก grading concern | Needs Clarification — ภายใต้ Hybrid max+bonus เดียวกัน visual=85 ทำให้ total ต่ำกว่า 85 ไม่ได้ |

## Test cases: Registration and consent

| TC ID | Trace | Component | Input / condition | Expected result from SRS v1.1 | Method | Status |
|---|---|---|---|---|---|---|
| W05-CT-11 | FR-AUTH-01 AC-1 + FR-PDPA-01 AC-2 | `/auth/register` + ConsentLog | system=true, research=true/false | HTTP 201 และ consent evidence ตรง contract ของ SRS โดยไม่คืน password/hash | FastAPI component/API + persistence assertion | Not Ready — storage shape ไม่ตรง AC-2 |
| W05-CT-12 | FR-AUTH-01 AC-5 | Register validation | system=false | HTTP 400 `System consent is required`; ต้องไม่สร้างบัญชี | Negative API test | Not Ready — implementation gap |
| W05-CT-13 | FR-AUTH-01 AC-1 | Registration | system=true, research=false | Research Consent เป็น optional; registration สำเร็จ | API test | Planned |
| W05-CT-14 | FR-PDPA-01 AC-3 | Research-consent update | `PUT /consent/research` `{is_granted:false}` | HTTP 200 และบันทึก revoke พร้อม `updated_at` | Component/API test | Not Ready — endpoint/model contract absent |
| W05-CT-15 | FR-PDPA-01 AC-5 | Consent audit trail | `GET /consent/logs` | HTTP 200 และ logs มี consent_type/is_granted/created_at/updated_at | Component/API + DB assertion | Not Ready — endpoint/audit contract absent |
| W05-CT-16 | FR-PDPA-01 AC-4 | Right to Access profile | `GET /users/me` | HTTP 200 พร้อม `{id, full_name, email, role, status, created_at}` | API contract test | Not Ready — main ใช้ `/api/v1/auth/me` และ response contract ต่างจาก SRS |
| W05-CT-17 | Historical W03 Q-06 | Retroactive research dataset | revoke หลังข้อมูลเคย export | ไม่มี expected result ใน SRS v1.1 | ไม่ใช้เป็น acceptance test จน baseline กำหนด | Deferred |

## Interpretation rules

- `Existing` หมายถึงมี execution evidence เฉพาะ behavior นั้น ไม่ได้แปลว่า requirement ทั้งข้อผ่านแล้ว
- SRS v1.1 ใน `Document/srs` เป็น authority; wording จาก W03/W04 ที่มาจาก v1.0 ใช้เป็นประวัติการ review ไม่ใช่ข้อกำหนดใหม่โดยอัตโนมัติ
- W05-CT-17 ถูก defer เพราะ canonical SRS ไม่กำหนด retroactive delete-vs-going-forward; ห้ามสร้าง policy แทน owner/stakeholder
- Requirement-code mismatch ต้องเปิด finding และให้ owner ตัดสินว่าจะปรับ requirement/design/implementation ก่อน re-test

## Canonical SRS reference

- URL: https://github.com/Panuwat-ta/project/tree/main/Document/srs
- Branch: main
- SRS version: 1.1

## Source-code reference

- URL: https://github.com/Panuwat-ta/project
- Branch: main
- Commit: `66bc9e4a`
- Date: 2026-09-22
