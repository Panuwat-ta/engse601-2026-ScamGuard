# DEF-02 ไม่มี endpoint จัดการ/ดูประวัติความยินยอม PUT /consent/research และ GET /consent/logs

| ช่อง | ข้อมูล |
|---|---|
| พบจาก TC | TC-05, TC-10 |
| ความต้องการที่เกี่ยวข้อง | REQ-04 REQ-05 FR-PDPA-01 AC-3, AC-5 |
| รุ่นและสภาพแวดล้อม | `Panuwat-ta/project` @ `c3bc7223` (branch `Refactor-mobile`) Python 3.10 FastAPI + httpx ASGITransport (in-memory session) SRS v1.1 |
| ผู้รายงาน วันที่ | นาย ภานุวัฒน์ ต๋าคำ 2026-10-22 |
| ความรุนแรง | สูง (High) เพราะผู้ใช้ถอน Research Consent และเข้าถึงประวัติความยินยอมของตนไม่ได้ ทำให้สิทธิ์ตาม PDPA และวงจร consent 4/4 ไม่ครบ |
| ความเร่งด่วน | P2 เพราะต้องปิดก่อนส่งมอบ แต่ไม่ทำให้ข้อมูลเสียหาย |
| สถานะ | Open — ยังไม่แก้ |

## ขั้นตอนทำซ้ำ

1. สมัครสมาชิกด้วย `research_consent: true` และเข้าสู่ระบบสำเร็จ
2. เรียก `PUT /api/v1/consent/research` ด้วย body `{"is_granted": false}` และ access token ของผู้ใช้
3. เรียก `GET /api/v1/consent/logs` ด้วย access token เดียวกัน

## ผลที่คาดหวัง (อ้างกฎ)

- `PUT /api/v1/consent/research` ตอบ HTTP 200 พร้อม `{consent_type: "research", is_granted: false}` และบันทึก `updated_at` (REQ-04 FR-PDPA-01 AC-3)
- `GET /api/v1/consent/logs` ตอบ HTTP 200 พร้อม `{logs: [{consent_type, is_granted, created_at, updated_at}, ...]}` เฉพาะของผู้ใช้คนนั้น (REQ-05 FR-PDPA-01 AC-5)

## ผลจริง

ทั้งสองคำขอได้ HTTP 404 `{"detail":"Not Found"}` เพราะไม่มี route ทั้งสองเส้นใน API

## หลักฐาน

`../../03-test-execution/evidence/s3-api-reference-run.txt` บรรทัด TC-05 และ TC-10

## ผลกระทบ

ผู้ใช้ใช้สิทธิ์ถอนความยินยอมและเข้าถึงประวัติความยินยอมของตนไม่ได้ และวงจร consent 4/4 ข้อของเกณฑ์จบไม่ครบ (ถอนและดูประวัติยังขาด)

## สาเหตุที่น่าจะเป็น

ยังไม่ได้ implement route และ service สำหรับอัปเดต/อ่าน `consent_logs` ตาม SRS

## แนวทางแก้

เพิ่ม `PUT /consent/research` ที่ตรวจสิทธิ์เจ้าของข้อมูล อัปเดตค่าและ `updated_at` พร้อมบันทึกประวัติ และเพิ่ม `GET /consent/logs` ที่คืนเฉพาะ log ของผู้ใช้ปัจจุบัน พร้อม test ตรวจว่าไม่คืนข้อมูลของผู้ใช้อื่น

## ประวัติ

| วันที่ | เหตุการณ์ | หลักฐาน |
|---|---|---|
| 2026-10-22 | เปิดรายงานจากผลรัน TC-10 | `../../03-test-execution/evidence/s3-api-reference-run.txt` |
| 2026-10-23 | รันชุด v2 เพิ่ม TC-05 พบว่า `PUT /consent/research` ก็ไม่มีเช่นกัน | `../../03-test-execution/evidence/s3-api-reference-run.txt` |
