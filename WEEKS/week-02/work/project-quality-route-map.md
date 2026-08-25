# W02 Work -- Project Quality Route Map

## Context

- Project/team: ScamGuard
- Current SDLC status: Requirements/SRS (SRS v1.0 complete; HLD/Architecture drafted; Implementation in progress on server, model, mobile branches)
- Milestone/sprint/date: SegFormer model training in progress, Backend API partially implemented (FastAPI + ONNX Worker), Mobile app (Flutter) under development
- Critical requirement/feature/risk: C-01 / QR-01 -- AI Model Accuracy: Visual Analysis (FR-ANALYSIS-02, NFR-05: Accuracy/F1 >= 85%)
- Source/version: 05_Software_Requirement_Specification.md v1.0 (August 23, 2026)
- Authors/reviewer: Panuwat Takham / Ekkphan Thotsatisangsan

## Route Map -- one critical slice

| Phase / Gate | V&V question | Evidence + status | Decision / feedback | Owner / when |
|---|---|---|---|---|
| Requirements/SRS -- Gate A | FR-ANALYSIS-02 ระบุ AC ครบ 5 ข้อ (Splicing detection, AI-Gen detection, Visual Risk Score calculation, True negative, Inference time) และมี acceptance basis ที่วัดได้ (Accuracy/F1 >= 85%, Inference <= 10s) หรือไม่ | SRS v1.0 Section 2.3 FR-ANALYSIS-02 AC-1 ถึง AC-5 + NFR-05 (Model Performance) -- **Existing** | Pass -- AC มี Input/Processing/Expected Output ครบทุกข้อ, เป้า 85% มี metric ชัด (Accuracy, Precision, Recall, F1) บน Testing Set 1,000 ภาพ (50% real / 50% fake) | Panuwat / 2026-08-23 (SRS v1.0 approved) |
| HLD/Detail Design -- Gate B | Architecture/Design ระบุ pipeline สำหรับ Visual Analysis (ELA Preprocessing -> PSCC-Net + SegFormer -> ONNX Runtime -> Heatmap -> visual_score) อย่างชัดเจนหรือไม่ และ trace กลับไป FR-ANALYSIS-02 ได้หรือไม่ | Software Architecture v1.0 Section 4 (C3 Component Diagram: AI Inference Container) + design/model.md (SegFormer architecture, ONNX pipeline, Risk Score formula) + design/server.md (API endpoint /scan) -- **Existing** | Conditional -- Design documents อธิบาย pipeline ได้ชัด แต่ยังไม่มี formal design review record; Trace จาก FR-ANALYSIS-02 -> AI Inference Container -> SegFormer Model มีอยู่ใน Architecture doc | Panuwat / 2026-08-24 (design doc drafted) |
| Implement/Build -- Gate C | Source code ของ inference pipeline (onnx_worker.py, inference_service.py) implement ELA + SegFormer + Heatmap generation ตรงตาม design หรือไม่ และ ONNX model file ตรงกับ version ที่ train หรือไม่ | server/app/services/inference_service.py (OCR + ONNX subprocess call), server/app/services/onnx_worker.py (Tiled Inference 512x512, ONNX Runtime), model/segformer/ (training scripts, configs, export_onnx.sh) -- **Planned** (code exists แต่ยังไม่ผ่าน integration test กับ production model) | Block -- onnx_worker.py มี tiled inference logic แต่ model .onnx file ยังอยู่ระหว่าง training; ต้องรอ model export เสร็จจึงจะทดสอบ end-to-end ได้ | Panuwat / target: model training completion |
| Test/Defect -- Gate C | มี test case, test data, และผลทดสอบที่ตอบ risk (Accuracy/F1 >= 85% บน 1,000 ภาพ) หรือไม่ และมี Confusion Matrix, Classification Report ที่วัดได้จริงหรือไม่ | Planned test cases: (1) Model evaluation report (Confusion Matrix, Classification Report) บน Testing Set 1,000 ภาพ (50/50 real/fake), (2) AC-1 ถึง AC-5 functional test สำหรับ FR-ANALYSIS-02, (3) Inference time benchmark (<= 10s/image on GPU) -- **Not Ready** | Not Executed -- ยังไม่มี trained model ที่พร้อม evaluate; Testing Set ยังไม่ถูกจัดเตรียมครบ; ต้องรอ Gate C (Implement) ผ่านก่อน | Panuwat / target: หลัง model training + dataset preparation |
| Release/Portfolio -- Gate D | มี evidence pack (model evaluation report, test results, inference benchmark) ครบถ้วนพอสำหรับการตัดสินใจ deploy model version นี้สู่ production หรือไม่ และ residual risk (False Negative/False Positive rate) อยู่ในระดับที่ยอมรับได้หรือไม่ | Evidence pack: Model evaluation report + AC test results + Load test report + UAT scenario results -- **Not Ready** | Not Accept (ยังไม่พร้อมตัดสิน) -- ต้องรอผลจาก Gate C (Test/Defect) ทั้งหมดก่อน; หาก F1 < 85% ต้อง retrain หรือปรับ threshold | Panuwat / target: ก่อน release cycle |

