# Week 05 Submission and Revision Record

## Original submission (v1)

Status: Submitted

Artifact:

- `W05_ScamGuard_Component-Test-Case-Set_v1.pdf`

Repository record:

- PR #5 merged into `main`
- Merge commit: `ca354a8`
- Tag: `w05-submission-v1`
- GitHub recorded independent review at verification time: none

The v1 artifact remains the historical submission evidence and is not overwritten by later documentation improvements.

## Documentation revision (v2)

Status: Revision Candidate

Artifact:

- `W05_ScamGuard_Component-Test-Case-Set_v2.pdf`

v2 follows the Week 04 evidence-package layout and improves report structure, terminology, traceability, evidence classification and page layout. It keeps the same frozen SRS/code baseline, raw evidence and 18 result statuses as v1.

## Verification coverage

The Week 05 evidence set contains:

- canonical SRS v1.1 pinned to `Document/srs` on `main`
- ENGSE212 code baseline pinned to commit `66bc9e4a`
- ENGSE212 testing input cross-check pinned to `develop` commit `162e0249abb9e9940f014ba6d5182d38213bc771`
- 18 traceable component test cases
- source contract snapshot: `../work/evidence/E05-source-contract-snapshot.txt`
- API route inventory: `../work/evidence/E05-route-inventory.txt`
- schema/model snapshot: `../work/evidence/E05-schema-contract.txt`
- raw automated/probe output under `../work/evidence/`
- reproducible component probe at `../work/probes/component_probe.py`
- findings W05-F01 through W05-F08 with status, owner and next action
- AI Use Declaration
- peer-review record with unresolved fields left pending rather than inferred

The `develop/tests_all` cross-check is supporting evidence only. It does not retroactively replace the Week 05 source baseline or its 7 Pass / 9 Fail / 1 Not Ready / 1 Needs Clarification results. Later `develop` reports must be treated as re-test candidates because their recorded metadata does not establish the same commit/build/environment.

Independent peer-review sign-off is still not present in the repository. Therefore v2 must not be described as peer-reviewed or newly submitted until a real review/merge/tag event is recorded.
