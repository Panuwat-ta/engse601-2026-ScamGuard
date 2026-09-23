# W05-04 - Findings, Disposition and Handoff

## 1. Purpose

รวบรวม gap/defect ที่พบจาก Component Test Case Set และกำหนดสถานะกับ next action โดยไม่ใช้คำว่า "accepted defect" เว้นแต่มี stakeholder decision จริง เอกสารนี้จึงแยกสิ่งที่ตรวจพบออกจากการตัดสินใจแก้ไขใน ENGSE212 อย่างชัดเจน

## 2. Findings register

| ID | Type | Finding | Evidence / trace | Status | Owner | Next action |
|---|---|---|---|---|---|---|
| W05-F01 | Implementation gap | Visual Analysis ไม่มี separate `forgery_confidence` / `ai_gen_confidence`; SegFormer max probability ถูกใช้กับทั้ง AI-Gen/visual output | FR-ANALYSIS-02 AC-1/2/3; CT-01/02/03; E05 visual probe | Open | ภานุวัฒน์ | ปรับ visual/AI-Gen output contract ใน ENGSE212 แล้ว re-test component ก่อน System/UAT |
| W05-F02 | Requirement ambiguity | FR-ANALYSIS-04 AC-7 ยกตัวอย่าง `risk_score=65, visual_score=85` แต่ Hybrid max+bonus ไม่สามารถสร้าง total < visual ได้ | FR-ANALYSIS-04 AC-7; CT-10 | Needs Clarification | ภานุวัฒน์ | เปิด controlled SRS clarification; ไม่แก้ algorithm โดยเดา intent |
| W05-F03 | API contract defect | Registration response ขาด `status` และ `created_at` ตาม AC-1 | FR-AUTH-01 AC-1; CT-11; E05 auth probe | Open | ภานุวัฒน์ | ปรับ response schema/handler แล้วเพิ่ม contract test |
| W05-F04 | Functional defect | `system_consent=false` ยังสร้าง User + ConsentLog แทน HTTP 400 | FR-AUTH-01 AC-5; CT-12; E05 auth probe | Open | ภานุวัฒน์ | เพิ่ม validation ก่อน persistence และ re-test negative case |
| W05-F05 | Data contract gap | Consent model เป็น one-row/two-booleans และไม่มี `updated_at` ตาม event/log contract | FR-PDPA-01 AC-2/3/5; CT-14/18 | Open | ภานุวัฒน์ | Reconcile schema/migration ก่อน integration testing |
| W05-F06 | Missing API | ไม่มี `PUT /consent/research` และ `GET /consent/logs` | FR-PDPA-01 AC-3/5; CT-15/17 | Open | ภานุวัฒน์ | Implement endpoints และ component/API tests |
| W05-F07 | Route contract mismatch | SRS ระบุ `GET /users/me`; code มี `GET /api/v1/auth/me` และ `/api/v1/users/me` เป็น DELETE | FR-PDPA-01 AC-4; CT-16 | Open | ภานุวัฒน์ | เลือก canonical route ผ่าน controlled change แล้ว sync SRS/code/test |
| W05-F08 | Baseline transition | W03/W04 ใช้ SRS v1.0 ขณะที่ W05 ใช้ canonical v1.1 | IN-02; input register | Closed for W05 | ภานุวัฒน์ | เก็บ W03/W04 เป็น historical evidence และใช้ v1.1 เป็น authority ต่อไป |
| W05-F09 | Re-test evidence gap | `develop/tests_all` มีผล unit/regression ภายหลัง แต่ report ที่เกี่ยวข้องไม่ได้บันทึก commit/build/env ให้ผูกกับผล Week 05 ได้ | IN-06; E05-tests-all-basis | Open verification gap | ภานุวัฒน์ | รัน CT IDs เดิมบน pinned `develop` commit/build แล้วเก็บ raw output ก่อนเปลี่ยนสถานะ finding |

## 3. Week 05 disposition

Week 05 เป็น V&V artifact ไม่ใช่ milestone ที่บังคับให้ product defect ทุกตัวต้องถูกแก้ก่อนส่ง สิ่งที่ต้องมีคือ test basis ที่ตรวจสอบได้, test case ที่ trace ได้, actual evidence ที่ซื่อสัตย์ และ handoff ที่ชัดเจน

ดังนั้น W05-F01 และ W05-F03 ถึง W05-F07 ยังคง `Open`; W05-F02 เป็น `Needs Clarification`; W05-F08 ปิดเฉพาะประเด็นการเลือก baseline ของ Week 05 แล้ว และ W05-F09 คงเปิดจนมี re-test ที่ pin commit/build/env การส่งเอกสารหรือการพบรายงานภายหลังไม่ได้เปลี่ยน product finding เป็น Closed โดยอัตโนมัติ

## 4. Downstream handoff

| Target | Findings / concern | Handoff intent |
|---|---|---|
| Week 06 Integration Testing | F01, F05, F06, F07 | ตรวจ contract ระหว่าง service/API/client หลัง implementation ถูก reconcile |
| Week 07 System/UAT | F01, F03, F04, F06, F07 | ยืนยัน user journey หลัง component defects ถูกแก้และ re-tested |
| Week 11 NFR Testing | FR-ANALYSIS-02 AC-5 และ model metrics | ทดสอบ performance/model quality ด้วย environment และ dataset ที่เหมาะสม |
| Week 14 Defect Management | F01-F07 ที่ยังค้าง | Promote เป็น formal defect records พร้อม lifecycle/evidence |
| Requirement change process | F02 | Clarify AC-7 โดยไม่เดา requirement intent |

## 5. Submission and review gate

Author-side Definition of Done สำหรับ Component Test Case Set ครบในด้าน baseline, traceability, evidence, finding disposition และ AI disclosure แล้ว

Repository event ของ v1 เกิดขึ้นจริง: PR #5 merged ที่ `ca354a8` และ tag `w05-submission-v1` ถูกสร้างแล้ว อย่างไรก็ตาม GitHub ไม่มี recorded independent PR review และ `05-peer-review.md` ยังไม่มี reviewer decision/sign-off ดังนั้นเอกสารต้องระบุข้อเท็จจริงสองส่วนพร้อมกัน: v1 ถูกส่งแล้ว แต่ยังไม่มีหลักฐานยืนยันว่า independent peer-review gate ผ่าน

เอกสาร v2 เป็น documentation-quality revision และไม่เขียนทับ submission/tag เดิม จนกว่าจะมี review/merge event ใหม่ที่ตรวจสอบได้
