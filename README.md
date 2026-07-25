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
- **2026-07-25** — M2 router proven — every eval case is now a pytest: Deterministic Router (triggers-as-data in registry.yml) + scripts/route.py CLI; 5 should-trigger + 3 should-not cases executable in tests/test_router.py, incl. the AGPL vendoring refusal and the cross-world penecho→design-anything chain.
- **2026-07-25** — M1 digest wave 1 — 9 satellites promoted to 🟡: blueprint/research/master/strategize/reverse-engineering-anything + rsi/FM/FDE/money-os digested with pinned local SHAs; private repos are public-safe pointers only; registry now 16 satellites.
- **2026-07-25** — allin-anything born green: Scaffolded from REPO_PLAYBOOK; registry seeded with 9 satellites (penecho digested at e1b936f, AGPL — pointer only); make check green at birth.
<!-- END GENERATED: news -->

## Satellites

Single source of truth: [`data/registry.yml`](data/registry.yml). This table is generated —
edit the YAML, run `make build`; CI fails on drift.

<!-- BEGIN GENERATED: satellites -->
| Satellite | World | Status | Capability |
|---|---|---|---|
| [anyagent](https://github.com/wjlgatech/anyagent) 🔒 | ⚙️ engine | 🟢 integrated | Build, grade, improve & accountably ship any agent app; goal-10x front door drives every repo in this registry |
| [FDE-os](https://github.com/wjlgatech/FDE-os) | 🌉 bridge | 🟡 digested | Operating system for Forward Deployed Engineers — ship agentic systems inside the customer's real environment; live 3-door webapp |
| [FM-os](https://github.com/wjlgatech/FM-os) | 💻 digital | 🟡 digested | Living map of how language models are actually built and shipped — pre/post-training, fine-tuning, RL, SLM-first |
| [blueprint-anything](https://github.com/wjlgatech/blueprint-anything) 🔒 | ⚙️ engine | 🟡 digested | Agent design & feasibility studio (Forge): autonomy dial L0-L5, design dossier, cost envelope, portable contract for six platforms |
| [master-anything](https://github.com/wjlgatech/master-anything) 🔒 | 💻 digital | 🟡 digested | Master any hard topic in ~60 min: teach-back gate, fun >=4/5 measured, one portfolio artifact, +7-day retention probe |
| [money-os](https://github.com/wjlgatech/money-os) | 💻 digital | 🟡 digested | AI financial co-pilot — local-only data, zero uploads, zero subscriptions (v4.0) |
| [penecho](https://github.com/penecho/penecho) `@e1b936f` | 🌉 bridge | 🟡 digested | AI spatial canvas — handwriting, equations, diagrams become model input; drafts return to the canvas (pen -> digital bridge) |
| [research-anything](https://github.com/wjlgatech/research-anything) 🔒 | 💻 digital | 🟡 digested | Any research question in -> a verified, window-dated, autonomy-aware brief out (science, engineering, medicine, business) |
| `reverse-engineering-anything` 🔒 | ⚙️ engine | 🟡 digested | AI-powered reverse engineering meta-repo: Observe -> Decompose -> Model -> Reconstruct -> Validate -> Improve -> Generalize |
| [rsi-os](https://github.com/wjlgatech/rsi-os) | ⚙️ engine | 🟡 digested | Living, community-driven map of Recursive Self-Improvement / automated AI research — Godel Machine (2003) to AI Scientists (2026) |
| `strategize-anything` 🔒 | 💻 digital | 🟡 digested | Private strategy operating system (AI-assisted and AI-autonomous modes) |
| [career-os](https://github.com/wjlgatech/career-os) | 💻 digital | ⚪ candidate | Autonomous job-search pipeline + self-upgrading inner loop |
| [company-os](https://github.com/wjlgatech/company-os) | 💻 digital | ⚪ candidate | Governed agent runtime for founders & operators |
| [design-anything](https://github.com/wjlgatech/design-anything) | 🦾 physical | ⚪ candidate | Design intent -> gate-verified physical blueprints: STL, floor plans, sewing patterns, sim scenes |
| [loop-engineering-anything](https://github.com/wjlgatech/loop-engineering-anything) | ⚙️ engine | ⚪ candidate | Self-improving orchestrator: generate, judge, refactor, re-judge toward convergence |
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
