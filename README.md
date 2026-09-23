# ScamGuard — ENGSE601 V&V Evidence Repository

Repository นี้ใช้จัดเก็บงาน Verification & Validation (V&V) ของโครงงาน **Scam Image Detection Application (ScamGuard)** ในรายวิชา ENGSE601 โดยเชื่อม requirement, source code, test design, raw evidence, findings และไฟล์ส่งงานกลับไปยังโครงงาน ENGSE212 อย่างตรวจสอบย้อนกลับได้

> หลักสำคัญ: repository นี้บันทึกเฉพาะสิ่งที่ตรวจหรือดำเนินการจริง ไม่สร้าง test result, peer review, approval, stakeholder decision หรือ UAT response ขึ้นเอง

## งานของ repository นี้

งานหลักคือสร้างชุดหลักฐาน V&V ที่เชื่อมโครงงาน ScamGuard ตั้งแต่ requirement ไปจนถึงการทดสอบและการตัดสินใจ โดยมีขอบเขตดังนี้

- วิเคราะห์ความเสี่ยงด้านคุณภาพและเลือกส่วนสำคัญของระบบที่ต้องตรวจ
- ตรวจ Requirement/SRS ให้ชัดเจน ครบถ้วน สอดคล้อง และทดสอบได้
- สร้าง Acceptance Criteria และ Requirement Traceability Matrix (RTM)
- ออกแบบและตรวจ Component, Integration/API, System และ UAT scenarios
- เก็บ raw evidence, source snapshot, route/schema contract, test output และ finding ที่ตรวจย้อนหลังได้
- จัดทำ PDF ส่งงาน, AI Use Declaration, commit และ tag ของแต่ละสัปดาห์
- แยกสิ่งที่ทำเสร็จจริงออกจากสิ่งที่ยัง `Not Ready` หรือ `Not Executed` เพื่อไม่ให้เกิดผลทดสอบหรือ approval ที่ไม่มีหลักฐาน

งานใน repository นี้เป็นงานเอกสารและหลักฐานของ ENGSE601 ส่วน source code, SRS และ project test assets ตัวจริงอยู่ใน ENGSE212 repository และถูกอ่านโดยตรึง branch/commit ที่ใช้อ้างอิง

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

## งานที่ทำเสร็จแล้ว

| Week | งานที่ดำเนินการและผลลัพธ์ | สถานะ / หลักฐาน |
|---:|---|---|
| [01](WEEKS/week-01/README.md) | วิเคราะห์ requirement, stakeholder และความเสี่ยง แล้วจัดทำ **Quality Risk Cards** สำหรับใช้เลือก critical risks ของ ScamGuard | ส่ง v1 และตรึงด้วย `w01-submission-v1` |
| [02](WEEKS/week-02/README.md) | นำ critical risk มาสร้าง **Project Quality Route Map** เชื่อม Requirements → Design → Implement → Test → Decision พร้อม V&V questions, gates และ feedback loop | ส่ง v1 และตรึงด้วย `w02-submission-v1` |
| [03](WEEKS/week-03/README.md) | ตรวจ critical requirements ด้านความชัดเจน ความครบ ความสอดคล้อง ความเป็นไปได้และ testability พร้อมปรับ wording และเขียน **Acceptance Criteria** | ส่ง v1 และตรึงด้วย `w03-submission-v1` |
| [04](WEEKS/week-04/README.md) | จัดทำ **SRS Review Log, RTM v1, Gate A decision และ Phase 2 Entry Pack** เพื่อส่งต่อไปยังการทดสอบระดับ Component/Integration/System/UAT | ส่ง v1 และตรึงด้วย `w04-submission-v1` |
| [05](WEEKS/week-05/README.md) | ออกแบบและตรวจ **Component Test Case Set 18 cases**; ผลจริงคือ 7 Pass, 9 Fail, 1 Not Ready และ 1 Needs Clarification พร้อม source/route/schema snapshots และ reproducible probe | v1 ส่งแล้วด้วย `w05-submission-v1`; v2 ปรับเอกสารและ cross-check `develop/tests_all` โดยไม่เปลี่ยนผลเดิม |
| [06](WEEKS/week-06/README.md) | ทำ **Interface/API Risk Mapping** และ Integration Test Design 18 cases ครอบคลุม Mobile, API, Redis, inference, heatmap, history และ report; ผลจริงคือ 6 Pass, 11 Fail และ 1 Not Ready | PDF/evidence merge แล้วและตรึงด้วย `w06-submission-v1`; independent review และ pinned re-test ยัง pending |
| [07](WEEKS/week-07/README.md) | map project E2E cases จริงเป็น **10 System Test scenarios** และออกแบบ **6 UAT scenarios** พร้อม readiness probe, result register, privacy/consent protocol และ PDF | Package merge แล้วและตรึงด้วย `w07-submission-v1`; 10 System Test ยัง Not Executed และ 6 UAT ยัง Not Ready |

ดังนั้น งานออกแบบ เอกสาร หลักฐาน และ package ของ Week 01–07 ถูกจัดทำและเก็บใน repository แล้ว แต่คำว่า “เสร็จ” ไม่ได้ใช้แทนกิจกรรมภายนอกที่ยังไม่เกิดขึ้นจริง โดยเฉพาะ independent peer review, pinned re-test, System Test/UAT execution, stakeholder approval และการส่งผ่านช่องทางรายวิชา

Tag ของ Week 06–07 ใช้ตรึง snapshot ที่ merge เข้า `main` แล้วเท่านั้น การมี tag ไม่ได้แปลว่า peer review, course submission, approval หรือการทดสอบที่ยังไม่เกิดขึ้นเสร็จสมบูรณ์แล้ว

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

