#!/usr/bin/env python3
"""Export the remote-demo data snapshot (webapp/static-data.json).

The deployed (Vercel) demo serves the same UI as `make demo`, but over this build-time
snapshot: registry ladder + reach, chain library, routing triggers (so the router demo runs
client-side over the SAME data), and recorded evidence where local execution would be.
Run by `make build`; freshness is drift-gated by tests/test_webapp.py.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from allin_anything.webapp import DemoApp  # noqa: E402


def main() -> int:
    app = DemoApp(ROOT)
    evidence = yaml.safe_load((ROOT / "data" / "evidence.yml").read_text())
    reg = yaml.safe_load((ROOT / "data" / "registry.yml").read_text())
    routing = [
        {"id": s["id"], "status": s["status"], "triggers": s.get("triggers", [])}
        for s in reg["satellites"]
    ]
    penecho_pin = next(s.get("pinned_sha", "") for s in reg["satellites"] if s["id"] == "penecho")
    out = {
        "exported_registry_version": reg["version"],
        "registry": app.registry_summary(),
        "chains": app.chain_list(),
        "routing": routing,
        "evidence": evidence,
        "penecho": {
            "pinned_sha": penecho_pin,
            "license": "AGPL-3.0-only",
            "rule": "run upstream from its own repo — pointer + pinned digest only, never vendored (AGPL-3.0-only)",
            "upstream": "https://github.com/penecho/penecho",
        },
    }
    (ROOT / "webapp" / "static-data.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(f"✓ webapp/static-data.json exported (reach {out['registry']['verified_reach']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
