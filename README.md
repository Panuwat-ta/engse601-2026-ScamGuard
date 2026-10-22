# ScamGuard — Scam Image Detection Application

ScamGuard คือแอปพลิเคชันสำหรับตรวจสอบรูปภาพที่อาจถูกตัดต่อหรือนำไปใช้หลอกลวง เช่น สลิปโอนเงินปลอมหรือภาพโปรไฟล์ปลอม โดยให้ผลประเมินความเสี่ยงและคำอธิบายประกอบผู้ใช้ทั่วไป

Repository นี้เป็น **ENGSE601 Verification & Validation (V&V) Evidence Repository** ของโครงงาน **ENGSE212** ทำหน้าที่เก็บ requirement review, test design, ผลรันจริง, ข้อบกพร่อง และหลักฐานส่งงานที่ตรวจสอบย้อนกลับได้

> หลักการสำคัญ: repository นี้บันทึกเฉพาะสิ่งที่ตรวจหรือรันจริง ไม่สร้างผลทดสอบ ภาพหน้าจอ หรือการตัดสินใจขึ้นเอง หากยังรันไม่ได้จะบันทึกเป็น `Not Executed` พร้อมเหตุผลและแผน

## ภาพรวมระบบ

| ส่วน | เทคโนโลยี/ขอบเขต |
|---|---|
| Mobile application | Flutter (Android) สำหรับผู้ใช้ทั่วไป |
| Backend API | FastAPI (Python 3.10) + PostgreSQL 15 + Redis 7 |
| AI / OCR | ตรวจภาพตัดต่อและสกัดข้อความ พร้อม Grad-CAM heatmap เพื่ออธิบายผล |
| Admin web | React สำหรับตรวจสอบและจัดการรายงาน |
| Privacy | System Consent บังคับ + Research Consent ทางเลือก พร้อม consent log ตาม PDPA |

ขอบเขตที่ทดสอบในรอบล่าสุดคือ **การสมัครสมาชิกและการจัดการความยินยอม 2 ระดับ** (FR-AUTH-01 และ FR-PDPA-01)

## สถานะล่าสุด

อัปเดต 23 ต.ค. 2569 บน baseline `Panuwat-ta/project` branch `Refactor-mobile` commit `c3bc7223`

| ด้าน | สถานะ | หลักฐาน |
|---|---|---|
| API reference suite (TC-01..TC-10) | **4 Pass / 6 Fail** | [ผลรัน](03-test-execution/evidence/s3-api-reference-run.txt) · [ภาพหน้าจอ](03-test-execution/evidence/s3-api.png) |
| System test (SYS-AUTH-01) | **Not Executed** — ยังไม่มี build/environment ครบวงจร | [ขั้นที่ 3](03-test-execution/S3-B_ScamGuard_v2.pdf) |
| UAT (UAT-AUTH-01) | **Not Executed** — ยังไม่มีผู้ใช้จริงนอกทีม | [ขั้นที่ 4](03-test-execution/S3-B_ScamGuard_v2.pdf) |
| ข้อบกพร่องค้าง | **3 ข้อ** — Critical 1, High 1, Medium 1 | [04-defects-release](04-defects-release/defects/) |
| การตัดสินส่งมอบ | **No-Go** จนกว่าจะปิด DEF-01/DEF-02 และรัน System/UAT | [S3-B v2](03-test-execution/S3-B_ScamGuard_v2.pdf) |

### ผลการทดสอบที่ผ่านและไม่ผ่าน

| ความสามารถ | TC | ผล |
|---|---|---|
| สมัครด้วยข้อมูลถูกต้องและเก็บรหัสผ่านเป็น hash | TC-02 | Pass |
| ปฏิเสธอีเมลซ้ำ | TC-04 | Pass |
| Research Consent เป็น false/true ตามที่ผู้ใช้เลือก | TC-08, TC-09 | Pass |
| รหัสผ่านสั้นต้องได้ HTTP 400 ตามสัญญา | TC-01, TC-03 | Fail — ได้ 422 จาก Pydantic |
| System Consent ต้องบังคับที่ฝั่งเซิร์ฟเวอร์ | TC-06, TC-07 | Fail — ระบบรับสมัครเมื่อ `false` หรือไม่ส่งฟิลด์ |
| ถอน Research Consent และดูประวัติ consent | TC-05, TC-10 | Fail — endpoint ยังไม่มี (404) |

## ข้อบกพร่องที่เปิดอยู่

| รหัส | ระดับ | สรุป | สถานะ |
|---|---|---|---|
| [DEF-01](04-defects-release/defects/DEF-01.md) | Critical / P1 | API สร้างผู้ใช้เมื่อ `system_consent = false` หรือไม่ส่งฟิลด์ | Open |
| [DEF-02](04-defects-release/defects/DEF-02.md) | High / P2 | ไม่มี `PUT /consent/research` และ `GET /consent/logs` | Open |
| [DEF-03](04-defects-release/defects/DEF-03.md) | Medium / P3 | รหัสผ่านสั้นคืน 422 แทน 400 ตาม AC-4 | Open |

## โครงสร้าง repository

