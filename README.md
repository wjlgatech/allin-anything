# allin-anything

**All-in interaction with both the digital and physical world — one super-repo that composes the
`-anything` / `-os` agent family into a single front door.**

You bring an intent ("design me a bracket I can print", "master this paper", "run my job search").
The flagship skill routes it to the right satellite repo; every satellite is indexed here with a
verified status — never vendored, never guessed.

Inspired by [penecho](https://github.com/penecho/penecho): a shared canvas where physical ink
becomes digital model input. allin-anything generalizes that bridge — *any* physical or digital
surface, one interaction contract.

## Verified reach

<!-- BEGIN GENERATED: reach -->
**Verified reach = 8 🟢 × 5 chains = 40** — computed from `data/registry.yml` + `docs/walkthroughs/`, drift-gated (see docs/VISION.md).
<!-- END GENERATED: reach -->

## News

<!-- BEGIN GENERATED: news -->
- **2026-07-27** — First learn-chain artifact: 2026 Fields Medalists, all-in style (zh-CN): examples/fields-2026/: 61KB English briefing → 6-session Simplified-Chinese learning page, each session with key idea + mechanism + pure-CSS animation (animate-anything craft), Anthropic brand, browser-verified (0 console errors). Router gap banked: animate-anything joined the registry as ⚪ candidate.
- **2026-07-25** — v1.0 launch article live — 'The Best Number in My v1.0 Was a NO-GO.': Long-form on the portfolio (PR #123, canonical URL live-verified) with cover + one-day-arc infographic; LinkedIn/X composers prefilled, posting stays Paul's click.
- **2026-07-25** — v1.0 — M8 bounded autonomy (BRACE-calibrated) + M9 cadence; reach 40: chains.yml + AutoRunner (🟢-only, human gates mandatory, journaled; live chain-02 run exit 0). BRACE Tier-1 honestly NO-GO 15/44 → autonomy ceiling = local gate-running. Enterprise 43%→50% (LICENSE CC0 + CODEOWNERS). Weekly freshness workflow (stale pin → human-gated issue). rsi-os, FM-os, FDE-os 🟢 by live gate runs (225 tests on FDE-os). Reach 5×5 → 8×5 = 40.
<!-- END GENERATED: news -->

## Satellites

Single source of truth: [`data/registry.yml`](data/registry.yml). This table is generated —
edit the YAML, run `make build`; CI fails on drift.

<!-- BEGIN GENERATED: satellites -->
| Satellite | World | Status | Capability |
|---|---|---|---|
| [FDE-os](https://github.com/wjlgatech/FDE-os) | 🌉 bridge | 🟢 integrated | Operating system for Forward Deployed Engineers — ship agentic systems inside the customer's real environment; live 3-door webapp |
| [FM-os](https://github.com/wjlgatech/FM-os) | 💻 digital | 🟢 integrated | Living map of how language models are actually built and shipped — pre/post-training, fine-tuning, RL, SLM-first |
| [anyagent](https://github.com/wjlgatech/anyagent) 🔒 | ⚙️ engine | 🟢 integrated | Build, grade, improve & accountably ship any agent app; goal-10x front door drives every repo in this registry |
| [design-anything](https://github.com/wjlgatech/design-anything) 🔒 | 🦾 physical | 🟢 integrated | Design intent -> gate-verified physical blueprints: STL, floor plans, sewing patterns, sim scenes |
| [graph-engineering-anything](https://github.com/wjlgatech/graph-engineering-anything) 🔒 | 💻 digital | 🟢 integrated | Graph Engineering Operating System — 'the model finds text; the graph finds reality'; evidence-tiered knowledge graphs + a copilot that won't bluff (live demo on Vercel) |
| [money-os](https://github.com/wjlgatech/money-os) | 💻 digital | 🟢 integrated | AI financial co-pilot — local-only data, zero uploads, zero subscriptions (v4.0) |
| [penecho](https://github.com/penecho/penecho) `@e1b936f` | 🌉 bridge | 🟢 integrated | AI spatial canvas — handwriting, equations, diagrams become model input; drafts return to the canvas (pen -> digital bridge) |
| [rsi-os](https://github.com/wjlgatech/rsi-os) | ⚙️ engine | 🟢 integrated | Living, community-driven map of Recursive Self-Improvement / automated AI research — Godel Machine (2003) to AI Scientists (2026) |
| [ai-native-os](https://github.com/wjlgatech/physical-ai-native-os) 🔒 | 💻 digital | 🟡 digested | Operating system for running an AI-native organization — knowledge captured in agents, contracts, durable state so it compounds instead of walking out the door |
| [blueprint-anything](https://github.com/wjlgatech/blueprint-anything) 🔒 | ⚙️ engine | 🟡 digested | Agent design & feasibility studio (Forge): autonomy dial L0-L5, design dossier, cost envelope, portable contract for six platforms |
| [career-os](https://github.com/wjlgatech/career-os) | 💻 digital | 🟡 digested | Autonomous job-search pipeline + self-upgrading inner loop |
| [loop-engineering-anything](https://github.com/wjlgatech/loop-engineering-anything) | ⚙️ engine | 🟡 digested | Self-improving orchestrator: generate, judge, refactor, re-judge toward convergence |
| [master-anything](https://github.com/wjlgatech/master-anything) 🔒 | 💻 digital | 🟡 digested | Master any hard topic in ~60 min: teach-back gate, fun >=4/5 measured, one portfolio artifact, +7-day retention probe |
| [neuro-os](https://github.com/wjlgatech/neuro-os) | 🦾 physical | 🟡 digested | Executable neuroscience knowledge — brain mechanisms as primitives (the wetware end of physical) |
| [research-anything](https://github.com/wjlgatech/research-anything) 🔒 | 💻 digital | 🟡 digested | Any research question in -> a verified, window-dated, autonomy-aware brief out (science, engineering, medicine, business) |
| `reverse-engineering-anything` 🔒 | ⚙️ engine | 🟡 digested | AI-powered reverse engineering meta-repo: Observe -> Decompose -> Model -> Reconstruct -> Validate -> Improve -> Generalize |
| `strategize-anything` 🔒 | 💻 digital | 🟡 digested | Private strategy operating system (AI-assisted and AI-autonomous modes) |
| [animate-anything](https://github.com/wjlgatech/animate-anything) | 💻 digital | ⚪ candidate | The ranked, living map of animation — CSS keyframes to AI-authored video; machine-readable registry for agents; interactive map on Pages |
<!-- END GENERATED: satellites -->

Status ladder: ⚪ candidate → 🟡 digested (pinned digest in `docs/satellites/`) → 🟢 integrated
(routed by the flagship skill). Each advance is gated by on-disk evidence.

## The finish line

```bash
make check   # pytest + drift gate + ainative self-audit (offline, deterministic)
```

## Honest edges

- A 🟡 satellite's own gate has NOT run here — only its facts are pinned. The table tells you
  exactly which; nothing here pretends otherwise (career-os isn't even checked out locally).
- Autonomy is bounded and BRACE-calibrated: the assessment says NO-GO beyond local gate-running,
  and the AutoRunner obeys it — every chain stops at a declared human gate (docs/AUTONOMY.md).
- penecho is AGPL-3.0 and lives upstream: we index it (pointer + pinned SHA + digest), we do not
  ship, fork, or wrap its code. Run it from its own repo.
- The physical-world reach is only as real as each satellite's own gates (e.g. design-anything's
  geometry checks). A gate is never a permit or a PE stamp.
- Private family repos (e.g. anyagent) are pointers only; their source is not public.

## How this repo operates

`docs/REPO_PLAYBOOK.md` is the build pattern; `data/ainative.yml` + `scripts/ainative.py` score
this repo against it inside `make check` — a discipline regression fails the build.
