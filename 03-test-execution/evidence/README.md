# หลักฐานจากการรันจริง

ตั้งชื่อ `<รหัส TC>_<ระดับ>_<วันที่ปี ค.ศ.>` เช่น `TC-02_unit_2026-10-08.txt` `SYS-01_system_2026-10-08.png`

ดูกติกาเต็มใน [README ของ 03-test-execution](../README.md) ไฟล์ในโฟลเดอร์นี้ต้องมาจากการรันจริงเท่านั้น

| ไฟล์ | ใช้เป็นหลักฐานอะไร | หมายเหตุ |
|---|---|---|
| `s3-api.png` | ภาพหน้าจอผลรัน v2 4 Pass / 6 Fail 23 ต.ค. 2569 | ภาพจริงจาก terminal (baseline `c3bc7223`) มีคำสั่งและ summary ครบ; ใช้ในภาคผนวกของ S3-B v2 |
| `s3-api-reference-run.txt` | ผลรันชุดอ้างอิง v2 4 Pass / 6 Fail 23 ต.ค. 2569 | ข้อความดิบจากเทอร์มินัล รวม warning ของไลบรารี |
| `s3-api-reference-run-v1.txt` | ผลรันชุด v1 6 Pass / 4 Fail | เก็บไว้เทียบก่อน rerun |
| `project-auth-pytest.txt` | `server/tests/api/test_auth.py` 2 passed | ชุดทดสอบเดิมของโปรเจกต์ ครอบเฉพาะ happy path ของ register/login |

## ภาพที่ยังไม่มี

- `SYS-AUTH-01_system_<วันที่>.png` — ยังไม่มี เพราะ System test ยัง `Not Executed` (ไม่มี build/environment ครบวงจร)
- `UAT-AUTH-01_uat_<วันที่>.png` — ยังไม่มี เพราะยังไม่มีผู้ใช้จริงนอกทีม

ห้ามสร้างภาพ UI หรือภาพผลรันขึ้นเอง; เมื่อรัน System/UAT ได้จริงให้เพิ่มภาพในโฟลเดอร์นี้และอัปเดต S3-B ขั้นที่ 3/4
