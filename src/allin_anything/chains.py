"""Load and validate the chain library (data/chains.yml) — spec-as-data for M8 autonomy."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

from .models import Registry

AUTONOMY_LEVELS = ("assisted", "autonomous_bounded")


@dataclass(frozen=True)
class Step:
    cwd: str
    cmd: tuple[str, ...]


@dataclass(frozen=True)
class Chain:
    id: str
    title: str
    walkthrough: str
    satellites: tuple[str, ...]
    autonomy: str
    human_gates: tuple[str, ...] = ()
    steps: tuple[Step, ...] = field(default_factory=tuple)


def load(path: Path) -> tuple[Chain, ...]:
    raw = yaml.safe_load(path.read_text())
    chains = []
    for c in raw.get("chains", []):
        chains.append(Chain(
            id=c["id"], title=c["title"], walkthrough=c["walkthrough"],
            satellites=tuple(c["satellites"]), autonomy=c["autonomy"],
            human_gates=tuple(c.get("human_gates", ())),
            steps=tuple(Step(cwd=s["cwd"], cmd=tuple(s["cmd"])) for s in c.get("steps", ())),
        ))
    return tuple(chains)


def validate(chains: tuple[Chain, ...], reg: Registry, repo_root: Path) -> list[str]:
    """Gate rules: real walkthroughs, known satellites, autonomy earned not asserted."""
    errors: list[str] = []
    known = {s.id: s for s in reg.satellites}
    seen: set[str] = set()
    for c in chains:
        where = f"chain '{c.id}'"
        if c.id in seen:
            errors.append(f"{where}: duplicate id")
        seen.add(c.id)
        if not (repo_root / "docs" / "walkthroughs" / c.walkthrough).exists():
            errors.append(f"{where}: walkthrough {c.walkthrough} does not exist")
        for sid in c.satellites:
            if sid not in known:
                errors.append(f"{where}: unknown satellite '{sid}'")
        if c.autonomy not in AUTONOMY_LEVELS:
            errors.append(f"{where}: autonomy '{c.autonomy}' not in {AUTONOMY_LEVELS}")
        if not c.human_gates:
            errors.append(f"{where}: every chain must declare >=1 human gate")
        if c.autonomy == "autonomous_bounded":
            if not c.steps:
                errors.append(f"{where}: autonomous_bounded requires executable steps")
            for sid in c.satellites:
                if sid in known and known[sid].status != "integrated":
                    errors.append(f"{where}: autonomous_bounded but '{sid}' is {known[sid].status}, not integrated")
    return errors