```text
.
├── 01-plan/                  S1-B แผนทดสอบและ entry/exit criteria
├── 02-test-design/           S2-B ชุดออกแบบกรณีทดสอบ TC-01..TC-10 (v1/v2)
├── 03-test-execution/        S3-B v2, execution report, tests และ evidence
├── 04-defects-release/       รายงานข้อบกพร่อง DEF-01..DEF-03
├── INPUTS/                   ทะเบียน source of truth และลิงก์โครงงาน
├── TEMPLATES/                แม่แบบเอกสารที่ใช้ซ้ำ
├── WEEKS/                    บันทึกตามสัปดาห์เดิม (historical)
├── PROJECT.md                ข้อมูลโครงงานและ critical context
├── TEAM.md                   สมาชิก บทบาท และ working agreement
├── STATUS.md                 submission ledger เดิม
├── CONTRIBUTING.md           วิธีทำงานร่วมกันด้วย Git
└── AI-LOG.md                 บันทึกการใช้ AI และการตรวจสอบ
```

โฟลเดอร์ `03-test-execution/` มีโครงย่อย:

```text
tests/       โค้ด probe ที่ใช้รัน TC-01..TC-10
evidence/    ผลรันจริง ภาพหน้าจอ และ archive v1
*.docx/pdf   ใบงาน S3-B ฉบับส่งและฉบับก่อน rerun
```

## การรันซ้ำ (API reference suite)

ต้องมี source project ที่ baseline `Refactor-mobile@c3bc7223` และ Python virtual environment ของ project:

```bash
cd /path/to/project/server
./venv/bin/python /path/to/engse601-2026-ScamGuard/03-test-execution/tests/test_s3_reference_suite.py
```

ผลที่ต้องเห็นบน baseline นี้คือ:

```text
Summary: 4 Pass, 6 Fail, 10 total
```

Probe ใช้ `httpx.ASGITransport` แบบ in-process และ isolated in-memory session จึงไม่ต้องยิง HTTP ไปยัง server ภายนอกสำหรับชุดนี้

## เอกสารหลัก

| เอกสาร | ใช้ทำอะไร |
|---|---|
| [01-plan/S1-B_ScamGuard.pdf](01-plan/S1-B_ScamGuard.pdf) | แผนทดสอบ, ความเสี่ยง และ entry/exit criteria |
| [02-test-design/S2-B_ScamGuard_v2.pdf](02-test-design/S2-B_ScamGuard_v2.pdf) | ชุดอ้างอิง TC-01..TC-10 ฉบับ v2 |
| [03-test-execution/execution-report.md](03-test-execution/execution-report.md) | รายงานผลรัน B1 ขั้นที่ 1–5 |
| [03-test-execution/S3-B_ScamGuard_v2.pdf](03-test-execution/S3-B_ScamGuard_v2.pdf) | ใบงาน S3-B ฉบับส่ง พร้อมภาคผนวกภาพผลรัน |
| [03-test-execution/evidence/README.md](03-test-execution/evidence/README.md) | ทะเบียนหลักฐานและสิ่งที่ยังไม่มี |
| [AI-LOG.md](AI-LOG.md) | การใช้ AI และการตรวจสอบก่อนนำผลไปใช้ |

## แหล่งอ้างอิง

| รายการ | แหล่งอ้างอิง |
|---|---|
| โครงงานต้นทาง | [Panuwat-ta/project](https://github.com/Panuwat-ta/project) |
| SRS | [`main/Document/srs`](https://github.com/Panuwat-ta/project/tree/main/Document/srs) — SRS v1.1 |
| Source baseline ที่ทดสอบ | `Refactor-mobile@c3bc7223` |
| Project test documentation | [`develop/tests_all`](https://github.com/Panuwat-ta/project/tree/develop/tests_all) — ใช้เป็นเอกสารประกอบ ไม่ใช่ผลรันของ S3 |
| Repository นี้ | [Panuwat-ta/engse601-2026-ScamGuard](https://github.com/Panuwat-ta/engse601-2026-ScamGuard) |

## ทีม

| สมาชิก | บทบาท |
|---|---|
| นาย ภานุวัฒน์ ต๋าคำ | หัวหน้าโครงงาน · Mobile, Backend, AI Model · Evidence Coordinator |
| นาย เอกพันธ์ ทศทิศรังสรรค์ | ผู้ร่วมโครงงาน · Mobile, Testing |

รายละเอียดบทบาทและ working agreement อยู่ใน [TEAM.md](TEAM.md)

## หลักการบันทึกหลักฐาน

- ทุก Pass/Fail ต้องอ้างผลรันจริงที่เปิดตรวจได้
- ห้ามแก้ expected result ให้ตรงกับผลจริง
- ถ้ายังไม่มี environment, build, reviewer หรือผู้ใช้จริง ให้ใช้ `Not Executed` พร้อม blocker และ next action
- ภาพ `03-test-execution/evidence/s3-api.png` เป็นภาพผลรัน API จาก terminal จริง ไม่ใช่ภาพ System test และไม่ใช้แทน System/UAT

---

อัปเดตล่าสุด: 23 ต.ค. 2569
