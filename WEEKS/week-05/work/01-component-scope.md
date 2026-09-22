# W05-01 — Component Test Scope and Test Basis

## Scope

Week 05 เริ่มจาก critical slice ที่ Week 04 ส่งต่อมา แต่ re-check test basis กับ SRS canonical ปัจจุบันก่อน ไม่ขยายไปทดสอบทั้งระบบในรอบเดียว

| Scope ID | Requirement / rule | Component under test | Reason |
|---|---|---|---|
| C01 | FR-ANALYSIS-02 | `server/app/services/onnx_worker.py` | เป็นจุดสร้าง visual model output, heatmap และ `visual_risk_score` |
| C02 | FR-ANALYSIS-04 | `server/app/utils/risk_calculator.py` | เป็น logic Hybrid max+bonus, grade boundaries และ Visual Override |
| C03 | FR-AUTH-01 + FR-PDPA-01 | `server/app/schemas/auth.py`, `server/app/api/v1/auth.py`, `server/app/models/consent.py` | registration, consent validation และ consent persistence มี code จริงบน main |

## Requirement baseline frozen for this draft

- Local canonical source: `/home/panuwat/project/Document/srs/`
- Canonical URL: https://github.com/Panuwat-ta/project/tree/main/Document/srs
- Branch: `main`
- SRS: `05_Software_Requirement_Specification.md` v1.1, dated 2026-09-12
- Requirement Candidates/Traceability ที่ใช้ประกอบต้องมาจากโฟลเดอร์ canonical เดียวกัน
- Week 03/04 เป็นหลักฐานย้อนหลังจาก SRS v1.0; หาก wording หรือ algorithm ขัดกับ SRS v1.1 จะไม่ใช้ wording เก่าเป็น acceptance basis

## Source-code baseline

ตรวจ code จาก repository ENGSE212 ที่ประกาศเป็น IN-04 โดยอ้าง `origin/main` ไม่ใช้ behavior จาก working branch อื่นเป็น acceptance basis

- URL: https://github.com/Panuwat-ta/project
- Branch: main
- Commit inspected: `66bc9e4a`
- Date referenced: 2026-09-22

## Code-reading result before test design

1. SRS v1.1 กำหนด SegFormer forgery confidence ด้วย `Normalize(Confidence×Coverage)` และกำหนด AI-Gen Detection เป็นสัญญาณแยก แต่ `onnx_worker.py` บน main ใช้ `max(prob_map)` เป็น `visual_risk_score` และใส่ค่าเดียวกันเป็น `ai_gen_probability`; ยังไม่เห็น separate AI-Gen detector/output contract ตาม FR-ANALYSIS-02 AC-2
2. `risk_calculator.py` บน main ใช้ Hybrid max+bonus และช่วง Low/Medium/High ซึ่งสอดคล้องกับ FR-ANALYSIS-04 v1.1; mismatch ที่เคยพบจาก SRS v1.0 ไม่ใช่ defect ของ baseline ปัจจุบัน
3. FR-AUTH-01 AC-5 ต้อง reject `system_consent=false` ด้วย HTTP 400 แต่ `RegisterRequest` ยอมรับ false และ route `/auth/register` ไม่มี guard ที่ reject ก่อนสร้าง user
4. FR-PDPA-01 AC-2/3/5 อธิบาย consent แบบ event/log (`consent_type`, `is_granted`, `created_at`, `updated_at`) แต่ model บน main เป็นหนึ่ง row ที่มี `system_consent` และ `research_consent` และยังไม่พบ GET/PUT consent-management endpoint
5. FR-PDPA-01 AC-4 ระบุ `GET /users/me` แต่ main expose profile read ที่ `/api/v1/auth/me`; `/api/v1/users/me` บน main เป็น DELETE account จึงต้อง reconcile route contract

## Test approach

- Unit/logic tests: deterministic pure logic เช่น Hybrid max+bonus, grade boundaries และ input clamping
- Component/API tests: FastAPI route + mocked/isolated DB สำหรับ registration/consent behavior
- Component adapter tests: ONNX worker contract โดยไม่อ้างว่า model accuracy ผ่าน จนกว่าจะมี model/dataset evidence จริง
- Requirement ที่ไม่มี behavior ระบุใน SRS v1.1 จะไม่สร้าง expected result ขึ้นเอง; ให้บันทึกเป็น gap/open issue แทน

## Out of scope for Week 05 draft

- Dataset-level Accuracy/Precision/Recall/F1/mDice: ส่งต่อ model/system evaluation
- System/UAT journey: Week 07
- Performance percentile/load test: Week 11
- Retroactive research-dataset handling หลังถอน consent เพราะ SRS v1.1 ยังไม่กำหนด behavior นี้
- Stakeholder approval หรือ legal decision ที่ยังไม่มีหลักฐาน
