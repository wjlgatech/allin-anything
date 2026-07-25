"""Chain 02 adapter tests: real penecho export fixture -> gate-shaped layout."""

import subprocess
import sys
from collections import deque
from pathlib import Path

import pytest

from allin_anything.adapters import penecho_floorplan

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "penecho-export-studio.png"
DESIGN_ANYTHING = Path.home() / "Documents" / "Projects" / "design-anything"


@pytest.fixture(scope="module")
def layout():
    return penecho_floorplan.convert(FIXTURE, width_mm=5200, name="chain02-test")


def test_finds_four_typed_rooms(layout):
    assert {r["type"] for r in layout["rooms"]} == {"hall", "bathroom", "kitchen", "living"}


def test_every_coordinate_on_the_module(layout):
    coords = [c for r in layout["rooms"] for p in r["polygon"] for c in p]
    assert coords and all(c % 100 == 0 for c in coords)


def test_neighbours_share_wall_coordinates_exactly(layout):
    by_name = {r["name"]: r["polygon"] for r in layout["rooms"]}
    hall_right = by_name["hall"][1][0]
    bath_left = by_name["bathroom"][0][0]
    assert hall_right == bath_left  # unified wall centerline, not two drifting edges


def test_openings_policy_gives_reachability_and_one_bathroom_door(layout):
    openings = layout["openings"]
    assert any(o["type"] == "door_entry" and "exterior" in o["between"] for o in openings)
    bath_doors = [o for o in openings if "bathroom" in o["between"]]
    assert len(bath_doors) == 1 and bath_doors[0]["type"] == "door_bathroom"
    adj = {}
    for o in openings:
        a, b = o["between"]
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    seen, queue = {"exterior"}, deque(["exterior"])
    while queue:
        for nb in adj.get(queue.popleft(), ()):
            if nb not in seen:
                seen.add(nb)
                queue.append(nb)
    assert {r["name"] for r in layout["rooms"]} <= seen


def test_missing_ink_is_an_error_not_a_guess(tmp_path):
    from PIL import Image
    blank = tmp_path / "blank.png"
    Image.new("RGBA", (100, 100), (255, 255, 255, 255)).save(blank)
    with pytest.raises(ValueError, match="no ink"):
        penecho_floorplan.convert(blank, width_mm=5000)


@pytest.mark.skipif(not DESIGN_ANYTHING.exists(), reason="design-anything not present (CI runner)")
def test_gate_exit_0_on_real_export(tmp_path):
    out = tmp_path / "chain02.json"
    penecho_floorplan.convert_file(FIXTURE, out, width_mm=5200, name="chain02-live")
    r = subprocess.run(
        [sys.executable, str(DESIGN_ANYTHING / "pipeline" / "construction_gate.py"), str(out)],
        capture_output=True, text=True, cwd=DESIGN_ANYTHING,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "READY" in r.stdout
