# AI Use Declaration

| รายการ | บันทึก |
|---|---|
| Week / artifact | Week 06 / Integration Test Design |
| ใช้ AI หรือไม่ | Yes |
| เครื่องมือ/รุ่นเท่าที่ทราบ | ChatGPT GPT-5.6 Sol + Remote Desktop Commander |
| ใช้เพื่อ | อ่าน course Week 06, canonical SRS, Week 05 handoff และ source code; ทำ Interface Risk Mapping; ร่าง integration test cases และ entry criteria |
| Requirement input | `/home/panuwat/project/Document/srs/` SRS v1.1 โดยอ้าง https://github.com/Panuwat-ta/project/tree/main/Document/srs |
| Code input | ENGSE212 `https://github.com/Panuwat-ta/project`, branch `main`, commit `66bc9e4a` |
| การปกป้องข้อมูล | ไม่อ่าน/คัดลอก `.env`, token, API key, password หรือ production data ลง evidence repo |
| Verification | expected behavior ตรวจกลับกับ SRS v1.1; interface/path/schema ตรวจจาก `origin/main`; Week 05 ใช้เป็น handoff evidence ไม่ใช่ requirement authority |
| ผล execution | Session เริ่มต้นนี้เป็น test design; ยังไม่สร้าง Pass/Fail สำหรับ W06 cases ที่ไม่ได้ execute |
| Verification owner/date | ภานุวัฒน์ / 2026-09-22 |

## AI suggestions accepted

- แยก interface เป็น Mobile/API, Redis, Inference, Source Verification, Heatmap และ History/Report
- ใช้ fake/stub เฉพาะที่มี production contract ชัด เพื่อ isolate integration boundary
- carry Week 05 visual contract gap เป็น dependency แทนการสมมติว่าแก้แล้ว
- ระบุ Source Verification และ history filter contract เป็น `Not Ready` ตาม code/SRS ที่ตรวจพบจริง
