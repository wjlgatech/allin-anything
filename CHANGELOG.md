# CHANGELOG

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
