# W04-04 — Quality Gate A Decision

## Evidence reviewed

- SRS/Requirement version: `INPUTS/requirements-srs/05_Software_Requirement_Specification.md` v1.0 (IN-02) + W03 revised wording proposals (ยังไม่เป็น SRS v1.1)
- W03-OUT: `WEEKS/week-03/submission/W03_ScamGuard_Revised-Critical-Requirements_v1.pdf` (tag w03-submission-v1, commit f001906)
- Review Log: `02-srs-review-log.md` (RV-01 ถึง RV-16, session 2026-08-25)
- RTM v1: `03-rtm-lite.csv` (R1 ถึง R10)
- Reviewers/decision owner/date: เอกพันธ์ (Peer Reviewer — รอ sign-off), ภานุวัฒน์ (Requirement owner/Decision owner) / 2026-08-25

## Decision

เลือกเพียงหนึ่งสถานะ

- [ ] `Ready` — ไม่มี unresolved critical issue; critical requirements มี acceptance basis และ trace เพียงพอสำหรับ Phase 2
- [x] `Conditional` — ไปต่อเฉพาะส่วนที่ระบุ พร้อม conditions, owner และ due
- [ ] `Not Ready` — ยังมี blocker ที่ทำให้ test/design basis สำคัญตัดสินไม่ได้

## Evidence-based rationale

- ไม่ใช่ `Ready`: ยังมี open decision 6 ข้อ (Q-01 ถึง Q-06 จาก W03) และ finding ระดับ Critical ที่ยัง unresolved คือ RV-08 — FR-XAI-01 infeasible ตาม method เดิม (Grad-CAM + ONNX Runtime + SegFormer) ทำให้ REQ-03 = Not Ready (RTM rows R5, R6) และ RV-02/RV-07 ที่ block การออกแบบ test case/dataset ของ REQ-01/REQ-02
- ไม่ใช่ `Not Ready`: 4 ใน 5 requirements มี acceptance basis ที่ตัดสินผ่าน–ไม่ผ่านได้แล้ว (AC-R1, AC-R2, AC-R4, AC-R5 ตรวจ re-check แล้วใน Review Log) โดยส่วนที่เหลือของแต่ละข้อถูกระบุเป็น placeholder ที่อ้าง Q-ID ชัดเจน และ RTM v1 trace ไปข้างหน้า (requirement → planned evidence) และย้อนกลับ (planned evidence → requirement/risk) ได้ทุกแถวโดยไม่มี actual result ปลอม
- การไปต่อของ Phase 2 จึงผูกเงื่อนไขตามตารางด้านล่าง — ห้ามเลื่อนสถานะเป็น `Ready` จนกว่า GA-01 ถึง GA-06 จะปิดพร้อม re-check evidence

## Conditions / blockers / actions

| ID | Condition or blocker | Affected requirement / Phase 2 work | Action | Owner | Due | Re-check evidence |
|---|---|---|---|---|---|---|
| GA-01 | Q-01: decision threshold ต่อภาพ (forgery/AI-Gen) + scope AI generators | REQ-01; W05 Component Test Case Set, W08 boundary partitions | ตัดสิน Q-01a/b แล้วอัปเดต AC-R1-02/AC-R1-03 และ SRS v1.1 | ภานุวัฒน์ | Week 05 | Decision record + revised AC (RTM rows R1, R3) |
| GA-02 | Q-02: composition ของ Testing Set 1,000 ภาพ | REQ-02; W07/W08 dataset evaluation design, W10 Test Data Sheet | กำหนดสัดส่วน real/fake + ประเภท forgery แล้วจัดทำ Dataset specification | ภานุวัฒน์ | ก่อน curate Testing Set | Dataset spec document (RTM rows R2, R4) |
| GA-03 | Q-03: XAI method compatible กับ ONNX Runtime + SegFormer / no-region behavior / signed URL | REQ-03 (Not Ready); W05 implementation start, W06 Integration design | เลือกวิธี XAI (เช่น attention-based/integrated gradients/XAI ฝั่ง PyTorch pre-export) และตัดสิน Q-03b/c | ภานุวัฒน์ (+ฝั่ง model) | Week 05 | Feasibility note + revised AC-R3 (RTM rows R5, R6) |
| GA-04 | Q-04: retention/access control ของไฟล์ heatmap | REQ-03, C-04; W07 UAT scenario, admin flow | กำหนด data retention policy ของ object storage lifecycle | ภานุวัฒน์ | ก่อน implement object storage lifecycle | Policy record (RTM row R5) |
| GA-05 | Q-05: measurement conditions ของ NFR-01 (n, environment, concurrency) + CPU fallback trigger | REQ-04; W11 NFR Test Outline, load test script design | ยืนยัน baseline conditions (propose: single-user, n >= 100, T4, health-check fail > 30s) ใน SRS v1.1 | ภานุวัฒน์ | Week 05 (ใช้จริงก่อน W11) | Measurement condition spec (RTM rows R7, R8) |
| GA-06 | Q-06: retroactive handling เมื่อถอน Research Consent | REQ-05, FR-ADMIN-02; W06/W07 admin approve flow + UAT | ปรึกษาอาจารย์ที่ปรึกษา ตัดสิน delete-vs-going-forward แล้วอัปเดต AC-R5-03 | ภานุวัฒน์ + อาจารย์ที่ปรึกษา | ก่อน implement admin approve flow | PDPA decision record (RTM row R10) |

## Sign-off

- Requirement owner/representative: ภานุวัฒน์ / 2026-08-25 (Review Log + RTM ฉบับนี้)
- Reviewer: [รอ review — เอกพันธ์ ต้องตรวจตาม Team Working Agreement ก่อน merge]
- Team: ภานุวัฒน์ / 2026-08-25

Sign-off นี้เป็นบันทึกการทบทวนในรายวิชา ไม่ใช่การอนุมัติจาก stakeholder ภายนอก (ST02 ศูนย์ชัวร์ก่อนแชร์ ยังไม่ได้ยืนยันข้อกำหนดใด ๆ)
