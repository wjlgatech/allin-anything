# Chain 01 — sketch a room layout by hand, then verify it's buildable

The founding allin-anything promise, walked end to end on 2026-07-25: one intent that starts as
physical ink and ends as a machine-verified physical blueprint.

## The intent

> "sketch a room layout by hand, then verify it's buildable"

## Router verdict (verbatim, `python3 scripts/route.py …`)

```
mode: route
satellites: penecho, design-anything
reason: trigger match (penecho=digested, design-anything=candidate)
```

The chain is declared, statuses disclosed. (design-anything has since advanced to 🟢 integrated —
this file is the evidence that promoted it.)

## Step A — the sketch (penecho, upstream, human-gated)

Run penecho from its own repo (`github.com/penecho/penecho`, pinned digest at
`docs/satellites/penecho.md`): draw the room layout on the canvas; the AI draft that comes back
stays separate from confirmed ink until you accept it. Export the confirmed layout.

## Step B — the buildability gate (design-anything @ `eb48a6f78f0c`)

```
$ python3 examples/studio-flat/generate.py /tmp/design-anything-studio.json
wrote /tmp/design-anything-studio.json: 4 rooms, 28.5 m2, 5000x5700 mm overall

$ python3 pipeline/construction_gate.py /tmp/design-anything-studio.json
  PASS  C1_topology: 4 rooms, 4 openings, all resolve
  PASS  C2_clearances: all openings meet table minima
  PASS  C3_habitability: areas, dimensions, daylight, ceiling OK
  PASS  C4_egress: all rooms reachable; entry door present
  PASS  C5_module_grid: 100% of coordinates on the 100mm module (target 90%)
READY: studio-flat  (design-sanity gate, not a permit or PE stamp; jurisdiction codes override)
```

**Gate exit code: 0.** design-anything's full `make check` also ran green (7.7s, ainative 12/12).

## Honest edges

- Step A was NOT machine-executed here: penecho is an upstream Node app (AGPL, never vendored);
  the sketch step is human + upstream by design. What this chain verifies end-to-end is the
  routing and the physical gate — the ink→layout translation is penecho's job, not ours.
- The gated layout is the studio-flat example, standing in for an exported sketch. Wiring a real
  penecho export into `construction_gate` input is the natural M3 follow-up.
- READY means design-sane, not permitted: jurisdiction codes override, always.
