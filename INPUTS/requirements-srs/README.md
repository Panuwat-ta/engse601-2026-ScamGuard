# Requirements and SRS — Historical Snapshot

**Snapshot version:** 1.0  
**Snapshot date:** August 23, 2026  
**Status:** Superseded for current development; retained as W01–W04 evidence

## Canonical current source

Requirement/SRS ที่ใช้จริงปัจจุบันอยู่ใน ENGSE212 repository:

- URL: https://github.com/Panuwat-ta/project/tree/main/Document/srs
- Branch: `main`
- Current SRS: `05_Software_Requirement_Specification.md` v1.1 (September 12, 2026)
- Current registered baseline/commit: ดู `../input-register.md` (IN-02)

ไฟล์ใน directory นี้ห้ามใช้เป็น current Source of Truth สำหรับ W05 เป็นต้น หากข้อมูลใน snapshot v1.0 ขัดกับ canonical source ให้ยึดเอกสารใน `Document/srs` บน `main`.

## Historical document index

- `01_Project_Overview.md` — project overview snapshot
- `02_Project_Scope.md` — project scope snapshot
- `03_Software_Architecture.md` — architecture snapshot
- `04_Requirement_Candidates.md` — Requirement Candidates snapshot
- `05_Software_Requirement_Specification.md` — SRS v1.0 snapshot
- `06_Requirement_Traceability.md` — traceability snapshot
- `07_Appendix_A_Full_Traceability_Matrix.md` — full RTM snapshot
- `07_Appendix_B_Key_Design_Decisions.md` — design-decision snapshot

## Usage rule

- W01–W04: ใช้ไฟล์ชุดนี้เพื่ออ่านหลักฐานตาม baseline ในเวลาที่งานเหล่านั้นถูกจัดทำ
- W05 เป็นต้น: ใช้ canonical GitHub path ข้างต้นเป็น Requirement/SRS authority
- ห้ามแก้ snapshot เก่าให้ดูเหมือนเป็น v1.1 เพราะจะทำลาย historical trace; การเปลี่ยน baseline ให้บันทึกใน `../input-register.md`
