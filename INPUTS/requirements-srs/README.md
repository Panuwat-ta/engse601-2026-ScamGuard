# Requirements and SRS — Current Local Mirror

**Current SRS version:** 1.1  
**SRS date:** September 12, 2026  
**Canonical branch:** `main`  
**Canonical source:** https://github.com/Panuwat-ta/project/tree/main/Document/srs

โฟลเดอร์นี้เก็บสำเนาใช้งานของ Requirement/SRS ปัจจุบันสำหรับ ENGSE601 โดยไฟล์หลักด้าน Requirement ต้องตรงกับ canonical source ใน ENGSE212 `Document/srs` บน branch `main`.

## Current synchronized documents

ไฟล์ต่อไปนี้ถูก sync จาก `/home/panuwat/project/Document/srs/` เมื่อ 2026-09-22:

- `04_Requirement_Candidates.md` — Requirement Candidates ปัจจุบัน
- `05_Software_Requirement_Specification.md` — SRS v1.1 ปัจจุบัน
- `06_Requirement_Traceability.md` — Requirement Traceability ปัจจุบัน
- `07_Appendix_A_Full_Traceability_Matrix.md` — Full Traceability Matrix ปัจจุบัน

## Supplementary retained documents

ไฟล์ต่อไปนี้ไม่มีไฟล์ชื่อเดียวกันใน canonical `Document/srs` ปัจจุบัน จึงเก็บไว้เป็นข้อมูลประกอบเดิมและไม่ให้ override เอกสาร current ด้านบน:

- `01_Project_Overview.md`
- `02_Project_Scope.md`
- `03_Software_Architecture.md`
- `07_Appendix_B_Key_Design_Decisions.md`

## Usage rule

- W05 เป็นต้นไป ให้ใช้ไฟล์ current synchronized documents ในโฟลเดอร์นี้ หรือ canonical GitHub path เป็น Requirement/SRS authority
- ถ้า local mirror ขัดกับ canonical source ให้ยึด canonical source และ sync local mirror ใหม่
- ห้ามแก้ Requirement/SRS current เฉพาะใน ENGSE601 แล้วปล่อยให้ต่างจาก ENGSE212; การแก้ baseline ต้องทำที่ canonical source ก่อน แล้วจึง sync กลับมาที่นี่
- W01–W04 ยังคงอ้าง baseline ที่ใช้ในเวลาจัดทำตาม artifact/submission เดิม เพื่อรักษา historical traceability
