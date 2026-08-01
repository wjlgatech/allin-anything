# CHANGELOG

## 1.8.0 — 2026-08-01

- **loop-engineering-anything 🟡→🟢** by its own pytest suite run live at re-pinned `a608273`:
  exit 0 (534 passed, 3 skipped, 21.4s). Upstream has no root `make check` — the registry note
  and digest state honestly that its gate IS its test suite. Reach **13 × 6 = 78**.

## 1.7.0 — 2026-08-01

- **agent-forge 🟡→🟢** by its own gate run live at the exact digest pin `a3b0fa0`: exit 0
  (`gate_check.py` PASS, 11 deliverables verified; 324 tests, 6.8s). Routed in the integrated
  table (autonomy dial L0–L5, cost envelope, portable contract). Reach **12 × 6 = 72**.
- Honest rulings the same hour: **ai-native-os** has no runnable gate at root — stays 🟡
  (promotion path upstream, like career-os). loop-engineering-anything and neuro-os have
  pyproject/tests and are queued as the next one-by-one ships.

## 1.6.0 — 2026-08-01

- **The demo is now remotely visitable: https://allin-anything-demo.vercel.app** (Paul's
  amendment: 127.0.0.1-only breaks the playbook). One dual-mode page: locally it drives the real
  engine; deployed it serves a build-time snapshot (`webapp/static-data.json`, exported by
  `make build`, drift-gated) and **never executes** — execution panels show recorded receipts
  from `data/evidence.yml` (the BRACE local-only ceiling, honored in the UI itself).
- **penecho FULLY working — Paul's challenge answered with a receipt.** The ink→AI→draft loop
  had a real bug: penecho's env sanitizer strips `ANTHROPIC_API_KEY`, so the Claude-CLI executor
  was "Not logged in" (502 model-error). Root-caused by reproduction, fixed via penecho's own
  `--api` config (zero upstream code touched). Its log now shows `upstreamStatus:200 …
  tools:["write_text"]` — handwritten `1+1=` answered on-canvas. Digest updated.
- Playbook rule amended at every source (anyagent row, REPO_PLAYBOOK §4a, seeded copy, memory,
  and the drift test now requires the REMOTE link atop README). 2 new tests (53 total).

## 1.5.0 — 2026-08-01

- **1-click activation, made a LAW not a favor** (Paul: "I am tired of repeating myself"):
  demo link now at the TOP of README; `make demo` auto-opens the browser (`--no-open` for CI);
  PWA manifest served at `/manifest.json` (installable). The rule is codified at the SOURCE —
  anyagent's agentic-webapp playbook row (rc0084 there), `_templates/REPO_PLAYBOOK.md` §4a, the
  seeded copy here — and enforced by `test_one_click_demo_contract` (README-top link is drift-gated).
- **/allin-anything ready gate**: SKILL.md § Ready gate (install symlink, self-check, demo);
  fixed the relative-path bug (`scripts/route.py` now addressed absolutely — the skill works from
  ANY directory, which is the whole point of a front door).
- Webapp validated per playbook in a real browser: all 6 sections exercised live (route, refusal,
  ladder reach 66, chain table incl. chain-05 bounded, bridge pin) — 0 console errors; bounded-run
  section proven via API (chain-05 executed, chain-01 refused). 51 tests.

## 1.4.0 — 2026-08-01

- **research-anything 🟡→🟢** by its own gate run live at re-pinned `9119fc2` (exit 0: 84 tests,
  data-spine + graph reachability, ainative 100/100, golden-claim-gate 5/5; `science-agent-bench`
  honestly not-measured by its own gate). Digest carries the evidence.
- **Chain 05 corpus→graph: assisted → autonomous_bounded** — the flip its comment promised once
  every satellite earned 🟢. Executable steps added; live AutoRunner run: both `make check` steps
  exit 0, stopped at the "publishing or acting on graph conclusions" human gate.
- Verified reach 10×6 → **11 × 6 = 66**. Registry v1.0. Router eval updated (partner disclosed
  at its new honest status).

## 1.3.0 — 2026-08-01

