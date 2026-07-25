# Chain 05 — knowledge: a corpus intent lands on the Graph Engineering OS

M7's knowledge chain, run live 2026-07-25: intent → graph-engineering-anything → its own
`make check`. Also a chain-declared pairing: the router surfaces research-anything as the
window-dated research partner, statuses disclosed.

## Router verdict (verbatim)

```
$ python3 scripts/route.py "build the knowledge graph for my research corpus"
mode: route
satellites: graph-engineering-anything, research-anything
reason: trigger match (graph-engineering-anything=integrated, research-anything=digested)
```

## The run (graph-engineering-anything @ `d39c26a8e1c0`, verbatim tail)

```
$ make -C graph-engineering-anything check
python3 -m unittest discover -s tests -q
✅ check green
✅ selftest: scaffolded repo is green at birth
```

**Exit code: 0** — including its green-at-birth scaffold selftest (the same discipline this
repo was born under; the family's patterns verify each other).

## Honest edges

- No actual corpus was graphed in this run — the chain verifies routing + the target's own gate,
  not a specific graph build. Its public demo (graph-engineering-anything-demo.vercel.app) is
  the user-facing proof surface.
- research-anything is declared in the chain at 🟡 — its gate wasn't run here; the router
  disclosed that instead of hiding it.
