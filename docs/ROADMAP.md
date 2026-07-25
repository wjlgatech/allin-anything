# ROADMAP — machine-checkable milestones

| M | Deliverable | DoD (runnable) | Status | analyze score |
|---|---|---|---|---|
| M0 | Repo born green: registry (9 satellites), engine, gates, self-audit, flagship skill | `make check` exit 0 | ✅ 2026-07-25 | 77/100 |
| M1 | Digest wave 1 (Paul's pick): blueprint/research/master/strategize/reverse-engineering-anything + rsi/FM/FDE/money-os → 🟡 | 9 `docs/satellites/*.md` with pinned SHAs; statuses advanced; `make check` green | ✅ 2026-07-25 | recorded below |
| M2 | Router proven: deterministic Router + every eval case executable (5 should + 3 should-not, incl. AGPL refusal + cross-world chain) | tests/test_router.py green inside `make check` | ✅ 2026-07-25 | recorded below |
| M3 | First digital↔physical chain: sketch (penecho, upstream) → design-anything construction gate | docs/walkthroughs/sketch-to-buildable.md (manifest-gated by tests/test_chain.py) + design-anything `make check` exit 0, run live | ✅ 2026-07-25 | recorded below |
| M4 | Portfolio launch: long-form live on agentic-portfolio (PR #121, canonical URL), prefilled LinkedIn + X composers handed to Paul | article + cover + infographic live; syndication clicks stay HUMAN | ✅ 2026-07-25 (posts pending Paul's click) | 78/100 |

Advance one satellite at a time: candidate → digested → integrated, each step gated by on-disk
evidence (`registry.validate` enforces it). Score with `anyagent analyze .` at EACH milestone.

## analyze scores

- M0 (2026-07-25): `anyagent analyze` 68 → 75 → 77/100 (docstring passes; structure sub-metric
  left honest at 14% — 2 classes / 9 files is right for a thin-CLI repo, not gamed).
- M1 (2026-07-25): 78/100 after wave 1 (renderer gained URL-less + 🔒 handling; docs completed).
- M2 (2026-07-25): 78/100 — structure up 14→21% for real reasons (Router + RouteDecision);
  tests 9 → 17, all eval cases executable.
- M3 (2026-07-25): 78/100 steady; tests 17 → 19 (chain manifest + evidence pins).
