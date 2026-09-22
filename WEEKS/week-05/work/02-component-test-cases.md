# W05-02 — Component Test Case Set

## Test basis

- Canonical SRS: `https://github.com/Panuwat-ta/project/tree/main/Document/srs`
- SRS: `05_Software_Requirement_Specification.md` v1.1, 2026-09-12
- Code baseline: `https://github.com/Panuwat-ta/project`, branch `main`, commit `66bc9e4a`
- Execution date: 2026-09-22

## Result vocabulary

- `Pass` — รัน/ตรวจจริงแล้วได้ผลตรง expected result ใน baseline
- `Fail` — รัน/ตรวจจริงแล้ว implementation ไม่ตรง baseline
- `Not Ready` — acceptance basis ชัด แต่ component ที่จำเป็นยังไม่พร้อมให้ทดสอบพฤติกรรมนั้น
- `Needs Clarification` — wording/ตัวอย่างใน requirement ไม่สามารถสร้าง test ที่ไม่ขัดกับกฎอื่นใน baseline เดียวกันได้

## A. Visual Analysis — FR-ANALYSIS-02

| TC ID | AC | Component / condition | Expected | Actual evidence | Result |
|---|---|---|---|---|---|
| W05-CT-01 | AC-1 | `onnx_worker.py` output contract หลัง SegFormer | มี `forgery_confidence` 0–100 ที่ trace กลับไปยัง forgery signal ได้ | probe พบ `visual_risk_score` แต่ไม่พบ key `forgery_confidence` | Fail |
| W05-CT-02 | AC-2 | AI-Generated detector output contract | มี signal/field `ai_gen_confidence` จาก AI-Gen detector แยกจาก forgery | probe พบ `ai_gen_prob = max(prob_map_true)` จาก SegFormer เดียวกับ visual score และไม่พบ `ai_gen_confidence` | Fail |
| W05-CT-03 | AC-3 | Visual-score calculation | คำนวณตาม canonical visual-analysis contract หลังมีสัญญาณที่ requirement กำหนด | ยังไม่มีสองสัญญาณ/contract ที่ทำให้ทดสอบ calculation นี้แบบอิสระได้ | Not Ready |

หมายเหตุ: FR-ANALYSIS-02 AC-5 เรื่องเวลา inference GPU <= 10 วินาทีเป็น performance/system concern จึงส่งต่อ NFR testing ไม่ใช้เป็น Unit/Component acceptance ของ W05
## B. Risk Calculation — FR-ANALYSIS-04

| TC ID | AC | Input / condition | Expected | Actual evidence | Result |
|---|---|---|---|---|---|
| W05-CT-04 | AC-1 | text=50, visual=85, source=0 | score=90, High, primary=visual | probe: `90 high visual True` | Pass |
| W05-CT-05 | AC-2 | 100/100/100 | cap score at 100, High | probe: `100 high visual True` | Pass |
| W05-CT-06 | AC-3 | score basis 10 | Low | existing calculator logic + boundary suite | Pass |
| W05-CT-07 | AC-4 | score basis 30 | Low | existing calculator logic + boundary suite | Pass |
| W05-CT-08 | AC-5 | score basis 55 | Medium | existing calculator logic + boundary suite | Pass |
| W05-CT-09 | AC-6 | score basis 80 | High | existing calculator logic + boundary suite | Pass |
| W05-CT-10 | AC-7 | stated example `risk_score=65`, `visual_score=85` | High by Visual Override | Hybrid max+bonus uses visual in `max()`, therefore visual=85 implies total >=85; state 65/85 cannot be produced by the same calculator | Needs Clarification |

Automated evidence: `work/evidence/E05-pytest-component.txt` reports `1 passed`; deterministic probe outputs are in `work/evidence/E05-component-probe.txt`.

## C. Registration — FR-AUTH-01

| TC ID | AC | Component / condition | Expected | Actual evidence | Result |
|---|---|---|---|---|---|
| W05-CT-11 | AC-1 | register with system=true, research=false | successful registration; response includes `id, full_name, email, role, status, created_at` and no password/hash | handler returns `UserResponse`; keys are `email, full_name, id, message, role`; `status` and `created_at` absent | Fail |
| W05-CT-12 | AC-5 | register with `system_consent=false` | HTTP 400 `System consent is required`; no user/consent persisted | handler returns `UserResponse` and adds both `User` + `ConsentLog(False, False)` in fake DB | Fail |
| W05-CT-13 | AC-1 subcondition | system=true, research=false | Research Consent is optional and must not block registration | handler succeeds and stores research=false | Pass |
## D. Consent Management — FR-PDPA-01

| TC ID | AC | Component / condition | Expected | Actual evidence | Result |
|---|---|---|---|---|---|
| W05-CT-14 | AC-2 | persist System=true, Research=true | consent log model/event fields support `consent_type`, `is_granted`, timestamp and 2 records | current model stores one row with `system_consent` + `research_consent`; event fields are not present | Fail |
| W05-CT-15 | AC-3 | `PUT /consent/research {is_granted:false}` | HTTP 200 and updated research-consent event with `updated_at` | route inventory finds no `/consent/research` endpoint | Fail |
| W05-CT-16 | AC-4 | `GET /users/me` | HTTP 200 current-user profile | main exposes profile GET at `/api/v1/auth/me`; `/api/v1/users/me` is DELETE | Fail |
| W05-CT-17 | AC-5 | `GET /consent/logs` | HTTP 200 audit history | route inventory finds no `/consent/logs` endpoint | Fail |
| W05-CT-18 | AC-3/5 | ConsentLog timestamp contract | history/update supports `updated_at` | current `ConsentLog` model has `created_at` only | Fail |

## Execution summary

| Result | Count |
|---|---:|
| Pass | 7 |
| Fail | 9 |
| Not Ready | 1 |
| Needs Clarification | 1 |
| Total | 18 |

A failed component test is valid V&V evidence and is not converted to `Pass` for submission. Findings and next actions are recorded in `04-open-issues-and-decisions.md`.
