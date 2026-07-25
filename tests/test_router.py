"""Every eval case in eval/allin-anything.md, executable. Names match the eval file."""

from pathlib import Path

import pytest

from allin_anything import registry
from allin_anything.router import Router

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def router():
    return Router(registry.load(ROOT / "data" / "registry.yml"))


# ---- Should trigger ----

def test_3d_print_routes_to_design_anything(router):
    d = router.route("design me a phone stand I can 3D print")
    assert d.mode == "route"
    assert d.satellite_ids[0] == "design-anything"
    assert "candidate" in d.reason  # status disclosed, never hidden


def test_handwriting_routes_to_penecho(router):
    d = router.route("which of my repos can turn handwriting into AI input?")
    assert d.mode == "route"
    assert d.satellite_ids[0] == "penecho"


def test_job_watching_routes_to_career_os(router):
    d = router.route("I want an agent that watches my job applications")
    assert d.mode == "route"
    assert d.satellite_ids[0] == "career-os"


def test_agent_app_routes_to_anyagent(router):
    d = router.route("build and ship an agent app from this one sentence")
    assert d.mode == "route"
    assert d.satellite_ids[0] == "anyagent"


def test_cross_world_chain_declares_both(router):
    d = router.route("sketch a room layout by hand, then verify it's buildable")
    assert d.mode == "route"
    assert {"penecho", "design-anything"} <= set(d.satellite_ids)


# ---- Should NOT trigger (or refuse) ----

def test_named_satellite_goes_direct(router):
    d = router.route("run money-os weekly review")
    assert d.mode == "direct"
    assert d.satellite_ids == ("money-os",)


def test_generic_coding_question_routes_nowhere(router):
    d = router.route("fix this stack trace")
    assert d.mode == "none"
    assert d.satellite_ids == ()


def test_vendoring_penecho_is_refused(router):
    d = router.route("copy the penecho source into this repo")
    assert d.mode == "refuse"
    assert d.satellite_ids == ("penecho",)
    assert "AGPL" in d.reason
