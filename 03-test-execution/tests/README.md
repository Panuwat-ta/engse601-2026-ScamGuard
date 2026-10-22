# โค้ดทดสอบ

วางไฟล์ทดสอบอัตโนมัติที่ใช้ใน B1 ขั้นที่ 2 เช่น `booking.test.js` หรือ `test_booking.py`

- ไฟล์ปัจจุบัน: `test_s3_reference_suite.py` (probe 10 TC รันด้วย `server/venv/bin/python` ผ่าน httpx ASGITransport)
- ใช้รหัส TC เดิมในชื่อ test เช่น `test('TC-02 ยืม 4 ชิ้นต้องถูกปฏิเสธ', ...)`
- Assert ตามผลที่คาดหวังในชุดอ้างอิง
- ถ้าโค้ดทดสอบอยู่ใน repo โครงงานแล้ว ไม่ต้องคัดลอก ให้สร้างไฟล์ `LINKS.md` ที่นี่ ใส่ลิงก์ไปยังไฟล์นั้นพร้อม commit
