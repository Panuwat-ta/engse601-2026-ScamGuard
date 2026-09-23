# AI Use Declaration

| รายการ | บันทึก |
|---|---|
| Week / artifact | Week 07 / System-UAT Scenarios v1 |
| ใช้ AI หรือไม่ | Yes |
| เครื่องมือ/รุ่นเท่าที่ทราบ | Codex (GPT-5 family; exact serving model configured by the host) + local shell/PDF verification tools |
| ใช้เพื่อ | อ่าน course scaffold และ canonical SRS; ตรวจ Week 05-06 handoff/source evidence; จัด critical journeys; ออกแบบ System Test/UAT scenarios; สร้าง readiness probe; ตรวจ traceability/status consistency; จัดทำและตรวจ PDF |
| Input ที่ให้ AI | Canonical SRS v1.1 จาก `/home/panuwat/project/Document/srs/`; frozen source/route/schema snapshots และ raw evidence ของ Week 05-06 จาก ENGSE212 `main` commit `66bc9e4a`; `STATUS.md`, Week 07 scaffold และเอกสารภายใน ENGSE601 repository |
| การปกป้องข้อมูล | อ่าน `/home/panuwat/project` แบบ read-only; ไม่อ่านหรือคัดลอก `.env`, credential, token, production database content หรือ user image; ไม่เก็บชื่อ/อีเมล/คำตอบของผู้เข้าร่วม UAT ที่ยังไม่มีจริง |
| ข้อเสนอที่ Accepted | โครง 6 critical journeys; 12 System Test scenarios; 6 UAT scenarios; entry/exit criteria; evidence requirements; privacy protocol; canonical NFR-06 heatmap questions; findings W07-F01 ถึง W07-F07 |
| ข้อเสนอที่ Modified | แยกความครบของ test design ออกจากผล execution; กำหนด System Test เป็น `Not Executed` และ UAT เป็น `Not Ready`; ใช้ frozen `main` evidence จาก Week 05-06 แทน local ENGSE212 `develop`; ระบุ official Week 07 template เป็น open dependency; แก้ PDF font embedding หลัง render QA รอบแรกพบ glyph หาย |
| ข้อเสนอที่ Rejected | การสร้าง Pass/Fail, execution log, screenshot, UAT response, satisfaction score หรือ comprehension percentage ที่ยังไม่เกิด; การใช้ source inspection แทน System Test; การอนุมาน peer review/stakeholder approval จาก merge; การใช้ production credential หรือข้อมูลส่วนบุคคล |
| วิธีตรวจสอบกับ artifact/owner จริง | เทียบ requirement/threshold กับ canonical SRS v1.1 SHA-256 `99bb8d5050fa54195b02869f1815e954fdd43ad0997e732b35426c70947cd40a`; ตรวจ source facts กับ `E05/E06` frozen snapshots และ raw result registers; รัน `system_readiness_probe.py`; ตรวจ scenario count 12+6; render PDF ทุกหน้าและบันทึกใน `E07-pdf-check.txt`; independent peer-review decision ยัง pending ใน `05-peer-review.md` |
| ผู้รับผิดชอบการตรวจ | ภานุวัฒน์ |
| วันที่ตรวจ | 2026-09-23 |

คำยืนยัน: ทีมไม่ได้ใช้ AI สร้างผลทดสอบ, log, screenshot, approval, stakeholder decision, UAT response, participant metric หรือหลักฐานที่ไม่ได้ดำเนินการจริง