- **The super-tool, tested end-to-end on a real article.** `/allin-anything` is now an installed
  meta-tool (symlink into `~/.claude/skills/` — one front door in any session). Test input:
  entry №1 of FM-os's Frontier AI Reading List ("The Bitter Lesson", Sutton 2019); the router
  verdict named penecho + animate-anything + master-anything (all 🟢), Chain 06 gates ran live,
  and `examples/bitter-lesson/` is the artifact: 5 sessions, each with a CSS animation.
- **penecho @e1b936f full-feature upstream**: sibling checkout at the exact pin; its own
  `npm run check` = **200 tests, 0 failed**; full UI served via its Claude CLI executor;
  4 real strokes drawn and exported by **penecho's own PNG exporter** (the two-curves figure,
  embedded in the artifact). Digest updated with live evidence. AGPL boundary intact — zero
  penecho code in this repo.
- Demo webapp: new §5 **pen→digital bridge** (`GET /api/penecho` — pin, license, rule, live
  reachability; offline-safe) + `/bitter-lesson` serves the artifact. 2 new tests (8 total in
  test_webapp.py): bridge is pointer-only/offline-safe; artifact carries the real ink.

## 1.2.0 — 2026-08-01

- **Chain 06 — article → animated understanding (learn-anything)**: master-anything ×
  animate-anything, autonomous_bounded, ran live through the AutoRunner (both `make check` steps
  exit 0; stops at the publishing human gate). Walkthrough manifest-gated; router eval case
  `test_learn_with_animation_routes_chain_06` added (the 2026-07-27 banked gap, closed).
- Promotions by live gate runs: **master-anything** 🟡→🟢 (15 tests + organ smoke, 8 organs) and
  **animate-anything** ⚪→🟢 (digest minted; 3b1b style-linter 100/100). Registry v0.9.
- **career-os ruled honestly**: local clone now exists at the pin (395b64b), but upstream has no
  machine gate (no Makefile/tests) — stays 🟡 per *no-evidence-means-no*; promotion path is
  upstream. The M9 deferred 9×6 target is thereby closed: reach 8×5 → **10 × 6 = 60**.
- CI actions re-bumped to checkout@v5 + setup-python@v6 (proven safe via workflow_dispatch —
  closes the 0.4.1 rollback thread).

## 1.1.0 — 2026-07-29

- Demo webapp: `scripts/webapp.py` (thin stdlib HTTP shell) over `src/allin_anything/webapp.py`
  (handlers on the real Router/Registry/AutoRunner — nothing mocked). Five point-by-point
  sections incl. running a bounded chain live from the browser. 6 new tests cover the security
  boundary: chain whitelist (no arbitrary execution), input caps, assisted-chain refusal.
  README gains the demo section + a 200-word explain-like-I'm-15 of today vs post-roadmap.

## 1.0.1 — 2026-07-28

- Satellite rename merged: blueprint-anything → **agent-forge** (registry id/url/notes, digest
  renamed + re-pinned at `a3b0fa082cf1`, SKILL hints, README regenerated). Registry version 0.8.

## 1.0.0 — 2026-07-25

- M8 (autonomy, bounded + calibrated): `data/chains.yml` is the chain library as data (autonomy
  per-chain; ≥1 human gate mandatory, validator-enforced). `AutoRunner` executes
  `autonomous_bounded` chains only — satellites re-checked 🟢 at runtime, missing checkouts are
  BLOCKED not faked, every run journaled to `runs/journal.jsonl`, execution always stops at the
  human gates. Live bounded run of chain-02: exit 0. **BRACE Tier-1: NO-GO 15/44 — recorded and
  OBEYED** (ceiling = local gate-running); enterprise 6/14 → 7/14 (LICENSE CC0, CODEOWNERS).
- M9 (cadence, v1.0): weekly `sync.yml` measures external-pin freshness (`scripts/freshness.py`,
  offline-tested; unreachable = not measured = flagged) and opens a human-gated issue on STALE —
  never auto-updates a pin. README gains a generated, drift-gated `Verified reach` badge.
