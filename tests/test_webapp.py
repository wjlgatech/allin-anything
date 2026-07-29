"""Demo webapp handler tests — incl. the security boundary (whitelist, caps, refusals)."""

from pathlib import Path

from allin_anything.webapp import MAX_INTENT_LEN, DemoApp

ROOT = Path(__file__).resolve().parents[1]


def app() -> DemoApp:
    return DemoApp(ROOT)


def test_route_endpoint_returns_real_verdict():
    d = app().route("design me a phone stand I can 3D print")
    assert d["mode"] == "route" and d["satellites"][0] == "design-anything"


def test_route_rejects_empty_and_caps_length():
    a = app()
    assert "error" in a.route("   ")
    long = a.route("x" * 5000)
    assert len(long["intent"]) == MAX_INTENT_LEN  # input capped, never echoed unbounded


def test_registry_summary_matches_north_star():
    d = app().registry_summary()
    assert d["verified_reach"] == d["counts"]["integrated"] * d["chains"]
    assert d["counts"]["integrated"] >= 2


def test_chain_list_exposes_human_gates():
    d = app().chain_list()
    assert len(d["chains"]) >= 5
    assert all(c["human_gates"] for c in d["chains"])


def test_autorun_whitelist_blocks_arbitrary_input():
    d = app().autorun("chain-99; rm -rf /")  # not a known id -> refused, nothing executes
    assert d["mode"] == "refused" and "unknown chain" in d["reason"]


def test_autorun_refuses_assisted_chain_without_executing():
    d = app().autorun("chain-01")
    assert d["mode"] == "refused" and "earned per-chain" in d["reason"]
    assert d.get("steps", []) == []
