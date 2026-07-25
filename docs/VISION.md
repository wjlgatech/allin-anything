# VISION — allin-anything

> The charter this repo should have been born with (retrofitted 2026-07-25, per
> `docs/META_REPO_PLAYBOOK.md` §1 — logged honestly in DECISIONS.md). Manifest-gated by
> `tests/test_charter.py`.

## Vision

Anyone — a person or an agent — can act on both the digital and the physical world through **one
front door**, and can see, before they act, exactly how much of each capability a machine has
verified. Interaction with reality becomes as composable as software: sketch → buildable plan,
question → verified brief, intent → shipped agent — with the trust level of every link printed on
the chain, never assumed.

## Mission

Compose the `-anything` / `-os` family (plus licensed external satellites like penecho) into a
single gate-verified registry, a deterministic router, and a growing library of **cross-border
chains** — digital↔physical first — where every satellite's status is earned by running its own
gate, every external repo stays a pointer (never vendored), and every irreversible step keeps a
human hand on it.

## North-star metric

**Verified reach = (🟢 integrated satellites) × (proven chains).** Computable offline from
`data/registry.yml` + `docs/walkthroughs/` — currently 8 × 5 = 40. Coverage
(zero ⚪ in the registry) and chain count are the two levers; a milestone that moves neither is
maintenance, not progress.

## Operating modes

- **AI-assisted (today):** the router declares the hand-off with statuses disclosed; a human runs
  the satellite. Chain 01 ran this way — the human/upstream sketch step is labeled, not hidden.
- **AI-autonomous (unlocked at M8, bounded):** `scripts/autorun.py` executes chains marked
  `autonomous_bounded` in `data/chains.yml` — only when every satellite is 🟢 (re-checked at run
  time), always stopping at the declared human gates. The autonomy *ceiling* is calibrated by
  assessment (BRACE Tier-1 currently NO-GO for anything beyond local gate-running — see
  docs/AUTONOMY.md); it rises only when those blockers actually close.

## Non-goals

- **Never implement a domain inline.** A missing capability becomes a satellite (or a new family
  repo), never code in this repo — one YAML entry + one digest is the whole cost of growth.
- **Never vendor external code.** AGPL or not, a satellite is a pointer + pinned SHA + digest.
- **Never confuse a gate with a guarantee.** READY means design-sane / test-green; it is not a
  permit, a PE stamp, or financial advice — each satellite's own honest edges govern.
- **Never publish the private.** Private/local-only family repos appear as public-safe pointers
  only (🔒), by owner's rule.
