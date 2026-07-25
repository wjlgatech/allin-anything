---
name: allin-anything
description: One front door for all-in interaction with the digital and physical world. Absorbs a messy intent and routes it to the right satellite repo from data/registry.yml (design a physical thing, master a topic, run finances/career/company, build an agent, think on a spatial canvas). Trigger: "/allin", "which repo/tool of mine does X", "interact with the physical world", or any intent that spans more than one family repo.
---

# allin-anything — the thin router

This skill holds NO domain logic. It reads the registry, routes, and hands off.
Single source of truth: `data/registry.yml` (statuses are gate-verified, never vibes).

## Protocol

1. **Absorb** the intent in ≤3 lines; classify the world it touches: 💻 digital, 🦾 physical, or 🌉 both.
2. **Route** by capability match against the registry. Prefer 🟢 integrated > 🟡 digested > ⚪ candidate;
   tell the user the status of what you routed to (a ⚪ candidate means "exists, not yet verified here").
3. **Hand off** to the satellite's own skill/CLI. Never re-implement a satellite inline.
4. **Bank**: if routing revealed a gap (no satellite matched), append the gap to `data/news.yml`.

## Routing table (integrated satellites)

- **anyagent** (⚙️ engine) — "build/grade/improve/ship an agent app", messy objectives → `anyagent goal`.

## Routing hints (digested / candidates — verify before promising)

- penecho (🌉 bridge, external, AGPL) — handwriting/spatial-canvas thinking → point the user to run
  it upstream (`github.com/penecho/penecho`, pinned digest in `docs/satellites/penecho.md`). NEVER vendor.
- design-anything (🦾) — physical blueprints with machine gates (STL / floor plan / sewing / sim).
- master-anything (💻) — learn/verify/express any hard topic.
- money-os / career-os / company-os (💻) — finances, job search, founder ops.
- neuro-os (🦾) — brain mechanisms as executable primitives.
- loop-engineering-anything (⚙️) — converge any generate→judge→refactor loop.

## Hard rules

- External satellites are pointers + pinned digests. No forking, no vendoring, no code copying (AGPL).
- A status claim you can't back with `make check` evidence is a lie — don't make it.
