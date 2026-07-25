# META_REPO_PLAYBOOK — how a Paul Wu meta-repo (super-repo / super-tool) is built

> **Canonical single source.** Lives in `Projects/_templates/`; seed a copy into each meta-repo's
> `docs/`. Extends `REPO_PLAYBOOK.md` (which governs the repo *mechanics*: spec-as-data, gates,
> satellites, self-audit). This file governs the layer above: WHY the meta-repo exists, WHAT it
> composes, and HOW its milestone arc runs. Earned from strategize-anything (founding brief +
> approval gate), research-anything (10x contract + windows), design-anything (organ gates +
> golden examples), and allin-anything (registry + router + chains).

## 0. What makes a repo *meta*

A meta-repo owns **no domain logic**. Its product is a **verified composition**: a registry of
capabilities (its own family repos + licensed external satellites), a router that turns an intent
into a hand-off, and chains that compose satellites across a border (digital↔physical,
domain↔domain). The moment a meta-repo implements a domain inline, it has failed — build or
promote a satellite instead. **Aggregate exit codes, never claims.**

## 1. Born with a charter, not a scaffold (the missing piece scaffolds skip)

Before `make check` exists, three documents exist — each drift/manifest-gated like code:

- **`docs/VISION.md`** — Vision (the world when this wins, one paragraph) · Mission (what THIS
  repo does about it, one paragraph) · **North-star metric** (one number a machine can compute
  from the repo, e.g. "verified chains × coverage") · **Operating modes** (AI-assisted: human
  leads, AI supports · AI-autonomous: bounded workflows, validation gates, human oversight —
  every meta-repo declares both and which milestones unlock the second) · **Non-goals** (what
  this repo will never do, stated where users read).
- **`GOAL.md`** — the verbatim founding intent, recompiled into a machine-verifiable 10x contract
  (10xgoal discipline: eval table of strong/bundled/unmeasurable, then the un-bundling).
- **`docs/ROADMAP.md`** — the milestone ARC (§3), each row with a runnable DoD.

Privacy is declared in the charter on day one (strategize-anything lesson): public build vs
private/spec-first decides publishing machinery, registry exposure, and digest depth.

## 2. Composition doctrine

- **Satellite, organ, or chain — name which one.** *Satellite*: an external/family repo indexed
  by pointer + pinned SHA + digest (never vendored; license recorded; AGPL/unlicensed ⇒ pointer
  only, run upstream). *Organ*: a swappable internal seam the composer calls (design-anything's
  Gate seam, master-anything's six organs). *Chain*: ≥2 satellites composed across a border,
  proven by a walkthrough with verbatim gate output.
- **The status ladder is the product**: ⚪ candidate (named) → 🟡 digested (facts pinned to a SHA,
  unconfirmed labeled) → 🟢 integrated (its own gate ran HERE, exit 0, routed by the flagship).
  A validator refuses promotions whose on-disk evidence is missing. Honest borders: a step a
  machine didn't verify (human/upstream) is labeled so and caps the status (penecho rule).
- **The router is executable, not prose**: triggers live in the registry (spec-as-data); every
  routing claim in the eval file is a pytest — including the refusals (license walls, go-direct,
  no-match ⇒ bank the gap).

## 3. The milestone arc (the shape recurs across every meta-repo)

| Phase | Milestone shape | DoD pattern |
|---|---|---|
| **Foundation** | born green: charter + registry + gates + self-audit + flagship skill | `make check` exit 0 at birth |
| **Coverage** | digest waves until zero ⚪ | every satellite 🟡+, each with pinned digest |
| **Proof** | first cross-border chain, run live | walkthrough doc (manifest-gated) + the satellite's own gate exit 0 |
| **Library** | N chains, golden examples banked from real runs | each chain has walkthrough + eval case + test |
| **Autonomy** | AI-autonomous mode unlocked for bounded chains | security/enterprise assessment passes; human gates at every irreversible step |
| **Cadence** | public launch + a compounding rhythm | portfolio-first long-form per chain; weekly freshness sync (STALE measured, human-gated PRs) |

Score with `anyagent analyze` at every milestone; record the trajectory honestly (don't game a
sub-metric). A milestone that shipped mechanics without moving the north-star metric is logged as
maintenance, not progress.

## 4. The meta-repo audits its meta-ness

Beyond the repo-level `ainative.yml`, the self-audit should assert the meta laws with in-repo
evidence: no vendored satellite trees; every 🟢 has a run receipt; the router refuses what the
licenses forbid; VISION/ROADMAP manifest-gated; the north-star metric computable offline.

## 5. Transferable lessons (earned)

1. **Charter-first beats scaffold-first** — allin-anything shipped M0–M4 in a day but had to
   retrofit its VISION; strategize-anything's founding brief made every later gate decidable.
2. **The border crossing must be explicit** — label the human/upstream step; the chain's
   credibility comes from the labeled seam, not despite it.
3. **Replace-don't-accrete registry curation** — the owner prunes (company-os → ai-native-os);
   the registry is a portfolio decision surface, not a hoard.
4. **Infra failures get evidence-driven rollbacks** — revert to last-green, record "a rollback,
   not a diagnosis," close the loop when evidence arrives.
5. **One YAML entry = one new capability** — if adding a satellite costs more than a registry
   entry + digest, the composition layer has leaked domain logic.
