# DEF-01 API รับสมัครสมาชิกเมื่อ system_consent = false หรือไม่ส่งฟิลด์

| ช่อง | ข้อมูล |
|---|---|
| พบจาก TC | TC-06, TC-07 |
| ความต้องการที่เกี่ยวข้อง | REQ-03 FR-AUTH-01 AC-5 |
| รุ่นและสภาพแวดล้อม | `Panuwat-ta/project` @ `c3bc7223` (branch `Refactor-mobile`) Python 3.10 FastAPI + httpx ASGITransport (in-memory session) SRS v1.1 |
| ผู้รายงาน วันที่ | นาย ภานุวัฒน์ ต๋าคำ 2026-10-22 |
| ความรุนแรง | วิกฤต (Critical) เพราะระบบสร้างผู้ใช้และ consent log ที่ไม่มี System Consent ทำให้ประมวลผลข้อมูลโดยไม่มีฐานความยินยอมและเสี่ยงไม่เป็นไปตาม PDPA |
| ความเร่งด่วน | P1 เพราะต้องปิดก่อนส่งมอบและก่อนทำ UAT |
| สถานะ | Open — ยังไม่แก้ |

## ขั้นตอนทำซ้ำ

1. ส่ง `POST /api/v1/auth/register` ด้วยอีเมลใหม่ รหัสผ่าน 8 ตัวอักษร และ `system_consent: false`
2. ทำซ้ำด้วยอีเมลใหม่อีกครั้งโดยไม่ส่งฟิลด์ `system_consent` เลย
3. ตรวจ HTTP status และตรวจว่ามีแถว `users` / `consent_logs` เพิ่มหรือไม่

## ผลที่คาดหวัง (อ้างกฎ)

HTTP 400 พร้อมข้อความ `System consent is required` ทั้งกรณี `false` และกรณีไม่ส่งฟิลด์ และต้องไม่มีผู้ใช้หรือ consent log เพิ่มขึ้น (REQ-03 FR-AUTH-01 AC-5 ตีความว่าไม่มี consent = ไม่ยอมรับ ตาม S1-B Exit 1)

## ผลจริง

HTTP 201 ทั้งสองกรณี พร้อม `UserResponse` และ route เรียก `db.add(User)` + `db.add(ConsentLog)` ก่อน commit กรณี `false` บันทึก `system_consent = false` กรณีไม่ส่งฟิลด์ schema ใช้ค่า default `True` จึงบันทึกเป็น `system_consent = true` โดยไม่มีคำตอบจากผู้ใช้

## หลักฐาน

`../../03-test-execution/evidence/s3-api-reference-run.txt` บรรทัด TC-06 และ TC-07

## ผลกระทบ

ผู้ใช้ที่ไม่ได้ให้ความยินยอมหรือไม่ได้ตอบคำถามถูกสร้างในระบบได้ อีกทั้งขัดเงื่อนไข exit ของทีมที่กำหนดให้เคสเชิงลบของ System Consent ต้องผ่าน 0/3

## สาเหตุที่น่าจะเป็น

`RegisterRequest.system_consent` ใน `server/app/schemas/auth.py` มีค่า default `True` และ `register()` ใน `server/app/api/v1/auth.py` ไม่ตรวจ `body.system_consent` ก่อนสร้าง User และ ConsentLog ชุดทดสอบเดิม `server/tests/api/test_auth.py` ไม่มีเคส `false`/ไม่ส่งฟิลด์ จึงไม่จับข้อบกพร่องนี้

## แนวทางแก้

ลบค่า default ของ `system_consent` ให้เป็นฟิลด์บังคับ และเพิ่ม validation ที่ชั้น API/schema ให้ปฏิเสธทั้ง `false` และกรณีไม่ส่งฟิลด์ พร้อมข้อความและ status ตาม AC-5 ก่อนเขียนฐานข้อมูล แล้วเพิ่ม API test สำหรับ `false`, ไม่ส่งฟิลด์ และ payload ที่ไม่ผ่าน client

## ประวัติ

| วันที่ | เหตุการณ์ | หลักฐาน |
|---|---|---|
| 2026-10-22 | เปิดรายงานจากผลรัน TC-06 | `../../03-test-execution/evidence/s3-api-reference-run.txt` |
| 2026-10-23 | รันชุด v2 ซ้ำ พบ TC-07 (ไม่ส่งฟิลด์) เป็นอีกเส้นทางของข้อบกพร่องเดียวกัน | `../../03-test-execution/evidence/s3-api-reference-run.txt` |
