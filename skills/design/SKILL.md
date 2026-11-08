---
name: design
description: Draw each screen, build a clickable mockup, and get sign-off before building.
disable-model-invocation: true
---

# Design the screens

Turn the spec's screens into a layout the student can see and click before
any real query exists. The student stands in for the stakeholder; a layout
signed off on a mockup is cheap to change, and one built on real queries is
not.

**Driver:** the Design Lead. Match `gh api user --jq .login` against
`## Our team` in `ROLES.md`. No row for this login, or an empty table: fill
in the student's row (name, GitHub username, role) first. If the row holds
another role, name the driver and ask whether to continue.

**Interview:** inside a step, settle choices one question at a time, each
with your recommendation first and a one-line reason.

## Before step 1

Gate commands in this skill use `--skill design`.

1. Resume check: after `git fetch`, look for a `design` branch, local or
   remote. If it exists, switch to it. If it has an open pull request
   (`gh pr list --head design --state open`), read the latest handoff
   comment and offer to resume at the step it names; with no pull request
   or no comment, propose the step the files show you reached.
2. With no `design` branch, create it from an up-to-date `main`.
3. Read `spec.md` (framed questions, metric definitions, screens and
   interactions) and `design.md`, whose style rules bind every choice below.
   No `design.md` or `dashboard/charts.py`? The repository predates them:
   copy `design.md`, `dashboard/charts.py`, and `.streamlit/config.toml` from
   `wfu-martin/dashboard-starter` with `gh api`.
4. End every step that changed a file with a commit and a push. After a
   push from a branch with no pull request, open a draft one
   (`gh pr create --draft`).

Then hold the gate for the step you start at.

<!-- gate -->
## Gates

Between steps there is a gate. At every gate, in this order:

1. Run `python tools/progress.py --skill <this skill> --step <next step>`
   (in a task, add `--issue <number>`) and show its two lines as printed.
   No `tools/progress.py`? Copy it from `wfu-martin/dashboard-starter` with
   `gh api` first.
2. Ask the student to read the context percentage on their status line (or
   run `/context`) and type it. Under 50%: continue. At 50% or more:
   recommend the handoff and stop unless the student says to go on.
3. Say what the next step does and why a disciplined team does it, in one or
   two plain sentences.
4. Wait for the student's go-ahead.

Run the commands yourself; the student approves each one. Point to the part
of the output worth reading. The student decides; you recommend.

**Handoff:** commit and push the work in progress, then post a comment (what
is done, what is left, the step to resume at, and the student's name) on the
Issue for a task, or on this skill's draft pull request for a planning skill.

**Roles:** read `ROLES.md`. A single row means one student holds every role.
<!-- /gate -->

## Steps

1. **Charts.** Choose a chart for every framed question from the "Choosing a
   chart" table in `design.md`, and the headline-number tiles for each
   screen. Show the student one table (question · chart · why · tiles) and
   settle changes one question at a time. Done when the agreed table sits at
   the top of `## Screens` in `design.md`, in place of the placeholder, with
   a row for every framed question.
2. **Drawings.** Under the table, draw each screen as a text wireframe in a
   code block: takeaway sentence, tile row, one section per framed question
   in the order the decision needs them, sidebar filters. Name the framed
   question and chart under each section. Done when every screen in
   `spec.md` has a drawing and every framed question appears in a section.
3. **Mockup.** Build `mockup.py` at the repository root: the screens exactly
   as drawn, every headline, tile, and chart through `dashboard/charts.py`.
   Numbers are made up but plausible: one short read-only query for real
   category names and rough totals is fine, pasted in as fixed values, and
   the mockup itself never connects to the database. The first element on
   every screen is `st.warning("Mockup: made-up numbers")`. Done when
   `python -c "from streamlit.testing.v1 import AppTest; e = AppTest.from_file('mockup.py').run().exception; print(e or 'no errors')"`
   prints `no errors` and every drawn screen has its counterpart in
   `mockup.py`.
4. **Sign-off.** The student runs `streamlit run mockup.py` and pastes a
   screenshot of each screen. For each section ask: can the stakeholder read
   the answer in five seconds, and does every element serve a framed
   question? Revise the drawing and the mockup together until the student
   signs off.

   Change a style rule only for a reason this stakeholder gives (a brand
   color, a number format they use): edit the rule in `design.md` and its
   code in `dashboard/charts.py` or `.streamlit/config.toml` together.

   Done when the student has signed off on every screen, the drawings and
   `mockup.py` still match, and `pytest` passes.
5. **Merge.** Mark the pull request ready (`gh pr ready`) and ask the team
   to read it. Once they have, the driver merges it
   (`gh pr merge --squash --delete-branch`), then `git switch main` and
   `git pull`. If the team needs time to read, hand off with Merge as the
   step to resume at. Done when the project line of
   `python tools/progress.py --skill design --step 5` shows ✓ Design.

**Done when** the design is merged to `main`, every framed question in
`spec.md` has a drawn section with a chosen chart, `mockup.py` matches the
drawings, `pytest` passes, and the student has signed off. Tell the student
to `/clear`; the Delivery Lead runs `/dashkit:roadmap` next.
