# ผลการรันจริง (B1)

| รายการ | ข้อมูล |
|---|---|
| ทีม · feature | ScamGuard · การสมัครสมาชิกและการจัดการความยินยอม 2 ระดับ (System Consent + Research Consent) |
| รุ่นของระบบที่รัน | `Refactor-mobile@c3bc7223` |
| ชุดอ้างอิงที่ใช้ | [S2-B_ScamGuard_v2.pdf](../02-test-design/S2-B_ScamGuard_v2.pdf) · v2 เปลี่ยน TC-05 เป็นถอน Research Consent และ TC-07 เป็นไม่ส่งฟิลด์ `system_consent` · ผล v1 เดิม 6 Pass / 4 Fail เก็บที่ [s3-api-reference-run-v1.txt](evidence/s3-api-reference-run-v1.txt) |
| เครื่องมือ | Python 3.10 + FastAPI/HTTPX `ASGITransport` (in-process) รันด้วย `server/venv/bin/python` |
| วันที่รัน · ผู้รัน | 23 ต.ค. 2569 (2026-10-23) · ภานุวัฒน์ ต๋าคำ |

## ขั้นที่ 1 เลือกระดับ (3 คะแนน)

| TC | ระดับ | เหตุผล (พฤติกรรมอยู่ที่ไหน) |
|---|---|---|
| TC-01 | Integration (API) | พฤติกรรมอยู่ที่ขอบเขต HTTP + schema ของ RegisterRequest และการตัดสินว่าจะเขียนฐานข้อมูลหรือไม่ ต้องเรียกผ่าน endpoint จริงจึงเห็น status/body ที่ client ได้ |
| TC-02 | Integration (API) | ไหลจาก route → service → ชั้นข้อมูล และต้องตรวจทั้ง response 201 กับแถว users/consent_logs ที่ถูกสร้าง จึงข้ามขอบเขตมากกว่าหนึ่งส่วนประกอบ |
| TC-03 | Integration (API) | เป็น validation ที่ขอบเขต HTTP เช่นเดียวกับ TC-01 แต่ใช้ค่าขอบล่างของโดเมน (รหัสผ่านว่าง) และต้องยืนยันว่าไม่มีแถวใหม่ |
| TC-04 | Integration (API) | ต้องตรวจการค้นหาอีเมลซ้ำในชั้นข้อมูลร่วมกับ response 400 และยืนยันว่าจำนวนผู้ใช้/consent log ไม่เปลี่ยน |
| TC-05 | Integration (API) | เส้นทางถอน Research Consent ตั้งแต่ HTTP จนถึงการอัปเดต consent log ที่บันทึก และต้องเรียก GET /consent/logs เพื่อยืนยันค่าหลังถอน |
| TC-06 | Integration (API) | กฎความปลอดภัยของ System Consent ต้องบังคับที่ฝั่งเซิร์ฟเวอร์ ไม่ใช่แค่ซ่อนปุ่มบนหน้าจอ จึงต้องยิง API ตรงและตรวจว่าไม่มีแถวใหม่ |
| TC-07 | Integration (API) | เป็น validation ที่ขอบเขต HTTP เมื่อไม่ส่งฟิลด์ system_consent และต้องยืนยันว่าไม่มีแถว users/consent ใหม่ |
| TC-08 | Integration (API) | ต้องตรวจว่า Research Consent ที่ไม่บังคับไม่บล็อกการสมัคร และค่าที่บันทึกตรงกับคำตอบของผู้ใช้ |
| TC-09 | Integration (API) | ต้องตรวจว่าเมื่อผู้ใช้เลือกยินยอมวิจัย ระบบบันทึก true จริง ไม่ใช่ค่าคงที่ |
| TC-10 | Integration (API) | เป็นสัญญาของ endpoint ประวัติความยินยอม ต้องเรียกผ่าน HTTP พร้อม token และตรวจรูปร่าง body ตาม SRS รวมถึงการแยกข้อมูลตามผู้ใช้ |

## ขั้นที่ 2 กรณีทดสอบอัตโนมัติ (6 คะแนน)

