# W03 Work — Critical Requirement Review

## Review scope

- Project/team: ScamGuard — แอปตรวจสอบรูปภาพตัดต่อที่ถูกนำมาหลอกลวง (Scam Image Detection Application)
- SRS/Requirement artifact + version/commit: `INPUTS/requirements-srs/05_Software_Requirement_Specification.md` v1.0 (August 23, 2026) — baseline ตาม `INPUTS/input-register.md` IN-02
- Critical slice / linked W01 risk / W02 route: W02 Route Map handoff ระบุ FR-ANALYSIS-02, NFR-05, FR-XAI-01; เพิ่ม NFR-01 (C-03/QR-03) และ FR-PDPA-01 (C-04/QR-04) ตามความเสี่ยงใน PROJECT.md Critical Context
- Authors: Panuwat Takham (Primary Author)
- Decision owner(s): ภานุวัฒน์ ต๋าคำ (หัวหน้าโครงงาน ตัดสินตาม Team Working Agreement)

> เลือก 5 requirements จาก 26 ข้อ (19 FR + 7 NFR) โดยยึด W02 handoff + Critical Context C-01–C-04 ไม่แก้ SRS ต้นฉบับ — ทุก revision จะถูก propose ผ่านเอกสารฉบับนี้และรอตัดสินใจก่อนอัปเดต SRS เป็น v1.1

---

## Requirement Record — REQ-01

### A. Source and risk

| Field | Record |
|---|---|
| Original Requirement ID | FR-ANALYSIS-02: Visual Analysis (Image Forgery + AI-Gen Detection) — Priority: Must |
| Original text | "ระบบต้องตรวจจับการตัดต่อและภาพ AI-Generated" พร้อม AC-1 ถึง AC-5 (Splicing → forgery_confidence: 85 และ "ความแม่นยำ ≥ 85% (F1-Score)"; AI-Gen จาก Stable Diffusion → ai_gen_confidence: 90; สูตร visual_score = forgery×0.6 + ai_gen×0.4; ภาพจริง → confidence ต่ำ; Inference ≤ 10s GPU) |
| Source/version/location | SRS v1.0, Section 2.3 (FR-ANALYSIS-02), อ้าง RC-ANALYSIS-02/03/04 |
| Linked risk/stakeholder | C-01 (PROJECT.md), QR-01 (W01), Gate A/B/C ของ W02 Route Map; ST01, ST02, ST03 |

### B. Lightweight review

| Check / issue type | Pass / Finding | Evidence, question or counterexample |
|---|---|---|
| Clear / unambiguous | Finding — Ambiguous | AC-1 Expected Output ผสม metric 2 ระดับในบรรทัดเดียว: `forgery_confidence: 85` คือค่า confidence ต่อภาพเดียว แต่ "ความแม่นยำ ≥ 85% (F1-Score)" เป็น metric ระดับ dataset ซึ่งวัดจากชุดภาพไม่ได้วัดจากภาพเดียว ทำให้ไม่ชัดว่าการทดสอบ 1 ครั้งตัดสินผ่าน/ไม่ผ่านด้วยเกณฑ์ใด |
| Complete | Finding — Incomplete | ไม่มี decision threshold: ไม่ระบุว่า forgery_confidence เท่าไรถือว่า "ตรวจจับสำเร็จ" (เช่น ≥ 50? ≥ 70?) counterexample: ภาพที่ได้ forgery_confidence = 60 ควรนับว่าตรวจพบหรือไม่ — ปัจจุบันตอบไม่ได้จาก SRS |
| Consistent | Pass (มีเงื่อนไข) | สูตรใน AC-3 (85×0.6)+(90×0.4)=87 และ AC-4 (10×0.6)+(5×0.4)=8 ถูกต้องทางคณิตศาสตร์และสอดคล้องกัน แต่น้ำหนัก 0.6/0.4 ปรากฏเฉพาะใน AC-3 ไม่เคยถูกประกาศเป็น business rule กลาง |
| Feasible | Pass (มีเงื่อนไข) | Pipeline ELA + PSCC-Net + SegFormer + ONNX feasible ตาม Design (C3-Component-Diagram: ONNX Worker) แต่ AC-2 ระบุ input เฉพาะ "Stable Diffusion" — ไม่ชัดว่า scope ครอบคลุม generator อื่น (Midjourney, GAN-based face swap) หรือทดสอบเฉพาะ Stable Diffusion |
| Testable / observable | Finding — Not Testable (ในรูปเดิม) | AC-1 ในรูปเดิมตัดสินไม่ได้เพราะรวม per-image output กับ dataset metric ไว้ด้วยกัน ต้องแยกเป็น (a) functional test ต่อภาพ กับ (b) evaluation test ระดับชุดข้อมูล จึงจะตัดสินผ่าน–ไม่ผ่านได้ |

### C. Revision and open decision

