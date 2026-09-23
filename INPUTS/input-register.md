# Input Register and Source of Truth

| Input ID | Artifact | File path / URL | Version / date / commit | Owner | Status | Used by | Notes / change impact |
|---|---|---|---|---|---|---|---|
| IN-01 | Proposal | `INPUTS/proposal/` | 1.0 (รออนุมัติ) | Team ScamGuard | Draft | W01–W04 | แนบไฟล์ `SE02-แบบเสนอหัวข้อโครงงานวิศวกรรม.pdf` แล้ว |
| IN-02 | Requirement/SRS | `INPUTS/requirements-srs/` (mirror) / `https://github.com/Panuwat-ta/project/tree/main/Document/srs` (canonical) | SRS 1.1 / 2026-09-12 / `2b8a1fb0` | Team ScamGuard | Current | W05–W16 (current); W01–W04 historical | ไฟล์หลัก 04/05/06/07A ใน local mirror sync จาก canonical `Document/srs`; canonical GitHub path เป็น authority เมื่อมีความต่าง |
| IN-03 | HLD/Detail Design | `INPUTS/design/` | 1.0 / 2026-08-24 | Team ScamGuard | Current | W02, W04–W08 | Baseline Design Documents |
| IN-04 | ENGSE212 source repository | `https://github.com/Panuwat-ta/project` | historical W05/W06 source baseline: `main` commit `66bc9e4a` | Team ScamGuard | Current reference | W02–W16 | Code behavior must be tied to the branch/commit used by each execution; do not infer current behavior from an older baseline |
| IN-05 | Stakeholder/glossary/risk notes | `PROJECT.md` | 2026-08-24 | ภานุวัฒน์ ต๋าคำ | Current | W01–W04 | Risk and constraints (Critical context) |
| IN-06 | Test plan, test cases, RTM and execution reports | `https://github.com/Panuwat-ta/project/tree/develop/tests_all` and `/home/panuwat/project/Document/tests_doc/` | branch `develop`, commit `162e0249abb9e9940f014ba6d5182d38213bc771`, referenced 2026-09-23 | Team ScamGuard | Current testing input | W05–W16 | `tests_all/manual_tests/` is design; `tests_all/tests_report/` is execution evidence. Historical reports without commit/build/env are supporting only; manual execution log currently has no real rows |

## Status meaning

- `Current`: version ที่ทีมประกาศเป็น source of truth สำหรับงานปัจจุบัน
- `Draft`: ใช้ทบทวนได้แต่ยังไม่เป็น baseline
- `Superseded`: มี version ใหม่กว่า; เก็บไว้เพื่อ trace
- `Not Ready`: ยังไม่มีหรือยังเปิดตรวจไม่ได้ ต้องมี owner/next action ใน Notes

## Input change log

| Date | Input ID | Old → New | Reason | Week/artifact affected | Action/owner |
|---|---|---|---|---|---|
| 2026-09-22 | IN-02 | local SRS v1.0 snapshot → local mirror synced from ENGSE212 `Document/srs` SRS v1.1 | อัปเดต `INPUTS/requirements-srs` ให้เป็น version ปัจจุบันและคง canonical GitHub source | W05 onward; re-check W03/W04 handoff เมื่อถูกนำมาใช้ | ภานุวัฒน์ |
| 2026-09-23 | IN-06 | Not registered → `develop/tests_all` and `Document/tests_doc` pinned | ผู้ใช้ยืนยันว่า repository/project จริงและชุดทดสอบอยู่ที่ `develop/tests_all`; แยก test authority ออกจาก SRS authority | W05–W07 re-check; W07 scenario re-baseline | ภานุวัฒน์ |
