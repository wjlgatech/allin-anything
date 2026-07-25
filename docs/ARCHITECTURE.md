# ARCHITECTURE

```
data/registry.yml ──┐                        (single source of truth)
data/news.yml ──────┤
                    ▼
      src/allin_anything/        typed engine
        models.py                Satellite / Registry (frozen dataclasses)
        registry.py              load + validate (evidence-gated status ladder)
        generate.py              render README blocks (maker)
                    │
        scripts/build.py         thin CLI: write | --check (drift gate)
        scripts/ainative.py      self-audit vs data/ainative.yml (checker)
                    │
        tests/  + Makefile check  ──────►  .github/workflows/check.yml (CI = make check)
                    │
        skills/allin-anything/SKILL.md    thin router (no domain logic)
        docs/satellites/<id>.md           pinned digests (the evidence)
```

Invariants (each has a test or an audit check):

1. Nothing downstream of `data/*.yml` is hand-edited — drift fails the build.
2. A satellite's status cannot advance without its on-disk evidence (`registry.validate`).
3. Maker ≠ checker: `generate.py` renders; pytest + `--check` + `ainative.py` gate.
4. External code is never in-repo (AGPL-safe by construction): pinned SHA + digest + pointer.
5. The gate is offline and deterministic; all network lives in future `sync` tooling, human-gated.
