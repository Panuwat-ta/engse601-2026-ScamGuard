# W07-02 - System Test Scenarios

## Status vocabulary

- `Not Executed`: design and oracle are ready, but no integrated-system run occurred
- `Not Ready`: a required environment, dataset, participant or decision is missing
- `Pass` / `Fail`: may be used only after raw execution evidence exists

All twelve scenarios below are `Not Executed`. Static source/probe evidence is used only for readiness and risk, not as an end-to-end result.

## System scenarios

| ID | Requirement trace | Scenario and precondition | Procedure summary | Acceptance oracle | Evidence required | Status |
|---|---|---|---|---|---|---|
| W07-ST-01 | FR-AUTH-01 AC-1/5; FR-PDPA-01 | New user; unique email; consent screen available | Try registration with system consent false, then true; research consent optional | false is rejected; true creates user and timestamped consent without exposing password/hash | sanitized HTTP log, DB/consent record extract, screen capture | Not Executed |
| W07-ST-02 | FR-AUTH-02-04; NFR-04 AC-2 | Active user and controlled token clock | Login, access protected route, refresh, logout, retry old access | valid login succeeds; access TTL 15 min; invalid/expired token rejected; logout behavior matches SRS | sanitized token claims, HTTP log, screen capture | Not Executed |
| W07-ST-03 | FR-SCAN-01 AC-1/2/3 | Android build with gallery permission | Select image, crop, repeat and skip crop | selected/cropped/original preview matches user choice without corrupting source | device video/screens, original/cropped checksums | Not Executed |
| W07-ST-04 | FR-SCAN-02 AC-1 | valid JPG/PNG/WebP within client/server/pixel limits | Upload, capture response, poll until terminal state | initial HTTP 202 with scan id; owned polling exposes id/status/progress and terminal result | HTTP transcript, timestamps, scan record | Not Executed |
| W07-ST-05 | FR-SCAN-02 AC-2/3/4 | unsupported, oversize and over-resolution controlled files | Attempt each invalid upload from client and direct API | each is rejected with the SRS-aligned message/status before analysis | file metadata/checksum, client/API response | Not Executed |
| W07-ST-06 | FR-SCAN-03; NFR-01 AC-1/2 | Redis enabled; identical consented image | Scan once, then repeat; time both; inspect cache flag/lifecycle | miss performs analysis; hit reuses usable result/heatmap; hit <=3 s; TTL 30 days | Redis-safe key/TTL evidence, timing log, API bodies | Not Executed |
| W07-ST-07 | FR-ANALYSIS-01-04 | ground-truth image set for OCR/visual/source | Run full pipeline for text, forgery/AI-gen, source and risk examples | outputs and Hybrid max+bonus grade match SRS; unavailable source is excluded and disclosed | dataset manifest, model/build id, raw result JSON | Not Executed |
| W07-ST-08 | FR-XAI-01 AC-1-5 | completed scan with original and heatmap | Open result, toggle overlay, set opacity 0/50/100, zoom and pan | correct base/heatmap alignment; controls work; red/yellow/green legend and breakdown visible | device recording, image URLs/checksums, accessibility notes | Not Executed |
| W07-ST-09 | FR-HISTORY-01 AC-1-5 | user owns several scans across dates/grades | list, paginate, search/filter, open detail, delete one, delete all | newest-first/pagination/filter behavior matches SRS; only owned records/files are removed | API/UI capture, before/after DB/media evidence | Not Executed |
| W07-ST-10 | FR-HISTORY-02 AC-1-4 | owned completed scan not yet reported | submit each category; try duplicate and unauthorized scan | first valid report HTTP 201/pending; duplicate HTTP 409; unauthorized rejected | HTTP log, report record, admin queue capture | Not Executed |
| W07-ST-11 | FR-PDPA-01 AC-1-6 | user with system/research consent and scan history | view/update consent, view logs/data, delete account after password confirmation | system consent immutable as defined; research withdrawal logged; permitted personal data removed/anonymized | consent/account audit evidence with PII redacted | Not Executed |
| W07-ST-12 | NFR-04; cross-user authorization | User A and User B; controlled failure injection | B requests A scan/history; force model/source/cache failures; retry/recover | 403/404 prevents disclosure; failures have honest state/message and no false completed result | HTTP log, app error capture, server correlation id | Not Executed |

## Known execution risks carried forward

| Scenario | Frozen-baseline fact | Execution treatment |
|---|---|---|
| ST-01 | Week 05 found `system_consent=false` was not rejected | execute as a high-priority negative test; do not expect Pass without re-baseline/retest |
| ST-04 | Week 06 observed POST scan returned 200 rather than SRS 202 | record actual status; do not normalize it in the report |
| ST-06/ST-08 | cache and heatmap lifecycle gaps exist | require both cache data and media reference evidence |
| ST-07 | separate forgery/AI-gen contract and production source adapter were incomplete | mark affected steps Not Ready if build still lacks them |
| ST-09/ST-10 | history filters/response and report response differed from SRS/consumer assumptions | capture full request/response contract |

## Execution record template

For each actual run, append a dated record containing build id, environment, tester, input checksum, expected/actual result, status, raw evidence path and defect id. Do not overwrite this design table with an unsupported Pass/Fail value.
