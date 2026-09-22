# W05-02 - Component Test Case Set

## 1. Test basis

- Canonical SRS: https://github.com/Panuwat-ta/project/tree/main/Document/srs
- SRS: `05_Software_Requirement_Specification.md` v1.1, 2026-09-12
- Code: https://github.com/Panuwat-ta/project
- Branch / commit: `main` / `66bc9e4a`
- Execution and inspection date: 2026-09-22
- Raw evidence: `work/evidence/`

## 2. Result vocabulary

| Result | Definition |
|---|---|
| Pass | Evidence จาก execution หรือ contract inspection ตรง expected result ของ SRS baseline |
| Fail | Evidence ยืนยันว่า implementation ปัจจุบันไม่ตรง expected result |
| Not Ready | Expected result ชัด แต่ component/contract ที่จำเป็นยังไม่มีพอให้ทดสอบ acceptance อย่างถูกต้อง |
| Needs Clarification | Requirement มีตัวอย่าง/เงื่อนไขภายใน baseline ที่ไม่สอดคล้องกัน จึงไม่เดา expected behavior |

แต่ละ case ระบุวิธี verification และ evidence source เพื่อแยกสิ่งที่รันจริงออกจาก static contract inspection อย่างชัดเจน

## 3. Visual Analysis - FR-ANALYSIS-02

| ID | AC | Verification | Expected result | Actual / evidence | Result |
|---|---|---|---|---|---|
| W05-CT-01 | AC-1 | Contract inspection | มี `forgery_confidence` 0-100 ที่ trace กลับไปยัง forgery signal และคำนวณจาก canonical forgery contract | `E05-component-probe.txt`: ไม่พบ key `forgery_confidence`; worker expose `visual_risk_score` จาก SegFormer max probability | Fail |
| W05-CT-02 | AC-2 | Contract inspection | มี `ai_gen_confidence` จาก AI-Gen detector แยกจาก forgery signal | Probe ยืนยัน `ai_gen_prob = max(prob_map_true)` จาก SegFormer เดียวกัน และไม่พบ `ai_gen_confidence` | Fail |
| W05-CT-03 | AC-3 | Readiness check | Visual-score behavior ต้องทดสอบจาก signal/contract ที่ SRS กำหนดได้อย่างอิสระ | Separate forgery/AI-Gen contracts ยังไม่พร้อม จึงไม่สร้าง expected calculation ขึ้นเอง | Not Ready |

หมายเหตุ: FR-ANALYSIS-02 AC-5 เรื่อง GPU inference <= 10 seconds เป็น performance concern จึงส่งต่อ NFR testing แทนการอ้างผลใน Component Test Set

## 4. Risk Calculation - FR-ANALYSIS-04

| ID | AC | Verification / input | Expected result | Actual / evidence | Result |
|---|---|---|---|---|---|
| W05-CT-04 | AC-1 | Example-based probe: `(50,85,0)` | score=90, grade=High, primary=visual | `90 high visual True` | Pass |
| W05-CT-05 | AC-2 | Example-based probe: `(100,100,100)` | score capped at 100, High | `100 high visual True` | Pass |
| W05-CT-06 | AC-3 | Probe: `(10,0,0)` | score=10, Low | `10 low textual False` | Pass |
| W05-CT-07 | AC-4 | Probe: `(30,0,0)` | score=30, Low | `30 low textual False` | Pass |
| W05-CT-08 | AC-5 | Probe: `(55,0,0)` | score=55, Medium | `55 medium textual False` | Pass |
| W05-CT-09 | AC-6 | Probe: `(80,0,0)` | score=80, High | `80 high textual False` | Pass |
| W05-CT-10 | AC-7 | Requirement consistency analysis: stated total=65, visual=85 | High by Visual Override | Hybrid max+bonus ใช้ visual เป็น candidate ของ `max()`, ดังนั้น visual=85 ทำให้ total ต่ำกว่า 85 ไม่ได้; state 65/85 ไม่สามารถเกิดจาก calculator เดียวกัน | Needs Clarification |

