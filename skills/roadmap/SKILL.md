---
name: roadmap
description: Turn spec.md into ROADMAP.md and one GitHub Issue per task.
disable-model-invocation: true
---

# Plan the build

Read `spec.md`, `design.md`, and `ROADMAP.md`. Turn the spec into phases and tasks the team
can build one at a time, then create the tasks as GitHub Issues.

If `/usage` leaves room, suggest `/model opus`; otherwise Sonnet with
`/effort high`.

## Phases, by critical path

Use these phases unless the spec needs another; each depends on the one
before it:

1. **Data connection**: the app reads the team's database locally and on
   Streamlit Community Cloud (deploy a hello-world early).
2. **Data layer**: a tested function in `dashboard/metrics.py` for every
   metric in the spec.
3. **Views**: one screen section per framed question, built as `design.md`
   draws it, with the mockup's made-up numbers replaced by the data layer.
4. **Filters**: the interactions the spec lists.
5. **Polish and deploy**: every style rule in `design.md` holds, `mockup.py`
   is deleted, the live link is in the README.

## Tasks

Split each phase into ordered tasks. Size each one to finish in a single
fresh session: one metric, one view, or one filter is typical. A task too big
to describe in five acceptance criteria is two tasks.

Each task becomes one Issue whose body has:

- **Goal**: one sentence in business language.
- **Acceptance criteria**: the Given / When / Then lines from the spec it covers.
- **Tests that prove it**: the reconciliation and acceptance tests to write first.
- **Files it touches**, and for a view, the `design.md` section it builds.
- **Depends on**: the Issue numbers that must merge first.

## Steps

1. Show the student the phase and task list as a table and ask for changes,
   one question at a time.
2. Once they agree, create the Issues in dependency order with
   `gh issue create --title ... --body ...`, so earlier numbers can be cited.
3. Fill `ROADMAP.md`: each phase's Issue numbers, and a short critical-path
   line saying which Issues block which.
4. On a branch named `roadmap`, commit `ROADMAP.md`, push, open a pull
   request, and merge it once the student has read it.

Done when every requirement in `spec.md` belongs to at least one Issue and
every Issue names its tests. Tell the student to `/clear`, then
`/dashkit:build-next`.
