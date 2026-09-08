# W03 Peer Review, Revision and AI Record

## Peer review

- Draft commit/version: b794f10
- Author(s): ภานุวัฒน์ ต๋าคำ (Panuwat Takham)
- Reviewer(s): เอกพันธ์ ทศทิศรังสรรค์ — **[รอ review — ต้องขอ review ก่อนกำหนดส่งอย่างน้อย 24 ชั่วโมง ตาม Team Working Agreement]**
- Date: [รอ review]

| Finding ID | Requirement/AC location | Finding/question | Disposition | Revision made / open action | Owner | Re-check |
|---|---|---|---|---|---|---|
| [รอ reviewer เพิ่มแถวจริง] | — | — | — | — | — | — |

> ห้ามเติม finding/disposition แทน reviewer — ให้เอกพันธ์ตรวจตาม Definition of Done แล้วบันทึกในตารางนี้

## Author pre-check (ตรวจก่อนส่ง review)

| Check | Result |
|---|---|
| ทุก requirement trace ไป SRS ID/version/location ได้ | ผ่าน — REQ-01–REQ-05 อ้าง Section 2.3, 2.4, 2.6, 3 ของ SRS v1.0 และ RC-XXX source ทุกข้อ |
| Original text ถูกคัดลอกโดยไม่แก้ต้นฉบับ | ผ่าน — original สรุปจาก SRS v1.0 เท่านั้น revision อยู่ในหมวด C แยกชัด |
| Five-check ครบ 5 ด้านต่อ requirement | ผ่าน — ทุก requirement มีตาราง Clear/Complete/Consistent/Feasible/Testable |
| AC ตัดสินผ่าน–ไม่ผ่านได้ ไม่ทวน requirement | ผ่าน — ทุก AC มี Input/Event/Observable result และ threshold หรือ behavior ที่วัดได้ |
| มี normal และ negative/boundary ตาม risk | ผ่าน — REQ-01 (2N/1Neg/1B), REQ-02 (2N/2Neg+process), REQ-03 (2N/1Neg/1B/1Sec), REQ-04 (2N/1B/1Neg), REQ-05 (2N/2Neg/1Audit) |
| ไม่มีผลทดสอบ/log/approval ที่แต่งขึ้น | ผ่าน — evidence status ทุกข้อ = Not Ready ตามความจริง, reviewer field ว่างจริง |
| Open question มี owner + due | ผม — Q-01 ถึง Q-06 ครบทั้ง owner และ decision point |

## Revision note

- จาก draft → revision commit/version: [ระบุหลัง peer review เสร็จ]
- เปลี่ยนอะไรและเพราะอะไร: [รอผล review]
- ยังมี open issue ใด: Q-01 ถึง Q-06 (critical-requirement-review.md หมวด Consolidated open questions)
- Reviewer re-check result: [รอ review — Ready / Conditional / Revise]

## AI Use Declaration

| รายการ | บันทึก |
|---|---|
| Week / artifact | Week 03 / Revised Critical Requirements (work/critical-requirement-review.md) |
| ใช้ AI หรือไม่ | Yes |
| เครื่องมือ/รุ่นเท่าที่ทราบ | opencode CLI (model: ox-alpha) |
| ใช้เพื่อ | ช่วยวิเคราะห์ requirement 5 ข้อจาก SRS v1.0 จริง: รัน Five-check, เสนอ revised wording, ร่าง Acceptance Criteria และจัดกลุ่ม open questions |
| Input ที่ให้ AI | ไฟล์ใน repository: INPUTS/requirements-srs/05_Software_Requirement_Specification.md v1.0, PROJECT.md, TEAM.md, INPUTS/design/ (C2/C3/C4-code-Diagram, design_mobile.md, admin_design.md), WEEKS/week-01/work/, WEEKS/week-02/work/, WEEKS/week-03/README.md และ template |
| การปกป้องข้อมูล | ไม่ได้ส่งรหัสผ่าน, token, secret หรือข้อมูลส่วนบุคคลเพิ่มนอกจากชื่อสมาชิกที่เปิดเผยอยู่แล้วใน TEAM.md/repository public |
| ข้อเสนอที่ Accepted | 1) การเลือก 5 requirements ตาม W02 handoff + Critical Context 2) การแยก metric ต่อภาพออกจาก dataset-level F1 (FR-ANALYSIS-02) 3) การจำกัด scope NFR-05 ไม่ครอบคลุม OCR 4) การเสนอ signed URL ให้ heatmap_url 5) โครง Q-01–Q-06 เป็น open question log |
| ข้อเสนอที่ Modified | 1) ค่า propose บางตัว (n ≥ 100 requests, health-check 30s, resolution 1920px) ปรับจากที่ AI เสนอให้เป็น "assumption ที่ยังไม่ใช่ decision" รอ Q-05/Q-03 2) สถานะ FR-XAI-01 ถูกปรับจาก Conditional เป็น Not Ready เพราะ feasibility finding มีหลักฐานจาก design docs ชัดเจน |
| ข้อเสนอที่ Rejected | ไม่มีข้อเสนอที่ถูกปฏิเสธทั้งหมด — ทุก finding ผ่านการ cross-check กับ SRS/design จริงก่อนรับ |
| วิธีตรวจสอบกับ artifact/owner จริง | 1) ตรวจทุก FR/NFR ID และเลข section กับ 05_Software_Requirement_Specification.md v1.0 2) ตรวจตัวเลข threshold (85%, 80%, 3s, 15s, 25s, 35s, 60s, 10s, 1,000 ภาพ, 0.6/0.4) กับ SRS 3) ตรวจ feasibility claim ของ Grad-CAM vs ONNX Runtime กับ C2-Container-Diagram.md (PyTorch / ONNX Runtime), C3-Component-Diagram.md (ONNX Worker subprocess) และ C4-code-Diagram.md 4) ตรวจ inconsistency ของ measurement basis กับ FR-SCAN-03/NFR-01/NFR-02 ต้นฉบับ 5) ตรวจ signed URL กับ admin_design.md line 420 |
| Verification owner/date | ภานุวัฒน์ ต๋าคำ / 2026-08-25 |

คำยืนยัน: ทีมไม่ได้ใช้ AI สร้าง stakeholder decision, approval, ผลทดสอบ, log หรือ screenshot ที่ไม่ได้ดำเนินการจริง — ทุก open question ยังเป็น "open" และทุก evidence status เป็นความจริง ณ วันที่จัดทำ
