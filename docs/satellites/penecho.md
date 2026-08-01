# Satellite digest — penecho

- **Pinned:** `e1b936fe51103243b79c82427eef5a369448a660` (HEAD at digest time, 2026-07-25)
- **Upstream:** https://github.com/penecho/penecho
- **License:** AGPL-3.0-only (commercial license offered separately) → **pointer + digest only; never vendored**
- **Role here:** 🌉 bridge — the inspiration seed for allin-anything's digital↔physical contract.

## Confirmed facts (from upstream README, 2026-07-25)

- "Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning."
- 20,000×20,000 px canvas; ink → visual model input; a structured **editable draft** returns and stays
  separate from confirmed work until accepted (a human gate — kin to ours).
- v0.7.0: sandboxed live HTML widgets on-canvas; data plugins (weather, stocks, GitHub).
- Executors: Claude CLI, Codex CLI, OpenAI-compatible APIs. Node.js ≥18.17, localhost/LAN, port 3888.

## Live evidence at the pin (2026-08-01 — full-feature upstream run)

- Sibling checkout cloned and pinned exactly (`git checkout e1b936f…`). **Its own gate run here:
  `npm run check` → 200 tests, 0 failed, exit 0** (syntax-checks every module + `node --test`).
- Full UI served from its own repo (`node cli.js --claude --port 3888` — Claude CLI executor, all
  AI features enabled, no API key file). Verified in a real browser: canvas loads, tour works,
  4 pen strokes drawn via pointer events, **its own "Export PNG" produced a valid 8059×4438 PNG**
  (the Bitter Lesson two-curves figure — embedded in `examples/bitter-lesson/`).
- The demo webapp's §5 bridge panel (`/api/penecho`) reports this instance live; the panel is a
  pointer across the bridge, never an embedding.
- Upstream quirks observed, not ours: two CSP inline-style console warnings from its tour overlay,
  and one 502 from an AI executor call — canvas/draw/export paths were clean (0 errors).

## Unconfirmed (do not state as fact)

- Internal architecture beyond the README's routing description; widget sandbox model.
  (Original digest was built from the rendered GitHub page; the 2026-08-01 run adds gate + UI
  evidence but still isn't a source-level review.)

## What allin-anything takes from it (ideas, not code)

- The draft-vs-confirmed split == our human-gated-irreversible discipline, applied to a canvas.
- Physical ink as a first-class input modality — the pattern our router generalizes.
