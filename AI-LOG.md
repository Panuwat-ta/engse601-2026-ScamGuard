# บันทึกการใช้ AI

ใช้ AI ได้เพื่อช่วยคิด ตรวจภาษา หรืออธิบายเครื่องมือ แต่ **ห้ามให้ AI สร้างผลการรัน หลักฐาน หรือข้อบกพร่อง** และทุกข้อเสนอของ AI ต้องตรวจกับงานจริงของทีมก่อนใช้

> สถานะ: ฉบับร่างสำหรับ S3 — สมาชิกทีมต้องตรวจสอบและยืนยันรายการก่อนส่ง

| วันที่ | ผู้ใช้ | เครื่องมือ | ใช้ทำอะไร | ตรวจหรือแก้อะไรก่อนใช้ | ส่วนที่ได้รับผล |
|---|---|---|---|---|---|
| 2026-10-22 | ภานุวัฒน์ | AI coding assistant | ร่างโครงชุดทดสอบ API สำหรับ TC-01..TC-10 | ตรวจกับ SRS v1.1 และ `auth.py`/`schemas/auth.py`; รันเองด้วย `server/venv/bin/python`; แก้ path, วิธีนับแถว และแก้ artifact `register=201` ที่ hardcode | B1 ขั้นที่ 2 |
| 2026-10-22 | ภานุวัฒน์ | AI coding assistant | ร่างแม่แบบรายงานข้อบกพร่อง DEF-01..DEF-03 | เทียบผลกับ `03-test-execution/evidence/s3-api-reference-run.txt` และโค้ดจริง; ระบุข้อจำกัดของ in-memory session | B2 ขั้นที่ 1–3 |
| 2026-10-22 | ภานุวัฒน์ | AI coding assistant | ช่วยจัดหัวข้อและตรวจความครบของคำตอบ S3-B | ตรวจตัวเลขผลรัน เลข TC และเงื่อนไข exit กับ S1-B/S2 B เอง; กรณีที่ยังไม่มีผลรันบันทึก Not Executed ตามจริง | B1–B3 |
| 2026-10-23 | ภานุวัฒน์ | AI coding assistant | ปรับ probe ตาม TC-05/TC-07 ของ S2 v2, rerun, อัปเดต S3-B/DEF และจัดโครงโฟลเดอร์ 03/04 | ตรวจผลจริงใน `03-test-execution/evidence/s3-api-reference-run.txt`; เทียบ TC mapping กับ S2 v2; เก็บผล v1 แยก; ไม่แก้ผู้ทบทวนตามการตัดสินใจของทีม | B1–B3 |
| 2026-10-23 | ภานุวัฒน์ | AI coding assistant | สร้างภาพสรุปผลรัน v2 จากข้อความจริงใน evidence (ภายหลังเปลี่ยนเป็นภาพหน้าจอจริง `s3-api.png`) | ตรวจข้อความในภาพกับ `s3-api-reference-run.txt` ทีละบรรทัด; ระบุในภาพและ README ว่าเป็นภาพจัดรูปแบบ ไม่ใช่ภาพหน้าจอ UI; เปลี่ยนตัวคั่นในภาพเป็นช่องว่างตามคำขอ; ไม่ได้รันผลใหม่หรือสร้างภาพ System/UAT | B1 ขั้นที่ 2 |
| 2026-10-23 | ภานุวัฒน์ | AI coding assistant | เปลี่ยนภาพหลักฐาน v2 เป็นภาพหน้าจอจริง `s3-api.png` ที่ผู้ใช้รันเอง | ตรวจภาพกับ `s3-api-reference-run.txt` ว่า 4 Pass / 6 Fail และรายการ Fail ตรงกัน; ภาพแสดง baseline c3bc7223; ไม่ได้แก้ผลรัน | B1 ขั้นที่ 2 |
| 2026-10-23 | ภานุวัฒน์ | AI coding assistant | ตรวจ checklist ก่อนส่ง 4 ข้อ; ปรับหัวคอลัมน์หลักฐานเป็นไฟล์ใน `evidence/`; เติม expected consents และข้อความ error ให้ตรง S2-B v2; อัปเดต `execution-report.md` ครบขั้น 1–5 | เทียบ TC-01..TC-10 กับ `02-test-design/S2-B_ScamGuard_v2.docx`; ตรวจว่า Pass/Fail ทุกแถวอ้าง `evidence/s3-api-reference-run.txt`; ตรวจ terminal output ใน `execution-report.md` ตรงกับ evidence ทุกบรรทัด; ไม่แก้ expected ตามผลจริง; System/UAT ยัง Not Executed พร้อมเหตุผล | B1 ขั้นที่ 1–5 |

