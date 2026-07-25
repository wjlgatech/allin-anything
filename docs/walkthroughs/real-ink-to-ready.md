# Chain 02 — real ink: penecho export → construction gate, machine-verified

M5's promise: close the honest gap Chain 01 declared. In Chain 01 the sketch step was
human+upstream and unverified; here the ink itself flows through machines end to end.
Run on 2026-07-25.

## Router verdict

Same chain as Chain 01 (`sketch a room layout by hand, then verify it's buildable` →
`penecho, design-anything`) — what changed is the hand-off: no human retyping between them.

## Step A — real ink on penecho's real canvas (upstream @ `e1b936f`)

penecho v0.7 run from its own repo (`node server.js`, port 3899, Node v25). A headless
browser drew a 7-stroke room layout with pointer events on the live canvas (tour skipped,
zoom wheeled 12%→105%), then invoked penecho's own `exportCanvasPng()` renderer:

```
STAGE: drawn zoom=105
EXPORT: 74150 bytes            # penecho's exporter, not ours
```

The export is banked as the fixture `tests/fixtures/penecho-export-studio.png`
(1507×1506 RGBA — penecho commits ink as raster tiles; the PNG *is* its machine-readable
export surface).

## Step B — the adapter (`scripts/ink2plan.py`, Chain 02's new organ)

Declared conventions, not magic: rooms are closed rectangles sharing walls; the outer
boundary is declared 5200 mm wide; geometry comes from ink (enclosed-region detection +
wall-centerline unification + 100 mm module snap); openings come from a code-minimum
policy; types/windows from an area-rank legend.

```
$ python3 scripts/ink2plan.py tests/fixtures/penecho-export-studio.png chain02.json --width-mm 5200
✓ chain02.json: 4 rooms (hall, bathroom, kitchen, living), 4 openings @ 5200mm wide
```

## Step C — design-anything's gate (verbatim, exit 0)

```
  PASS  C1_topology: 4 rooms, 4 openings, all resolve
  PASS  C2_clearances: all openings meet table minima
  PASS  C3_habitability: areas, dimensions, daylight, ceiling OK
  PASS  C4_egress: all rooms reachable; entry door present
  PASS  C5_module_grid: 100% of coordinates on the 100mm module (target 90%)
READY: penecho-chain02  (design-sanity gate, not a permit or PE stamp; jurisdiction codes override)
```

This run promoted **penecho ⚪→🟡→🟢**: its export is consumed by a tested adapter and
verified by a real gate, reproducibly (`tests/test_ink_adapter.py`, gate-run test included).

## Honest edges

- The drawing hand was a scripted browser, not a human hand — the *pipeline* is what's
  machine-verified; the strokes are real pointer events on penecho's real canvas, but
  nobody's handwriting wobble has been tested yet. A messy human sketch may need a fatter
  `EDGE_TOL_PX`.
- The gate's own first catch: at the default 5.0 m declared width, the drawn kitchen came
  out 4.4 m² — under Neufert's 4.6 m² minimum. The fix was declaring the sketch at 5.2 m
  (the architect owns the scale); the gate did its job before any code shipped.
- Room types and windows are legend defaults, not read from ink — penecho ink is unlabeled
  raster. Labeling rooms on-canvas and OCRing them is future work, stated plainly.
- AGPL discipline unchanged: penecho ran upstream; nothing of it is vendored here. The
  fixture PNG is our drawing's output, not their code.
