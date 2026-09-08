# AI Use Declaration

| รายการ | บันทึก |
|---|---|
| Week / artifact | Week 04 / SRS Review and RTM v1 (work/01-review-scope.md, 02-srs-review-log.md, 03-rtm-lite.csv, 04-gate-a-decision.md, 05-phase-2-entry-pack.md) |
| ใช้ AI หรือไม่ | Yes |
| เครื่องมือ/รุ่นเท่าที่ทราบ | opencode CLI (model: ox-alpha) |
| ใช้เพื่อ | ช่วยจัดโครงสร้าง Review Log: แปลง five-check findings ของ Week 03 เป็น RV-01 ถึง RV-16 พร้อม disposition, ร่าง RTM v1 จาก planned evidence ของ W03, ร่าง Gate A rationale ที่อ้าง Finding/RTM rows และจัด Phase 2 Entry Pack |
| Input ที่ให้ AI | ไฟล์ใน repository: INPUTS/requirements-srs/05_Software_Requirement_Specification.md v1.0 (อ่านครบ), WEEKS/week-03/work/critical-requirement-review.md (REQ-01 ถึง REQ-05 + Q-01 ถึง Q-06), WEEKS/week-01/work/quality-risk-cards.md, WEEKS/week-02/work/project-quality-route-map.md, PROJECT.md, TEAM.md, INPUTS/design/ (C3/C4-code-Diagram, design_mobile.md, admin_design.md — ผ่านการอ้างอิงใน W03) และ template ของ week-04 |
| การปกป้องข้อมูล | ไม่ได้ส่งรหัสผ่าน, token, secret หรือข้อมูลส่วนบุคคลเพิ่มนอกจากชื่อสมาชิกที่เปิดเผยอยู่แล้วใน TEAM.md/repository public |
| ข้อเสนอที่ Accepted | 1) การ map five-check ของ W03 เป็น finding IDs RV-01 ถึง RV-16 ต่อ requirement/lens 2) การคง disposition = Deferred สำหรับทุก finding ที่ผูกกับ Q-01 ถึง Q-06 (ไม่ถือเป็น decision จนกว่า owner ยืนยัน) 3) Gate A = Conditional พร้อม conditions GA-01 ถึง GA-06 4) RTM status vocabulary ตาม guide (Planned/Not Ready ฯลฯ) โดยไม่มี actual result ปลอม |
| ข้อเสนอที่ Modified | 1) จำนวน findings ปรับจากการรวมข้อที่ซ้ำกัน (เช่น signed URL ambiguity + inconsistency รวมเป็น RV-09) 2) row ID ของ RTM ถูก fix ให้ตรงลำดับ CSV จริง R1 ถึง R10 หลังตรวจทาน 3) REQ-04 fallback trigger/REQ-02 composition ถูกระบุเป็น "propose/assumption" ไม่ใช่ค่าตัดสิน |
| ข้อเสนอที่ Rejected | ข้อเสนอให้ตั้ง threshold ตัวอย่าง (เช่น forgery >= 50) ลงใน AC-R1 — rejected เพราะยังเป็น open decision Q-01a ห้ามสร้าง acceptance basis ใหม่แทน owner |
| วิธีตรวจสอบกับ artifact/owner จริง | 1) อ่าน SRS v1.0 ครบทุก section และเทียบ location (Sec 2.3/2.4/2.6/3) ของทุก RV 2) ตรวจว่า evidence ทุก finding ชี้ไฟล์จริง (admin_design.md line 420, C3/C4-code-Diagram, design_mobile.md) ตามที่ W03 อ้างไว้ 3) นับ RTM rows ให้ตรง 10 แถวก่อนอ้างใน Gate A 4) ตรวจว่า Evidence_Status ใน CSV ไม่มี Existing สำหรับ artifact ทดสอบที่ยังไม่มีจริง |
| Verification owner/date | ภานุวัฒน์ / 2026-08-25 |

คำยืนยัน: ทีมไม่ได้ใช้ AI สร้าง stakeholder decision, approval, ผลทดสอบ, log หรือ screenshot ที่ไม่ได้ดำเนินการจริง — ทุก open question ยังเป็น "open", ทุก Evidence Status เป็น Planned/Not Ready ตามความจริง ณ วันที่จัดทำ และ reviewer sign-off ยังว่างจริง
