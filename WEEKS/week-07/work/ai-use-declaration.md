# AI Use Declaration

| รายการ | บันทึก |
|---|---|
| Week / artifact | Week 07 / System-UAT Scenarios v1 |
| ใช้ AI หรือไม่ | Yes |
| เครื่องมือ/รุ่นเท่าที่ทราบ | Codex (GPT-5 family; exact serving model configured by the host) + local shell/PDF verification tools |
| ใช้เพื่อ | อ่าน course scaffold, canonical SRS, Master Test Plan และ `develop/tests_all`; ตรวจ Week 05-06 handoff; map 10 project E2E journeys; ออกแบบ UAT scenarios; สร้าง readiness probe; ตรวจ traceability/status consistency; จัดทำและตรวจ PDF |
| Input ที่ให้ AI | Canonical SRS v1.1 จาก `/home/panuwat/project/Document/srs/`; project test assets จาก `/home/panuwat/project/Document/tests_doc/` และ `/home/panuwat/project/tests_all/` ที่ `develop` commit `162e0249abb9e9940f014ba6d5182d38213bc771`; frozen Week 05-06 evidence จาก `main` commit `66bc9e4a`; `STATUS.md` และ Week 07 scaffold |
| การปกป้องข้อมูล | อ่าน `/home/panuwat/project` แบบ read-only; ไม่อ่านหรือคัดลอก `.env`, credential, token, production database content หรือ user image; ไม่เก็บชื่อ/อีเมล/คำตอบของผู้เข้าร่วม UAT ที่ยังไม่มีจริง |
| ข้อเสนอที่ Accepted | ใช้ 10 project E2E scenarios เป็น System Test baseline; 6 UAT scenarios; authority separation; evidence requirements; privacy protocol; canonical NFR-06 heatmap questions; findings W07-F01 ถึง W07-F09 |
| ข้อเสนอที่ Modified | แยก SRS `main` ออกจาก test assets `develop`; ลด System scenarios จาก 12 ที่ร่างเองเป็น 10 cases จริง; แยก internal-beta UAT ออกจาก 100-participant NFR-06 measurement; เก็บ historical automated reports เป็น supporting evidence เพราะ metadata ไม่ครบ |
| ข้อเสนอที่ Rejected | การนับ historical report เป็น current Week 07 pass; การนับ JUnit `tests=0` ว่าผ่าน; การนับ template row ใน manual log เป็นผล; การสร้าง Pass/Fail, UAT response, approval หรือ sign-off ที่ยังไม่เกิด; การใช้ production credential/ข้อมูลส่วนบุคคล |
| วิธีตรวจสอบกับ artifact/owner จริง | เทียบ requirement/threshold กับ canonical SRS v1.1 SHA-256 `99bb8d5050fa54195b02869f1815e954fdd43ad0997e732b35426c70947cd40a`; pin `develop` ref and hashes of Master Test Plan/E2E/manual-log/JUnit; รัน `system_readiness_probe.py`; ตรวจ scenario count 10+6; render PDF ทุกหน้า; independent review ยัง pending |
| ผู้รับผิดชอบการตรวจ | ภานุวัฒน์ |
| วันที่ตรวจ | 2026-09-23 |

คำยืนยัน: ทีมไม่ได้ใช้ AI สร้างผลทดสอบ, log, screenshot, approval, stakeholder decision, UAT response, participant metric หรือหลักฐานที่ไม่ได้ดำเนินการจริง