- Revised wording: **"เมื่อผู้ใช้อัปโหลดรูปภาพที่ผ่านการตรวจไฟล์ (FR-SCAN-02) ระบบต้องรัน Visual Analysis Pipeline (ELA Preprocessing → PSCC-Net + SegFormer → ONNX Runtime) และคืนค่าต่อภาพ: `forgery_confidence` (0–100), `ai_gen_confidence` (0–100) และ `visual_score = round(forgery_confidence×0.6 + ai_gen_confidence×0.4)` โดยน้ำหนัก 0.6/0.4 เป็น business rule ที่ประกาศกลาง และความแม่นยำระดับชุดข้อมูล (F1-Score ≥ 85%) ให้ย้ายไปวัดรวมที่ NFR-05 บน Testing Set ตามที่ NFR-05 กำหนด ส่วนการจัดระดับความเสี่ยงใช้ visual_score ผ่านกฎของ FR-ANALYSIS-04 (รวม Special Rule visual_score ≥ 80 → High)"**
- Assumption ที่ยังไม่ใช่ decision: น้ำหนัก 0.6/0.4 คงค่าเดิมตาม SRS; F1 ≥ 85% ย้ายไปวัดที่ NFR-05 เพื่อกำจัดการวัดซ้ำซ้อน
- Open question: Q-01 (a) decision threshold ต่อภาพที่ใช้แยก "ตรวจพบ/ไม่พบ" สำหรับ forgery และ AI-Gen คือเท่าไร (b) scope ของ AI generators ที่ใช้ทดสอบ AC AI-Gen — จำกัดที่ Stable Diffusion หรือต้องครอบคลุม generator อื่น
- Decision owner + due/decision point: ภานุวัฒน์ / ภายใน Week 05 (ก่อนจัดทำ Component Test Case Set) หรือก่อน model evaluation อย่างช้า
- Status: Conditional — revised wording ใช้ได้ทันที แต่ threshold/scope ต้องรอ Q-01

### D. Acceptance Criteria

| AC ID | Context/Input/State | Event/Rule | Observable expected result | Type/risk covered |
|---|---|---|---|---|
| AC-R1-01 | ภาพ splicing ที่รู้ ground truth (สอดแทรกวัตถุ/จำนวนเงินในสลิป) ผ่าน FR-SCAN-02 แล้ว | รัน pipeline เต็ม (ELA → PSCC-Net + SegFormer → ONNX) | Response มี `forgery_confidence` อยู่ในช่วง 0–100, `visual_score = round(forgery_confidence×0.6 + ai_gen_confidence×0.4)` ตรงสูตร (ยอมรับ rounding ±1) | Normal — QR-01 |
| AC-R1-02 | ภาพจริงที่ไม่ถูกแก้ไข (จากกล้องจริง ไม่ผ่าน generator) | รัน pipeline เต็ม | `forgery_confidence` และ `ai_gen_confidence` ต่ำกว่า decision threshold ตาม Q-01 และ `visual_score` ไม่ trigger Special Rule (< 80) | Negative/Boundary — ลด False Positive |
| AC-R1-03 | รูปภาพที่สร้างจาก Stable Diffusion (scope ตาม Q-01b) | รัน AI-Gen Detection Model | `ai_gen_confidence` สูงกว่า decision threshold ตาม Q-01 | Normal — QR-01 |
| AC-R1-04 | ภาพมาตรฐาน 1920×1080 บน GPU (NVIDIA T4) | รัน Visual Analysis วัดเวลา inference | เวลา inference ≤ 10 วินาที/ภาพ (เฉลี่ย n ≥ 20 runs) | Boundary/Performance — C-03 |

### E. Planned evidence

- Planned test level: Component (per-image functional test) + System (dataset evaluation ร่วมกับ NFR-05) + Review (threshold decision record)
- Planned evidence: 1) Test case results ของ AC-R1-01 ถึง AC-R1-04 2) Decision record ของ Q-01 (threshold + generator scope) 3) Dataset evaluation report (ร่วม REQ-02)
- Current status: Not Ready (ยังไม่มี trained model ที่ export แล้ว — ตาม W02 Gate C)
- Owner/next action: ภานุวัฒน์ / ตัดสิน Q-01 แล้วอัปเดต SRS เป็น v1.1 ก่อนเข้า W05

---

## Requirement Record — REQ-02

### A. Source and risk

| Field | Record |
|---|---|
| Original Requirement ID | NFR-05: Accuracy — Model Performance — Priority: Must |
| Original text | "โมเดล AI ต้องมีความแม่นยำ ≥ 85%" พร้อม AC-1 ถึง AC-4 (Accuracy/F1/Precision/Recall ≥ 85% บน Testing Set 1,000 ภาพ) |
| Source/version/location | SRS v1.0, Section 3 (NFR-05), อ้าง RC-NFR-06 |
| Linked risk/stakeholder | C-01 (PROJECT.md), QR-01 (W01), Gate A/D ของ W02 Route Map; ST01, ST02, ST03 |

