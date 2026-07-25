"""AutoRunner — bounded autonomous execution of 🟢-only chains (M8).

Boundaries, enforced in code:
- Only chains marked `autonomous_bounded` run; anything else is REFUSED with the reason.
- Satellite statuses are re-checked at run time (a demotion revokes autonomy immediately).
- A missing sibling checkout is an honest BLOCKED, never a fake pass.
- Every run appends to runs/journal.jsonl (observability: attributable, auditable).
- Execution ALWAYS stops before the declared human gates — the runner never owns them.
"""

from __future__ import annotations

import json
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

from .chains import Chain
from .models import Registry


@dataclass(frozen=True)
class StepResult:
    cmd: tuple[str, ...]
    cwd: str
    status: str            # "ok" | "failed" | "blocked-missing-local"
    exit_code: int | None
    tail: str


@dataclass(frozen=True)
class RunReport:
    chain_id: str
    mode: str              # "executed" | "refused"
    reason: str
    steps: tuple[StepResult, ...]
    human_gates: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return self.mode == "executed" and all(s.status == "ok" for s in self.steps)


class AutoRunner:
    """Executes bounded chains; refuses everything the evidence doesn't support."""

    def __init__(self, reg: Registry, chains: tuple[Chain, ...], repo_root: Path,
                 projects_root: Path | None = None):
        self._reg = reg
        self._chains = {c.id: c for c in chains}
        self._root = repo_root
        self._projects = projects_root or repo_root.parent

    def _resolve(self, cwd: str) -> Path:
        if cwd == ".":
            return self._root
        if cwd.startswith("projects/"):
            return self._projects / cwd.split("/", 1)[1]
        return self._root / cwd

    def run(self, chain_id: str, timeout: int = 300, journal: bool = True) -> RunReport:
        """Run one chain's machine steps; stop at failure, blockage, or the human gate."""
        chain = self._chains.get(chain_id)
        if chain is None:
            return RunReport(chain_id, "refused", f"unknown chain '{chain_id}'", (), ())
        if chain.autonomy != "autonomous_bounded":
            return RunReport(chain_id, "refused",
                             f"chain is '{chain.autonomy}' — autonomy is earned per-chain, not assumed",
                             (), chain.human_gates)
        by_id = {s.id: s for s in self._reg.satellites}
        for sid in chain.satellites:
            if by_id[sid].status != "integrated":
                return RunReport(chain_id, "refused",
                                 f"'{sid}' is {by_id[sid].status} — a demotion revokes autonomy",
                                 (), chain.human_gates)
        results: list[StepResult] = []
        for step in chain.steps:
            cwd = self._resolve(step.cwd)
            if not cwd.is_dir():
                results.append(StepResult(step.cmd, step.cwd, "blocked-missing-local", None,
                                          f"missing local checkout: {cwd}"))
                break
            proc = subprocess.run(step.cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
            tail = "\n".join((proc.stdout + proc.stderr).strip().splitlines()[-3:])
            results.append(StepResult(step.cmd, step.cwd,
                                      "ok" if proc.returncode == 0 else "failed",
                                      proc.returncode, tail))
            if proc.returncode != 0:
                break
        report = RunReport(chain_id, "executed", "bounded run complete", tuple(results), chain.human_gates)
        if journal:
            self._journal(report)
        return report

    def _journal(self, report: RunReport) -> None:
        """Append an auditable record of what actually ran (observability seam)."""
        runs = self._root / "runs"
        runs.mkdir(exist_ok=True)
        entry = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                 "chain": report.chain_id, "mode": report.mode, "ok": report.ok,
                 "steps": [{"cmd": list(s.cmd), "cwd": s.cwd, "status": s.status,
                            "exit_code": s.exit_code} for s in report.steps]}
        with (runs / "journal.jsonl").open("a") as fh:
            fh.write(json.dumps(entry) + "\n")
