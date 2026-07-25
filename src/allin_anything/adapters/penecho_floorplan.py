"""penecho ink export (PNG) -> design-anything construction_gate layout (JSON).

The bridge of Chain 02: a room layout hand-drawn on penecho's canvas, exported by
penecho's own renderer, becomes a machine-checkable floor plan.

Conventions (declared, not inferred):
- Rooms are drawn as closed axis-aligned rectangles sharing walls; no door gaps in ink.
- The outer boundary's drawn width IS `width_mm` (the sketch's scale anchor).
- Geometry comes from the ink; openings are synthesized by a code-minimum policy
  (every adjacent pair gets a door; bathrooms get exactly one, to their smallest
  neighbour; one entry-grade door on the exterior). Room types/windows come from a
  legend (default: by area rank — hall, bathroom, kitchen, living).
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from PIL import Image

CELL = 4                # px per analysis cell
INK_LUMA = 128          # below = ink (penecho ink is near-black; its grid is near-white)
MIN_ROOM_CELLS = 25     # smaller enclosed regions are noise, not rooms
EDGE_TOL_PX = 10        # room edges closer than this share one wall centerline
MODULE_MM = 100         # ISO 2848 basic module

DEFAULT_LEGEND = [      # by ascending area: (type, windows)
    ("hall", 0), ("bathroom", 0), ("kitchen", 1), ("living", 2),
]


@dataclass(frozen=True)
class RoomBox:
    x0: float
    y0: float
    x1: float
    y1: float

    @property
    def area(self) -> float:
        return (self.x1 - self.x0) * (self.y1 - self.y0)

    def adjacent(self, other: "RoomBox", tol: float) -> bool:
        """True if the two boxes share a wall segment (touching within tol)."""
        x_overlap = min(self.x1, other.x1) - max(self.x0, other.x0)
        y_overlap = min(self.y1, other.y1) - max(self.y0, other.y0)
        x_touch = abs(self.x1 - other.x0) <= tol or abs(other.x1 - self.x0) <= tol
        y_touch = abs(self.y1 - other.y0) <= tol or abs(other.y1 - self.y0) <= tol
        return (x_touch and y_overlap > tol) or (y_touch and x_overlap > tol)


def _ink_cells(png: Path) -> tuple[list[list[bool]], tuple[int, int, int, int]]:
    """Binarize the export into CELL-sized cells; return grid + ink bbox in px."""
    im = Image.open(png).convert("RGBA")
    w, h = im.size
    px = im.load()
    xs, ys = [], []
    gw, gh = (w + CELL - 1) // CELL, (h + CELL - 1) // CELL
    grid = [[False] * gw for _ in range(gh)]
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a > 0 and (0.299 * r + 0.587 * g + 0.114 * b) < INK_LUMA:
                grid[y // CELL][x // CELL] = True
                xs.append(x)
                ys.append(y)
    if not xs:
        raise ValueError("no ink found in export")
    return grid, (min(xs), min(ys), max(xs), max(ys))


def _regions(grid: list[list[bool]]) -> list[RoomBox]:
    """Enclosed non-ink regions (not connected to the border) = rooms, in px."""
    gh, gw = len(grid), len(grid[0])
    label = [[0] * gw for _ in range(gh)]  # 0 unvisited, 1 outside, 2 room-visited
    stack = [(x, y) for x in range(gw) for y in (0, gh - 1)] + \
            [(0, y) for y in range(gh)] + [(gw - 1, y) for y in range(gh)]
    stack = [(x, y) for x, y in stack if not grid[y][x]]
    for x, y in stack:
        label[y][x] = 1
    while stack:
        x, y = stack.pop()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < gw and 0 <= ny < gh and not grid[ny][nx] and label[ny][nx] == 0:
                label[ny][nx] = 1
                stack.append((nx, ny))
    rooms = []
    for y0 in range(gh):
        for x0 in range(gw):
            if not grid[y0][x0] and label[y0][x0] == 0:
                cells, run = [(x0, y0)], [(x0, y0)]
                label[y0][x0] = 2
                while run:
                    x, y = run.pop()
                    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if 0 <= nx < gw and 0 <= ny < gh and not grid[ny][nx] and label[ny][nx] == 0:
                            label[ny][nx] = 2
                            cells.append((nx, ny))
                            run.append((nx, ny))
                if len(cells) >= MIN_ROOM_CELLS:
                    xs = [c[0] for c in cells]
                    ys = [c[1] for c in cells]
                    rooms.append(RoomBox(min(xs) * CELL, min(ys) * CELL,
                                         (max(xs) + 1) * CELL, (max(ys) + 1) * CELL))
    return rooms


def _unify_walls(rooms: list[RoomBox], outer: tuple[float, float, float, float]) -> list[RoomBox]:
    """Move room edges to shared wall centerlines so neighbours meet exactly."""
    def unify(values: list[float]) -> dict[float, float]:
        mapping: dict[float, float] = {}
        for v in sorted(set(values)):
            for seen in mapping.values():
                if abs(v - seen) <= EDGE_TOL_PX:
                    mapping[v] = (v + seen) / 2
                    break
            else:
                mapping[v] = v
        # second pass: everything in a cluster maps to the cluster mean
        for v in mapping:
            for w in mapping:
                if abs(mapping[v] - mapping[w]) <= EDGE_TOL_PX:
                    m = (mapping[v] + mapping[w]) / 2
                    mapping[v] = mapping[w] = m
        return mapping

    xs = unify([r.x0 for r in rooms] + [r.x1 for r in rooms] + [outer[0], outer[2]])
    ys = unify([r.y0 for r in rooms] + [r.y1 for r in rooms] + [outer[1], outer[3]])
    return [RoomBox(xs[r.x0], ys[r.y0], xs[r.x1], ys[r.y1]) for r in rooms]


def _openings(named: list[dict], boxes: list[RoomBox], tol: float) -> list[dict]:
    """Code-minimum door policy over the adjacency graph (see module docstring)."""
    openings = []
    by_area = sorted(range(len(named)), key=lambda i: boxes[i].area)
    adjacent = {(i, j) for i in range(len(named)) for j in range(len(named))
                if i < j and boxes[i].adjacent(boxes[j], tol)}
    for i in by_area:
        if named[i]["type"] != "bathroom":
            continue
        neighbours = sorted((j for j in range(len(named))
                             if (min(i, j), max(i, j)) in adjacent and named[j]["type"] != "bathroom"),
                            key=lambda j: boxes[j].area)
        if neighbours:
            openings.append({"type": "door_bathroom", "width": 700,
                             "between": [named[neighbours[0]]["name"], named[i]["name"]]})
    for i, j in sorted(adjacent):
        if "bathroom" in (named[i]["type"], named[j]["type"]):
            continue
        openings.append({"type": "door_interior", "width": 800,
                         "between": [named[i]["name"], named[j]["name"]]})
    entry = next((i for i in by_area if named[i]["type"] == "hall"), by_area[0])
    openings.insert(0, {"type": "door_entry", "width": 900,
                        "between": ["exterior", named[entry]["name"]]})
    return openings


def convert(png: Path, width_mm: float, name: str = "penecho-sketch",
            ceiling_mm: int = 2400, legend: list[tuple[str, int]] | None = None) -> dict:
    """Convert a penecho ink export into a construction_gate layout dict."""
    legend = legend or DEFAULT_LEGEND
    grid, bbox = _ink_cells(png)
    rooms_px = _unify_walls(_regions(grid), bbox)
    if len(rooms_px) != len(legend):
        raise ValueError(f"found {len(rooms_px)} rooms, legend has {len(legend)}")
    scale = width_mm / (bbox[2] - bbox[0])
    snap = lambda v: round(v * scale / MODULE_MM) * MODULE_MM  # noqa: E731

    order = sorted(range(len(rooms_px)), key=lambda i: rooms_px[i].area)
    named = [None] * len(rooms_px)
    for rank, idx in enumerate(order):
        rtype, windows = legend[rank]
        named[idx] = {"type": rtype, "windows": windows,
                      "name": rtype if [t for t, _ in legend].count(rtype) == 1 else f"{rtype}{rank}"}
    rooms = []
    for i, r in enumerate(rooms_px):
        x0, y0, x1, y1 = snap(r.x0 - bbox[0]), snap(r.y0 - bbox[1]), snap(r.x1 - bbox[0]), snap(r.y1 - bbox[1])
        rooms.append({"name": named[i]["name"], "type": named[i]["type"],
                      "polygon": [[x0, y0], [x1, y0], [x1, y1], [x0, y1]],
                      "windows": named[i]["windows"]})
    return {"name": name, "units": "mm", "ceiling_height": ceiling_mm,
            "rooms": rooms, "openings": _openings(named, rooms_px, EDGE_TOL_PX * 2)}


def convert_file(png: Path, out: Path, width_mm: float, name: str = "penecho-sketch") -> dict:
    """Convert and write JSON; returns the layout dict."""
    layout = convert(png, width_mm, name=name)
    out.write_text(json.dumps(layout, indent=2))
    return layout