### B. Lightweight review

| Check / issue type | Pass / Finding | Evidence, question or counterexample |
|---|---|---|
| Clear / unambiguous | Finding — Ambiguous | คำว่า "โมเดล AI" กว้างเกินไป — ระบบมีหลายโมเดล (OCR/Surya, Forgery Detection, AI-Gen Detection) ไม่ชัดว่าเป้า 85% ใช้กับตัวไหนบ้าง |
| Complete | Finding — Incomplete | Testing Set "1,000 ภาพ" ไม่ระบุ composition: สัดส่วน real/fake, ประเภท forgery (splicing/inpainting/AI-gen), แหล่ง dataset และวิธี split จาก Training Set — W01 QR-01 เคยใช้สมมติฐาน "50% real / 50% fake" ซึ่งยังไม่ใช่ข้อกำหนดใน SRS |
| Consistent | Finding — Inconsistent | ถ้าตีความ "โมเดล AI ทุกตัว" จะขัดกับ FR-ANALYSIS-01 ที่กำหนด OCR ภาษาไทย ≥ 80% (AC-1) และอังกฤษ ≥ 85% (AC-2) — OCR ไทยทำ 85% อาจ infeasible และเป็น target คนละตัว |
| Feasible | Pass (มีเงื่อนไข) | Training อยู่ระหว่างดำเนินการตาม W02 Route Map แต่ความเป็นไปได้ของ 85% ขึ้นกับ composition ของ testing set ที่ยังไม่ถูกกำหนด |
| Testable / observable | Pass | สูตร Accuracy/Precision/Recall/F1 ระบุชัดใน AC เดิม วัดได้จริงเมื่อ dataset spec สมบูรณ์ |

### C. Revision and open decision

- Revised wording: **"โมเดล Visual Analysis (Forgery Detection: PSCC-Net + SegFormer และ AI-Gen Detector) ต้องมี Accuracy, Precision, Recall และ F1-Score ≥ 85% เมื่อประเมินบน Testing Set 1,000 ภาพที่ hold-out จาก Training Set (composition รอตัดสินตาม Q-02) โดยข้อกำหนดนี้ไม่ครอบคลุม OCR ซึ่งใช้เป้าหมายแยกตาม FR-ANALYSIS-01 (ไทย ≥ 80%, อังกฤษ ≥ 85%) และ .onnx ที่ deploy ต้องเป็น artifact เดียวกับที่ evaluate (ตรวจด้วย hash/version)"**
- Assumption ที่ยังไม่ใช่ decision: คงเป้า 85% และจำนวน 1,000 ภาพเดิม; เพิ่มเงื่อนไข version-consistency เพื่อปิดช่องที่ deploy model ต่างจากที่ evaluate (verification question ข้อ 3 ของ QR-01)
- Open question: Q-02 composition ของ Testing Set — สัดส่วน real/fake และสัดส่วนประเภท forgery (splicing / inpainting / AI-generated / face) ที่จะใช้เป็นเกณฑ์ทางการ
- Decision owner + due/decision point: ภานุวัฒน์ / ก่อน curate Testing Set (W02 gap item) และก่อน W05
- Status: Conditional — metrics พร้อมใช้ เหลือรอ Q-02 เท่านั้น

### D. Acceptance Criteria

| AC ID | Context/Input/State | Event/Rule | Observable expected result | Type/risk covered |
|---|---|---|---|---|
| AC-R2-01 | Testing Set 1,000 ภาพ (hold-out, composition ตาม Q-02) ที่มี ground-truth label | รัน evaluation script กับ .onnx artifact ที่ deploy | Accuracy ≥ 85% พร้อม Confusion Matrix และ Classification Report ที่วัดได้จริง | Normal — QR-01 |
| AC-R2-02 | Testing Set เดียวกับ AC-R2-01 | คำนวณ F1 = 2×(P×R)/(P+R) | F1-Score ≥ 85% | Normal — QR-01 |
| AC-R2-03 | กลุ่มภาพจริงใน Testing Set | นับ FP (ภาพจริงถูกตัดสินว่าปลอม) | Precision ≥ 85% | Negative/Boundary — ลด False Positive |
| AC-R2-04 | กลุ่มภาพปลอมใน Testing Set | นับ FN (ภาพปลอมถูกตัดสินว่าจริง) | Recall ≥ 85% | Negative/Boundary — ลด False Negative (ผลกระทบทรัพย์สินผู้ใช้) |
| AC-R2-05 | ไฟล์ .onnx ที่ deploy บน production/worker | เทียบ hash/version กับ artifact ที่ใช้ evaluate | ตรงกัน 100% หากไม่ตรง ให้ผล evaluation ไม่มีผลตัดสิน | Process/Negative — ปิดช่อง version mismatch |

### E. Planned evidence