- Promotions by live gate runs: rsi-os, FM-os, FDE-os (225 tests) → 🟢. Reach 5×5 → **8×5 = 40**.

## 0.7.0 — 2026-07-25

- M6: digest wave 2 — registry reaches **zero ⚪** (17/17 satellites 🟡+). career-os digested from
  a shallow remote pin (no local checkout — stated in its digest, 🟡 is its ceiling until a live
  gate run). Honest gaps recorded for repos without a root `make check`.
- M7: the five-chain library — Chains 03 (brief→printable STL, ready_gate G1–G4 exit 0),
  04 (finance intent→money-os `make check`, 28 tests, exit 0), 05 (corpus→graph-engineering-
  anything `make check`, green-at-birth selftest, exit 0) join 01–02. Every walkthrough is
  manifest-gated; every router verdict is a pytest. money-os + graph-engineering-anything 🟢.
  Verified reach 3×2 → **5×5 = 25**.

## 0.6.0 — 2026-07-25

- M5: Chain 02 "real ink" — penecho export → `ink2plan` adapter (enclosed-region rooms,
  wall-centerline unification, 100mm module snap, code-minimum openings policy) →
  construction_gate exit 0 on a REAL export drawn on penecho's live canvas and rendered by
  penecho's own exporter. penecho promoted 🟢; verified reach 2×1 → 3×2 = 6. Fixture banked;
  6 adapter tests incl. a live gate run (skipped where design-anything is absent). CI gains pillow.

## 0.5.0 — 2026-07-25

- M4: portfolio launch. Long-form live at
  agentic-portfolio-lovat.vercel.app/articles/allin-anything-born-green.html (PR #121); cover +
  Chain-01 infographic in house style; LinkedIn/X share composers prefilled — posting stays
  human-gated. Registry curation earlier today: company-os → ai-native-os,
  + graph-engineering-anything (17 satellites).
- CI post-mortem closed: the log-less failures were GitHub queue infrastructure — the v5/v6
  workflow passed via workflow_dispatch once the queue recovered; re-bumping actions is safe
  whenever convenient.

## 0.4.1 — 2026-07-25

- Reverted CI actions to checkout@v4 + setup-python@v5 (the last-green config, kept
  `workflow_dispatch`): every run on the v5/v6 file died log-less (startup_failure or zero-step
  "failure") while the v4/v5 file passed. Tags exist upstream, so root cause is unproven — this
  is the evidence-driven rollback, not a diagnosis. Deprecation-warning cleanup retried later.

## 0.4.0 — 2026-07-25

- M3: Chain 01 (sketch → buildable) walked with live evidence — design-anything's own gate run
  green (construction_gate C1–C5, `make check` 7.7s) and promoted ⚪→🟢; penecho stays 🟡 by
  honesty (sketch step is upstream + human). Walkthrough manifest-gated by tests/test_chain.py.
- CI wrinkle fix: actions/checkout@v5 + setup-python@v6 (Node 20 deprecation gone) and
  `workflow_dispatch` so a transient `startup_failure` is one click to re-run.

## 0.3.0 — 2026-07-25

- M2: deterministic `Router` over registry triggers (spec-as-data), `scripts/route.py` thin CLI,
  and tests/test_router.py making all 8 eval cases executable (route / direct / none / refuse;
  AGPL vendoring refused; cross-world penecho→design-anything chain declared).

## 0.2.0 — 2026-07-25

- M1 digest wave 1: 9 satellites promoted to 🟡 digested (blueprint-, research-, master-,
  strategize-, reverse-engineering-anything; rsi-, FM-, FDE-, money-os), each with a pinned local
  SHA. Private repos appear as public-safe pointers (🔒, generic one-liner only). Registry: 16
  satellites. Renderer now handles URL-less satellites + 🔒 badge.

## 0.1.0 — 2026-07-25

- Born green per REPO_PLAYBOOK: registry (9 satellites: penecho digested @e1b936f, anyagent
  integrated, 7 candidates), typed engine, drift-gated README, ainative self-audit (gate 90),
  flagship router skill + eval, CI = `make check`. `anyagent analyze`: 68 → 77/100.
