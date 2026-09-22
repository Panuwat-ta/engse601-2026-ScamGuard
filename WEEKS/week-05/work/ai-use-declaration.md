# AI Use Declaration

| รายการ | บันทึก |
|---|---|
| Week / artifact | Week 05 / Component Test Case Set v1 |
| ใช้ AI หรือไม่ | Yes |
| เครื่องมือ/รุ่นเท่าที่ทราบ | ChatGPT GPT-5.6 Sol + Remote Desktop Commander |
| ใช้เพื่อ | อ่าน canonical SRS v1.1, ทำ Code & Logic Reading Clinic, สร้างและรัน component probes, สรุปผล Pass/Fail/Not Ready, จัด findings/handoff และเตรียม submission |
| Input ที่ให้ AI | `/home/panuwat/project/Document/srs/` บน branch `main`, W03/W04 historical evidence, ENGSE601 Week 05 guide และ source code จาก ENGSE212 `origin/main` commit `66bc9e4a` |
| การปกป้องข้อมูล | ไม่คัดลอก `.env`, password, token, API key หรือ secret ลง evidence repo; probe ใช้ test-only config และ fake DB ใน memory |
| ข้อเสนอที่ Accepted | ใช้ SRS v1.1 เป็น authority; 18 component test cases; execution evidence 3 ชุด; findings W05-F01 ถึง W05-F08; เก็บ product defects เป็น Fail/Not Ready แทนการแต่งผล Pass |
| ข้อเสนอที่ Modified | W03/W04 ถูกใช้เป็น historical handoff เท่านั้น; weighted-score finding เดิมถูกยกเลิกหลัง rebaseline; auth validation ตรวจผ่าน direct handler probe แทน full-app test เพื่อแยก component จาก unrelated model startup |
| ข้อเสนอที่ Rejected | การตั้ง threshold เอง, การสร้าง model metric ที่ไม่ได้รัน, การถือ missing endpoint เป็น Pass, การปลอม human peer-review sign-off |
| วิธีตรวจสอบ | เทียบทุก expected result กับ canonical SRS v1.1; extract `origin/main` แบบ isolated; รัน `pytest` และ `work/probes/component_probe.py`; เก็บ raw output ใน `work/evidence/` |
| Verification owner/date | ภานุวัฒน์ / 2026-09-22 |

คำยืนยัน: ไม่มีการสร้าง test result, screenshot, approval, stakeholder decision หรือ peer-review approval ที่ไม่ได้เกิดขึ้นจริง

- Canonical SRS: https://github.com/Panuwat-ta/project/tree/main/Document/srs
- Source code: https://github.com/Panuwat-ta/project
- Branch: main
