# Week 07 Submission Candidate

Status: Ready for Review

Artifact:

- `W07_ScamGuard_System-UAT-Scenarios_v1.pdf`

Coverage:

- canonical SRS v1.1 and SHA-256 pinned
- frozen ENGSE212 `main` source baseline commit `66bc9e4a` retained as historical Week 05-06 risk evidence
- project testing baseline `develop/tests_all` pinned to commit `162e0249abb9e9940f014ba6d5182d38213bc771`
- 10 canonical project E2E journeys
- 10 System Test scenarios mapped one-to-one to `TC-E2E-SCAN-01` through `TC-E2E-HIST-10`
- 6 UAT scenarios with privacy protocol, canonical heatmap questions and NFR-06 metrics
- execution register: 10 System Test Not Executed + 6 UAT Not Ready; no fabricated Pass/Fail
- readiness findings W07-F01-F09 with owner and next action
- reproducible readiness probe and raw output
- AI Use Declaration and peer-review gate
- PDF render/structure verification

The official Week 07 course template/file naming was still pending in the repository at authoring time. This candidate is course-scope aligned but must be compared with the official release. Historical automated reports under `develop/tests_all` are supporting evidence only because they do not pin the same build metadata; the current JUnit artifact contains zero tests and the manual execution log has no real rows. Independent peer review, pinned-build System Test execution, UAT decision/execution, NFR-06 measurement with 100 valid participants, merge/tag and actual submission are still pending; therefore no Submitted/Accepted/Passed claim is made.
