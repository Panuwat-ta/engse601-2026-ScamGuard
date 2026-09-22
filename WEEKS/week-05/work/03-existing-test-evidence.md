# W05-03 — Execution Evidence

## Baseline

- Requirement authority: `https://github.com/Panuwat-ta/project/tree/main/Document/srs`
- SRS: v1.1, 2026-09-12
- Code authority: `https://github.com/Panuwat-ta/project`, branch `main`
- Code baseline: `66bc9e4a` (2026-09-16)
- Baseline record: `work/evidence/E05-baseline.txt`

การทดสอบใช้ isolated archive ของ `origin/main` ที่ `/tmp/scamguard-w05-main-final` เพื่อไม่ checkout ทับ working tree `/home/panuwat/project` ซึ่งมีงาน branch อื่นอยู่

## E05-01 — Existing unit-test execution

รัน test ที่มีอยู่จริงใน baseline:

```text
server/tests/utils/test_risk_calculator.py
1 passed in 0.03s
```

Raw output: `work/evidence/E05-pytest-component.txt`

## E05-02 — Reproducible component probe

สร้าง probe แบบ read-only ที่ `work/probes/component_probe.py` และรันกับ extracted `origin/main` baseline. Probe ใช้ fake DB ใน memory และ test-only config; ไม่เชื่อม production database/Redis และไม่อ่าน secret เพื่อสร้างผลทดสอบ
Raw output: `work/evidence/E05-component-probe.txt`

Observed results:

- Risk AC-1 example `50/85/0` -> `90 high visual True` — aligned
- Risk AC-2 example `100/100/100` -> `100 high visual True` — aligned
- Grade samples 10/30/55/80 -> Low/Low/Medium/High — aligned
- Boundary samples 39/40/69/70 -> Low/Medium/Medium/High — aligned
- Register with System=true, Research=false returns `UserResponse` and persists one `ConsentLog(True, False)`
- Register with System=false still returns `UserResponse` and persists one `ConsentLog(False, False)` — mismatch with FR-AUTH-01 AC-5
- Registration response keys are `email, full_name, id, message, role`; `status` and `created_at` required by AC-1 are absent
- No `PUT /consent/research` and no `GET /consent/logs` route found on baseline main
- Profile GET exists under `/api/v1/auth/me`; `/api/v1/users/me` is DELETE, while SRS AC-4 states GET `/users/me`
- ONNX worker assigns max SegFormer probability to both `ai_gen_prob` and `visual_risk_score`; separate `forgery_confidence` / `ai_gen_confidence` contract is absent

## E05-03 — What was not claimed

- No model Accuracy/mDice/F1 result is claimed in W05; dataset-level evaluation is outside Component/Unit scope.
- No GPU inference <=10s result is claimed; performance evidence belongs to later NFR testing.
- No pass result is claimed for missing consent endpoints or visual dual-signal behavior.
- No stakeholder decision or human peer-review approval is fabricated.
## E05-04 — Submission PDF verification

`work/evidence/E05-pdf-check.txt` records A4/4-page metadata and per-page bbox margins. No text box reaches the page edge in the automated bbox check.
