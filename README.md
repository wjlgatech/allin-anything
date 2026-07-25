# allin-anything

**All-in interaction with both the digital and physical world — one super-repo that composes the
`-anything` / `-os` agent family into a single front door.**

You bring an intent ("design me a bracket I can print", "master this paper", "run my job search").
The flagship skill routes it to the right satellite repo; every satellite is indexed here with a
verified status — never vendored, never guessed.

Inspired by [penecho](https://github.com/penecho/penecho): a shared canvas where physical ink
becomes digital model input. allin-anything generalizes that bridge — *any* physical or digital
surface, one interaction contract.

## News

<!-- BEGIN GENERATED: news -->
- **2026-07-25** — allin-anything born green: Scaffolded from REPO_PLAYBOOK; registry seeded with 9 satellites (penecho digested at e1b936f, AGPL — pointer only); make check green at birth.
<!-- END GENERATED: news -->

## Satellites

Single source of truth: [`data/registry.yml`](data/registry.yml). This table is generated —
edit the YAML, run `make build`; CI fails on drift.

<!-- BEGIN GENERATED: satellites -->
| Satellite | World | Status | Capability |
|---|---|---|---|
| [anyagent](https://github.com/wjlgatech/anyagent) | ⚙️ engine | 🟢 integrated | Build, grade, improve & accountably ship any agent app; goal-10x front door drives every repo in this registry |
| [penecho](https://github.com/penecho/penecho) `@e1b936f` | 🌉 bridge | 🟡 digested | AI spatial canvas — handwriting, equations, diagrams become model input; drafts return to the canvas (pen -> digital bridge) |
| [career-os](https://github.com/wjlgatech/career-os) | 💻 digital | ⚪ candidate | Autonomous job-search pipeline + self-upgrading inner loop |
| [company-os](https://github.com/wjlgatech/company-os) | 💻 digital | ⚪ candidate | Governed agent runtime for founders & operators |
| [design-anything](https://github.com/wjlgatech/design-anything) | 🦾 physical | ⚪ candidate | Design intent -> gate-verified physical blueprints: STL, floor plans, sewing patterns, sim scenes |
| [loop-engineering-anything](https://github.com/wjlgatech/loop-engineering-anything) | ⚙️ engine | ⚪ candidate | Self-improving orchestrator: generate, judge, refactor, re-judge toward convergence |
| [master-anything](https://github.com/wjlgatech/master-anything) | 💻 digital | ⚪ candidate | Master any hard topic: compress -> learn -> verify-by-transfer -> express -> build |
| [money-os](https://github.com/wjlgatech/money-os) | 💻 digital | ⚪ candidate | AI financial consciousness — 17 skills, zero-trust, local-only |
| [neuro-os](https://github.com/wjlgatech/neuro-os) | 🦾 physical | ⚪ candidate | Executable neuroscience knowledge — brain mechanisms as primitives (the wetware end of physical) |
<!-- END GENERATED: satellites -->

Status ladder: ⚪ candidate → 🟡 digested (pinned digest in `docs/satellites/`) → 🟢 integrated
(routed by the flagship skill). Each advance is gated by on-disk evidence.

## The finish line

```bash
make check   # pytest + drift gate + ainative self-audit (offline, deterministic)
```

## Honest edges

- Most satellites are still ⚪ candidates — named and role-assigned, not yet verified. The table
  above tells you exactly which; nothing here pretends otherwise.
- penecho is AGPL-3.0 and lives upstream: we index it (pointer + pinned SHA + digest), we do not
  ship, fork, or wrap its code. Run it from its own repo.
- The physical-world reach is only as real as each satellite's own gates (e.g. design-anything's
  geometry checks). A gate is never a permit or a PE stamp.
- Private family repos (e.g. anyagent) are pointers only; their source is not public.

## How this repo operates

`docs/REPO_PLAYBOOK.md` is the build pattern; `data/ainative.yml` + `scripts/ainative.py` score
this repo against it inside `make check` — a discipline regression fails the build.
