# ScamGuard — ENGSE601 V&V Evidence Repository

Repository นี้ใช้จัดเก็บงาน Verification & Validation (V&V) ของโครงงาน **Scam Image Detection Application (ScamGuard)** ในรายวิชา ENGSE601 โดยเชื่อม requirement, source code, test design, raw evidence, findings และไฟล์ส่งงานกลับไปยังโครงงาน ENGSE212 อย่างตรวจสอบย้อนกลับได้

> หลักสำคัญ: repository นี้บันทึกเฉพาะสิ่งที่ตรวจหรือดำเนินการจริง ไม่สร้าง test result, peer review, approval, stakeholder decision หรือ UAT response ขึ้นเอง

## ภาพรวมโครงงาน

| รายการ | แหล่งอ้างอิง |
|---|---|
| ENGSE601 evidence repository | `Panuwat-ta/engse601-2026-ScamGuard` |
| ENGSE212 project repository | [Panuwat-ta/project](https://github.com/Panuwat-ta/project) |
| Canonical Requirement/SRS | [`main/Document/srs`](https://github.com/Panuwat-ta/project/tree/main/Document/srs) — SRS v1.1 |
| Project test plan/cases/reports | [`develop/Document/tests_doc`](https://github.com/Panuwat-ta/project/tree/develop/Document/tests_doc) และ [`develop/tests_all`](https://github.com/Panuwat-ta/project/tree/develop/tests_all) |
| Test-document baseline | `develop` commit `162e0249abb9e9940f014ba6d5182d38213bc771` |
| Historical source baseline สำหรับ Week 05–06 | `main` commit `66bc9e4af3747808ef45273d31b50dbc59ad91ab` |
| สถานะล่าสุด | ดู [STATUS.md](STATUS.md) |

Requirement authority และ testing authority ถูกแยกจากกันอย่างตั้งใจ: SRS ใช้จาก `main/Document/srs` ส่วน test plan, test cases และ reports ของโครงการใช้จาก `develop`. หลักฐานแต่ละสัปดาห์ต้องระบุ branch/commit ของตนเอง และห้ามนำผลจากคนละ baseline มาแทนกัน

## สถานะ Week 01–07

| Week | Output | สถานะหลักฐาน | Tag / snapshot |
|---:|---|---|---|
| 01 | Quality Risk Cards v1 | Submitted | `w01-submission-v1` |
| 02 | Project Quality Route Map v1 | Submitted | `w02-submission-v1` |
| 03 | Revised Critical Requirements v1 | Submitted | `w03-submission-v1` |
| 04 | SRS Review and RTM v1 | Submitted | `w04-submission-v1` |
| 05 | Component Test Case Set | v1 Submitted; v2 documentation revision | `w05-submission-v1` |
| 06 | Integration Test Design v1 | Merged/tagged; independent review และ pinned re-test ยัง pending | `w06-submission-v1` |
| 07 | System/UAT Scenarios v1 | Merged/tagged; execution และ human gates ยัง pending | `w07-submission-v1` |

Tag ของ Week 06–07 ใช้ตรึง snapshot ที่ merge เข้า `main` แล้วเท่านั้น การมี tag ไม่ได้แปลว่า peer review, course submission, approval หรือการทดสอบที่ยังไม่เกิดขึ้นเสร็จสมบูรณ์แล้ว

### ผลที่ยืนยันได้ในปัจจุบัน

| Week | ผล / สถานะ | ข้อจำกัด |
|---:|---|---|
| 05 | 18 cases: 7 Pass, 9 Fail, 1 Not Ready, 1 Needs Clarification | ผลอยู่บน historical `main` commit `66bc9e4a`; เอกสาร `develop/tests_all` ใช้ cross-check เท่านั้น |
| 06 | 18 cases: 6 Pass, 11 Fail, 1 Not Ready | ผลจาก integration harness บน frozen baseline; historical reports บน `develop` ไม่ใช่ pinned re-run |
| 07 | 10 System Test = Not Executed; 6 UAT = Not Ready | Manual execution log ยังไม่มีผลรันจริง, JUnit ปัจจุบันมี 0 tests และยังไม่มี approved System/UAT build |

รายละเอียด case, raw output, source snapshots, SHA-256 และ findings อยู่ใน `WEEKS/week-XX/work/` ของแต่ละสัปดาห์

## เริ่มตรวจงานจากจุดไหน

1. อ่าน [PROJECT.md](PROJECT.md) เพื่อดู scope, stakeholder, constraints และ current truth
2. อ่าน [INPUTS/input-register.md](INPUTS/input-register.md) เพื่อดู version และ source of truth ของ input
3. อ่าน [STATUS.md](STATUS.md) เพื่อดู submission ledger และ revision history
4. เปิด `WEEKS/week-XX/README.md` ของสัปดาห์ที่ต้องการตรวจ
5. ตรวจ design/record ใน `work/`, raw evidence ใน `work/evidence/` และไฟล์ส่งใน `submission/`
6. ตรวจ tag และ commit ที่ระบุ โดยไม่ตีความ tag แทน human sign-off

## Evidence flow

```text
Canonical SRS + project test assets + pinned source baseline
                         ↓
              scope / risk / test design
                         ↓
           probe or real execution evidence
                         ↓
             result register + findings
                         ↓
        peer review + Definition of Done
                         ↓
              PDF + commit + tag
                         ↓
            STATUS.md + human handoff
```

หากยังไม่มี execution, environment, reviewer หรือ participant จริง ให้ใช้ `Not Executed` หรือ `Not Ready` พร้อม blocker และ next action ห้ามใส่ผลสมมติให้เอกสารดูสมบูรณ์

## ความหมายของสถานะหลักฐาน

| Status | ใช้เมื่อ | สิ่งที่ต้องมี |
|---|---|---|
| `Existing` | หลักฐานมีอยู่จริงและเปิดตรวจได้ | path/URL, version/build, วันที่หรือ commit |
| `Planned` | วางแผนจะสร้าง แต่ยังไม่เกิด | owner, next action และช่วงเวลาที่คาดไว้ |
| `Not Ready` | ยังทำไม่ได้เพราะ input, decision, environment หรือคนยังไม่พร้อม | blocker, decision owner และ next action |
| `Not Executed` | ออกแบบ test แล้วแต่ยังไม่ได้รัน | case/scenario, expected result และหลักฐานที่ต้องเก็บเมื่อรัน |
| `Pass` / `Fail` | มีการตรวจหรือรันจริงบน baseline ที่ระบุ | raw output/log, expected-vs-actual และ trace ไปยัง requirement |

## โครงสร้าง repository

```text
.
├── PROJECT.md                  ข้อมูลโครงงานและ current truth
├── TEAM.md                     สมาชิก บทบาท และ working agreement
├── STATUS.md                   Submission ledger และ revision history
├── CONTRIBUTING.md             วิธีทำงานร่วมกันด้วย Git
├── INPUTS/                     ทะเบียน Proposal/SRS/Design และ source of truth
├── TEMPLATES/                  แบบบันทึกกลางที่ใช้ซ้ำได้
└── WEEKS/
    ├── week-01/ ... week-04/   Foundation, requirements review และ RTM
    ├── week-05/                Component / Unit Testing
    ├── week-06/                Integration / API Testing
    ├── week-07/                System Testing และ UAT scenarios
    └── week-08/ ... week-17/   งานตามแผนรายวิชาที่ยังดำเนินต่อ
```

ในแต่ละสัปดาห์:

```text
README.md       ขอบเขต, baseline และสถานะของสัปดาห์
work/           เอกสารทำงาน, test design, findings และ AI declaration
work/evidence/  Raw evidence และ source-derived snapshots
work/probes/    Script ที่จำเป็นต่อการ reproduce (ถ้ามี)
submission/     PDF หรือ artifact สำหรับรอบส่ง
```

## วิธีส่งงานและออก tag

1. ทำงานบน branch ของสัปดาห์และระบุ baseline ให้ครบ
2. ตรวจ Definition of Done และให้ผู้ที่ไม่ใช่ผู้เขียนหลักทำ peer review
3. Export PDF ไปที่ `WEEKS/week-XX/submission/`
4. Merge เข้า `main` เมื่อเงื่อนไขของทีมผ่าน
5. สร้าง annotated tag รูปแบบ `wXX-submission-vN`
6. บันทึก tag, commit hash, วันที่ส่ง และหลักฐานการ review ใน [STATUS.md](STATUS.md)
7. ส่ง URL/tag ผ่านช่องทางที่อาจารย์กำหนด

หากแก้หลังส่ง ให้เพิ่ม version และ tag ใหม่ เช่น `v2`; ห้ามย้าย tag เดิมหรือเขียนทับประวัติโดยไม่มี revision record

## Data protection และ AI use

- ห้ามเก็บ credential, token, password ดิบ, production secret หรือข้อมูลผู้ใช้ที่ไม่จำเป็น
- ห้ามนำรูปภาพหรือข้อมูลส่วนบุคคลของผู้ใช้ที่ไม่มี consent ไปใช้กับเครื่องมือ AI
- งานที่ใช้ AI ต้องมี `ai-use-declaration.md` และต้องตรวจข้อเสนอเทียบกับ artifact จริง
- AI ช่วยจัดโครงสร้าง วิเคราะห์ หรือสร้าง draft ได้ แต่ไม่สามารถทำ peer review, approval, stakeholder decision หรือ UAT response แทนคนจริง

## รายการที่ยังต้องดำเนินการโดยมนุษย์

- Independent peer review ของ Week 05 revision, Week 06 และ Week 07
- Pinned re-test ของ Week 05–06 บน build/commit/environment ที่อนุมัติ
- System Test จริงของ Week 07 พร้อม manual execution evidence
- เลือก UAT option, เตรียม consent/recruitment และดำเนิน UAT จริง
- ผู้เข้าร่วมที่ valid 100 คนสำหรับ metric NFR-06
- Dev/QA/PM sign-off และการส่งงานผ่านช่องทางรายวิชา