## Feedback loop

| Trigger/finding | ย้อนกลับไปแก้ artifact ใด | Evidence ที่ต้องอัปเดต | Owner/when |
|---|---|---|---|
| Model evaluation ได้ Accuracy/F1 < 85% ใน Gate C (Test/Defect) | (1) กลับไป retrain model ด้วย dataset ที่ปรับปรุง (เพิ่ม augmentation, เพิ่มข้อมูล splicing/inpainting) -- แก้ Gate C (Implement), (2) ทบทวน preprocessing pipeline (ELA parameters, tile size/overlap) -- แก้ Gate B (Design) | Model evaluation report (Confusion Matrix ใหม่), Training log/config ที่ปรับปรุง, ONNX model file version ใหม่ | Panuwat / ทันทีที่พบว่า metric ต่ำกว่าเป้า |
| Inference time เกิน 10 วินาที/ภาพ บน GPU (NVIDIA T4) | (1) ปรับ tile_size/overlap ใน onnx_worker.py -- แก้ Gate C (Implement), (2) พิจารณา model quantization หรือลดขนาด input -- แก้ Gate B (Design) | Inference benchmark report ใหม่, onnx_worker.py commit ที่ปรับปรุง | Panuwat / ทันทีที่พบจาก benchmark |

## Evidence gap and next action

| Gap / Not Ready item | Why | Next action | Owner | Target milestone |
|---|---|---|---|---|
| Model evaluation report (Confusion Matrix, Classification Report) | SegFormer model ยังอยู่ระหว่าง training; ยังไม่มี final .onnx model ที่พร้อม evaluate | รอ model training เสร็จ -> export ONNX -> run evaluation script บน Testing Set 1,000 ภาพ | Panuwat | Model training completion |
| Testing Set 1,000 ภาพ (50% real / 50% fake) | Dataset preparation scripts มีอยู่ (prepare_dataset_splicing.py, prepare_dataset_imd2020.py, prepare_dataset_face.py, prepare_dataset_inpainting.py) แต่ยังไม่ได้ curate testing set แยกออกมา | จัดเตรียม Testing Set แยกจาก Training Set พร้อม ground-truth labels | Panuwat | ก่อน model evaluation |
| Integration test: end-to-end scan flow | inference_service.py + onnx_worker.py ยังไม่ได้ทดสอบกับ production model | Deploy model -> run integration test ผ่าน /scan API endpoint | Panuwat | หลัง model export |
| Design review record | Architecture/Design doc มีอยู่แต่ยังไม่มี formal review | จัดทำ design review checklist และบันทึกผล review | Panuwat, Ekkphan | ก่อนเริ่ม intensive testing |

## Peer review and handoff

- Reviewer + date/commit: Ekkphan Thotsatisangsan / [รอ review]
- Revision made: [รอ review]
- Requirement IDs ที่จะเข้า Week 03: FR-ANALYSIS-02 (Visual Analysis), NFR-05 (Model Performance >= 85%), FR-XAI-01 (Grad-CAM Heatmap)
- AI Use Declaration: WEEKS/week-02/work/ai-use-declaration.md