Boundary evidence เพิ่มเติมจาก probe: `(0,39,0)->39 Low`, `(0,40,0)->40 Medium`, `(0,69,0)->69 Medium`, `(70,0,0)->70 High` ซึ่งยืนยันจุดเปลี่ยน risk bands โดยไม่เพิ่มจำนวน test cases ใน summary

## 5. Registration - FR-AUTH-01

| ID | AC | Verification | Expected result | Actual / evidence | Result |
|---|---|---|---|---|---|
| W05-CT-11 | AC-1 | Handler probe + response-schema inspection | Registration สำเร็จและ response มี `id, full_name, email, role, status, created_at`; ไม่มี password/hash | response keys จริงคือ `email, full_name, id, message, role`; ขาด `status`, `created_at` | Fail |
| W05-CT-12 | AC-5 | Negative handler probe: `system_consent=false` | HTTP 400 `System consent is required`; ไม่สร้าง user/consent | handler คืน `UserResponse` และ fake DB พบ `User` + `ConsentLog(False, False)` | Fail |
| W05-CT-13 | AC-1 subcondition | Handler probe: system=true, research=false | Research Consent เป็น optional และต้องไม่ block registration | handler สำเร็จและ persist `research_consent=false` | Pass |

## 6. Consent Management - FR-PDPA-01

| ID | AC | Verification | Expected result | Actual / evidence | Result |
|---|---|---|---|---|---|
| W05-CT-14 | AC-2 | Model contract inspection | Consent audit modelรองรับ `consent_type`, `is_granted`, timestamp และแยก System/Research เป็น 2 records | current model เก็บหนึ่ง row ด้วย `system_consent` + `research_consent`; ไม่พบ event fields ตาม SRS | Fail |
| W05-CT-15 | AC-3 | Route inventory | `PUT /consent/research` คืน HTTP 200 และบันทึก updated research consent | route inventory ไม่พบ `/consent/research` | Fail |
| W05-CT-16 | AC-4 | Route contract inspection | `GET /users/me` คืน current-user profile ตาม SRS | profile GET อยู่ที่ `/api/v1/auth/me`; `/api/v1/users/me` เป็น DELETE | Fail |
| W05-CT-17 | AC-5 | Route inventory | `GET /consent/logs` คืน consent history | route inventory ไม่พบ `/consent/logs` | Fail |
| W05-CT-18 | AC-3/5 | Model contract inspection | Consent history/update รองรับ `updated_at` | current `ConsentLog` มี `created_at` เท่านั้น | Fail |

## 7. Execution summary

| Result | Count | Interpretation |
|---|---:|---|
| Pass | 7 | behavior ที่ตรวจแล้วสอดคล้อง baseline |
| Fail | 9 | implementation ปัจจุบันไม่ตรง expected result |
| Not Ready | 1 | component contract ยังไม่พร้อมสำหรับ acceptance test |
| Needs Clarification | 1 | requirement ต้อง clarify ก่อนสร้าง test ที่ไม่ขัดกัน |
| Total | 18 | selected component test cases |

ผล `Fail` เป็นหลักฐาน V&V ที่ถูกต้องและไม่ถูกแปลงเป็น `Pass` เพื่อให้รายงานดูดีขึ้น ส่วน case ที่ยังไม่สามารถ execute อย่างถูกต้องจะใช้ `Not Ready` หรือ `Needs Clarification` ตามหลักฐาน

## 8. Evidence mapping

- Baseline/version: `work/evidence/E05-baseline.txt`
- Existing automated unit test: `work/evidence/E05-pytest-component.txt`
- Deterministic component probe and contract inventory: `work/evidence/E05-component-probe.txt`
- Reproducible probe source: `work/probes/component_probe.py`
- Finding disposition and downstream handoff: `work/04-open-issues-and-decisions.md`
