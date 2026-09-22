# W05-01 — Component Test Scope and Test Basis

## Scope

Week 05 เริ่มจาก critical slice ที่ Week 04 ระบุไว้ ไม่ขยายไปทดสอบทั้งระบบในรอบเดียว

| Scope ID | Requirement / rule | Component under test | Reason |
|---|---|---|---|
| C01 | REQ-01 / FR-ANALYSIS-02 | `server/app/services/onnx_worker.py` | เป็นจุดสร้าง `visual_risk_score` จากผล visual model |
| C02 | FR-ANALYSIS-04 supporting rule | `server/app/utils/risk_calculator.py` | เป็น logic ตัด Low/Medium/High และ Visual Override ที่ AC-R1 อ้างต่อ |
| C03 | REQ-05 / FR-PDPA-01 + FR-AUTH-01 | `server/app/schemas/auth.py`, `server/app/api/v1/auth.py`, `server/app/models/consent.py` | registration และ consent persistence เป็น component ที่มี code จริงบน main |

## Inputs frozen for this draft

- Requirement baseline: SRS v1.0 / IN-02
- Design baseline: IN-03 v1.0 ใช้ประกอบ แต่หากขัดกับ SRS ให้ SRS เป็น test basis
- Week 03 revised wording ใช้เป็น proposed clarification; Q-01 ถึง Q-06 ที่ยังไม่ปิดไม่ถือเป็น decision ใหม่
- Week 04 Gate A = Conditional; W05 จึงต้องคง blocker และ owner ไว้ให้เห็น

## Source-code baseline

ตรวจ code จาก repository ENGSE212 ที่ประกาศเป็น IN-04 โดยอ้าง `origin/main` ไม่ใช้ behavior จาก working branch อื่นเป็น acceptance basis

- URL: https://github.com/Panuwat-ta/project
- Branch: main
- Commit inspected: `66bc9e4a`
- Date referenced: 2026-09-22

## Code-reading result before test design

1. `onnx_worker.py` บน main สร้าง `visual_risk_score = round(max(forgery_probability) * 100)` และใส่ค่าเดียวกันเป็น `ai_gen_probability`; ยังไม่เห็นสองสัญญาณอิสระ `forgery_confidence` และ `ai_gen_confidence` ตามสูตร SRS/W03 `0.6/0.4` จึงยังใช้ code ปัจจุบันพิสูจน์ AC-R1-01 ตาม revised wording ไม่ได้
2. `risk_calculator.py` มี logic Low 0–39, Medium 40–69, High 70–100 และ Visual Override เมื่อ `visual_score >= 80`; สามารถออกแบบ boundary unit test ได้ทันที
3. `RegisterRequest` ยอมรับ `system_consent=False` และ route `/auth/register` ไม่มี guard ที่ reject ค่านี้ก่อนสร้าง user; ขัดกับ SRS ที่คาด HTTP 400 เมื่อไม่ให้ System Consent
4. `ConsentLog` บน main เป็นหนึ่ง row ที่มี `system_consent` และ `research_consent`; ยังไม่มี `updated_at` และไม่พบ GET/PUT consent-management endpoint ใน `server/app/api/v1`

## Test approach

- Unit/logic tests: deterministic pure logic เช่น risk-grade boundaries และ input clamping
- Component/API tests: FastAPI route + mocked/isolated DB สำหรับ registration/consent behavior
- Component adapter tests: ONNX worker contract โดยไม่อ้างว่า model accuracy ผ่าน จนกว่าจะมี model/dataset evidence จริง
- ทุก case ที่พึ่ง Q-01/Q-06 หรือ endpoint ที่ยังไม่มี ให้ใช้ `Not Ready` หรือ `Planned` แทนการสร้างผลผ่าน–ไม่ผ่านขึ้นมาเอง

## Out of scope for Week 05 draft

- Dataset-level Accuracy/Precision/Recall/F1 ของ NFR-05: ส่งต่อ System evaluation
- System/UAT journey: Week 07
- Performance percentile/load test: Week 11
- Stakeholder approval หรือ PDPA legal decision ที่ยังไม่มีหลักฐาน
