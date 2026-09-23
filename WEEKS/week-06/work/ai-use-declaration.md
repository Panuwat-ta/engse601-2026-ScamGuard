# AI Use Declaration

| รายการ | บันทึก |
|---|---|
| Week / artifact | Week 06 / Integration Test Design v1 |
| ใช้ AI หรือไม่ | Yes |
| เครื่องมือ/รุ่นเท่าที่ทราบ | ChatGPT GPT-5.6 Sol + Remote Desktop Commander |
| ใช้เพื่อ | อ่าน course Week 06, canonical SRS, Week 05 handoff และ source code; ทำ Interface/API Risk Mapping; สร้าง integration probe; execute tests; สรุป evidence/findings; จัดทำ PDF |
| Requirement input | `/home/panuwat/project/Document/srs/` SRS v1.1 และ URL https://github.com/Panuwat-ta/project/tree/main/Document/srs |
| Code input | ENGSE212 https://github.com/Panuwat-ta/project branch `main`, commit `66bc9e4a` |
| Project testing input | https://github.com/Panuwat-ta/project/tree/develop/tests_all, branch `develop`, commit `162e0249abb9e9940f014ba6d5182d38213bc771` |
| การปกป้องข้อมูล | ไม่อ่าน/คัดลอก `.env`, token, API key, password หรือ production data ลง evidence; ใช้ dummy environment และ test doubles |
| Accepted | แบ่ง 6 interface groups; 18 cases; ใช้ ASGI/fake DB/fake Redis/inference stub เฉพาะ seam จริง; เก็บ 11 Fail และ 1 Not Ready ตาม evidence |
| Modified | เพิ่ม strict contract assertions ของ history/report หลัง re-check canonical SRS; แยก Google Vision positive case เป็น Not Ready แทน mock แล้วนับ Pass |
| Rejected | การสร้าง production Google Vision contract ขึ้นเอง, การใช้ production credentials, การเปลี่ยน product Fail เป็น Pass, การสร้าง reviewer sign-off ปลอม |
| Verification | เทียบ expected กับ SRS v1.1; ดึง source/route/schema facts จาก `/home/panuwat/project` โดย freeze `origin/main` commit `66bc9e4a` พร้อม path/line/hash; execute probe บน isolated `origin/main`; cross-check project integration suites/reports from pinned `develop/tests_all` without treating historical reports as a re-run; เก็บ raw pytest output และ per-case register; ตรวจ PDF render ก่อนส่ง |
| Verification owner/date | ภานุวัฒน์ / 2026-09-23 |

คำยืนยัน: ไม่มีการสร้าง test result, log, screenshot, stakeholder decision, approval หรือ peer-review sign-off ที่ไม่ได้เกิดขึ้นจริง
