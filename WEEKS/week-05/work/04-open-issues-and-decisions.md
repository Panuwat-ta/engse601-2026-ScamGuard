# W05-04 — Findings, Disposition and Handoff

## Findings from Code & Logic Reading Clinic

| ID | Finding | Evidence / trace | Disposition | Owner | Next action |
|---|---|---|---|---|---|
| W05-F01 | Visual Analysis main ไม่มี separate `forgery_confidence` / `ai_gen_confidence`; SegFormer max probability ถูกใช้ทั้ง `ai_gen_prob` และ `visual_risk_score` | FR-ANALYSIS-02 AC-1/2/3; CT-01/02/03; E05-component-probe | Accepted implementation gap; does not block W05 evidence | ภานุวัฒน์ | แก้ output contract/AI-Gen detector ใน ENGSE212 แล้ว re-test ก่อน System/UAT |
| W05-F02 | FR-ANALYSIS-04 AC-7 ตัวอย่าง `risk_score=65, visual_score=85` สร้างจาก Hybrid max+bonus เดียวกันไม่ได้ เพราะ total ต้อง >= visual | FR-ANALYSIS-04 AC-7; CT-10 | Needs requirement clarification; algorithm AC-1/2 remains accepted | ภานุวัฒน์ | Clarify AC-7 wording in canonical SRS change process |
| W05-F03 | Register response ขาด `status` และ `created_at` ตาม FR-AUTH-01 AC-1 | CT-11; E05-component-probe | Accepted API contract defect | ภานุวัฒน์ | ปรับ response schema/handler และเพิ่ม contract test |
| W05-F04 | `system_consent=false` ยังสร้าง User + ConsentLog แทน HTTP 400 | FR-AUTH-01 AC-5; CT-12 | Accepted functional defect | ภานุวัฒน์ | เพิ่ม guard/validation ก่อน create user; re-test negative case |
| W05-F05 | Consent model เก็บหนึ่ง row สอง booleans ไม่มี event fields/`updated_at` ตาม SRS | FR-PDPA-01 AC-2/3/5; CT-14/18 | Accepted data/API contract gap | ภานุวัฒน์ | Reconcile consent schema + migration before integration testing |
| W05-F06 | ไม่มี `PUT /consent/research` และ `GET /consent/logs` | FR-PDPA-01 AC-3/5; CT-15/17 | Accepted missing implementation | ภานุวัฒน์ | Implement endpoints and component tests |
| W05-F07 | SRS ระบุ GET `/users/me`; main profile GET อยู่ `/api/v1/auth/me` และ `/api/v1/users/me` เป็น DELETE | FR-PDPA-01 AC-4; CT-16 | Accepted route-contract mismatch | ภานุวัฒน์ | เลือก canonical route แล้ว sync SRS/code ผ่าน controlled change |
| W05-F08 | W03/W04 ใช้ baseline v1.0 แต่ W05 canonical เป็น v1.1 | IN-02; input register | Closed for W05 | ภานุวัฒน์ | เก็บ W03/W04 เป็น historical evidence; W05 ใช้ v1.1 เท่านั้น |
## Week 05 disposition

W05 is a V&V artifact, not a requirement that every product defect be fixed before submission. The component test set is complete when each selected requirement has a traceable test basis, actual result where executed, honest `Fail/Not Ready` status where implementation is missing, and a next action/owner.

Therefore W05-F01–F07 are handed off as real project gaps rather than hidden or converted to Pass. They must be revisited in ENGSE212 and in later ENGSE601 integration/system/NFR activities as applicable.

## Handoff to later weeks

- W06 Integration: consent endpoints, profile route contract, Visual Analysis service contract
- W07 System/UAT: end-to-end scan/result behavior after visual contract is fixed
- W08 Test Design Techniques: add partitions/boundaries around consent and visual outputs after contract stabilization
- W11 NFR: GPU inference time and model-performance evaluation conditions
- W14 Defect Management: promote unresolved W05-F01–F07 to formal defect records if still open

## Submission gate

Author-side Definition of Done is satisfied: canonical source/version pinned, 18 test cases defined, executable evidence stored, results not fabricated, findings dispositioned, AI use disclosed, and final PDF can be generated.

The team agreement still requires an independent human peer review before merge/tag as `Submitted`; reviewer assigned in `TEAM.md` is เอกพันธ์. Until that sign-off exists, repository status must be `Ready for Review`, not `Submitted`.