- Planned test level: System (model evaluation) + Review (version/hash check)
- Planned evidence: 1) Model evaluation report (Confusion Matrix, Classification Report) บน Testing Set 2) Dataset specification document ที่ตอบ Q-02 3) Hash comparison record ของ .onnx
- Current status: Not Ready (model training ยังไม่เสร็จ, Testing Set ยังไม่ curate — ตาม W02 Evidence gap)
- Owner/next action: ภานุวัฒน์ / ตัดสิน Q-02 → curate Testing Set → evaluate หลัง training เสร็จ

---

## Requirement Record — REQ-03

### A. Source and risk

| Field | Record |
|---|---|
| Original Requirement ID | FR-XAI-01: Grad-CAM Heatmap Generation & Display — Priority: Must |
| Original text | "ระบบต้องสร้างและแสดงแผนที่ความร้อน" พร้อม AC-1 ถึง AC-5 (Grad-CAM → heatmap.jpg → Object Storage → heatmap_url; Overlay + Toggle + Opacity Slider 0–100%; Risk Breakdown gauge/bars) |
| Source/version/location | SRS v1.0, Section 2.4 (FR-XAI-01), อ้าง RC-XAI-01/02/03 |
| Linked risk/stakeholder | C-02, C-08 (PROJECT.md), QR-02 (W01), Gate B ของ W02 Route Map; ST01, ST03 |

### B. Lightweight review

| Check / issue type | Pass / Finding | Evidence, question or counterexample |
|---|---|---|
| Clear / unambiguous | Finding — Ambiguous | AC-1 expected output `heatmap_url: "https://storage/scan_id/heatmap.jpg"` ไม่ชัดว่าเป็น literal pattern หรือตัวอย่าง และไม่ระบุ access control ของไฟล์ — admin_design.md (line 420) ใช้ signed URL (`?token=...`) ต่างจาก SRS ที่เขียน URL ตรง ๆ |
| Complete | Finding — Incomplete | ไม่มี negative case: เมื่อ visual analysis ไม่พบบริเวณเสี่ยง (confidence ต่ำ) heatmap ควรแสดงอย่างไร (ไม่สร้าง? neutral?) และไม่ระบุ format/resolution ของ heatmap.jpg |
| Consistent | Finding — Inconsistent | SRS ระบุ method ว่า "Grad-CAM" ตรง ๆ ขณะที่ design (C2/C3/C4-code-Diagram) รัน inference ผ่าน ONNX Runtime แบบ subprocess — ข้อมูล 2 แหล่งไม่ขัดกันโดยตรงแต่ยังไม่พิสูจน์ว่าทำได้จริงร่วมกัน (ดูข้อ Feasible) |
| Feasible | Finding — Infeasible (ตาม method ที่ระบุ) | Grad-CAM ต้องเข้าถึง gradient ของโมเดล แต่ (1) ONNX Runtime สำหรับ inference ทั่วไปไม่ expose gradient และ (2) SegFormer เป็น transformer architecture ที่ Grad-CAM แบบ CNN classic (target conv feature map) ใช้ตรง ๆ ไม่ได้ ต้องเลือก alternative (attention map / attention rollout / integrated gradients / CAM head แยก) หรือรัน XAI ฝั่ง PyTorch ก่อน export |
| Testable / observable | Pass (UI controls) | Toggle On/Off (AC-3) และ Opacity Slider 0–100% (AC-4) ตรงกับ design_mobile.md HeatmapViewerScreen (Slider 0.0–1.0) ทดสอบได้ด้วย UI test บน Android |

### C. Revision and open decision

- Revised wording: **"เมื่อ scan เสร็จสิ้น ระบบต้องสร้างภาพ Heatmap ที่ชี้บริเวณความเสี่ยงด้วยวิธี XAI ที่เข้ากับ inference stack จริง (Grad-CAM หรือวิธีเทียบเท่า ตาม decision Q-03) สีตาม Color Map เดิม (แดง=เสี่ยงสูง, เหลือง=ปานกลาง, เขียว=ปลอดภัย) เก็บเป็น JPEG (resolution ตามภาพต้นฉบับ ยาวด้านยาวไม่เกิน 1920px) บน Object Storage และเข้าถึงผ่าน signed URL ที่มีวันหมดอายุ จากนั้นแสดง overlay บนมือถือพร้อม Toggle On/Off และ Opacity Slider 0–100% ตาม design_mobile.md"**
- Assumption ที่ยังไม่ใช่ decision: signed URL ยืมจาก admin_design.md เพื่อความสอดคล้องภายในและ PDPA (C-04) — ยังรอยืนยันเป็น decision
- Open question: Q-03 (a) เลือกวิธี XAI ที่ compatible กับ ONNX Runtime + SegFormer (b) พฤติกรรมเมื่อไม่พบ region เสี่ยง (c) ยืนยัน signed URL เป็นมาตรฐาน; Q-04 เกี่ยวข้องกับ PDPA retention ของไฟล์ heatmap (ผูกกับ data retention policy ที่ QR-04 อ้างถึง)
- Decision owner + due/decision point: ภานุวัฒน์ (Q-03a ร่วมกับฝั่ง model) / ภายใน Week 05 ก่อน implement heatmap generation
- Status: Not Ready — ห้าม implement ตาม wording เดิม ("Grad-CAM") จนกว่า Q-03 จะตัดสิน เพราะเสี่ยงสร้างฟีเจอร์ที่ทำตาม SRS เดิมไม่ได้จริง

