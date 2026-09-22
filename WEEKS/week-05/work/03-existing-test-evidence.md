# W05-03 - Verification and Execution Evidence

## 1. Evidence policy

เอกสารนี้แยกหลักฐานเป็น 4 ประเภทเพื่อป้องกันการตีความเกินจริง:

- `Source snapshot`: ข้อเท็จจริงที่ดึงจาก `/home/panuwat/project` โดย pin `origin/main` และบันทึก path/line/SHA-256 ของ source ที่เกี่ยวข้อง
- `Executed test`: คำสั่ง test ถูก execute จริงและมี raw output
- `Executed probe`: probe เฉพาะ component ถูก execute จริงด้วย test-only configuration/fake DB
- `Static contract inspection`: ตรวจ field, route หรือ source contract ที่มี/ไม่มีจริง โดยไม่อ้างว่าเป็น runtime end-to-end test

ไม่มีการใช้ production secret, production database หรือค่าผลทดสอบที่สร้างขึ้นเอง

## 2. Frozen baseline

- Requirement authority: https://github.com/Panuwat-ta/project/tree/main/Document/srs
- SRS: v1.1, 2026-09-12
- SRS SHA-256: `99bb8d5050fa54195b02869f1815e954fdd43ad0997e732b35426c70947cd40a`
- Source authority: https://github.com/Panuwat-ta/project
- Source branch / commit: `main` / `66bc9e4a`
- Baseline raw record: `work/evidence/E05-baseline.txt`
- Source contract snapshot: `work/evidence/E05-source-contract-snapshot.txt`
- API route inventory: `work/evidence/E05-route-inventory.txt`
- Schema/model contract snapshot: `work/evidence/E05-schema-contract.txt`

Source-derived evidence ทั้ง 3 ไฟล์สร้างจาก `/home/panuwat/project` ด้วย `git show origin/main:<path>` ที่ commit `66bc9e4a` โดยไม่ใช้ local working-tree changes และไม่อ่าน `.env` หรือ production data

เพื่อไม่กระทบ working branch อื่น การทดสอบถูก execute กับ isolated archive ของ `origin/main` ที่ `/tmp/scamguard-w05-main-final`

## 3. E05-S01 ถึง E05-S03 - Source-derived contract evidence

- `E05-source-contract-snapshot.txt`: เก็บ source excerpt พร้อม line number และ SHA-256 จาก `risk_calculator.py`, `auth.py`, `onnx_worker.py`
- `E05-route-inventory.txt`: เก็บ route decorators จริงของ `auth.py`/`users.py` และผลค้นหา consent route บน API v1
- `E05-schema-contract.txt`: เก็บ field contract จริงจาก `schemas/auth.py` และ `models/consent.py`

ไฟล์เหล่านี้เป็นหลักฐาน source provenance สำหรับอธิบายว่า probe/assertion อ่าน behavior จาก implementation ใด ไม่ได้แทน runtime execution evidence

## 4. E05-01 - Existing automated unit test

Type: `Executed test`

Target:

```text
server/tests/utils/test_risk_calculator.py
```

Raw result:

```text
.                                                                        [100%]
1 passed in 0.03s
```

Evidence file: `work/evidence/E05-pytest-component.txt`

## 5. E05-02 - Reproducible component probe

Type: `Executed probe` + `Static contract inspection`

Probe source: `work/probes/component_probe.py`
Raw output: `work/evidence/E05-component-probe.txt`

Probe ใช้ fake DB ใน memory และ test-only environment values เพื่อเรียก component logic โดยไม่เชื่อม external services จริง ผลสำคัญที่ตรวจได้มีดังนี้:

- Hybrid max+bonus: `(50,85,0) -> 90 High`, `(100,100,100) -> 100 High`
- Grade samples: 10/30/55/80 -> Low/Low/Medium/High
- Boundary samples: 39/40/69/70 -> Low/Medium/Medium/High
- Registration system=true, research=false สำเร็จและ persist research=false
- Registration system=false ยังคืน `UserResponse` และเพิ่ม `User` + `ConsentLog(False, False)`
- Registration response keys ขาด `status` และ `created_at`
- ไม่พบ `PUT /consent/research` และ `GET /consent/logs`
- พบ profile GET ที่ `/api/v1/auth/me`; users `/me` เป็น DELETE
- Visual worker ใช้ SegFormer max probability เป็นทั้ง `ai_gen_prob` และฐานของ `visual_risk_score`; ไม่พบ separate `forgery_confidence` / `ai_gen_confidence`

## 6. Evidence-to-test mapping

| Evidence | Test cases supported | Evidence type |
|---|---|---|
| `E05-source-contract-snapshot.txt` | CT-01 ถึง CT-13 | Source snapshot |
| `E05-route-inventory.txt` | CT-15 ถึง CT-17 | Source/API route inventory |
| `E05-schema-contract.txt` | CT-11, CT-14, CT-18 | Source schema/model snapshot |
| `E05-pytest-component.txt` | CT-04 ถึง CT-09 (supporting unit evidence) | Executed test |
| `E05-component-probe.txt` risk section | CT-04 ถึง CT-10 | Executed probe / requirement analysis |
| `E05-component-probe.txt` auth section | CT-11 ถึง CT-13 | Executed handler probe |
| `E05-component-probe.txt` consent section | CT-14 ถึง CT-18 | Static route/model contract inspection |
| `E05-component-probe.txt` visual section | CT-01 ถึง CT-03 | Static source/output contract inspection |

## 7. Reproducibility notes

การ rerun ควรใช้ code commit เดิม `66bc9e4a` หรือบันทึก commit ใหม่ให้ชัดก่อนเปรียบเทียบผล เพราะการแก้ implementation หลัง Week 05 อาจทำให้ผลเปลี่ยนได้ การ rerun บน code ใหม่ถือเป็น re-test ไม่ใช่การแก้ย้อนหลังผลเดิม

## 8. Claims intentionally excluded

Week 05 ไม่อ้างผลต่อไปนี้ เนื่องจากไม่มี execution evidence ที่เหมาะสมใน scope นี้:

- model Accuracy, Precision, Recall, F1 หรือ mDice
- GPU inference <= 10 seconds
- end-to-end mobile/backend/system pass
- production Redis/Database availability
- stakeholder decision หรือ legal approval
- independent peer-review approval

การไม่อ้างผลเหล่านี้เป็นส่วนหนึ่งของ evidence integrity และช่วยให้ Week 06/07/11 สามารถรับ handoff ไปทดสอบในระดับที่เหมาะสมได้โดยไม่ปะปนกับ component evidence
