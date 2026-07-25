"""Load and validate the satellite registry against the playbook's gate rules."""

from __future__ import annotations

from pathlib import Path

import yaml

from .models import KINDS, ROLES, STATUSES, Registry, Satellite


def load(path: Path) -> Registry:
    raw = yaml.safe_load(path.read_text())
    sats = tuple(
        Satellite(**{**item, "triggers": tuple(item.get("triggers", ()))})
        for item in raw.get("satellites", [])
    )
    return Registry(version=str(raw["version"]), updated=str(raw["updated"]), satellites=sats)


def validate(reg: Registry, repo_root: Path) -> list[str]:
    """Return a list of gate violations. Empty list == valid."""
    errors: list[str] = []
    seen: set[str] = set()
    skill_path = repo_root / "skills" / "allin-anything" / "SKILL.md"
    skill_text = skill_path.read_text() if skill_path.exists() else ""

    for s in reg.satellites:
        where = f"satellite '{s.id}'"
        if s.id in seen:
            errors.append(f"{where}: duplicate id")
        seen.add(s.id)
        if s.kind not in KINDS:
            errors.append(f"{where}: kind '{s.kind}' not in {KINDS}")
        if s.role not in ROLES:
            errors.append(f"{where}: role '{s.role}' not in {ROLES}")
        if s.status not in STATUSES:
            errors.append(f"{where}: status '{s.status}' not in {STATUSES}")
        if not s.capability.strip():
            errors.append(f"{where}: capability is empty")

        if s.kind == "external":
            if not s.pinned_sha or len(s.pinned_sha) != 40:
                errors.append(f"{where}: external satellite needs a 40-char pinned_sha")
            if not s.license:
                errors.append(f"{where}: external satellite needs an explicit license")

        if s.status in ("digested", "integrated"):
            digest = repo_root / "docs" / "satellites" / f"{s.id}.md"
            if not digest.exists():
                errors.append(f"{where}: status '{s.status}' requires {digest.relative_to(repo_root)}")

        if s.status == "integrated" and s.id not in skill_text:
            errors.append(f"{where}: status 'integrated' requires routing in skills/allin-anything/SKILL.md")

    return errors
