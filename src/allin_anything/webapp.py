"""Demo webapp handlers — pure functions over the engine (the HTTP shell stays thin).

Every endpoint is backed by the REAL engine: the deterministic Router, the gate-verified
registry, the chain library, and the bounded AutoRunner. Nothing is mocked; the security
boundary is a whitelist (known chain ids only, autonomous_bounded only, capped inputs).
"""

from __future__ import annotations

from pathlib import Path

from . import chains as chains_mod
from . import registry
from .autorun import AutoRunner
from .models import Registry
from .router import Router

MAX_INTENT_LEN = 300
PENECHO_URL = "http://127.0.0.1:3888/"


class DemoApp:
    """Loads the spec-as-data once and answers demo queries from it."""

    def __init__(self, root: Path):
        self.root = root
        self.reg: Registry = registry.load(root / "data" / "registry.yml")
        self.chains = chains_mod.load(root / "data" / "chains.yml")
        self.router = Router(self.reg)
        self.runner = AutoRunner(self.reg, self.chains, root)

    def route(self, intent: str) -> dict:
        """Point 1 — one front door: a real router verdict, statuses disclosed."""
        intent = str(intent)[:MAX_INTENT_LEN]
        if not intent.strip():
            return {"error": "give me an intent"}
        d = self.router.route(intent)
        return {"intent": intent, "mode": d.mode, "satellites": list(d.satellite_ids), "reason": d.reason}

    def registry_summary(self) -> dict:
        """Point 2 — no badge without a gate: the live ladder, computed not claimed."""
        by = {"integrated": [], "digested": [], "candidate": []}
        for s in self.reg.sorted():
            by.setdefault(s.status, []).append(
                {"id": s.id, "role": s.role, "capability": s.capability,
                 "private": s.visibility == "private", "notes": s.notes})
        chains_n = len(list((self.root / "docs" / "walkthroughs").glob("*.md")))
        greens = len(by["integrated"])
        return {"counts": {k: len(v) for k, v in by.items()}, "satellites": by,
                "chains": chains_n, "verified_reach": greens * chains_n}

    def chain_list(self) -> dict:
        """Point 3 — chains across the digital↔physical border, autonomy per chain."""
        return {"chains": [
            {"id": c.id, "title": c.title, "autonomy": c.autonomy,
             "satellites": list(c.satellites), "human_gates": list(c.human_gates),
             "walkthrough": f"docs/walkthroughs/{c.walkthrough}"}
            for c in self.chains]}

    def penecho_bridge(self) -> dict:
        """Point 5 — the pen→digital bridge: penecho runs UPSTREAM (AGPL, never vendored).

        Reports the pin and, if a locally-started upstream instance is up, says so.
        Offline-safe: no instance just means running=False — never an error.
        """
        s = next((x for x in self.reg.satellites if x.id == "penecho"), None)
        running = False
        try:
            import urllib.request

            with urllib.request.urlopen(PENECHO_URL, timeout=0.8) as r:
                running = r.status == 200
        except Exception:
            running = False
        return {
            "pinned_sha": (s.pinned_sha if s else "") or "",
            "license": (s.license if s else "") or "",
            "rule": "run upstream from its own repo — pointer + pinned digest only, never vendored (AGPL-3.0-only)",
            "url": PENECHO_URL,
            "running": running,
            "checkout": (self.root.parent / "penecho").exists(),
            "launch": "cd ~/Documents/Projects/penecho && node cli.js --claude --port 3888",
        }

    def autorun(self, chain_id: str) -> dict:
        """Point 4 — bounded autonomy: really run a chain; refusals are the feature."""
        known = {c.id for c in self.chains}
        if chain_id not in known:  # whitelist — no arbitrary execution surface
            return {"mode": "refused", "reason": f"unknown chain (allowed: {sorted(known)})"}
        report = self.runner.run(chain_id)
        return {"chain": chain_id, "mode": report.mode, "reason": report.reason,
                "ok": report.ok,
                "steps": [{"cmd": " ".join(s.cmd), "cwd": s.cwd, "status": s.status,
                           "exit_code": s.exit_code, "tail": s.tail} for s in report.steps],
                "human_gates": list(report.human_gates)}
