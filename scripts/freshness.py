#!/usr/bin/env python3
"""Freshness gate for external satellite pins (M9): STALE is measured, never promised.

Compares each external satellite's pinned_sha against its remote HEAD (`git ls-remote`).
Exit 1 if any pin is stale — the weekly workflow turns that into a human-gated issue;
this script NEVER updates a pin itself.
"""

from __future__ import annotations

import subprocess
import sys
from collections.abc import Callable
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from allin_anything import registry  # noqa: E402


def remote_head(url: str) -> str:
    """Resolve a remote's HEAD sha (network); raises on failure."""
    out = subprocess.run(["git", "ls-remote", url, "HEAD"],
                         capture_output=True, text=True, timeout=60, check=True)
    return out.stdout.split()[0]


def check(resolver: Callable[[str], str] = remote_head) -> tuple[int, list[str]]:
    """Return (exit_code, report_lines). Unreachable remote = not measured => stale-flagged."""
    reg = registry.load(ROOT / "data" / "registry.yml")
    lines, stale = [], 0
    for s in reg.satellites:
        if s.kind != "external":
            continue
        try:
            head = resolver(s.url)
        except Exception as exc:  # no evidence => flagged, never a silent pass
            lines.append(f"? {s.id}: remote unreachable ({exc}) — not measured, treat as needs-review")
            stale += 1
            continue
        if head == s.pinned_sha:
            lines.append(f"✓ {s.id}: pin {s.pinned_sha[:7]} == remote HEAD (fresh)")
        else:
            lines.append(f"✗ {s.id}: STALE — pinned {s.pinned_sha[:7]}, remote HEAD {head[:7]} "
                         f"(re-digest before re-pinning; a pin update is a human decision)")
            stale += 1
    return (1 if stale else 0), lines


if __name__ == "__main__":
    code, lines = check()
    print("\n".join(lines))
    raise SystemExit(code)
