# REPO_PLAYBOOK — how a Paul Wu `-anything` / `-os` repo is built

> **Canonical single source.** This file lives in `Projects/_templates/` and is seeded into
> every new repo by `new-project.sh` (as `docs/REPO_PLAYBOOK.md`). Edit it HERE; the copies in
> repos are instances. Earned across design-anything, graph-engineering-anything,
> reverse-engineering-anything, strategize-anything, and research-anything.

## 0. Two project shapes — pick first

| Shape | When | CLAUDE.md template | Publishing |
|---|---|---|---|
| **Content / publishing** (default) | public build with a LinkedIn/X/portfolio launch | `_templates/CLAUDE.md.template` | LinkedIn docs + portfolio-first flow |
| **Private engineering** | private repo, spec-first build | `_templates/CLAUDE.md.private-engineering.template` | NONE (a publish flow in a must-stay-private repo invites accidental exposure) |

Record any deviation from either shape in the project's decision log.

## 1. The shape (what every repo has)

```
<name>/
├── GOAL.md              10x contract: verbatim intent → eval → the 10x move → milestone table
├── Makefile             `make check` = the offline, deterministic finish line
├── data/*.yml           the SINGLE SOURCE OF TRUTH (spec-as-data). Nothing hand-edited downstream.
├── docs/                ARCHITECTURE · SPEC · ROADMAP · LANDSCAPE · REPO_PLAYBOOK (this file)
├── src/<pkg>/           the OOP engine (typed models + single-responsibility services)
├── scripts/             thin CLIs over the engine (logic lives in src, never in the CLI)
├── tests/               pytest; every gate has an executable test
├── skills/              the flagship thin-router skill + generated satellites (if it composes repos)
├── research/            window-dated digests (30 days / months / years / 300 years) — if research-shaped
├── llms.txt · README (with a drift-gated News block) · CHANGELOG · CONTRIBUTING · CLAUDE.md
└── .github/workflows/   check.yml (gate) + a weekly, human-gated sync (if it tracks upstreams)
```

## 2. The non-negotiable disciplines (each becomes a `data/ainative.yml` principle)

- **spec-as-data** — curated knowledge lives in `data/*.yml`; every published surface (README
  sections, skills, contracts) is GENERATED and **drift-gated** (`build --check`).
- **ready-is-a-gate** — the repo's domain has a definition of "done" as a machine gate with exit
  codes (design=geometry; research=claim-gate; a doc phase=a manifest gate). A gate never vibes.
- **no-evidence-means-no** — an unmeasured/unreachable item is excluded, never a fake pass; a
  blocking gate cannot pass on unmeasured items.
- **maker-is-not-checker** — generators and gates are independent, held together by tests.
- **satellites, never vendored** — a cited external repo is a pointer + a SHA-pinned digest + a
  generated thin skill; freshness is *measured* (STALE flag), not promised.
- **compounding-memory** — updates and lessons land in `data/` (news, tables, this playbook), not chat.
- **honest-edges** — limitations stated where users read them (`README ## Honest edges`).
- **human-gated-irreversible** — network sync opens a PR; merges/publishes stay human.
- **the repo audits itself** — `data/ainative.yml` + `scripts/ainative.py` score HOW the repo
  operates with in-repo evidence, gated in CI (a discipline regression fails the build).

## 3. The build loop (goal-10x)

Research (map, don't guess; read backbone + sibling repos) → Absorb (reflect intent ≤6 lines) →
Coach (≤2 forks) → **Drive to green** (verification is the only truth; drive the *discovered*
check) → Self-improve (bank the lesson into `data/`, not chat). The ROADMAP is a machine-checkable
milestone table; each milestone has a runnable DoD. **Score with `anyagent analyze <dir>` at EACH
milestone**, not once at the end — and don't game a sub-metric (trust the artifact, not the label).

## 4. Signature files often forgotten — add them

`data/ainative.yml` + `scripts/ainative.py` + test (self-audit, CI-gated ≥90) · `data/news.yml`
→ drift-gated README block · `eval/<skill>.md` (should / should-not-trigger, each backed by a
test) · `llms.txt` · `.github/ISSUE_TEMPLATE/gate-dispute.md` · `## Honest edges` in README.

### 4a. Agentic webapp? Then 1-click activation is part of DONE

Paul's standing rule (2026-08-01): if the repo has a demo/webapp, its link goes at the
**top of README** (first screen), the server **auto-opens the browser** on start
(`--no-open` escape hatch for CI), and the app is installable (PWA manifest / one
`make demo` command). Add a drift test that pins the README link — undemoed ⇒ unshipped.
**Amendment (2026-08-01):** 1-click means **remotely visitable** — deploy a public
demo (Vercel) serving a build-time snapshot that NEVER executes; receipts replace
execution panels remotely; the local command stays the power path.

## 5. Transferable lessons (earned, promote-worthy)

1. **The satellite pattern is domain-agnostic** — if your repo composes external repos, index +
   pinned digest + generated skill, never a fork.
2. **The gate's semantics are domain-specific; the gate discipline is universal** — build the gate
   that encodes YOUR domain's "verified" (geometry / claim / manifest).
3. **Model orchestration as a graph and gate reachability** — no orphan node; no path reaches the
   output bypassing the gate (networkx).
4. **Make the closed loop a real object** — generate → score vs an independent referee → refine,
   roll back regressions, report how it converged (F→A).
5. **Benchmarks/evals are first-class modules with honest "not measured."**
6. **Keep the gate offline & deterministic**; put all network in `sync` + a weekly workflow (use a
   FakeProvider/fixtures for reproducibility).
7. **Digest a cited repo with a parallel sub-agent** that pins the HEAD sha and flags unconfirmed
   facts (never invent an install command or API signature).
8. **An evidence-type taxonomy defeats "engagement is not evidence"** — tag every finding; weak
   evidence can't rank until it crosses an adoption window.
9. **Encode architectural invariants as executable tests** (import-lint for dependency direction,
   schema-enforced provenance, graph-integrity) — structural gates catch the real bugs.
10. **Greenfield doc phases** — `anyagent goal` can't route a document phase; build the finish line
    first (a manifest gate: file exists + min words + required headings), then drive docs to green.
    Human approval lives in a doc's `Status:` line the gate relays verbatim, never infers.

## 6. Minting the next repo

`./new-project.sh <name> …` seeds this playbook + the shape's CLAUDE.md. Then: compile `GOAL.md`,
stand up `data/*.yml` + `make check` FIRST (green at birth), add the flagship skill, then
satellites one repo at a time (candidate → digested → integrated, each advance gated by on-disk
evidence). Wire `data/ainative.yml` early so the repo holds its own discipline from day one.
