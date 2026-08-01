# Chain 06 — article → animated understanding (learn-anything)

**Satellites:** master-anything (💻 🔒, learning organ) × animate-anything (💻, motion craft)
**Autonomy:** autonomous_bounded (both satellites 🟢 by live gate runs; runner stops at the human gate)

The learn-anything chain: a dense source (paper, briefing, article) goes in; what comes out is a
session-structured learning artifact where every key idea carries an animation of its operational
mechanism — master-anything's teach-back discipline supplying the pedagogy, animate-anything's
executable craft rules supplying the motion.

## Router verdict

`python3 scripts/route.py "learn this article deeply, with an animation for each key idea"`
→ mode **route**, satellites **[master-anything, animate-anything]** — "learn" trips the teaching
organ, "animation" trips the motion organ; the verdict is a pytest
(`test_learn_with_animation_routes_chain_06` in tests/test_router.py). This exact intent is also
the chain's origin story: on 2026-07-27 it routed to *nothing* for the motion half, the gap was
banked to `data/news.yml` per protocol, and animate-anything joined the registry as ⚪ that day.

## Step A — master-anything's own gate, run live (2026-08-01)

```
$ cd projects/master-anything && make check       # pinned a635d58
15 passed in 0.50s
smoke OK — 8 organs registered: [('act','browser'), ('compress','graph'), ('compress','skill'),
('express','post'), ('express','scene3d'), ('express','verse'), ('render','song'),
('verify','teachback')]                            → exit 0
```

Promotion 🟡→🟢 rests on that exit code, not on the digest's description.

## Step B — animate-anything's own gate, run live (2026-08-01)

```
$ cd projects/animate-anything && make check      # pinned 946bef8
3b1b style score: 100/100 (10/10 checks)          → exit 0
```

Ten executable craft checks (warm-grey canvas, palette-by-role, morph-to-equivalence,
pacing beats, one-idea-per-play, narrative arc…) — the craft rules are a linter, not taste.

## Second artifact (2026-08-01): The Bitter Lesson, with real penecho ink

`examples/bitter-lesson/` — entry №1 of FM-os's Frontier AI Reading List (Sutton 2019) as a
5-session learning page: statement → the two curves → search-and-learning mechanism →
the prior-ceiling anti-pattern → the meta-lesson, each with a CSS animation. Session 2's figure
was **drawn as real strokes on a locally-running upstream penecho at pin `e1b936f`** (its own
gate: 200 tests, exit 0) **and exported by penecho's own PNG exporter** — all three routed
satellites exercised in one artifact. Browser-verified: 5 sessions, ink image loaded, 0 console
errors. Served by the demo webapp at `/bitter-lesson`; published canonically (human click,
2026-08-01) at https://agentic-portfolio-lovat.vercel.app/articles/bitter-lesson-allin.html.

## The artifact this chain already produced

`examples/fields-2026/` — a 61KB institutional research briefing on the 2026 Fields Medalists
became a 6-session bilingual (zh-CN faithful translation + EN) learning page, each session with
key idea + operational mechanism + a pure-CSS animation following animate-anything's craft rules;
browser-verified with 0 console errors and published to the portfolio. That artifact predates the
satellites' promotions — the chain formalizes, as data + gates, the route it was built by.

## Honest edges

- The bounded steps verify the two organs' own gates; the *composition* (writing the sessions,
  authoring the animations for a NEW article) is agent work between the gates, and its quality is
  human-judged — the chain proves the organs, not the prose.
- master-anything's teach-back/fun/retention metrics need a human learner; no autonomous run can
  claim them. animate-anything's linter scores animation source, not rendered video.
- Publishing the resulting artifact is the declared human gate — always a human click, never
  autonomous (the AGPL/publishing rules of this repo apply unchanged).
