#!/usr/bin/env python3
"""Self-audit: score HOW this repo operates against data/ainative.yml.

Rules (no-evidence-means-no): a check that cannot run is 'not measured' —
excluded from the score AND blocks the gate. Exit non-zero below the gate.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def _read(rel: str) -> str:
    """Return the file's text, or '' if it does not exist (absence = no evidence)."""
    p = ROOT / rel
    return p.read_text() if p.exists() else ""


def data_is_source() -> tuple[bool, str]:
    """spec-as-data: registry exists and README carries a generated block."""
    ok = (ROOT / "data" / "registry.yml").exists() and "BEGIN GENERATED: satellites" in _read("README.md")
    return ok, "data/registry.yml + generated README block"


def makefile_check_target() -> tuple[bool, str]:
    """ready-is-a-gate: the repo has one deterministic finish line."""
    return "check:" in _read("Makefile"), "Makefile has a `check:` target"


def unmeasured_blocks_gate() -> tuple[bool, str]:
    """no-evidence-means-no: this auditor excludes and blocks on unmeasured items."""
    src = _read("scripts/ainative.py")
    return "not measured" in src and "unmeasured" in src, "auditor implements not-measured exclusion + block"


def generator_and_gate_separate() -> tuple[bool, str]:
    """maker-is-not-checker: generation and gating are independent code paths."""
    ok = (ROOT / "scripts" / "build.py").exists() and (ROOT / "tests").is_dir() and "--check" in _read("scripts/build.py")
    return ok, "build.py generates; --check + tests/ gate"


def no_vendored_satellites() -> tuple[bool, str]:
    """satellites-never-vendored: externals are pinned+licensed pointers, no vendor tree."""
    reg = yaml.safe_load(_read("data/registry.yml"))
    externals = [s for s in reg["satellites"] if s["kind"] == "external"]
    pinned = all(len(s.get("pinned_sha", "")) == 40 and s.get("license") for s in externals)
    no_vendor_dir = not (ROOT / "vendor").exists() and not (ROOT / "third_party").exists()
    return pinned and no_vendor_dir, f"{len(externals)} external(s) pinned+licensed; no vendor/ tree"


def news_ledger_alive() -> tuple[bool, str]:
    """compounding-memory: lessons land in data/news.yml, not chat."""
    news = yaml.safe_load(_read("data/news.yml") or "{}")
    n = len(news.get("entries", []))
    return n >= 1, f"data/news.yml has {n} entrie(s)"


def readme_honest_edges() -> tuple[bool, str]:
    """honest-edges: limitations are stated where users actually read."""
    return "## Honest edges" in _read("README.md"), "README contains `## Honest edges`"


def ci_has_no_publish() -> tuple[bool, str]:
    """human-gated-irreversible: CI only checks; shipping stays human."""
    wf = _read(".github/workflows/check.yml")
    return bool(wf) and "--approve" not in wf and "publish" not in wf, "check.yml exists and never publishes"


def audit_wired_to_ci() -> tuple[bool, str]:
    """repo-audits-itself: this audit is inside make check, and CI runs make check."""
    ok = "ainative" in _read("Makefile") and "make check" in _read(".github/workflows/check.yml")
    return ok, "audit runs in `make check`, CI runs `make check`"


CHECKS = {f.__name__: f for f in (
    data_is_source, makefile_check_target, unmeasured_blocks_gate, generator_and_gate_separate,
    no_vendored_satellites, news_ledger_alive, readme_honest_edges, ci_has_no_publish, audit_wired_to_ci,
)}


def run(gate: int) -> int:
    """Score every principle, print evidence, and gate: unmeasured or < gate exits 1."""
    spec = yaml.safe_load((ROOT / "data" / "ainative.yml").read_text())
    passed, measured, unmeasured = 0, 0, []
    for p in spec["principles"]:
        fn = CHECKS.get(p["check"])
        if fn is None:
            unmeasured.append(p["id"])
            print(f"  ? {p['id']:28s} not measured (no checker '{p['check']}')")
            continue
        ok, evidence = fn()
        measured += 1
        passed += ok
        print(f"  {'✓' if ok else '✗'} {p['id']:28s} {evidence}")
    score = round(100 * passed / measured) if measured else 0
    print(f"\nainative score: {score}/100 (gate {gate}; {measured} measured, {len(unmeasured)} unmeasured)")
    if unmeasured:
        print("✗ gate blocked: unmeasured items are never a pass")
        return 1
    return 0 if score >= gate else 1


if __name__ == "__main__":
    gate = int(sys.argv[sys.argv.index("--gate") + 1]) if "--gate" in sys.argv else 90
    raise SystemExit(run(gate))