### D. Acceptance Criteria

| AC ID | Context/Input/State | Event/Rule | Observable expected result | Type/risk covered |
|---|---|---|---|---|
| AC-R3-01 | Scan ภาพที่พบบริเวณเสี่ยง (visual analysis ให้ confidence สูง) | สร้าง Heatmap ด้วยวิธีตาม Q-03 → บันทึก JPEG → Object Storage | Response มี `heatmap_url` ที่เข้าถึงได้ผ่าน signed URL และไฟล์เป็น JPEG สีตาม Color Map | Normal — QR-02 |
| AC-R3-02 | หน้า HeatmapViewerScreen บน Android มี heatmap_url | แสดง overlay + คลิก Toggle Button | Heatmap Layer แสดง/ซ่อนตามสถานะ toggle ทุกครั้งที่คลิก | Normal/UI — QR-02 |
| AC-R3-03 | Opacity Slider ตั้งค่า 0% และ 100% | ปรับ opacity ของ heatmap layer | 0% = heatmap โปร่งใสสนิท (มองไม่เห็น), 100% = ทึบเต็มที่; ค่ากลาง (เช่น 50%) แสดงความโปร่งใสระหว่างกัน | Boundary — QR-02 |
| AC-R3-04 | ภาพที่ visual analysis ให้ความเสี่ยงต่ำ (visual_score < threshold ตาม Q-01) | สร้างผลลัพธ์ scan โดยไม่มี region เสี่ยงชัดเจน | ระบบแสดง Risk Breakdown ครบ (gauge, bars, grade) โดยไม่ crash และแสดง heatmap ตามพฤติกรรมที่ตัดสินใน Q-03b | Negative — QR-02 |
| AC-R3-05 | heatmap_url ที่ได้รับ | ลองเข้าถึงไฟล์โดยไม่มี token / หลัง token หมดอายุ | เข้าถึงไม่ได้ (HTTP 401/403) — ป้องกันข้อมูลภาพผู้ใช้รั่วผ่าน URL เปล่า | Negative/Security — เชื่อม C-04 |

### E. Planned evidence

- Planned test level: Integration (heatmap generation ต่อ pipeline) + Component (mobile UI test) + Review (XAI method decision record)
- Planned evidence: 1) API test ของ heatmap_url + signed URL expiry test 2) Android UI test ของ toggle/slider 3) ภาพเปรียบเทียบ heatmap กับ ground-truth mask (validation ว่าจุดแดงตรงบริเวณตัดต่อจริง)
- Current status: Not Ready (รอ Q-03 และ implementation)
- Owner/next action: ภานุวัฒน์ + เอกพันธ์ (mobile) / ตัดสิน Q-03 ก่อน implement

---

## Requirement Record — REQ-04

### A. Source and risk

| Field | Record |
|---|---|
| Original Requirement ID | NFR-01: Performance — Response Time — Priority: Must |
| Original text | "ระบบต้องมีเวลาตอบสนองตามที่กำหนด" พร้อม AC-1 ถึง AC-4 (Cache Hit P95 ≤ 3s; New Analysis P50 ≤ 15s / P95 ≤ 25s / P99 ≤ 35s; GPU Inference ≤ 10s; CPU Fallback ≤ 60s + UI message) |
| Source/version/location | SRS v1.0, Section 3 (NFR-01), อ้าง RC-NFR-01/02/03 |
| Linked risk/stakeholder | C-03, C-06 (PROJECT.md), QR-03 (W01); ST01 |

### B. Lightweight review

