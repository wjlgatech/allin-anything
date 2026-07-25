#!/usr/bin/env python3
"""Thin CLI over AutoRunner: `python3 scripts/autorun.py chain-02` (or --list)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from allin_anything import chains as chains_mod  # noqa: E402
from allin_anything import registry  # noqa: E402
from allin_anything.autorun import AutoRunner  # noqa: E402


def main() -> int:
    """List chains or run one bounded chain, printing the honest report."""
    reg = registry.load(ROOT / "data" / "registry.yml")
    chains = chains_mod.load(ROOT / "data" / "chains.yml")
    if len(sys.argv) < 2 or sys.argv[1] == "--list":
        for c in chains:
            print(f"{c.id}  [{c.autonomy:19s}] {c.title}")
        return 0
    report = AutoRunner(reg, chains, ROOT).run(sys.argv[1])
    if report.mode == "refused":
        print(f"✗ REFUSED: {report.reason}")
        return 1
    for s in report.steps:
        mark = {"ok": "✓", "failed": "✗", "blocked-missing-local": "⛔"}[s.status]
        print(f"{mark} [{s.status}] {' '.join(s.cmd)} (cwd {s.cwd}, exit {s.exit_code})")
        if s.tail:
            print("    " + s.tail.replace("\n", "\n    "))
    print("\n⏸ execution stops here — human owns:")
    for g in report.human_gates:
        print(f"  🔑 {g}")
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
