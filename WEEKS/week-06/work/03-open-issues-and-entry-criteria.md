# W06-03 — Open Issues and Entry Criteria

## Integration findings from interface reading

| ID | Finding | Trace | Impact on Week 06 | Status | Owner | Next action |
|---|---|---|---|---|---|---|
| W06-F01 | Mobile มี DELETE `/scan/{id}` สำหรับ cancel แต่ backend scan router มีเฉพาะ POST/GET | I01, W06-IT-04 | cancel contract ทดสอบ acceptance ไม่ได้ | Not Ready | ภานุวัฒน์ | ตัดสินว่าจะ implement cancel endpoint หรือถอด/disable client action แล้วเพิ่ม contract test |
| W06-F02 | Cache เก็บ analysis object หลังถอด `heatmap_bytes`; media file อยู่ filesystem แยกจาก Redis | I02/I05, W06-IT-05/07/13/14 | cache hit อาจคืน result ที่ media file หายหรือ path ใช้ไม่ได้ | Open | ภานุวัฒน์ | เพิ่ม integration case สำหรับ cache/media consistency และกำหนด recovery behavior |
| W06-F03 | Source Verification ตาม SRS ยังไม่มี Google Vision integration; ScanService ใช้ `DEFAULT_SOURCE_SCORE` | FR-ANALYSIS-03 AC-1–4, I04 | positive/fallback source tests ไม่มี production interface และ current total score อาจรวม source ที่ไม่มี evidence | Not Ready | ภานุวัฒน์ | implement source adapter/fallback ตาม SRS หรือออก controlled baseline change ก่อน re-test |
| W06-F04 | SRS heatmap contract คือ `/uploads/{filename}` แต่ backend persist filesystem path แล้วพึ่ง mobile normalize URL | FR-XAI-01 AC-1, I05 | contract กระจายข้าม server/client และเสี่ยงเมื่อมี consumer อื่น | Open | ภานุวัฒน์ | ทดสอบ end-to-end media reference และกำหนด API response contract ให้ชัด |
| W06-F05 | History SRS ใช้ `start_date/end_date/risk_grade`; backend route ใช้ `keyword/risk_level` และไม่มี date range | FR-HISTORY-01 AC-2/3, I06 | acceptance test ตาม SRS ยังไม่พร้อม | Not Ready | ภานุวัฒน์ | reconcile query contract และเพิ่ม API integration tests |
| W06-F06 | W05 visual output contract ยังไม่แยก forgery/AI-Gen signal ตาม SRS | FR-ANALYSIS-02, I03 | integration test ทำได้เฉพาะ characterization ของ current contract ไม่ใช่ requirement pass | Open dependency | ภานุวัฒน์ | carry W05 finding จน component contract ถูกแก้แล้ว re-run I03 |

## Entry criteria for integration execution

- Canonical SRS/version และ code commit ต้อง pin ชัดก่อนรัน
- Test DB, Redis และ upload directory ต้องเป็น isolated/test environment
- ห้ามใช้ production credential, production database หรือ production uploads
- External services ต้องใช้ sandbox/stub ที่ deterministic เว้นแต่ test case ระบุชัดว่าต้องทดสอบ real adapter
- Case ที่พึ่ง interface ที่ยังไม่มีให้คง `Not Ready`; ห้ามสร้าง mock contract ที่ไม่มีใน requirement แล้วนับเป็น Pass

## Exit criteria for Week 06 artifact

- Interface map ครอบคลุม critical producer/consumer และ dependency ที่ส่งต่อจาก Week 05
- ทุก integration test มี requirement trace, stimulus, expected integration behavior, technique และ status
- ทุก `Not Ready` มี blocker/owner/next action
- ไม่มี Pass/Fail ที่ไม่ได้ execute จริง
- มี peer review ก่อนเปลี่ยนเป็น Submitted ตาม `TEAM.md`
- AI Use Declaration ระบุขอบเขตการใช้และวิธี verify กับ artifact จริง

## Handoff to later weeks

- W06-F03 และ W06-F06 ส่งผลโดยตรงต่อ system/UAT result; ต้องไม่ซ่อนด้วย mock เมื่อไป Week 07
- W06-F02/F04 ควรถูกใช้เป็น test-data/environment requirement สำหรับ heatmap/cache scenarios
- Defect ที่ reproduce ได้จาก execution ภายหลังควรถูกส่งต่อ defect/metric work โดยเก็บ trace จาก W06 test ID เดิม
