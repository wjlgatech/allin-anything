# ROADMAP — the milestone arc

> Shape per `docs/META_REPO_PLAYBOOK.md` §3: Foundation → Coverage → Proof → Library → Autonomy →
> Cadence. Every DoD is runnable; north-star = **verified reach = 🟢 satellites × proven chains**
> (see docs/VISION.md). Score with `anyagent analyze` at each milestone; honest trajectory below.

## Done (Foundation + first Proof + first Cadence beat — all 2026-07-25)

| M | Phase | Deliverable | DoD (ran, exit 0) | Reach |
|---|---|---|---|---|
| M0 | Foundation | Born green: registry (9 sats), engine, drift gates, ainative self-audit, flagship skill | `make check` | 1×0 |
| M1 | Coverage | Digest wave 1 (Paul's pick, 9 repos → 🟡; private = public-safe pointers) | digests + `make check` | 1×0 |
| M2 | Foundation | Deterministic Router — all 8 eval cases are pytest (route/direct/none/refuse) | tests/test_router.py | 1×0 |
| M3 | Proof | **Chain 01**: sketch by hand → buildable floor plan (construction_gate C1–C5) | design-anything `make check` + gate exit 0, run live | 2×1 |
| M4 | Cadence | Launch: long-form live on the portfolio (PR #121), 1-click syndication human-gated | live URL 200 + og assets 200 | 2×1 |

## Ahead

| M | Phase | Deliverable | DoD (runnable) | Reach target |
|---|---|---|---|---|
| M5 ✅ 2026-07-25 | Proof | **Chain 02 — real ink**: 7 strokes drawn on penecho's live canvas (headless browser, zoom 12→105%), exported by penecho's own renderer, adapted by `scripts/ink2plan.py`, gated | fixture in-repo; construction_gate C1–C5 exit 0 on the REAL export (walkthrough: real-ink-to-ready.md); penecho 🟢 | 3×2 ✓ |
| M6 ✅ 2026-07-25 | Coverage | Digest wave 2 — **zero ⚪**: loop-engineering-anything, career-os (remote-pinned; no local checkout), neuro-os, ai-native-os, graph-engineering-anything all 🟡+ | 5 digests with pinned SHAs; `make check` green | 3×2 |
| M7 ✅ 2026-07-25 | Library | **Five chains live**: 01 sketch→buildable · 02 real-ink→READY · 03 brief→printable STL (ready_gate G1–G4) · 04 finance intent→money-os gates (28 tests) · 05 corpus→graph-engineering-anything gates (green-at-birth selftest) | 5 walkthroughs manifest-gated (test_every_walkthrough…); each router verdict a pytest; money-os + graph-engineering-anything 🟢 by live gate runs | 5×5 ✓ |
| M8 ✅ 2026-07-25 | Autonomy | **Bounded autonomy, calibrated by assessment**: `data/chains.yml` (per-chain flags, human gates mandatory) + AutoRunner (🟢-only, re-checked at runtime, journaled, stops at human gates); live bounded run of chain-02 exit 0. BRACE Tier-1 honestly **NO-GO 15/44** → ceiling set to local gate-running; enterprise 6/14→7/14 (LICENSE+CODEOWNERS) | chains.validate green in tests; live run exit 0; assessments recorded in docs/AUTONOMY.md | 8×5 ✓ (target was 7×5) |
| M9 ✅ 2026-07-25 | Cadence | **v1.0**: weekly freshness workflow (STALE measured via `scripts/freshness.py`; stale pin → human-gated issue, never an auto-update) + `## Verified reach` README badge generated + drift-gated | sync.yml merged; reach block drift-gated by `make check`; freshness logic offline-tested | 8×5 (9×6 target deferred: career-os 🟢 needs a live gate run; Chain 06 queued) |

## analyze trajectory (honest, not gamed)

- M6+M7 (2026-07-25): 79/100 steady; tests 29 → 33 (3 chain-route cases + walkthrough sweep).
- M5 (2026-07-25): 79/100; tests 23 → 29 (adapter suite incl. live gate run).
- M0: 68 → 75 → 77/100 (docstring passes; structure left honest at 14%).
- M1: 78/100 (renderer: URL-less + 🔒). M2: 78/100 (structure 14→21%, real Router classes;
  tests 9→17). M3: 78/100 (tests 17→19). M4: 78/100 (no engine change — launch milestone).
- Standing note: structure sub-metric stays low-20s by design (thin-CLI meta-repo, few classes);
  raising it with padding classes would violate "don't game a sub-metric."