| รายการ | ข้อมูล |
|---|---|
| TC และระดับ | TC-01 ถึง TC-10 · Integration (API) |
| ไฟล์โค้ดทดสอบ | [tests/test_s3_reference_suite.py](tests/test_s3_reference_suite.py) |
| คำสั่งที่ใช้รัน | `cd /home/panuwat/project/server && ./venv/bin/python /home/panuwat/work/engse601-2026-ScamGuard/03-test-execution/tests/test_s3_reference_suite.py` |
| หลักฐาน | [s3-api-reference-run.txt](evidence/s3-api-reference-run.txt) · [s3-api.png](evidence/s3-api.png) |
| สถานะ | 4 Pass / 6 Fail (รันจริง 2026-10-23; TC-01..TC-10 ไม่มี Blocked หรือ Not Executed) |

ผลเทอร์มินัล (คัดลอกจากการรันจริงทั้งก้อน)

```text
# S3-B1 reference suite (v2 TCs) · run 2026-10-23T02:57:49+07:00
# Baseline: /home/panuwat/project @ c3bc72235d6890c962e967360443aedbeecef617 (branch Refactor-mobile)
# Command: cd /home/panuwat/project/server && ./venv/bin/python /home/panuwat/work/engse601-2026-ScamGuard/03-test-execution/tests/test_s3_reference_suite.py

/home/panuwat/project/server/venv/lib64/python3.10/site-packages/huggingface_hub/file_download.py:949: FutureWarning: `resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`.
  warnings.warn(
XAI model file not found at /tmp/s3-missing.gguf
Loaded detection model vikp/surya_det3 on device cuda with dtype torch.float16
Loaded recognition model vikp/surya_rec2 on device cuda with dtype torch.float16
Loaded official Surya OCR models successfully
S3-B1 API reference suite · ScamGuard · FR-AUTH-01 / FR-PDPA-01
Baseline: /home/panuwat/project/server · commit c3bc7223
Transport: httpx ASGITransport (in-process), isolated in-memory session
----------------------------------------------------------------------------------------------------
TC-01  Fail  HTTP 422 · body={"detail":[{"type":"string_too_short","loc":["body","password"],"msg":"String should have at least 8 characters","input":"Test123","ctx":{"min_length":8}}]} · users 0->0 · consents 0->0
TC-02  Pass  HTTP 201 · users=1 · consents=1 · hashed=$2b$12$TTn/a0YIVmz… · system=True
TC-03  Fail  HTTP 422 · body={"detail":[{"type":"string_too_short","loc":["body","password"],"msg":"String should have at least 8 characters","input":"","ctx":{"min_length":8}}]} · users 0->0 · consents 0->0
TC-04  Pass  HTTP 400 · body={"detail":"Email already registered"} · users 1->1 · consents 1->1
TC-05  Fail  register HTTP 201 · login HTTP 200 · PUT /consent/research HTTP 404 · body={"detail":"Not Found"} · GET /consent/logs HTTP 404 · body={"detail":"Not Found"} · users 0->1 · consents 0->1
TC-06  Fail  HTTP 201 · body={"id":1,"email":"new.user04@example.com","full_name":"Probe 06","role":"user","message":"User registered successfully"} · users 0->1 · consents 0->1
TC-07  Fail  HTTP 201 · body={"id":1,"email":"new.user08@example.com","full_name":"Probe 07","role":"user","message":"User registered successfully"} · users 0->1 · consents 0->1
TC-08  Pass  HTTP 201 · research=False
TC-09  Pass  HTTP 201 · research=True
TC-10  Fail  register HTTP 201 · login HTTP 200 · GET /consent/logs HTTP 404 · body={"detail":"Not Found"}
----------------------------------------------------------------------------------------------------
Summary: 4 Pass, 6 Fail, 10 total
```

## ขั้นที่ 3 System ทำมือ (4 คะแนน)

