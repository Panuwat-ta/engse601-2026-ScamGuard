# หน้าส่งงานกลุ่ม ENGSE601 (หน้าเดียว)

## ข้อมูลทีม

| รายการ | กรอก |
|---|---|
| ชื่อทีม (`<TeamName>` ภาษาอังกฤษ ไม่มีช่องว่าง ใช้ชื่อเดียวกันทุกไฟล์) | ScamGuard |
| โครงงาน ENGSE212 | ScamGuard — Scam Image Detection Application |
| feature ที่ใช้ทดสอบ (เลือกในใบงานครั้งที่ 1) | การสมัครสมาชิกและการจัดการความยินยอม 2 ระดับ (System Consent + Research Consent) |
| ผู้ส่งหลัก | ภานุวัฒน์ ต๋าคำ |
| ลิงก์ repo นี้ | [Panuwat-ta/engse601-2026-ScamGuard](https://github.com/Panuwat-ta/engse601-2026-ScamGuard) <br> [Panuwat-ta/project](https://github.com/Panuwat-ta/project/tree/develop) |

## งานที่ต้องส่ง

| # | งาน | ไฟล์และตำแหน่ง | นับเข้า | สถานะ | หมายเหตุ |
|---|---|---|---|---|---|
| G1 | W01 Quality Risk Cards | `WEEKS/week-01/submission/W01_ScamGuard_Quality-Risk-Cards_v1.pdf` | จิตพิสัย | ส่งแล้ว | tag `w01-submission-v1` |
| G2 | W02 Project Quality Route Map | `WEEKS/week-02/submission/W02_ScamGuard_Project-Quality-Route-Map_v1.pdf` | จิตพิสัย | ส่งแล้ว | tag `w02-submission-v1` |
| G3 | W03 Revised Critical Requirements | `WEEKS/week-03/submission/W03_ScamGuard_Revised-Critical-Requirements_v1.pdf` | Gate A | ส่งแล้ว | tag `w03-submission-v1` |
| G4 | W04 SRS Review, RTM Lite และ Gate A | `WEEKS/week-04/submission/W04_ScamGuard_SRS-Review-and-RTM_v1.pdf` | Gate A | ส่งแล้ว | tag `w04-submission-v1` |
| G5 | W05 Component Test Case Set (ไฟล์ที่ส่งจริง; template เดิมระบุ Requirement-to-Design Trace) | `WEEKS/week-05/submission/W05_ScamGuard_Component-Test-Case-Set_v2.pdf` | Gate B | ส่งแล้ว | v1 tag `w05-submission-v1`; v2 ปรับเอกสาร ไม่เปลี่ยนผล 7 Pass / 9 Fail / 1 Not Ready / 1 Needs Clarification |
| G6 | ใบงานครั้งที่ 1 ส่วน B วางแผนก่อนทดสอบ | [01-plan/S1-B_ScamGuard.pdf](01-plan/S1-B_ScamGuard.pdf) **เฉพาะส่วน B** | Evidence Pack | ส่งแล้ว | ไฟล์ครบ; คงรหัสนักศึกษาใน PDF ตามคำสั่ง |
| G7 | ใบงานครั้งที่ 2 ส่วน B ออกแบบกรณีทดสอบ | [02-test-design/S2-B_ScamGuard_v2.pdf](02-test-design/S2-B_ScamGuard_v2.pdf) | Evidence Pack | ส่งแล้ว | v2 ล่าสุด; คงรหัสนักศึกษาใน PDF ตามคำสั่ง |
| G8 | ใบงานรวม 3–4 ส่วน B1 รันชุดอ้างอิงของทีม | [03-test-execution/execution-report.md](03-test-execution/execution-report.md) · [S3-B_ScamGuard_v2.pdf](03-test-execution/S3-B_ScamGuard_v2.pdf) · [tests/](03-test-execution/tests/) · [evidence/](03-test-execution/evidence/) | Evidence Pack | ส่งแล้ว | ผลจริง 4 Pass / 6 Fail; System/UAT `Not Executed` ตามจริง; คงรหัสนักศึกษาใน PDF ตามคำสั่ง |
| G9 | ใบงานรวม 3–4 ส่วน B3 หน้าที่และการใช้ AI | [TEAM.md](TEAM.md) · [AI-LOG.md](AI-LOG.md) | Evidence Pack | ส่งบางส่วน | AI-LOG ครบ; TEAM.md ยังขาด Git username ของสมาชิกคนที่ 2 |

**สถานะที่ใช้:** `ส่งแล้ว` · `พร้อมส่ง` (ไฟล์ครบ แต่ยังมี blocker ก่อน Release) · `ส่งบางส่วน` (เขียนในหมายเหตุว่าขาดอะไร) · `ไม่ได้ทำ` (เขียนเหตุผล) · `แก้หลังส่ง` (บอกว่าแก้อะไร)

## ไม่ต้องทำ

- **ใบงานรวม 3–4 ส่วน B2** (ข้อบกพร่อง ความรุนแรง ทดสอบซ้ำ คำตัดสินส่งมอบ) เพราะไม่ได้สอนครั้งที่ 4 · ไม่นับคะแนน
- **ใบงานรวม 3–4 ส่วน A ข้อ 3–5** (งานเดี่ยว) ไม่นับคะแนน ทำเฉพาะข้อ 1–2
- **สัปดาห์ที่ 6–17** ในโฟลเดอร์ `WEEKS/` ไม่ได้ใช้ในภาคนี้

## วิธีส่ง

1. ตรวจไฟล์และเติม Git username ใน `TEAM.md` ให้ครบ; คงรหัสนักศึกษาใน PDF ตามคำสั่ง
2. วางไฟล์ตามตารางด้านบน แล้ว commit และ push · ตั้งชื่อไฟล์ตามตารางทุกตัวอักษร
3. กรอกตาราง “งานที่ต้องส่ง” ในหน้านี้ให้ครบ
4. ผู้ส่งหลักสร้าง Release: หน้า repo → **Releases** → **Draft a new release** → Choose a tag พิมพ์ `engse601-submit` → **Create new tag** → ตั้งชื่อ `engse601-submit` → **Publish release**
5. ผู้ส่งหลักกรอกลิงก์ repo ในฟอร์มลงทะเบียนทีมที่ผู้สอนแจก

แก้หลังสร้าง Release ได้ก่อนกำหนดส่ง โดยสร้าง Release ใหม่ชื่อ `engse601-submit-v2` · ผู้สอนตรวจ Release ล่าสุดที่สร้างก่อนกำหนดส่ง

## ตัวอย่าง

ตัวอย่างงานที่ทำครบจาก Case X ของผู้สอน (ทีมสมมติ Team00): https://github.com/se-rmutl/ENGSE601-Team00-CaseX-Example · เปิด `SUBMISSIONS.md` ของตัวอย่างเทียบกับหน้านี้ได้ทีละแถว · ใช้ดูรูปแบบและระดับความละเอียด **ห้ามคัดลอกข้อความหรือหลักฐาน** เพราะงานของทีมต้องมาจากโครงงานของทีมเอง

## ตรวจก่อนส่ง

- [x] ชื่อไฟล์ใช้ `<TeamName>` เดียวกันทุกไฟล์ และตรงกับตาราง
- [x] ไม่มีรหัสนักศึกษาและไม่มีส่วน A ใน repo (ยกเว้นในไฟล์ .pdf)
- [x] `03-test-execution/` มีโค้ดทดสอบใน `tests/` และผลการรันจริงใน `evidence/` (System/UAT เป็น Not Executed พร้อมเหตุผล)
- [x] TEAM.md บอกว่าใครทำส่วนไหน · AI-LOG.md กรอกแล้ว — เหลือ Git username ของสมาชิกคนที่ 2
- [x] สร้าง Release `engse601-submit` แล้ว
