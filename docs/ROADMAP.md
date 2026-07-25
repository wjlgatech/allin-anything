# ROADMAP — machine-checkable milestones

| M | Deliverable | DoD (runnable) | Status | analyze score |
|---|---|---|---|---|
| M0 | Repo born green: registry (9 satellites), engine, gates, self-audit, flagship skill | `make check` exit 0 | ✅ 2026-07-25 | 77/100 |
| M1 | Digest wave 1: design-anything, master-anything, money-os → 🟡 | 3 new `docs/satellites/*.md`; statuses advanced in registry; `make check` green | ⬜ | — |
| M2 | Router proven: 5 eval cases pass end-to-end (route → hand-off → satellite gate) | eval/allin-anything.md cases exercised; gaps banked in data/news.yml | ⬜ | — |
| M3 | First digital↔physical chain: sketch (penecho, upstream) → design-anything geometry gate | a walkthrough doc + the satellite's own gate exit 0 | ⬜ | — |
| M4 | Portfolio launch (content shape): long-form on agentic-portfolio first, then 1-click syndication | LINKEDIN_PUBLISH_EVAL checklist green; human gate | ⬜ | — |

Advance one satellite at a time: candidate → digested → integrated, each step gated by on-disk
evidence (`registry.validate` enforces it). Score with `anyagent analyze .` at EACH milestone.

## analyze scores

- M0 (2026-07-25): `anyagent analyze` 68 → 75 → 77/100 (docstring passes; structure sub-metric
  left honest at 14% — 2 classes / 9 files is right for a thin-CLI repo, not gamed).
