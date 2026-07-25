# Chain 03 — all-physical: a text brief becomes a printable artifact, gate-verified

M7's physical chain, run live 2026-07-25: intent → design-anything's parametric planter →
`ready_gate` (real STL geometry checks).

## Router verdict (verbatim)

```
$ python3 scripts/route.py "design and 3D print a self-watering planter"
mode: route
satellites: design-anything
reason: trigger match (design-anything=integrated)
```

## The run (design-anything @ `eb48a6f`, verbatim)

```
$ python3 examples/planter/generate.py chain03-planter.stl
wrote chain03-planter.stl: 28 triangles, 120.0x80.0x60.0 mm, wall 3.0 mm, base 4.0 mm

$ python3 pipeline/ready_gate.py chain03-planter.stl --min-feature 3.0
  PASS  G1_watertight: closed 2-manifold
  PASS  G2_outward_normals: signed volume 103584.0 mm^3
  PASS  G3_bed_fit: model (120.0, 80.0, 60.0) mm vs bed (220.0, 220.0, 250.0) mm
  PASS  G4_min_feature: min feature 3.0 mm vs 2x nozzle 0.8 mm
READY: chain03-planter.stl
```

**Gate exit code: 0.** Watertight, outward normals, fits a 220×220×250 bed, features above the
2×-nozzle floor — the STL is printable by rule, not by eyeball.

## Honest edges

- Nothing was physically printed in this run — READY means slicer-ready geometry, not a
  photographed object on a desk. The print itself is the human step.
- The planter is design-anything's golden example, not a fresh brief; a novel brief exercises
  its brief→parametric path, which this chain doesn't test.
