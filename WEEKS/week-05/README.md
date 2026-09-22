# Week 05 — Component / Unit Testing

สถานะ: Submitted

## เป้าหมาย

ออกแบบและรัน Component Test Case Set จาก requirement/acceptance criteria และ code/logic จริงของ ScamGuard โดยเก็บทั้งผล Pass และ defect/gap ที่ตรวจพบเป็นหลักฐาน V&V อย่างตรวจย้อนกลับได้

## Test basis

- Canonical Requirement/SRS: https://github.com/Panuwat-ta/project/tree/main/Document/srs
- Branch: `main`
- SRS: `05_Software_Requirement_Specification.md` v1.1 (2026-09-12)
- Source code: https://github.com/Panuwat-ta/project
- Code baseline: branch `main`, commit `66bc9e4a`
- Primary scope: FR-ANALYSIS-02, FR-ANALYSIS-04, FR-AUTH-01, FR-PDPA-01

## Result summary

- 18 test cases
- Pass: 7
- Fail: 9
- Not Ready: 1
- Needs Clarification: 1
- Existing automated test execution: `1 passed in 0.03s`
## Work artifacts

- `work/01-component-scope.md`
- `work/02-component-test-cases.md`
- `work/03-existing-test-evidence.md`
- `work/04-open-issues-and-decisions.md`
- `work/05-peer-review.md`
- `work/06-submission-source.md`
- `work/ai-use-declaration.md`
- `work/probes/component_probe.py`
- `work/evidence/E05-baseline.txt`
- `work/evidence/E05-pytest-component.txt`
- `work/evidence/E05-component-probe.txt`
- `work/evidence/E05-pdf-check.txt`

## Submission artifact

- `submission/W05_ScamGuard_Component-Test-Case-Set_v1.pdf`

Submission closure: PR #5 was merged into `main` at commit `ca354a8` and tag `w05-submission-v1` points to that merge commit. GitHub reports no recorded PR review, and `work/05-peer-review.md` still has pending reviewer fields; therefore the artifact is Submitted but is not represented as independently peer-reviewed.
