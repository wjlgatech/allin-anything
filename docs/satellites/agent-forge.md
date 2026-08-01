# Satellite digest — agent-forge 🔒

- **Pinned (local HEAD, 2026-07-28):** `a3b0fa082cf1`
- **Upstream:** https://github.com/wjlgatech/agent-forge (PRIVATE — pointer only)
- **Renamed** from `blueprint-anything` (owner's call, 2026-07-28); local folder + remote + this
  registry all follow the new name.
- **Role here:** ⚙️ engine — the *before-you-build* studio for every agent this family ships.

## Public-safe summary

- Turns "we want an agent that does X" into a build-ready blueprint: deterministic L0–L5 autonomy
  placement (with loud rejections), design dossier, red-team review, cost envelope, and a portable
  platform-neutral agent contract compiling to six platform targets. Engine codename: Forge.
- Each capability is a tested package; Makefile check gate present.

Details beyond this summary stay in the private repo.

## Live gate evidence (2026-08-01)

- `make check` run here at the exact pin (`a3b0fa0`): **exit 0** — `gate_check.py` PASS
  (11 deliverables verified) + **324 tests passed** (6.8s). Promoted 🟡→🟢 on that run.
