# AI Use Declaration

| รายการ | บันทึก |
|---|---|
| Week / artifact | Week 01 / Quality Risk Cards (quality-risk-cards.md) |
| ใช้ AI หรือไม่ | Yes |
| เครื่องมือ/รุ่นเท่าที่ทราบ | Antigravity IDE (Claude Opus 4.6) |
| ใช้เพื่อ | ช่วยร่างเนื้อหา Quality Risk Cards โดยอ้างอิงจาก SRS v1.0 จริง: วิเคราะห์ว่า requirement ใดมีความเสี่ยงสูง, ร่าง risk statement, V&V action, และ planned evidence |
| Input ที่ให้ AI | สรุปเนื้อหาจาก 05_Software_Requirement_Specification.md v1.0 (FR/NFR/AC), PROJECT.md (Critical Context C-01 ถึง C-09), TEAM.md, และ week-01 README.md (ไม่มีข้อมูลส่วนบุคคลที่เป็นความลับ) |
| การปกป้องข้อมูล | ไม่ได้ส่งรหัสผ่าน, token, หรือข้อมูลส่วนบุคคลอื่นนอกเหนือจากชื่อสมาชิกที่เปิดเผยอยู่แล้วใน repository |
| ข้อเสนอที่ Accepted | 1. การเลือก 5 risk areas (AI Accuracy, Heatmap, Performance, PDPA, OCR) ตาม Critical Context 2. โครงสร้าง risk statement แบบ "เมื่อ...อาจเกิด...ทำให้..." 3. การ trace กลับไป FR/NFR ID จริง 4. การเลือก QR-01 เป็น critical slice ไป Week 02 |
| ข้อเสนอที่ Modified | 1. ปรับ risk statement ให้เจาะจงกับบริบทไทย (สลิป K-Bank, SCB) แทนคำกว้าง 2. เพิ่มรายละเอียด impact ที่เชื่อมกับน้ำหนักในสูตร Risk Score (45%, 25%, 30%) 3. ปรับ evidence status ทั้งหมดเป็น Not Ready ตามความจริง (ยังไม่มี implementation) |
| ข้อเสนอที่ Rejected | ไม่มี |
| วิธีตรวจสอบกับ artifact/owner จริง | 1. ตรวจ FR/NFR ID ทุกตัวว่าตรงกับ 05_Software_Requirement_Specification.md v1.0 2. ตรวจตัวเลข threshold (85%, 80%, 15s, 25s, 100 users) ว่าตรงกับ SRS 3. ตรวจ Critical Context C-01 ถึง C-09 ว่าตรงกับ PROJECT.md |
| ผู้รับผิดชอบการตรวจ | Panuwat Takham |
| วันที่ตรวจ | 2026-08-24 |

คำยืนยัน: ทีมไม่ได้ใช้ AI สร้างผลทดสอบ, log, screenshot, approval, stakeholder decision หรือหลักฐานที่ไม่ได้ดำเนินการจริง