| Check / issue type | Pass / Finding | Evidence, question or counterexample |
|---|---|---|
| Clear / unambiguous | Finding — Ambiguous | ไม่ระบุเงื่อนไข measurement: จำนวน request ขั้นต่ำ (sample size) สภาพแวดล้อม (hardware/GPU model) และ concurrency ระหว่างวัด — ตัวเลข percentile จะ reproducible ไม่ได้หากไม่ fix เงื่อนไข |
| Complete | Finding — Incomplete | CPU fallback (AC-4) ไม่ระบุ trigger condition ว่าเมื่อไรถือว่า "GPU ไม่พร้อม" (GPU down? queue overflow? deployment แบบ CPU-only?) |
| Consistent | Finding — Inconsistent | 3 จุดใน SRS วัดคนละ basis โดยไม่ระบุเงื่อนไขแยก: FR-SCAN-03 AC-1 บอก cache hit "≤ 3 วินาที" (ไม่มี percentile), NFR-01 AC-1 บอก cache hit "P95 ≤ 3 วินาที", NFR-02 AC-1 บอก load test cache hit "Average ≤ 5 วินาที" — ถ้าไม่ระบุว่าแต่ละเกณฑ์ใช้ตอนไหน จะขัดกันเวลาตัดสิน (เช่น P95=4s ผ่าน NFR-02 แต่ fail NFR-01) |
| Feasible | Pass | P50 ≤ 15s สอดคล้อง C-03 ใน PROJECT.md และ pipeline parallel + pHash cache ตาม design; GPU T4 เป็น hardware ที่ระบุชัด |
| Testable / observable | Pass (มีเงื่อนไข) | Percentile metrics วัดได้ด้วย JMeter/Locust ตาม SRS — เพียงแต่ต้อง pin เงื่อนไขก่อน |

### C. Revision and open decision

- Revised wording: **"ภายใต้เงื่อนไข baseline (single-user sequential, n ≥ 100 requests, GPU NVIDIA T4): Cache Hit P95 ≤ 3 วินาที และภาพใหม่ P50 ≤ 15 / P95 ≤ 25 / P99 ≤ 35 วินาที ส่วนเกณฑ์ Average ≤ 5s (hit) และ ≤ 20s (miss) ใช้เฉพาะภายใต้ load test 100 concurrent users ตาม NFR-02 — สองชุดเงื่อนไขเป็นเกณฑ์แยกกัน ไม่ใช่เกณฑ์เดียวกัน CPU fallback mode เกิดเมื่อ GPU node ไม่พร้อมใช้งาน (health check fail > 30 วินาที) โดย average ≤ 60 วินาที/ภาพ และ UI ต้องแสดงข้อความ 'Processing may take longer (CPU mode)' ภายใน 5 วินาทีหลังเข้าสู่โหมด"**
- Assumption ที่ยังไม่ใช่ decision: n ≥ 100 requests และ health-check timeout 30 วินาที เป็นค่า propose ที่ยังรอยืนยัน
- Open question: Q-05 ยืนยันเงื่อนไข measurement (sample size, environment spec, concurrency) และ CPU fallback trigger ให้เป็นทางการใน SRS v1.1
- Decision owner + due/decision point: ภานุวัฒน์ / ก่อน W11 (NFR Test Outline) — แต่ควรยืนยันตั้งแต่ W05 เพื่อให้ load test script ออกแบบถูก
- Status: Conditional

### D. Acceptance Criteria

| AC ID | Context/Input/State | Event/Rule | Observable expected result | Type/risk covered |
|---|---|---|---|---|
| AC-R4-01 | Cache hit (pHash match), single-user, n ≥ 100, GPU T4 | วัด response time ทุก request แล้วคำนวณ P95 | P95 ≤ 3 วินาที | Normal — QR-03 |
| AC-R4-02 | ภาพใหม่ (cache miss), single-user, n ≥ 100, GPU T4 | วัด end-to-end response time | P50 ≤ 15s, P95 ≤ 25s, P99 ≤ 35s | Normal — QR-03 |
| AC-R4-03 | GPU node health check fail > 30 วินาที (จำลองด้วยการ disable GPU worker) | ระบบสลับเป็น CPU mode | Inference เฉลี่ย ≤ 60 วินาที/ภาพ และ UI แสดงข้อความ CPU mode ภายใน 5 วินาที | Boundary — QR-03 |
| AC-R4-04 | Google Vision API ล่ม (จำลอง HTTP 503) ระหว่าง scan ภาพใหม่ | Source analysis fallback (FR-ANALYSIS-03 AC-4: source_score = 50, source_status = unavailable) | End-to-end response ยังอยู่ในเป้าของ AC-R4-02 (fallback ไม่ block pipeline) | Negative — QR-03 |

### E. Planned evidence

- Planned test level: System (performance test ด้วย JMeter/Locust)
- Planned evidence: 1) Performance test report (percentile table ตามเงื่อนไข AC-R4-01/02) 2) Chaos/fallback test log ของ AC-R4-03/04 3) Measurement condition spec ที่ตอบ Q-05
- Current status: Not Ready (Backend + Redis Cache + AI service ยังพัฒนาไม่เสร็จ — ตาม W01 QR-03)
- Owner/next action: ภานุวัฒน์ / ยืนยัน Q-05 → เขียน performance test plan ใน W11

---

## Requirement Record — REQ-05

### A. Source and risk

