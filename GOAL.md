# GOAL — allin-anything

## Verbatim intent (Paul, 2026-07-25)

> "I want to create a super-repo called allin-anything, which give people all-in interaction with
> both the digital and physical world, I got inspired and want to start from
> https://github.com/penecho/penecho. Use our super-repo (i.e. meta-repo) playbook to build it.
> Reference to all my recent \<X\>-anything, \<Y\>-os repos."

## Compiled objective

One gate-verified registry + one thin router skill that turns 20+ scattered family repos into a
single front door for digital-AND-physical intents — with penecho indexed (AGPL: pointer only)
as the founding bridge satellite.

## Eval — what "done" means, machine-checkable

- `make check` exits 0: pytest + README drift gate + ainative self-audit ≥90 (offline, deterministic).
- Every registry status is backed by on-disk evidence (digest file, skill routing) — enforced by
  `registry.validate`, not by promises.
- `anyagent analyze .` score recorded per milestone in docs/ROADMAP.md.

## The 10x move

Not another app — a **composition contract**. Each satellite already does one world well; the 10x
is the verified index + router that makes them one product, at the cost of one YAML entry per repo.

## Charter → docs/VISION.md (vision · mission · north-star · operating modes · non-goals)
## Milestones → docs/ROADMAP.md (the arc: Foundation → Coverage → Proof → Library → Autonomy → Cadence)
## Pattern → docs/META_REPO_PLAYBOOK.md (canonical copy: `_templates/META_REPO_PLAYBOOK.md`)
