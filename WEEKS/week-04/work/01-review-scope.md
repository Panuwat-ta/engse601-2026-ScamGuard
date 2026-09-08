# W04-01 — Review Scope and Preparation

| Field | Team record |
|---|---|
| Project/team | ScamGuard — แอปตรวจสอบรูปภาพตัดต่อที่ถูกนำมาหลอกลวง (Scam Image Detection Application) |
| SRS/Requirement source + version/commit | `INPUTS/requirements-srs/05_Software_Requirement_Specification.md` v1.0 (August 23, 2026) — baseline ตาม `INPUTS/input-register.md` IN-02 (ยังไม่มี SRS v1.1 — ทุก revision จาก review นี้เป็น proposal รอตัดสิน) |
| Review date/session | 2026-08-25 (structured review session 1 รอบ ครอบคลุมทั้ง 5 requirements) |
| Critical slice / requirement IDs (3–5) | REQ-01 = FR-ANALYSIS-02 (Visual Analysis), REQ-02 = NFR-05 (Model Performance), REQ-03 = FR-XAI-01 (Heatmap), REQ-04 = NFR-01 (Response Time), REQ-05 = FR-PDPA-01 (Consent) — ตาม W03 handoff |
| Linked W01 risks / W02 route / W03 output | QR-01–QR-04 (`WEEKS/week-01/work/quality-risk-cards.md`), Gate A–D (`WEEKS/week-02/work/project-quality-route-map.md`), `WEEKS/week-03/submission/W03_ScamGuard_Revised-Critical-Requirements_v1.pdf` + `WEEKS/week-03/work/critical-requirement-review.md` |
| Author/Requirement owner | ภานุวัฒน์ (Primary Author/Artifact Owner) |
| Reviewer(s) | เอกพันธ์ (Peer Reviewer ตาม TEAM.md — ยังไม่ sign-off จนกว่าจะตรวจจริง) |
| Recorder/facilitator | ภานุวัฒน์ |
| Out of scope | FR/NFR นอก 5 ข้อข้างต้น (21 requirements), การเขียน SRS v1.1 ใหม่ทั้งเล่ม, design review แบบ formal ของ C2–C4, ผลการรัน test จริงทุกชนิด (ยังไม่มี actual result), UAT execution |

## Sources available

| Artifact | Path/URL + version | Status | How used in review |
|---|---|---|---|
| Proposal | `INPUTS/proposal/SE02-แบบเสนอหัวข้อโครงงานวิศวกรรม.pdf` v1.0 (IN-01, Draft) | Existing | ใช้เป็นบริบทปัญหา/ผู้ใช้ (ST01–ST03) เมื่อชี้นัยสำคัญของ finding — ยังไม่ใช่ approved baseline จึงไม่ใช้ตัดสิน acceptance basis |
| Requirement/SRS | `INPUTS/requirements-srs/05_Software_Requirement_Specification.md` v1.0 (IN-02) | Existing | Object of review — ตรวจ AC ของ FR-ANALYSIS-02 (Section 2.3), NFR-05 (Section 3), FR-XAI-01 (Section 2.4), NFR-01 (Section 3), FR-PDPA-01 (Section 2.6) ด้วย lens 7 ด้าน |
| W03-OUT | `WEEKS/week-03/submission/W03_ScamGuard_Revised-Critical-Requirements_v1.pdf` + `work/critical-requirement-review.md`, commit b794f10 → f001906 | Existing | Input หลัก: proposed revised wording, AC-R1-01 ถึง AC-R5-05 และ open questions Q-01 ถึง Q-06 ที่ต้องได้ disposition ใน review log ฉบับนี้ |
| Glossary/business rule | `PROJECT.md` Critical Context C-01 ถึง C-09 (2026-08-24, IN-05) | Existing | ใช้ยืนยันว่า requirement ตอบ risk/stakeholder ครบ (Traceable) และเทียบ business rule (เช่น visual_score ≥ 80 → High) |
| Design/interface notes | `INPUTS/design/` v1.0 (IN-03): C2/C3/C4-code-Diagram.md, design_mobile.md, admin_design.md | Existing | ใช้เป็นหลักฐาน feasibility/consistency (เช่น ONNX Runtime subprocess vs Grad-CAM, signed URL ใน admin_design.md line 420, HeatmapViewerScreen slider 0.0–1.0) |

## Review lenses ที่ใช้

Correct / Complete / Consistent / Clear / Feasible / Testable / Traceable — ตรวจทั้ง SRS AC เดิมและ revised wording + AC-R* ที่ propose ใน W03

## เกณฑ์การตัดสินของ session นี้

- Finding ทุกข้อต้องมี location/evidence ชี้ไฟล์+version จริง
- Proposed revision ที่ยังรอ owner decision (Q-01 ถึง Q-06) บันทึก disposition เป็น `Deferred` พร้อม owner/due — ห้ามถือว่าเป็น stakeholder decision
- Requirement status หลัง review: `Ready` / `Conditional` / `Not Ready`