| Field | Record |
|---|---|
| Original Requirement ID | FR-PDPA-01: Consent Management — Priority: Must |
| Original text | "ระบบต้องจัดการความยินยอม 2 ระดับ (System Consent และ Research Consent)" พร้อม AC-1 ถึง AC-5 (Consent Screen, Consent Logs, ถอน Research Consent, Right to Access ข้อมูลส่วนตัว/consent logs) |
| Source/version/location | SRS v1.0, Section 2.6 (FR-PDPA-01), อ้าง RC-PDPA-01/02/03 |
| Linked risk/stakeholder | C-04 (PROJECT.md), QR-04 (W01); ST01 (ผู้ใช้), สถาบัน (ความเสี่ยงทางกฎหมาย) |

### B. Lightweight review

| Check / issue type | Pass / Finding | Evidence, question or counterexample |
|---|---|---|
| Clear / unambiguous | Pass | 2 ระดับ consent (System = บังคับ, Research = ไม่บังคับ) และ fields ของ consent_logs (user_id, consent_type, is_granted, created_at) ระบุชัดเจน |
| Complete | Finding — Incomplete | (a) ไม่ระบุผลของการถอน Research Consent ต่อข้อมูลที่เก็บไปแล้ว — ต้องลบ/ถอนจาก research dataset ย้อนหลัง หรือหยุดเฉพาะการเก็บใหม่? (b) ไม่ระบุ behavior เมื่อผู้ใช้ต้องการถอน System Consent ซึ่งเป็นเงื่อนไขบริการ |
| Consistent | Finding — Inconsistent | AC-3 ให้ update consent_logs พร้อม `updated_at` แต่ field definition ใน AC-2 มีเพียง (user_id, consent_type, is_granted, created_at) — updated_at ไม่เคยถูกประกาศใน schema ต้องเพิ่มเข้า schema ให้สอดคล้อง |
| Feasible | Pass | เป็น CRUD + logging มาตรฐาน feasible ชัดเจน ไม่มี dependency ที่เป็นไปไม่ได้ |
| Testable / observable | Pass (มีเงื่อนไข) | AC เดิมทดสอบได้ด้วย API test — แต่ขาด negative case ของ system_consent=false ตอน register (มีอยู่ใน FR-AUTH-01 AC-5 แล้ว ควร cross-reference แทนการซ้ำ) และขาด case พยายามถอน System Consent |

### C. Revision and open decision

- Revised wording: **"ระบบต้องจัดการความยินยอม 2 ระดับ: System Consent (บังคับ — ถอนได้เฉพาะโดยลบบัญชีผ่านการลบประวัติ/บัญชีตาม FR-HISTORY-01) และ Research Consent (ไม่บังคับ — ถอนได้ตลอดเวลาผ่าน PUT /consent/research) เมื่อถอน Research Consent ระบบต้องบันทึก is_granted = false พร้อม updated_at ทันที และหยุดนำข้อมูลใหม่ของผู้ใช้ไปใช้ใน research dataset ตั้งแต่ scan ถัดไป ส่วนข้อมูลที่รวบรวมไว้ก่อนหน้า ให้ปฏิบัติตามมติ Q-06 ทุกการเปลี่ยนแปลงต้องปรากฏใน GET /consent/logs เป็น audit trail"**
- Assumption ที่ยังไม่ใช่ decision: "หยุดเก็บใหม่ตั้งแต่ scan ถัดไป" เป็น minimum viable compliance ที่ propose ไว้ — retroactive deletion ยังเป็น open question
- Open question: Q-06 การถอน Research Consent แบบย้อนหลัง — ลบข้อมูลออกจาก research dataset ที่ export ไปแล้ว (approved reports) หรือ exclude going forward พอ? (ผลกระทบ: FR-ADMIN-02 AC-3 ที่ copy ภาพเข้า Dataset Storage)
- Decision owner + due/decision point: ภานุวัฒน์ (พิจารณาร่วมกับอาจารย์ที่ปรึกษาเรื่อง PDPA) / ก่อน implement admin approve flow และก่อน W05
- Status: Conditional — ส่วนที่ไม่ผูกกับ Q-06 ใช้ได้ทันที

### D. Acceptance Criteria

| AC ID | Context/Input/State | Event/Rule | Observable expected result | Type/risk covered |
|---|---|---|---|---|
| AC-R5-01 | ผู้ใช้สมัครสมาชิกครั้งแรก | แสดง Consent Screen | แสดง 2 ส่วนแยกกัน: System (บังคับ) / Research (ไม่บังคับ) และ consent_logs ถูกบันทึก 2 records พร้อม created_at | Normal — QR-04 |
| AC-R5-02 | Register ด้วย System Consent = false | Validate consent (cross-ref FR-AUTH-01 AC-5) | HTTP 400 "System consent is required" — สร้างบัญชีไม่สำเร็จ | Negative — QR-04 |
| AC-R5-03 | ผู้ใช้เคย grant Research Consent แล้ว เรียก PUT /consent/research {is_granted: false} | อัปเดต consent_logs (is_granted = false, updated_at) | HTTP 200 และ scan ถัดไปของผู้ใช้ไม่ถูกนำเข้า research dataset (ตรวจได้จาก approved report/dataset export หลังวันถอน) | Normal — QR-04 |
| AC-R5-04 | เรียก GET /consent/logs หลังมีประวัติ grant → revoke | ดึง audit trail | แสดง history ครบทุก event เรียงตามเวลา พร้อม created_at/updated_at — ไม่มี record หาย | Boundary/Audit — QR-04 |
| AC-R5-05 | ผู้ใช้พยายามถอน System Consent ผ่าน endpoint ใด ๆ ที่ไม่ใช่การลบบัญชี | ตรวจ business rule ตาม revised wording | ไม่มี endpoint รองรับ / server reject — System Consent ถอนได้เฉพาะ path การลบบัญชีตาม FR-HISTORY-01 | Negative — QR-04 |

