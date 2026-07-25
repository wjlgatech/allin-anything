#!/usr/bin/env python3
"""Thin CLI over the router: `python3 scripts/route.py "<intent>"` prints the verdict."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from allin_anything import registry  # noqa: E402
from allin_anything.router import Router  # noqa: E402


def main() -> int:
    """Route the intent given as argv and print mode, targets, and reason."""
    if len(sys.argv) < 2:
        print('usage: route.py "<intent>"')
        return 2
    reg = registry.load(ROOT / "data" / "registry.yml")
    d = Router(reg).route(" ".join(sys.argv[1:]))
    print(f"mode: {d.mode}")
    print(f"satellites: {', '.join(d.satellite_ids) or '—'}")
    print(f"reason: {d.reason}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
