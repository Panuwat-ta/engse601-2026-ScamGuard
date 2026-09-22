# W05-04 — Open Issues, Findings and Decisions Needed

## Findings from Code & Logic Reading Clinic

| ID | Finding | Trace / evidence | Impact | Status | Owner | Next action |
|---|---|---|---|---|---|---|
| W05-F01 | Visual Analysis contract ไม่ตรง SRS: SRS/W03 ต้องมี `forgery_confidence` + `ai_gen_confidence` และสูตร 0.6/0.4 แต่ `onnx_worker.py` main ใช้ max forgery probability เป็นทั้ง `visual_risk_score` และ `ai_gen_probability` | REQ-01, AC-R1-01; `server/app/services/onnx_worker.py` | W05-CT-02 และ threshold tests ยังพิสูจน์ requirement ไม่ได้ | Not Ready | ภานุวัฒน์ | ตัดสิน canonical visual pipeline/contract แล้วปรับ code หรือออก SRS baseline ใหม่พร้อมเหตุผล |
| W05-F02 | Overall Risk algorithm ไม่ตรง SRS: FR-ANALYSIS-04 ใช้ weighted 0.25/0.45/0.30 แต่ main codeใช้ Hybrid Worst-Case + compounding | FR-ANALYSIS-04 AC-1; E05-03 ได้ 97 แทน expected 80 | คะแนน/grade ที่ผู้ใช้เห็นอาจไม่ตรง requirement; Special Rule AC-6 ไม่สามารถแยกพิสูจน์ตาม semantics เดิม | Not Ready | ภานุวัฒน์ | Reconcile SRS/design/code ก่อนเพิ่ม acceptance test ถาวร |
| W05-F03 | `system_consent=False` ผ่าน `RegisterRequest` และ route ไม่มี explicit reject | REQ-05 AC-R5-02; E05-04 | ขัดข้อกำหนด System Consent บังคับ | Not Ready | ภานุวัฒน์ | เพิ่ม validation/route guard หรือแก้ requirement ผ่าน baseline process; จากนั้นเพิ่ม negative API test |
| W05-F04 | Consent storage contract ไม่ตรง SRS: code เก็บ 1 row มีสอง boolean และไม่มี `updated_at`; SRS/W03 อ้าง event/audit semantics | REQ-05 AC-R5-01/03/04 | audit trail grant→revoke ตาม requirement ยังยืนยันไม่ได้ | Not Ready | ภานุวัฒน์ | กำหนด canonical consent schema และ migration/update strategy |
| W05-F05 | ไม่พบ GET/PUT consent-management endpoint บน main | REQ-05 AC-R5-03/04/05; E05-05 | revoke, read logs และ withdrawal rule ยังทดสอบไม่ได้ | Not Ready | ภานุวัฒน์ | Implement endpoint ตาม baseline หลัง schema decision แล้วเพิ่ม API component tests |
| W05-F06 | Q-01 threshold + AI-generator scope ยังไม่ถูกตัดสิน | GA-01 / W04 | block W05-CT-03 และ model decision tests | Open | ภานุวัฒน์ | ปิด Q-01 ด้วย decision record ก่อน model acceptance testing |
| W05-F07 | Q-06 retroactive research-consent handling ยังเปิด | GA-06 / W04 | block W05-CT-17 และ admin dataset flow | Open | ภานุวัฒน์ | ปรึกษาอาจารย์ที่ปรึกษาและบันทึก decision ก่อน implement flow ที่เกี่ยวข้อง |

## Week 05 working decision

Week 05 ดำเนินต่อได้เฉพาะ test ที่มี acceptance basis ชัดและไม่พึ่ง open decision ได้แก่ risk-grade boundaries และ registration happy path ส่วน visual-score formula, Q-01 threshold, consent revoke/audit และ Q-06 ต้องคงสถานะ `Not Ready` จนกว่าจะมี decision/implementation ที่ตรวจสอบได้

ยังไม่แก้ SRS v1.0 และยังไม่แก้ source code ENGSE212 ใน session นี้ เพราะ findings W05-F01 ถึง W05-F07 ต้องผ่าน owner/review process ก่อน

## Re-check criteria

- W05-F01 ปิดได้เมื่อมี code contract ที่แยก signal ตาม baseline หรือมี approved SRS revision ที่อธิบาย algorithm ใหม่
- W05-F02 ปิดได้เมื่อ FR-ANALYSIS-04 กับ code ใช้ algorithm เดียวกัน และ W05-CT-04 ผ่านบน main
- W05-F03 ปิดได้เมื่อ negative test `system_consent=false` ได้ HTTP 400 และไม่มี user/consent row ถูกสร้าง
- W05-F04/F05 ปิดได้เมื่อ consent schema/API รองรับ revoke + audit trail ตาม baseline และ component tests ผ่าน
- W05-F06/F07 ปิดได้เมื่อมี decision record จริงจาก owner/advisor ตามที่ Gate A กำหนด

## Source-code reference

- URL: https://github.com/Panuwat-ta/project
- Branch: main
- Commit: `66bc9e4a`
- Date: 2026-09-22
