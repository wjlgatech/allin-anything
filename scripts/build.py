#!/usr/bin/env python3
"""Generate README blocks from data/*.yml. `--check` = drift gate (exit 1 on drift)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from allin_anything import generate, registry  # noqa: E402


def main() -> int:
    """Validate the registry, then regenerate README blocks (or drift-check with --check)."""
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail on drift instead of writing")
    args = ap.parse_args()

    reg = registry.load(ROOT / "data" / "registry.yml")
    errors = registry.validate(reg, ROOT)
    if errors:
        for e in errors:
            print(f"✗ registry: {e}")
        return 1

    readme = ROOT / "README.md"
    current = readme.read_text()
    rendered = generate.render_readme(current, reg, ROOT / "data" / "news.yml",
                                      ROOT / "docs" / "walkthroughs")

    if args.check:
        if rendered != current:
            print("✗ drift: README generated blocks do not match data/*.yml — run `make build`")
            return 1
        print("✓ no drift: README matches data/*.yml")
        return 0

    readme.write_text(rendered)
    print("✓ README regenerated from data/*.yml")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
