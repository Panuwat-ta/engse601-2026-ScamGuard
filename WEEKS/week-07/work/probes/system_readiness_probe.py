#!/usr/bin/env python3
"""Verify Week 07 source/test-document readiness without running the product."""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path


EXPECTED_SRS_SHA256 = "99bb8d5050fa54195b02869f1815e954fdd43ad0997e732b35426c70947cd40a"
EXPECTED_HISTORICAL_CODE_COMMIT = "66bc9e4af3747808ef45273d31b50dbc59ad91ab"
EXPECTED_DEVELOP_COMMIT = "162e0249abb9e9940f014ba6d5182d38213bc771"
EXPECTED_TEST_PLAN_SHA256 = "8bb43a9e074cd3a1191041a9da2ab88e6e71e2b15edaeac79b1631be3153c64b"
EXPECTED_E2E_SHA256 = "227c281117196dfb4ea4cdfc62e7891e4ba9eb53fdf68930f624f2df12a5b515"
EXPECTED_MANUAL_LOG_SHA256 = "dabb8fbf817f282698fee6a62e981583e3ed71c69d7d24394af014709c4c30ba"
EXPECTED_JUNIT_SHA256 = "95527df8fe72f85dca515838dd330fca90237d1328935d52086a7d1705ed4179"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def check(label: str, condition: bool, detail: str) -> bool:
    state = "CONFIRMED" if condition else "MISSING"
    print(f"[{state}] {label}: {detail}")
    return condition


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: system_readiness_probe.py <engse601-repo> <project-repo> <canonical-srs>"
        )

    engse = Path(sys.argv[1]).resolve()
    project = Path(sys.argv[2]).resolve()
    srs = Path(sys.argv[3]).resolve()

    test_plan = project / "Document/tests_doc/test_plan/README.md"
    e2e = project / "tests_all/manual_tests/test_cases_e2e.md"
    manual_log = project / "tests_all/tests_report/manual_tests/execution_log.md"
    junit = project / "tests_all/automate_tests/reports/junit.xml"
    develop_ref = project / ".git/refs/heads/develop"
    historical_snapshot = engse / "WEEKS/week-06/work/evidence/E06-source-contract-snapshot.txt"

    e2e_text = e2e.read_text(encoding="utf-8")
    manual_text = manual_log.read_text(encoding="utf-8")
    junit_text = junit.read_text(encoding="utf-8")
    snapshot_text = historical_snapshot.read_text(encoding="utf-8")
    develop_commit = develop_ref.read_text(encoding="utf-8").strip()

    checks = [
        check("canonical SRS hash", sha256(srs) == EXPECTED_SRS_SHA256, sha256(srs)),
        check(
            "historical Week 05-06 code commit",
            EXPECTED_HISTORICAL_CODE_COMMIT in snapshot_text,
            EXPECTED_HISTORICAL_CODE_COMMIT,
        ),
        check("develop ref", develop_commit == EXPECTED_DEVELOP_COMMIT, develop_commit),
        check("Master Test Plan hash", sha256(test_plan) == EXPECTED_TEST_PLAN_SHA256, sha256(test_plan)),
        check("E2E design hash", sha256(e2e) == EXPECTED_E2E_SHA256, sha256(e2e)),
        check("manual log hash", sha256(manual_log) == EXPECTED_MANUAL_LOG_SHA256, sha256(manual_log)),
        check("JUnit hash", sha256(junit) == EXPECTED_JUNIT_SHA256, sha256(junit)),
    ]

    scenario_ids = re.findall(r"^\| `?(TC-E2E-[A-Z]+-\d+)`? \|", e2e_text, flags=re.MULTILINE)
    checks.append(check("project E2E scenario count", len(scenario_ids) == 10, str(len(scenario_ids))))
    checks.append(
        check(
            "manual execution absent",
            "ยังไม่มีผลรัน manual จริง" in manual_text,
            "template rows only",
        )
    )
    checks.append(
        check(
            "current JUnit contains zero tests",
            'tests="0"' in junit_text,
            "tests=0; not a pass claim",
        )
    )

    print("[STATUS] Project E2E scenarios mapped: 10")
    print("[STATUS] System scenarios designed: 10; executed on pinned Week 07 build: 0")
    print("[STATUS] UAT scenarios designed: 6; executed: 0")
    print("[STATUS] NFR-06 participant metric requires 100 valid participants; observed: 0")
    print("[STATUS] This probe establishes document/readiness facts only; it is not a System Test/UAT result.")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
