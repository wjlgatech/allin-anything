---
name: allin-anything
description: One front door for all-in interaction with the digital and physical world. Absorbs a messy intent and routes it to the right satellite repo from data/registry.yml (design a physical thing, master a topic, run finances/career/company, build an agent, think on a spatial canvas). Trigger: "/allin", "which repo/tool of mine does X", "interact with the physical world", or any intent that spans more than one family repo.
---

# allin-anything — the thin router

This skill holds NO domain logic. It reads the registry, routes, and hands off.
Single source of truth: `data/registry.yml` (statuses are gate-verified, never vibes).

## Protocol

1. **Absorb** the intent in ≤3 lines; classify the world it touches: 💻 digital, 🦾 physical, or 🌉 both.
2. **Route** — run the deterministic pre-router first: `python3 scripts/route.py "<intent>"`
   (modes: route / direct / none / refuse; every eval case is a pytest in tests/test_router.py).
   Use judgment only to refine its verdict, never to contradict a `refuse`. Prefer 🟢 integrated >
   🟡 digested > ⚪ candidate; tell the user the status of what you routed to (a ⚪ candidate means
   "exists, not yet verified here").
3. **Hand off** to the satellite's own skill/CLI. Never re-implement a satellite inline.
4. **Bank**: if routing revealed a gap (no satellite matched), append the gap to `data/news.yml`.

## Routing table (integrated satellites)

- **anyagent** (⚙️ engine) — "build/grade/improve/ship an agent app", messy objectives → `anyagent goal`.
- **design-anything** (🦾 physical) — physical blueprints with machine gates; Chains 01–03
  (sketch-to-buildable, real-ink-to-ready, brief-to-printable).
- **penecho** (🌉 bridge, external, AGPL — run upstream, NEVER vendor) — handwriting/canvas ink;
  its export feeds `scripts/ink2plan.py` (Chain 02).
- **money-os** (💻) — finances; own gates run live (Chain 04, intent-to-money-gates).
- **graph-engineering-anything** (💻 🔒) — evidence-tiered knowledge graphs; own gates run live
  (Chain 05, corpus-to-graph).
- **rsi-os / FM-os** (⚙️ 💻) — self-improvement + foundation-model knowledge maps; gates run live.
- **FDE-os** (🌉) — ship agents inside the customer's real environment; gates run live (225 tests).

## Routing hints (digested / candidates — verify before promising)

- agent-forge (⚙️ 🔒) — design/scope an agent BEFORE building (autonomy dial, cost, contract).
- master-anything (💻 🔒) — learn/verify/express any hard topic.
- research-anything (💻 🔒) — verified, window-dated research briefs.
- strategize-anything / reverse-engineering-anything (🔒 local-only) — strategy / reconstruction;
  pointer entries, route only for Paul locally.
- career-os / ai-native-os (💻) — job search, AI-native org operations.
- neuro-os (🦾) — brain mechanisms as executable primitives.
- loop-engineering-anything (⚙️) — converge any generate→judge→refactor loop.

## Hard rules

- External satellites are pointers + pinned digests. No forking, no vendoring, no code copying (AGPL).
- A status claim you can't back with `make check` evidence is a lie — don't make it.
