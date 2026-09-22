# W07-03 - UAT Protocol and Questionnaire

## 1. UAT objective

Validate that intended users can complete the main ScamGuard journey, understand that the output is a preliminary risk assessment, interpret the heatmap and decide an appropriate next action without expert explanation.

## 2. Requirement basis and success metrics

| Metric | Requirement | Success threshold |
|---|---|---:|
| Overall satisfaction | NFR-06 AC-1 | mean >= 4.00/5.00 |
| Heatmap meaning Q1 | NFR-06 AC-2 | correct >= 80% |
| Red vs green Q2 | NFR-06 AC-2 | correct >= 80% |
| Heatmap usefulness Q3 | NFR-06 AC-2 | mean >= 4.00/5.00 |
| Understand without expert Q4 | NFR-06 AC-2 | Yes >= 80% |
| Required sample size | NFR-06 | 100 real participants |

No UAT metric is reported in this package because no participant session has occurred.

## 3. Participant and privacy protocol

- Target: general Android users representing ST01; 100 valid participants
- Exclude project team responses from the independent user metric or report them separately
- Provide purpose, voluntary participation, data use, retention and withdrawal notice before the session
- Do not collect real financial slips, faces or personal images; use approved synthetic/licensed test images
- Assign anonymous participant IDs; do not place names, emails or raw personal images in this repository
- Obtain explicit consent before screen/audio recording
- Facilitator must not explain heatmap answers before Q1-Q4 are completed
- Record accessibility needs, device/Android version and failed sessions without forcing completion

## 4. UAT scenarios

| ID | User task | Acceptance observation | Data captured | Status |
|---|---|---|---|---|
| W07-UAT-01 | Complete onboarding and register/login | user identifies required system consent and completes access without facilitator intervention | completion, assistance count, time, comment | Not Ready |
| W07-UAT-02 | Select or crop an approved suspicious-image sample and submit | user understands supported input and reaches processing/result state | completion, error/retry, time | Not Ready |
| W07-UAT-03 | Explain risk score and three evidence dimensions | user states that score is screening evidence, not a forensic/legal guarantee | correct/incorrect rubric, confidence | Not Ready |
| W07-UAT-04 | Inspect heatmap, toggle layer and adjust opacity | controls are usable and Q1-Q4 meet NFR-06 thresholds | Q1-Q4, task completion, issue note | Not Ready |
| W07-UAT-05 | Find the prior scan and submit a scam report | user finds history item, understands category and sees confirmation | completion, time, confusion/error | Not Ready |
| W07-UAT-06 | Complete satisfaction and safety debrief | participant gives 1-5 ratings and identifies safe next action | satisfaction items, free text, adverse event | Not Ready |

## 5. Canonical heatmap questions

Ask these before giving explanatory feedback:

1. บริเวณสีแดงสื่อความหมายถึงอะไร?
   - Correct rubric: จุดที่ระบบประเมินว่าเสี่ยงว่าถูกดัดแปลง
2. เปรียบเทียบสีแดงกับสีเขียว ส่วนใดน่าเชื่อถือมากกว่า?
   - Correct rubric: สีเขียว
3. Heatmap ช่วยให้ท่านมั่นใจในการแยกแยะสลิปปลอมมากขึ้นเพียงใด?
   - Likert 1-5
4. ท่านเข้าใจแผนที่ความร้อนโดยไม่ต้องให้ผู้เชี่ยวชาญอธิบายหรือไม่?
   - Yes/No

Additional non-leading items:

- ความง่ายในการเลือกและส่งรูปภาพ: 1-5
- ความชัดเจนของคะแนนความเสี่ยงและคำอธิบาย: 1-5
- ความมั่นใจว่าทราบว่าควรทำอะไรต่อ: 1-5
- ความพึงพอใจโดยรวม: 1-5
- จุดใดทำให้สับสนหรือไม่มั่นใจ: free text
- หากระบบระบุความเสี่ยงสูง ท่านจะทำอะไรต่อ: free text/safe-action rubric

## 6. Analysis rules

- Denominator is valid completed responses; report excluded/abandoned sessions separately
- Do not replace missing answers with neutral values
- Report count, denominator, mean and distribution for each Likert item
- Report correct count/denominator/percentage for Q1-Q2 and Yes count/denominator/percentage for Q4
- Preserve negative comments and accessibility failures; do not remove outliers solely to improve scores
- A threshold miss is a Fail against that criterion, not a reason to change the target after collection

## 7. Human execution gate

UAT can begin only after the approved build, test-data package, facilitator script, privacy/consent text, recruitment list and issue-escalation process are reviewed by humans. Peer review of this plan does not substitute for participant consent or stakeholder acceptance.
