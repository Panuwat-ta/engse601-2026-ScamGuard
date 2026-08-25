# AI Use Declaration

| รายการ | บันทึก |
|---|---|
| Week / artifact | Week 02 / Project Quality Route Map (project-quality-route-map.md) |
| ใช้ AI หรือไม่ | Yes |
| เครื่องมือ/รุ่นเท่าที่ทราบ | Antigravity IDE (Claude Opus 4.6 Thinking) |
| ใช้เพื่อ | ช่วยร่างเนื้อหา Project Quality Route Map โดยอ้างอิงจาก SRS v1.0, Architecture docs, และ source code จริง: กำหนด V&V question, evidence + status, decision, owner ในแต่ละ Gate (A-D), feedback loop, evidence gap |
| Input ที่ให้ AI | สรุปเนื้อหาจาก 05_Software_Requirement_Specification.md v1.0 (FR-ANALYSIS-02 AC-1 ถึง AC-5, NFR-05), PROJECT.md (Critical Context C-01), TEAM.md, quality-risk-cards.md (QR-01), Architecture docs (03_Software_Architecture.md), source code structure (server/app/services/inference_service.py, onnx_worker.py, model/segformer/) |
| การปกป้องข้อมูล | ไม่ได้ส่งรหัสผ่าน, token, secret, หรือข้อมูลส่วนบุคคลอื่นนอกเหนือจากชื่อสมาชิกที่เปิดเผยอยู่แล้วใน repository; ไม่ได้ส่งไฟล์ .env หรือ credential ใด |
| ข้อเสนอที่ Accepted | 1. การเลือก QR-01 (AI Model Accuracy / FR-ANALYSIS-02) เป็น critical slice ตาม Team conclusion จาก Week 01 2. โครงสร้าง V&V question ที่เจาะจงตาม AC ของ FR-ANALYSIS-02 3. การกำหนด evidence status ตามสถานะจริง (Existing/Planned/Not Ready) 4. Feedback loop กรณี Accuracy/F1 < 85% |
| ข้อเสนอที่ Modified | 1. ปรับ evidence references ให้ชี้ไปยัง path จริงใน project repo (server/app/services/, model/segformer/) 2. เพิ่มรายละเอียด evidence gap โดยอ้างอิง dataset preparation scripts ที่มีจริง (prepare_dataset_splicing.py, prepare_dataset_imd2020.py) 3. ปรับ Gate B status จาก Not Ready เป็น Conditional เนื่องจาก Architecture doc และ Design doc มีอยู่จริงแล้ว |
| ข้อเสนอที่ Rejected | ไม่มี |
| วิธีตรวจสอบกับ artifact/owner จริง | 1. ตรวจ FR-ANALYSIS-02 AC-1 ถึง AC-5 ว่าตรงกับ SRS v1.0 2. ตรวจ evidence path (inference_service.py, onnx_worker.py, model/segformer/) ว่ามีไฟล์จริงใน project repo 3. ตรวจ architecture docs ว่ามี C3/C4 diagram ที่ครอบคลุม AI Inference Container 4. ตรวจ evidence status ว่าตรงกับสถานะจริง (ยังไม่มี trained model, ยังไม่มี test results) |
| ผู้รับผิดชอบการตรวจ | Panuwat Takham |
| วันที่ตรวจ | 2026-08-25 |

คำยืนยัน: ทีมไม่ได้ใช้ AI สร้างผลทดสอบ, log, screenshot, approval, stakeholder decision หรือหลักฐานที่ไม่ได้ดำเนินการจริง
