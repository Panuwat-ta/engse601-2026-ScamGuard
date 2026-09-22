# W05 - AI Use Declaration

## Declaration summary

| Item | Record |
|---|---|
| Week / artifact | Week 05 / Component Test Case Set |
| AI used | Yes |
| Tool/model as known | ChatGPT GPT-5.6 Sol + Remote Desktop Commander |
| Primary author / verifier | ภานุวัฒน์ |
| Verification date | 2026-09-22 |

## How AI was used

AI assisted with:

- reading and organizing canonical SRS v1.1 requirements relevant to Week 05
- Code & Logic Reading Clinic and component-scope selection
- structuring component test cases and traceability
- executing/reviewing read-only local probes and test output
- comparing observed code/API contracts with expected SRS contracts
- organizing findings, downstream handoff and documentation-quality revision v2

## Inputs and authoritative sources

- Canonical SRS: `/home/panuwat/project/Document/srs/`, branch `main`
- Public canonical reference: https://github.com/Panuwat-ta/project/tree/main/Document/srs
- ENGSE212 source repository: https://github.com/Panuwat-ta/project
- Source baseline: branch `main`, commit `66bc9e4a`
- W03/W04 evidence was used only as historical handoff and did not override SRS v1.1

## Human verification and safeguards

All expected results were checked against canonical SRS v1.1. Actual results were accepted only when supported by stored execution output or direct source/schema/route inspection on the frozen baseline.

The following AI-generated or AI-suggested actions were explicitly rejected:

- inventing thresholds or requirement behavior not present in the canonical SRS
- generating model Accuracy/F1/mDice or performance results that were not executed
- converting missing endpoints or missing contracts into Pass results
- inferring stakeholder approval or peer-review sign-off from a merge event
- exposing `.env`, token, API key, password or production database content

The component probe uses test-only environment values and an in-memory fake DB. No production secret is stored in the evidence repository.

## Result integrity statement

Week 05 records 18 cases: 7 Pass, 9 Fail, 1 Not Ready and 1 Needs Clarification. These counts come from the documented test/probe/inspection evidence and were not altered for the v2 documentation revision.

No test result, screenshot, stakeholder decision, product metric, approval or reviewer sign-off was fabricated.
