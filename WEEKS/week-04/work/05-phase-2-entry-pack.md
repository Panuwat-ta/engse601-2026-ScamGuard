# W04-05 — Phase 2 Entry Pack (Week 05–08)

อ้างอิง RTM v1 (`03-rtm-lite.csv` rows R1 ถึง R10) และ Gate A = `Conditional`

| Phase 2 week | Candidate scope from RTM | Input/evidence ready now | Conditional / Not Ready item | Owner/next action | Entry status |
|---:|---|---|---|---|---|
| 05 Component/Unit Testing | REQ-01 visual_score formula + risk grade rules (R1), REQ-05 consent endpoints (R9) | AC-R1-01 ถึง AC-R1-04, AC-R5-01 ถึง AC-R5-05 ตัดสินได้; business rule 0.6/0.4 + Special Rule visual_score >= 80 ประกาศแล้วใน revised wording | AC-R1-02/AC-R1-03 ยังเป็น placeholder รอ Q-01 threshold (GA-01); AC-R5-03 ส่วน retroactive รอ Q-06 (GA-06) | ภานุวัฒน์ / ตัดสิน Q-01 ก่อนจัดทำ Component Test Case Set | Conditional |
| 06 Integration Testing | REQ-03 heatmap generation + signed URL (R5), REQ-04 fallback chain Google Vision/CPU mode (R8) | API contract จาก SRS v1.0 + design C3/C4-code-Diagram; signed URL pattern มี precedent ใน admin_design.md line 420 | REQ-03 ทั้งข้อ Not Ready — Q-03a XAI method ยังไม่ตัดสิน (GA-03); fallback trigger รอ Q-05 (GA-05) | ภานุวัฒน์ (+ฝั่ง model) / เลือกวิธี XAI ภายใน Week 05 | Conditional |
| 07 System/UAT | End-to-end journey อัปโหลด -> ผลวิเคราะห์ -> heatmap -> consent audit (R2, R7, R10) | User journey ครบจาก SRS v1.0 Sec 2.2-2.6 + stakeholder basis ST01-ST03 | Dataset evaluation (R2) ยังไม่มี model/dataset (GA-02); performance baseline (R7) ยังไม่มี backend พร้อม + Q-05 | ภานุวัฒน์ / ร่าง UAT scenario บน journey ที่ไม่ผูกกับ open decision ก่อน | Conditional |
| 08 Test Design Techniques | Equivalence/boundary ของ scores (risk_grade 39/40, 69/70, Special Rule >= 80), opacity slider 0%/50%/100%, file size/type limits (R1, R6) | กฎการให้ grade ชัดเจนจาก FR-ANALYSIS-04 AC-1 ถึง AC-6; UI boundary จาก design_mobile.md HeatmapViewerScreen | Partition ของ confidence thresholds (forgery/AI-Gen) รอ Q-01 (GA-01); no-region case รอ Q-03b | ภานุวัฒน์ + เอกพันธ์ / เริ่มจากกฎที่ fix แล้ว (grade/score/slider) | Conditional |

## Priority handoff

- Critical slice ที่ควร trace ต่อก่อน: REQ-01 (FR-ANALYSIS-02) — visual_score chain จาก component test (R1) ไป dataset evaluation (R2) เพราะเป็น Gate A/B/C ของ W02 Route Map และมี finding Critical (RV-01) ที่แก้แล้วต้องคง re-check ไว้
- Requirement/AC ที่พร้อมที่สุด: REQ-05 (FR-PDPA-01) AC-R5-01 ถึง AC-R5-05 — ไม่มี dependency กับ model training และ RV-15/RV-16 re-check ผ่านแล้ว (ยกเว้นส่วน retroactive ของ Q-06)
- Open decision ที่เสี่ยง block หลายสัปดาห์: Q-03a (XAI method) — ถ้าไม่ตัดสินภายใน Week 05 จะ block implementation + integration test ของ FR-XAI-01 ทั้ง feature (RTM R5/R6) และกระทบ UAT ใน Week 07; รองลงมาคือ Q-01 ซึ่ง block W05 test case set
- สิ่งที่ ENGSE212 ต้องทบทวน/อัปเดต: ออก SRS v1.1 รวม revised wording ของ REQ-01 ถึง REQ-05 + business rule น้ำหนัก 0.6/0.4 + consent_logs schema เพิ่ม updated_at + แยก measurement basis ของ NFR-01/NFR-02; ปรับ design_mobile.md/admin_design.md ให้ยืนยัน signed URL เป็นมาตรฐานเดียว
- AI Use Declaration: `WEEKS/week-04/work/ai-use-declaration.md`
