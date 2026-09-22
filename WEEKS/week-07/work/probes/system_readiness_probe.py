#!/usr/bin/env python3
"""Verify Week 07 baseline/readiness facts without executing the product system."""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path


EXPECTED_SRS_SHA256 = "99bb8d5050fa54195b02869f1815e954fdd43ad0997e732b35426c70947cd40a"
EXPECTED_CODE_COMMIT = "66bc9e4af3747808ef45273d31b50dbc59ad91ab"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def check(label: str, condition: bool, detail: str) -> None:
    state = "CONFIRMED" if condition else "MISSING"
    print(f"[{state}] {label}: {detail}")


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: system_readiness_probe.py <engse601-repo> <canonical-srs>")

    repo = Path(sys.argv[1]).resolve()
    srs = Path(sys.argv[2]).resolve()
    evidence = repo / "WEEKS/week-06/work/evidence"
    source_snapshot = (evidence / "E06-source-contract-snapshot.txt").read_text(encoding="utf-8")
    route_inventory = (evidence / "E06-route-inventory.txt").read_text(encoding="utf-8")
    schema_snapshot = (evidence / "E06-schema-contract.txt").read_text(encoding="utf-8")

    actual_srs_sha = sha256(srs)
    check("canonical SRS hash", actual_srs_sha == EXPECTED_SRS_SHA256, actual_srs_sha)
    check("frozen main commit", EXPECTED_CODE_COMMIT in source_snapshot, EXPECTED_CODE_COMMIT)
    check("POST scan route captured", '@router.post("/", response_model=ScanResponse)' in route_inventory, "POST /scan/")
    check("GET scan route captured", '@router.get("/{scan_id}", response_model=ScanResponse)' in route_inventory, "GET /scan/{id}")
    scan_routes = route_inventory.split("[server/app/api/v1/history.py]")[0]
    check("DELETE scan route absent", '@router.delete("/{scan_id}")' not in scan_routes, "consumer cancel contract gap")
    check("scan status/progress schema", "status: str" in schema_snapshot and "progress: int" in schema_snapshot, "polling fields")
    check("source fallback gap", "source_score = settings.DEFAULT_SOURCE_SCORE" in source_snapshot, "frozen baseline uses default score")
    check("heatmap path gap", "scan.heatmap_image_url = heatmap_path" in source_snapshot, "filesystem path stored")
    check("history filter gap", "start_date" not in route_inventory and "end_date" not in route_inventory, "date filters absent")
    check("report HTTP 201 captured", "status_code=201" in source_snapshot, "POST /reports")

    print("[STATUS] System scenarios designed: 12; executed: 0")
    print("[STATUS] UAT scenarios designed: 6; executed: 0; required participants: 100")
    print("[STATUS] This probe establishes readiness facts only; it is not a System Test/UAT result.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
