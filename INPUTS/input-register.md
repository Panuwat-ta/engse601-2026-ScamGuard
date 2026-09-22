# Input Register and Source of Truth

| Input ID | Artifact | File path / URL | Version / date / commit | Owner | Status | Used by | Notes / change impact |
|---|---|---|---|---|---|---|---|
| IN-01 | Proposal | `INPUTS/proposal/` | 1.0 (รออนุมัติ) | Team ScamGuard | Draft | W01–W04 | แนบไฟล์ `SE02-แบบเสนอหัวข้อโครงงานวิศวกรรม.pdf` แล้ว |
| IN-02 | Requirement/SRS | `https://github.com/Panuwat-ta/project/tree/main/Document/srs` | SRS 1.1 / 2026-09-12 / `2b8a1fb0` | Team ScamGuard | Current | W05–W16 (current); W01–W04 historical | Canonical source คือ `Document/srs`; `INPUTS/requirements-srs/` เป็น snapshot เก่าและห้ามใช้ override current baseline |
| IN-03 | HLD/Detail Design | `INPUTS/design/` | 1.0 / 2026-08-24 | Team ScamGuard | Current | W02, W04–W08 | Baseline Design Documents |
| IN-04 | ENGSE212 repository | `https://github.com/Panuwat-ta/project` | branch: main | Team ScamGuard | Current | W02–W16 | Source code repository |
| IN-05 | Stakeholder/glossary/risk notes | `PROJECT.md` | 2026-08-24 | ภานุวัฒน์ ต๋าคำ | Current | W01–W04 | Risk and constraints (Critical context) |

## Status meaning

- `Current`: version ที่ทีมประกาศเป็น source of truth สำหรับงานปัจจุบัน
- `Draft`: ใช้ทบทวนได้แต่ยังไม่เป็น baseline
- `Superseded`: มี version ใหม่กว่า; เก็บไว้เพื่อ trace
- `Not Ready`: ยังไม่มีหรือยังเปิดตรวจไม่ได้ ต้องมี owner/next action ใน Notes

## Input change log

| Date | Input ID | Old → New | Reason | Week/artifact affected | Action/owner |
|---|---|---|---|---|---|
| 2026-09-22 | IN-02 | local SRS v1.0 snapshot → ENGSE212 `Document/srs` SRS v1.1 | ยืนยัน canonical source ที่ใช้จริง | W05 onward; re-check W03/W04 handoff เมื่อถูกนำมาใช้ | ภานุวัฒน์ |
