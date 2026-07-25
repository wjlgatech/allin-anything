"""M8 tests: chain spec validation + AutoRunner boundaries (refuse > fake)."""

from pathlib import Path

from allin_anything import chains as chains_mod
from allin_anything import registry
from allin_anything.autorun import AutoRunner

ROOT = Path(__file__).resolve().parents[1]
DESIGN_ANYTHING = Path.home() / "Documents" / "Projects" / "design-anything"


def _load():
    reg = registry.load(ROOT / "data" / "registry.yml")
    chains = chains_mod.load(ROOT / "data" / "chains.yml")
    return reg, chains


def test_chain_spec_is_valid():
    reg, chains = _load()
    assert chains_mod.validate(chains, reg, ROOT) == []
    assert len(chains) >= 5


def test_every_chain_declares_a_human_gate():
    _, chains = _load()
    assert all(c.human_gates for c in chains)


def test_autonomy_is_earned_not_asserted():
    """A chain listing a non-integrated satellite cannot be autonomous_bounded."""
    reg, chains = _load()
    for c in chains:
        if c.autonomy == "autonomous_bounded":
            by_id = {s.id: s for s in reg.satellites}
            assert all(by_id[sid].status == "integrated" for sid in c.satellites), c.id


def test_runner_refuses_assisted_chains():
    reg, chains = _load()
    report = AutoRunner(reg, chains, ROOT).run("chain-01", journal=False)
    assert report.mode == "refused"
    assert "earned per-chain" in report.reason


def test_runner_refuses_unknown_chain():
    reg, chains = _load()
    assert AutoRunner(reg, chains, ROOT).run("chain-99", journal=False).mode == "refused"


def test_missing_local_checkout_is_blocked_not_faked(tmp_path):
    reg, chains = _load()
    runner = AutoRunner(reg, chains, ROOT, projects_root=tmp_path)  # empty world
    report = runner.run("chain-03", journal=False)
    assert report.mode == "executed" and not report.ok
    assert report.steps[0].status == "blocked-missing-local"


def test_bounded_run_chain02_live(tmp_path):
    import pytest
    if not DESIGN_ANYTHING.exists():
        pytest.skip("design-anything not present (CI runner)")
    reg, chains = _load()
    report = AutoRunner(reg, chains, ROOT).run("chain-02", journal=False)
    assert report.ok, [(s.status, s.tail) for s in report.steps]
    assert "READY" in report.steps[-1].tail
    assert report.human_gates  # the runner surrendered at the human gate


def test_freshness_gate_offline():
    import sys
    sys.path.insert(0, str(ROOT / "scripts"))
    import freshness
    code, lines = freshness.check(resolver=lambda url: "e1b936fe51103243b79c82427eef5a369448a660")
    assert code == 0 and any("fresh" in l for l in lines)
    code, lines = freshness.check(resolver=lambda url: "f" * 40)
    assert code == 1 and any("STALE" in l for l in lines)
    code, lines = freshness.check(resolver=lambda url: (_ for _ in ()).throw(OSError("no net")))
    assert code == 1 and any("not measured" in l for l in lines)