| รายการ | ข้อมูล |
|---|---|
| TC | SYS-AUTH-01 — สมัครสมาชิกผ่านหน้าจอโดยไม่เลือก Research Consent |
| ขั้นตอน | 1. เปิดแอป Flutter เวอร์ชันที่ต่อ API baseline บน Chrome/อุปกรณ์จริง<br>2. เลือกสมัครสมาชิก กรอกอีเมลใหม่ รหัสผ่าน 8 ตัวอักษร และยอมรับ System Consent<br>3. ไม่เลือก Research Consent แล้วกดสมัคร<br>4. เข้าหน้าจัดการความยินยอม ตรวจว่าค่า Research Consent เป็นปิดตามที่เลือก |
| ผลที่คาดหวัง | สมัครสำเร็จและเข้าสู่หน้าหลักได้ · ค่า Research Consent ที่แสดงและบันทึกเป็น false ตรงกับคำตอบของผู้ใช้ · ไม่มีข้อความผิดพลาดที่ผู้ใช้แก้เองไม่ได้ |
| ผลจริง | ยังไม่ได้รัน — ไม่มีภาพหน้าจอ (ยังไม่มี PostgreSQL 15/Redis 7, ไม่มี `build/web` หรือ deployed API และไม่มี aiosqlite สำหรับรันแทน) · ภาพผล API v2 ในขั้นที่ 2 ไม่ใช่ภาพ System test และไม่ใช้แทนกัน |
| สถานะ | **Not Executed** เพราะยังไม่มี build/environment สำหรับรัน UI ครบวงจร · แผน: เตรียม PostgreSQL/Redis และ build Flutter แล้วรันบนเครื่อง dev ภายใน 29 ต.ค. 2569 พร้อมเก็บภาพหน้าจอที่ `03-test-execution/evidence/` |

## ขั้นที่ 4 UAT (3 คะแนน)

| รายการ | ข้อมูล |
|---|---|
| ชื่อสถานการณ์ · ผู้ทดสอบ | UAT-AUTH-01 · ผู้ใช้จริง 1 คนนอกทีม (นักศึกษาสาขาอื่น/บุคคลทั่วไปที่ไม่ใช่นักพัฒนา — จะระบุชื่อก่อนทดสอบ) |
| ขั้นตอน (ลำดับงานของผู้ใช้) | 1. ผู้ทดสอบเปิดแอปด้วยลิงก์/เครื่องที่ทีมเตรียมให้ และสมัครสมาชิกด้วยอีเมลของตนเองโดยไม่ให้ทีมช่วยกรอก<br>2. อ่านหน้า Privacy Consent ของแอป แล้วเลือก Research Consent ตามความสมัครใจก่อนกดสมัคร<br>3. เข้าสู่หน้า Privacy Consent ใน Settings ตรวจว่าค่าที่แอปแสดงตรงกับที่เลือก<br>4. ลองถอน Research Consent และตรวจข้อความยืนยันผล |
| ถือว่าผ่านเมื่อ | ผู้ทดสอบสมัครและเข้าสู่ระบบได้เองภายใน 10 นาที · ค่า Research Consent ที่แอปแสดงและ consent log ฝั่งเซิร์ฟเวอร์ตรงกับที่เลือกทั้งตอนสมัครและหลังถอน · ระบบแจ้งผลการเปลี่ยนอย่างชัดเจน · ไม่มีข้อผิดพลาดที่ผู้ใช้แก้เองไม่ได้ |
| สถานะ และแผน | **Not Executed** เพราะยังไม่มีผู้ใช้จริงนอกทีมมาทดสอบในรอบนี้ · โค้ดจริงยังไม่มี route `PUT /consent/research` ตาม AC-3 จึงต้องแก้ก่อน UAT · แผน: ทดสอบกับผู้ใช้ 1 คนนอกทีมภายใน 29 ต.ค. 2569 หลังปิด DEF-01/DEF-02 และเพิ่ม route ถอน consent แล้วบันทึกผล/ภาพหน้าจอใน `03-test-execution/evidence/` |

## ขั้นที่ 5 ตารางผลของทุกกรณีทดสอบ (3 คะแนน)

