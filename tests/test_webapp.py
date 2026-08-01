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


def test_penecho_bridge_is_pointer_only_and_offline_safe():
    d = app().penecho_bridge()
    assert d["pinned_sha"].startswith("e1b936f")  # the registry pin, disclosed
    assert d["license"] == "AGPL-3.0-only" and "never vendored" in d["rule"]
    assert isinstance(d["running"], bool)  # offline (CI) must yield False, never an error


def test_one_click_demo_contract():
    """Playbook rule (Paul, 2026-08-01): every agentic webapp ships 1-click activation —
    demo link at the TOP of README, server auto-opens the browser, PWA manifest present."""
    import json

    readme_top = "\n".join((ROOT / "README.md").read_text().splitlines()[:15])
    assert "make demo" in readme_top and "127.0.0.1:8642" in readme_top, "demo link must be at the TOP of README"
    manifest = json.loads((ROOT / "webapp" / "manifest.json").read_text())
    assert manifest["display"] == "standalone" and manifest["theme_color"] == "#d97757"
    assert 'rel="manifest"' in (ROOT / "webapp" / "index.html").read_text()
    shell = (ROOT / "scripts" / "webapp.py").read_text()
    assert "webbrowser" in shell and "--no-open" in shell  # auto-open with a headless escape hatch


def test_bitter_lesson_artifact_carries_real_penecho_ink():
    page = (ROOT / "examples" / "bitter-lesson" / "index.html").read_text()
    assert page.count('class="session"') == 5  # master-anything session structure
    assert "penecho-two-curves.png" in page  # the exported ink, embedded
    assert (ROOT / "examples" / "bitter-lesson" / "assets" / "penecho-two-curves.png").exists()
    assert "prefers-reduced-motion" in page  # animate-anything craft rule
    assert "Paul Jialiang Wu" in page and "agentic-portfolio-lovat.vercel.app" in page
