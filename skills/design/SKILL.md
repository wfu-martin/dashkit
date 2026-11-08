---
name: design
description: Draw each screen, build a clickable mockup, and get sign-off before building.
disable-model-invocation: true
---

# Design the screens

Turn the spec's screens into a layout the student can see and click before
any real query exists. The student stands in for the stakeholder and makes
every decision; you recommend.

Read `spec.md` (framed questions, metric definitions, screens and
interactions) and `design.md`, whose style rules bind every choice below.
No `design.md` or `dashboard/charts.py`? The repository predates them: copy
`design.md`, `dashboard/charts.py`, and `.streamlit/config.toml` from
`wfu-martin/dashboard-starter` with `gh api`.

## Steps

1. **Choose a chart for every framed question** from the "Choosing a chart"
   table in `design.md`, and the headline-number tiles for each screen. Show
   the student one table (question · chart · why · tiles) and settle changes
   one question at a time.
2. **Draw each screen** under "Screens" in `design.md`: a text wireframe in a
   code block (takeaway sentence, tile row, one section per framed question
   in the order the decision needs them, sidebar filters), with the framed
   question and chart named under each section.
3. **Build `mockup.py`** at the repository root: the screens exactly as
   drawn, every headline, tile, and chart through `dashboard/charts.py`.
   Numbers are made up but plausible: one short read-only query for real
   category names and rough totals is fine, pasted in as fixed values, and
   the mockup itself never connects to the database. The first element on
   every screen is `st.warning("Mockup: made-up numbers")`.
4. **Walk the mockup for sign-off.** The student runs `streamlit run mockup.py`
   and pastes a screenshot of each screen. For each section ask: can the
   stakeholder read the answer in five seconds, and does every element serve
   a framed question? Revise the drawing and the mockup together until the
   student signs off.
5. **Change a style rule** only for a reason this stakeholder gives (a
   brand color, a number format they use): edit the rule in `design.md` and
   its code in `dashboard/charts.py` or `.streamlit/config.toml` together.
6. On a branch named `design`, commit, push, open a pull request, and merge
   it once the student has read it.

Done when every framed question in `spec.md` has a drawn section with a
chosen chart, `mockup.py` matches the drawings, `pytest` still passes, and
the student has signed off. Tell the student to `/clear`, then
`/dashkit:roadmap`.
