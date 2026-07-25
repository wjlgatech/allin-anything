# Chain 04 — all-digital: a finance intent lands on money-os's own gates

M7's all-digital chain, run live 2026-07-25: intent → money-os (a sibling meta-repo) → its own
`make check` as the verification hand-off.

## Router verdict (verbatim)

```
$ python3 scripts/route.py "run my weekly finance review and rebalance my budget"
mode: route
satellites: money-os
reason: trigger match (money-os=integrated)
```

## The run (money-os local checkout, verbatim tail)

```
$ make -C money-os check
python3 -m pytest -q tests/
............................                                             [100%]
28 passed in 0.78s
✅ make check — all gates green
```

**Exit code: 0.** money-os is itself playbook-shaped (registry + certify + ainative self-audit +
satellites + pytest per its CLAUDE.md) — so its green is a composed verdict, not one test file.

## Honest edges

- This chain verifies the hand-off target's health, not a specific financial computation — no
  budget was actually rebalanced. The next depth is running one money-os skill end-to-end and
  banking its output as a golden example.
- money-os data stays local by its design (zero uploads); nothing financial crossed into this repo.
