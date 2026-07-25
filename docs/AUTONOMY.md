# AUTONOMY — M8: bounded, earned, and calibrated by assessment (2026-07-25)

> The rule: **autonomy is granted per-chain, at the level the evidence supports — never
> repo-wide, never asserted.** Spec: `data/chains.yml` · Enforcer: `src/allin_anything/autorun.py`
> · Tests: `tests/test_autonomy.py`.

## What the AutoRunner is (and is not)

A **deterministic subprocess orchestrator** — no LLM in the execution loop. It runs only chains
marked `autonomous_bounded`, re-checks every satellite is 🟢 at run time (a demotion revokes
autonomy immediately), treats a missing local checkout as BLOCKED (never a fake pass), journals
every run to `runs/journal.jsonl` (attributable, auditable), and **always stops before the
declared human gates**. Every chain must declare at least one — the validator refuses a chain
without a human gate.

## The live bounded run (verbatim, chain-02)

```
✓ [ok] python3 scripts/ink2plan.py tests/fixtures/penecho-export-studio.png … (exit 0)
✓ [ok] python3 pipeline/construction_gate.py /tmp/allin-chain02.json (exit 0)
    READY: chain02-autorun  (design-sanity gate, not a permit or PE stamp…)
⏸ execution stops here — human owns:
  🔑 approving any real-world build (READY is design-sanity, not a permit)
```

## The assessments (honest numbers, not trophies)

- **BRACE Tier-1 (`anyagent brace data/brace-manifest.json`): NO-GO ⛔ · 15/44** (22/29 items
  assessed). Named blockers: wildcard-free scoped credentials, independently revocable
  credentials, recursive kill switch — all true of a local, host-run, human-launched CLI.
- **Consequence encoded, not argued with:** because Tier-1 is NO-GO, autonomy here is *bounded
  to read-only gate-running chains on a human-launched local process* — exactly what the
  AutoRunner enforces. Anything more (network egress, credentialed actions, unattended
  scheduling of chain runs) requires closing the BRACE blockers first. The manifest is honest
  (no container, no isolation claimed); the score is the design constraint, not a failure.
- **Enterprise readiness (`anyagent enterprise .`): 6/14 → 7/14 (50%)** after M8 (governance ✓:
  LICENSE + CODEOWNERS; evaluation ✓; packaging ✓). Remaining gaps recorded, not gamed:
  MCP integration and OTel observability are v1.x candidates; "security & containment" tracks
  the BRACE blockers above.

## Threshold statement (the M8 DoD, resolved honestly)

The gate M8 ships with: **every autonomous chain passes `chains.validate` (all satellites 🟢 +
human gates declared) and a live bounded run exits 0** — met. The BRACE/enterprise scores are
recorded as calibration inputs, and the autonomy ceiling is set to what they support. An honest
NO-GO with a matching ceiling beats a gamed GO.
