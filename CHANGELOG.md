# CHANGELOG

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
