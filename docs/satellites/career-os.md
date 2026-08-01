# Satellite digest — career-os

- **Pinned (remote HEAD via shallow clone, 2026-07-25):** `395b64b2cb2f`
- **Upstream:** https://github.com/wjlgatech/career-os (PUBLIC)
- **Role here:** 💻 digital — the family's job-search organ.

## Confirmed facts (README @ pin)

- "Autonomous job search pipeline + precision self-upgrading engine."
- Built on career-ops by @santifer (credited upstream base), extended with a diagnostic inner
  loop that didn't exist before.

## Unconfirmed / honest gaps

- ~~No local checkout on this machine~~ **Resolved 2026-08-01**: cloned locally, HEAD matches the
  pin exactly (`395b64b`).
- **The repo has no machine gate.** The clone was inspected for a live gate run and there is
  nothing to run: no Makefile, no tests/, no pyproject — it is a markdown/config-driven repo
  (CLAUDE.md protocol, templates, modes/). Per *no-evidence-means-no*, 🟡 remains its ceiling;
  the promotion path is upstream (career-os grows a `make check`), not here.
