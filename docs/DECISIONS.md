# Decision log

- **2026-07-25 · M8: autonomy is calibrated by assessment, not argued with.** BRACE Tier-1 scored
  the AutoRunner deployment NO-GO (15/44) — so the autonomy ceiling IS local, human-launched
  gate-running with mandatory human gates. The score is the design constraint; raising the
  ceiling requires actually closing the named blockers (scoped revocable credentials, recursive
  kill switch, isolation). An honest NO-GO obeyed beats a gamed GO.
- **2026-07-25 · License = CC0 1.0 (family precedent: FM-os, rsi-os), with explicit boundaries**
  (external satellites keep their licenses; 🔒 pointers not covered). Swap to MIT/other is one
  file if Paul prefers.
- **2026-07-25 · M9 target shortfall stated:** 9×6 was the aspiration; shipped 8×5. The deltas
  are named work (career-os needs a live gate run for 🟢; Chain 06 queued), not silently dropped.

- **2026-07-25 · M6: career-os digested from a remote pin.** No local checkout exists on this
  machine; the digest was built from a shallow clone pinned at `395b64b2cb2f`. Its gate was not
  run, so 🟡 is its ceiling — a live run is the promotion path.
- **2026-07-25 · M7: a chain's minimum bar = router verdict (pytest) + the target's own gate run
  live (exit 0) + a manifest-gated walkthrough with honest edges.** Chains 04/05 verify the
  hand-off target's health, not a domain computation — the deeper golden examples are named as
  the next depth in each walkthrough, not claimed.

- **2026-07-25 · Charter retrofitted; META_REPO_PLAYBOOK minted.** Paul's audit was correct: no
  meta-repo playbook existed — the repo followed REPO_PLAYBOOK mechanics but had a build log where
  a founding charter belonged. Fixed both ends: `_templates/META_REPO_PLAYBOOK.md` (canonical,
  earned from strategize-/research-/design-/allin-anything) now mandates charter-before-scaffold;
  this repo gained docs/VISION.md (north-star: verified reach = 🟢 × chains) + a phased ROADMAP
  (M5–M9), both manifest-gated by tests/test_charter.py so the charter can't rot into prose.

- **2026-07-25 · Shape = content/publishing (playbook default).** Public build with a portfolio
  launch (M4). No deviation from the playbook shapes.
- **2026-07-25 · penecho is a satellite, never a base.** AGPL-3.0-only upstream → pointer +
  pinned digest + routing hint. No fork, no vendoring, no code reuse. We take the *pattern*
  (draft-vs-confirmed human gate; physical ink as input modality), not the expression.
- **2026-07-25 · Private repos are excluded or pointer-only.** strategize-anything and
  ai-strategy-engine are NOT in the public registry; anyagent appears as a pointer with
  `visibility: private` and no source exposure.
- **2026-07-25 · M1: private satellites are public-safe pointers.** Paul explicitly listed
  strategize-anything and reverse-engineering-anything (both marked "do not expose" in their own
  READMEs, both local-only) for digest wave 1. Resolution: registry entries + digests carry ONLY a
  generic one-liner and a pinned SHA — names were already public via the seeded REPO_PLAYBOOK.md;
  no architecture, URL, or roadmap detail is published. Revert = delete two entries + two files.
- **2026-07-25 · M1: "FED-os" read as FDE-os.** No FED-os exists locally; FDE-os does and fits the
  wave. Recorded here so a wrong guess is one grep away from correction.
- **2026-07-25 · Registry starts honest.** 7 of 9 satellites are ⚪ candidates on day one; the
  README says so. Statuses advance only with evidence (playbook: no-evidence-means-no).
