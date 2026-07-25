import subprocess
import sys
from pathlib import Path

from allin_anything import generate, registry

ROOT = Path(__file__).resolve().parents[1]


def test_readme_has_no_drift():
    reg = registry.load(ROOT / "data" / "registry.yml")
    current = (ROOT / "README.md").read_text()
    assert generate.render_readme(current, reg, ROOT / "data" / "news.yml") == current


def test_ainative_gate_passes():
    r = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "ainative.py"), "--gate", "90"],
        capture_output=True, text=True,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "unmeasured" in r.stdout  # the honest count is always reported


def test_inject_refuses_missing_markers():
    import pytest
    with pytest.raises(ValueError):
        generate.inject("no markers here", "satellites", "body")


def test_flagship_skill_routes_every_integrated_satellite():
    reg = registry.load(ROOT / "data" / "registry.yml")
    skill = (ROOT / "skills" / "allin-anything" / "SKILL.md").read_text()
    for s in reg.by_status("integrated"):
        assert s.id in skill


def test_skill_eval_has_both_directions():
    text = (ROOT / "eval" / "allin-anything.md").read_text()
    assert "## Should trigger" in text and "## Should NOT trigger" in text
