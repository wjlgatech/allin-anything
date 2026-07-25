"""Manifest gates for the charter (META_REPO_PLAYBOOK §1: charter docs gate like code)."""

import re
from pathlib import Path

from allin_anything import registry

ROOT = Path(__file__).resolve().parents[1]


def test_vision_manifest():
    text = (ROOT / "docs" / "VISION.md").read_text()
    for heading in ("## Vision", "## Mission", "## North-star metric", "## Operating modes", "## Non-goals"):
        assert heading in text, f"VISION.md missing '{heading}'"
    assert len(text.split()) >= 250


def test_roadmap_has_a_future_not_just_a_past():
    text = (ROOT / "docs" / "ROADMAP.md").read_text()
    assert "## Ahead" in text
    for m in ("M5", "M6", "M7", "M8", "M9"):
        assert m in text, f"ROADMAP missing horizon milestone {m}"


def test_north_star_is_computable_offline():
    reg = registry.load(ROOT / "data" / "registry.yml")
    integrated = len(reg.by_status("integrated"))
    chains = len(list((ROOT / "docs" / "walkthroughs").glob("*.md")))
    reach = integrated * chains
    assert reach >= 2  # 2 x 1 at charter time (anyagent, design-anything × Chain 01); may only grow
    stated = re.search(r"currently (\d+) × (\d+) = (\d+)", (ROOT / "docs" / "VISION.md").read_text())
    assert stated, "VISION.md must state the current north-star value"
    assert int(stated.group(3)) == reach, "VISION.md north-star value drifted from repo reality"


def test_meta_playbook_seeded():
    assert (ROOT / "docs" / "META_REPO_PLAYBOOK.md").exists()
