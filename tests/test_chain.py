"""Manifest gate for Chain 01 (playbook lesson 10: docs get a machine finish line too)."""

from pathlib import Path

from allin_anything import registry

ROOT = Path(__file__).resolve().parents[1]
WALKTHROUGH = ROOT / "docs" / "walkthroughs" / "sketch-to-buildable.md"


def test_chain_walkthrough_manifest():
    text = WALKTHROUGH.read_text()
    for heading in ("## Router verdict", "## Step A", "## Step B", "## Honest edges"):
        assert heading in text, f"walkthrough missing '{heading}'"
    assert "penecho" in text and "design-anything" in text
    assert len(text.split()) >= 200  # a walkthrough, not a stub


def test_chain_satellites_carry_their_evidence():
    reg = registry.load(ROOT / "data" / "registry.yml")
    by_id = {s.id: s for s in reg.satellites}
    assert by_id["design-anything"].status == "integrated"
    assert "walkthroughs" in by_id["design-anything"].notes  # evidence pointer, not vibes
    assert by_id["penecho"].status == "integrated"  # earned by Chain 02 (real-ink-to-ready)
    assert "walkthroughs" in by_id["penecho"].notes
