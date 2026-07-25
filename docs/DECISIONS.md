# Decision log

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
