#!/usr/bin/env python3
"""Thin CLI over the Chain 02 adapter: penecho ink PNG -> construction_gate JSON.

Usage: python3 scripts/ink2plan.py <export.png> <out.json> [--width-mm 5200] [--name n]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from allin_anything.adapters import penecho_floorplan  # noqa: E402


def main() -> int:
    """Parse args, convert, and print an honest one-line summary."""
    ap = argparse.ArgumentParser()
    ap.add_argument("png", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--width-mm", type=float, default=5200, help="declared width of the drawn outer boundary")
    ap.add_argument("--name", default="penecho-sketch")
    args = ap.parse_args()
    layout = penecho_floorplan.convert_file(args.png, args.out, args.width_mm, name=args.name)
    rooms = ", ".join(f"{r['name']}" for r in layout["rooms"])
    print(f"✓ {args.out}: {len(layout['rooms'])} rooms ({rooms}), "
          f"{len(layout['openings'])} openings @ {args.width_mm:.0f}mm wide")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
