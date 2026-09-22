# W05-01 - Component Test Scope and Test Basis

## 1. Purpose

กำหนดขอบเขตและฐานอ้างอิงสำหรับ Component / Unit Testing ของ ScamGuard โดยเลือก critical components ที่มีผลต่อผลวิเคราะห์ความเสี่ยง การสมัครสมาชิก และการจัดการ consent จากนั้นตรวจสอบ behavior ของแต่ละ component เทียบกับ canonical SRS v1.1

Week 05 ไม่ได้มีเป้าหมายทดสอบระบบทั้งหมด แต่ต้องแสดงเหตุผลในการเลือก component, เทคนิคที่ใช้ และเส้นทาง Requirement -> Test -> Evidence อย่างตรวจสอบย้อนกลับได้

## 2. Requirement baseline

- Canonical local source: `/home/panuwat/project/Document/srs/`
- Canonical URL: https://github.com/Panuwat-ta/project/tree/main/Document/srs
- Branch: `main`
- SRS: `05_Software_Requirement_Specification.md` v1.1, 2026-09-12
- SRS file SHA-256: `99bb8d5050fa54195b02869f1815e954fdd43ad0997e732b35426c70947cd40a`
- Latest inspected SRS-path commit on main: `2b8a1fb0`

Week 03/04 เป็น historical evidence จาก baseline v1.0 เท่านั้น หากข้อความเดิมขัดกับ SRS v1.1 จะไม่ใช้เป็น expected result ของ Week 05

## 3. Source-code baseline

- Repository: https://github.com/Panuwat-ta/project
- Branch: `main`
- Commit inspected: `66bc9e4a`
- Date referenced: 2026-09-22

การ execute ใช้ isolated archive ของ `origin/main` เพื่อไม่แก้หรือ checkout ทับ working branch อื่นใน `/home/panuwat/project`

## 4. Selected component scope

| Scope ID | Requirement | Component under test | Verification focus | Reason for selection |
|---|---|---|---|---|
| C01 | FR-ANALYSIS-02 | `server/app/services/onnx_worker.py` | Output contract ของ forgery / AI-Gen / visual score | เป็นจุดเชื่อม model output ไปยัง risk pipeline และ XAI/result contract |
| C02 | FR-ANALYSIS-04 | `server/app/utils/risk_calculator.py` | Hybrid max+bonus, grade boundaries, visual override | เป็น pure logic ที่ deterministic และมีผลต่อ final risk grade |
| C03 | FR-AUTH-01 | `server/app/schemas/auth.py`, `server/app/api/v1/auth.py` | Registration response และ mandatory System Consent | เป็น security/privacy gate ก่อนสร้าง user |
| C04 | FR-PDPA-01 | `server/app/models/consent.py` และ route inventory | Consent persistence, update/history endpoint, profile route | เป็น contractual interface ที่ต้องรองรับ PDPA/consent lifecycle |

## 5. Test strategy

| Technique | ใช้กับ | เหตุผล |
|---|---|---|
| Example-based unit/component test | FR-ANALYSIS-04 AC-1/2 | มี input/output ตัวอย่างชัดเจนใน SRS |
| Boundary-value check | Risk grade boundaries | ตรวจจุดเปลี่ยน Low/Medium/High ที่ 39/40/69/70 |
| Negative component test | FR-AUTH-01 AC-5 | ตรวจว่า mandatory consent ถูกปฏิเสธก่อน persistence |
| Contract/schema inspection | FR-ANALYSIS-02, FR-PDPA-01 | ใช้เมื่อ requirement ระบุ field/endpoint ชัด แต่ production component ยังไม่มี contract ครบ |
| Reproducible probe with fake DB | Registration/Consent | แยก handler logic จาก external DB/Redis และไม่ใช้ production secret |

## 6. Pre-test code-reading observations

1. `onnx_worker.py` ใช้ SegFormer maximum probability เป็นทั้ง `ai_gen_prob` และฐานของ `visual_risk_score`; ไม่พบ output `forgery_confidence` และ `ai_gen_confidence` แยกตาม FR-ANALYSIS-02
2. `risk_calculator.py` ใช้ Hybrid max+bonus และ risk bands ตาม SRS v1.1; finding เรื่อง weighted formula จาก baseline เก่าจึงไม่ใช่ defect ปัจจุบัน
3. Registration handler ยอมรับ `system_consent=false` และ response schema ไม่มี `status`/`created_at` ตาม FR-AUTH-01
4. Consent model ปัจจุบันเป็นหนึ่ง row ที่มีสอง boolean และไม่มี `updated_at`; ไม่พบ `PUT /consent/research` หรือ `GET /consent/logs`
5. SRS ระบุ profile read ที่ `GET /users/me` แต่ code baseline expose `GET /api/v1/auth/me`; `/api/v1/users/me` เป็น DELETE

## 7. Result status rule

- `Pass`: มี execution/inspection evidence ที่ตรง expected result ของ baseline
- `Fail`: evidence แสดงว่า implementation ปัจจุบันไม่ตรง expected result
- `Not Ready`: acceptance basis ชัด แต่ component/contract ที่ต้องใช้ยังไม่พร้อมให้ทดสอบอย่างถูกต้อง
- `Needs Clarification`: requirement ภายใน baseline เดียวกันมีตัวอย่างหรือเงื่อนไขที่ไม่สอดคล้องกันจนไม่ควรเดาผลที่คาดหวัง

## 8. Out of scope

- Dataset-level Accuracy, Precision, Recall, F1 และ mDice
- GPU inference performance <= 10 seconds
- Full System/UAT journey
- Performance/load percentile testing
- Retroactive research-dataset handling หลังถอน consent เนื่องจาก SRS v1.1 ยังไม่กำหนด behavior
- Stakeholder/legal approval ที่ไม่มีหลักฐาน

รายการ out-of-scope จะถูกส่งต่อไปยัง Week 06/07/11 หรือ requirement change process ตามประเภท โดยไม่สร้างผลทดสอบแทนสิ่งที่ยังไม่ได้ execute จริง