### E. Planned evidence

- Planned test level: Component/API test + Review (PDPA decision record Q-06)
- Planned evidence: 1) API test suite ของ consent endpoints (AC-R5-01 ถึง AC-R5-05) 2) Database snapshot แสดง consent_logs audit trail 3) Decision record ของ Q-06 พร้อมผลกระทบต่อ FR-ADMIN-02
- Current status: Not Ready (Mobile consent screen + backend endpoints ยังพัฒนาไม่เสร็จ — ตาม W01 QR-04)
- Owner/next action: ภานุวัฒน์ + เอกพันธ์ / ตัดสิน Q-06 ก่อน implement admin approve flow

---

## Consolidated open questions

| ID | Question | Type | Decision owner | Due/decision point | Affects |
|---|---|---|---|---|---|
| Q-01 | Decision threshold ต่อภาพ (forgery/AI-Gen) และ scope ของ AI generators ที่ทดสอบ | Ambiguity/Scope | ภานุวัฒน์ | Week 05 / ก่อน model evaluation | FR-ANALYSIS-02, NFR-05 |
| Q-02 | Composition ของ Testing Set 1,000 ภาพ (สัดส่วน real/fake, ประเภท forgery) | Completeness | ภานุวัฒน์ | ก่อน curate Testing Set | NFR-05, W02 Gap |
| Q-03 | วิธี XAI ที่ compatible กับ ONNX Runtime + SegFormer / พฤติกรรม heatmap เมื่อไม่พบ region เสี่ยง / signed URL เป็นมาตรฐาน | Feasibility | ภานุวัฒน์ (+ฝั่ง model) | Week 05 / ก่อน implement heatmap | FR-XAI-01, C-02 |
| Q-04 | Retention/access control ของไฟล์ heatmap (ผูกกับ data retention policy) | Compliance | ภานุวัฒน์ | ก่อน implement object storage lifecycle | FR-XAI-01, C-04 |
| Q-05 | เงื่อนไข measurement ของ NFR-01 (n, environment, concurrency) และ CPU fallback trigger | Ambiguity | ภานุวัฒน์ | Week 05 (ยืนยันก่อน W11) | NFR-01, NFR-02 |
| Q-06 | Retroactive handling เมื่อถอน Research Consent (ลบย้อนหลัง vs exclude going forward) | Completeness/Compliance | ภานุวัฒน์ (+อาจารย์ที่ปรึกษา) | ก่อน implement admin approve flow | FR-PDPA-01, FR-ADMIN-02 |

> ทุก requirement ที่มี Status = Conditional/Not Ready จะยังไม่ถูกแก้ใน SRS จนกว่า open question ที่เกี่ยวข้องจะตัดสิน — SRS v1.0 ยังเป็น baseline ตาม input-register

## Handoff summary for Week 04

| Requirement ID | Revision status | Acceptance basis ready? | Open decision/blocker | Owner/due | Candidate test level |
|---|---|---|---|---|---|
| FR-ANALYSIS-02 | Revised (Conditional) | Yes — AC-R1-01 ถึง AC-R1-04 ตัดสินได้ | Q-01 (threshold, generator scope) | ภานุวัฒน์ / W05 | Component + System |
| NFR-05 | Revised (Conditional) | Conditional — ขาด dataset composition | Q-02 (testing set composition) | ภานุวัฒน์ / ก่อน curate set | System |
| FR-XAI-01 | Revised (Not Ready) | No — method ยัง infeasible ตาม wording เดิม | Q-03, Q-04 (XAI method, retention) | ภานุวัฒน์ / W05 | Integration + Component (UI) |
| NFR-01 | Revised (Conditional) | Yes เมื่อยืนยันเงื่อนไขวัด | Q-05 (measurement conditions) | ภานุวัฒน์ / W05 | System (Performance) |
| FR-PDPA-01 | Revised (Conditional) | Yes — ยกเว้น AC ที่ผูกกับ retroactive handling | Q-06 (retroactive consent) | ภานุวัฒน์ + อาจารย์ที่ปรึกษา / ก่อน admin flow | Component/API |
