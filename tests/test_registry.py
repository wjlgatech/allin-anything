from pathlib import Path

from allin_anything import registry
from allin_anything.models import STATUSES

ROOT = Path(__file__).resolve().parents[1]


def test_registry_loads_and_validates():
    reg = registry.load(ROOT / "data" / "registry.yml")
    assert registry.validate(reg, ROOT) == []
    assert len(reg.satellites) >= 5


def test_externals_are_pinned_and_licensed():
    reg = registry.load(ROOT / "data" / "registry.yml")
    for s in reg.satellites:
        if s.kind == "external":
            assert s.pinned_sha and len(s.pinned_sha) == 40
            assert s.license


def test_status_ladder_is_the_only_vocabulary():
    reg = registry.load(ROOT / "data" / "registry.yml")
    assert all(s.status in STATUSES for s in reg.satellites)


def test_sorted_puts_integrated_first():
    reg = registry.load(ROOT / "data" / "registry.yml")
    ranks = [s.status_rank for s in reg.sorted()]
    assert ranks == sorted(ranks, reverse=True)