| TC | ระดับ | ผลที่คาดหวัง | ผลจริง | สถานะ | หลักฐาน |
|---|---|---|---|---|---|
| TC-01 | Integration (API) | HTTP 400 · `Password must be at least 8 characters` · users 0 · consents 0 | HTTP 422 · Pydantic `string_too_short` · users 0 | **Fail** | [ผลรัน](evidence/s3-api-reference-run.txt) TC-01 |
| TC-02 | Integration (API) | HTTP 201 · users 1 · consents 1 · hash ไม่ใช่ plaintext · system=true | HTTP 201 · users 1 · consents 1 · bcrypt hash · system=true | **Pass** | [ผลรัน](evidence/s3-api-reference-run.txt) TC-02 |
| TC-03 | Integration (API) | HTTP 400 · `Password must be at least 8 characters` · users 0 | HTTP 422 · Pydantic `string_too_short` · users 0 | **Fail** | [ผลรัน](evidence/s3-api-reference-run.txt) TC-03 |
| TC-04 | Integration (API) | HTTP 400 · `Email already registered` · users 1→1 · consents 1→1 | HTTP 400 · `Email already registered` · users 1→1 · consents 1→1 | **Pass** | [ผลรัน](evidence/s3-api-reference-run.txt) TC-04 |
| TC-05 | Integration (API) | HTTP 200 · PUT สำเร็จ · research=false · GET logs แสดง false | HTTP 404 · PUT และ GET logs ไม่มี route · `{"detail":"Not Found"}` | **Fail** | [ผลรัน](evidence/s3-api-reference-run.txt) TC-05 · [DEF-02](../04-defects-release/defects/DEF-02.md) |
| TC-06 | Integration (API) | HTTP 400 · `System consent is required` · users 0 · consents 0 | HTTP 201 · สร้างผู้ใช้และ consent log · users 0→1 · consents 0→1 | **Fail** | [ผลรัน](evidence/s3-api-reference-run.txt) TC-06 · [DEF-01](../04-defects-release/defects/DEF-01.md) |
| TC-07 | Integration (API) | HTTP 400 · `System consent is required` · users 0 · consents 0 | HTTP 201 · schema ใช้ default `system=true` · users 0→1 · consents 0→1 | **Fail** | [ผลรัน](evidence/s3-api-reference-run.txt) TC-07 · [DEF-01](../04-defects-release/defects/DEF-01.md) |
| TC-08 | Integration (API) | HTTP 201 · research=false · users 1 · consents 1 | HTTP 201 · research=false · users 1 | **Pass** | [ผลรัน](evidence/s3-api-reference-run.txt) TC-08 |
| TC-09 | Integration (API) | HTTP 201 · research=true · users 1 · consents 1 | HTTP 201 · research=true · users 1 | **Pass** | [ผลรัน](evidence/s3-api-reference-run.txt) TC-09 |
| TC-10 | Integration (API) | HTTP 200 · `{logs:[...]}` เฉพาะของผู้ใช้ | HTTP 404 · `{"detail":"Not Found"}` | **Fail** | [ผลรัน](evidence/s3-api-reference-run.txt) TC-10 · [DEF-02](../04-defects-release/defects/DEF-02.md) |
| SYS-AUTH-01 | System (manual) | สมัครผ่านหน้าจอสำเร็จ · Research=false ตรงกับที่เลือก | ยังไม่ได้รัน | **Not Executed** | — (ยังไม่มีภาพ; ดูขั้นที่ 3) |
| UAT-AUTH-01 | UAT | ผู้ใช้จริงสมัครเองได้ · ค่าความยินยอมตรงกับที่เลือก · ถอนได้ | ยังไม่ได้ทดสอบ | **Not Executed** | — (ยังไม่มีภาพ; ดูขั้นที่ 4) |

สรุป: Pass **4** · Fail **6** · Blocked **0** · Not Executed **2** (SYS-AUTH-01 และ UAT-AUTH-01)

หมายเหตุ: ภาพ [s3-api.png](evidence/s3-api.png) เป็นภาพผลรัน API v2 จาก terminal จริง ใช้เป็นหลักฐานของ TC-01 ถึง TC-10 เท่านั้น ไม่ใช่ภาพ System test และไม่ใช้แทนภาพ System/UAT ที่ยัง `Not Executed`
