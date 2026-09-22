# AI Use Declaration

| รายการ | บันทึก |
|---|---|
| Week / artifact | Week 05 / Component Test Case Set draft |
| ใช้ AI หรือไม่ | Yes |
| เครื่องมือ/รุ่นเท่าที่ทราบ | ChatGPT GPT-5.6 Sol + Remote Desktop Commander สำหรับอ่าน/แก้ไฟล์และรันคำสั่งที่ผู้ใช้อนุญาต |
| ใช้เพื่อ | อ่าน SRS/W03/W04, ทำ Code & Logic Reading Clinic, สร้าง traceable component test cases, แยก Existing/Planned/Not Ready และบันทึก requirement-code mismatch |
| Input ที่ให้ AI | `INPUTS/requirements-srs/05_Software_Requirement_Specification.md` v1.0, W03 critical review, W04 RTM/Gate A/Phase 2 Entry Pack, ENGSE601 Week 05 course guide และ source code ที่ตรวจจาก ENGSE212 main |
| การปกป้องข้อมูล | ไม่คัดลอก `.env`, password, token, API key หรือ secret ลง evidence repo; การรัน isolated archive ที่ไม่มี `.env` ถูกบันทึกเป็น Not Executed เมื่อ configuration ไม่ครบ |
| ข้อเสนอที่ Accepted | 1) scope REQ-01 + REQ-05 และ FR-ANALYSIS-04 supporting rule 2) test-case IDs W05-CT-01 ถึง W05-CT-17 3) findings W05-F01 ถึง W05-F07 4) ใช้ `origin/main` commit `66bc9e4a` เป็น code baseline ตาม IN-04 |
| ข้อเสนอที่ Modified | 1) boundary cases ปรับให้สะท้อน signature ของ `calculate_risk_score()` จริง 2) ผล test จาก branch `refactoring-admin` ลดสถานะเป็น supplementary เพราะไม่ใช่ baseline 3) auth test บน isolated main ระบุ Not Executed ไม่ใช่ Fail เพราะขาด runtime configuration |
| ข้อเสนอที่ Rejected | 1) การตั้ง Q-01 threshold เอง 2) การตัดสิน Q-06 แทน owner/advisor 3) การถือว่า test เดิมผ่านแล้วเท่ากับ SRS ผ่าน 4) การแก้ source code ก่อนมี decision ต่อ algorithm mismatch |
| วิธีตรวจสอบกับ artifact จริง | เทียบทุก case กับ SRS v1.0 และ W03/W04; ใช้ `git show`/`git grep` ที่ `origin/main`; รัน test/verification commands จริงและบันทึกเฉพาะ output ที่เกิดขึ้นจริง |
| Verification owner/date | ภานุวัฒน์ / 2026-09-22 |

คำยืนยัน: ไม่มีการสร้าง test result, screenshot, defect, approval หรือ stakeholder decision ที่ไม่ได้เกิดขึ้นจริง และ open questions ยังคงเป็น open ตามหลักฐานปัจจุบัน

Source-code reference used for verification:

- **URL**: https://github.com/Panuwat-ta/project
- **Branch**: main
- **Date**: 2026-09-22
