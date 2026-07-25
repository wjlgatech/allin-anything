# eval — allin-anything flagship skill

Each case is backed by `tests/test_gates.py::test_skill_eval_has_both_directions` (structure)
and exercised manually per release.

## Should trigger

- "/allin design me a phone stand I can 3D print" → route: design-anything (🦾, ⚪ — say so)
- "which of my repos can turn handwriting into AI input?" → route: penecho (🌉, external, run upstream)
- "I want an agent that watches my job applications" → route: career-os
- "build and ship an agent app from this one sentence" → route: anyagent (🟢)
- an intent spanning worlds: "sketch a room layout by hand, then verify it's buildable" → penecho + design-anything (declare the chain)

## Should NOT trigger

- A task fully inside ONE satellite the user already named ("run money-os weekly review") — go direct.
- Generic coding questions with no routing need ("fix this stack trace").
- Anything asking to copy penecho source into this repo — refuse; AGPL + satellites-never-vendored.
