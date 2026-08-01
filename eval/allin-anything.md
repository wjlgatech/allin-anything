# eval — allin-anything flagship skill

Every case below is EXECUTABLE: `tests/test_router.py` runs each against the deterministic
`Router` (`python3 scripts/route.py "<intent>"` to try one by hand). Structure is additionally
pinned by `tests/test_gates.py::test_skill_eval_has_both_directions`.

## Should trigger

- "design me a phone stand I can 3D print" → design-anything (🦾, status disclosed)
  · `test_3d_print_routes_to_design_anything`
- "which of my repos can turn handwriting into AI input?" → penecho (🌉, external, run upstream)
  · `test_handwriting_routes_to_penecho`
- "I want an agent that watches my job applications" → career-os
  · `test_job_watching_routes_to_career_os`
- "build and ship an agent app from this one sentence" → anyagent (🟢)
  · `test_agent_app_routes_to_anyagent`
- cross-world chain: "sketch a room layout by hand, then verify it's buildable" → penecho +
  design-anything, chain declared · `test_cross_world_chain_declares_both`
- "design and 3D print a self-watering planter" → design-anything (Chain 03)
  · `test_planter_routes_to_design_anything`
- "run my weekly finance review and rebalance my budget" → money-os (Chain 04)
  · `test_finance_routes_to_money_os`
- "build the knowledge graph for my research corpus" → graph-engineering-anything first,
  research-anything declared at its honest status (Chain 05) · `test_graph_routes_to_gea_first`
- "learn this article deeply, with an animation for each key idea" → master-anything +
  animate-anything, both 🟢 (Chain 06) · `test_learn_with_animation_routes_chain_06`

## Should NOT trigger

- "run money-os weekly review" — satellite named → go direct, no routing
  · `test_named_satellite_goes_direct`
- "fix this stack trace" — generic coding, no satellite → none; bank the gap if it recurs
  · `test_generic_coding_question_routes_nowhere`
- "copy the penecho source into this repo" — REFUSED (AGPL + satellites-never-vendored)
  · `test_vendoring_penecho_is_refused`
