---
name: spec
description: Turn a stakeholder brief into spec.md, one question at a time.
disable-model-invocation: true
argument-hint: "[path to the stakeholder brief]"
---

# Write the dashboard spec

You are interviewing the student the way a senior business analyst would: the
brief gives high-level business questions, and your job is to help the
student turn each one into questions the database can answer, metrics with
exact definitions, and numbered acceptance criteria a test can check.
`spec.md` becomes the team's source of truth for what to build.

Brief: $ARGUMENTS (if empty, ask for the file or the pasted text).

This is thinking work. If `/usage` leaves room, suggest `/model opus`;
otherwise Sonnet with `/effort high`.

**Driver:** the Spec Lead, or the Stakeholder Lead on a team of four. Match
`gh api user --jq .login` against `## Our team` in `ROLES.md`. No row for
this login, or an empty table: fill in the student's row (name, GitHub
username, role) first. If the row holds another role, name the driver and
ask whether to continue.

**Interview:** inside a step, ask one question at a time, each with your
recommended answer first and a one-line reason, and wait for the answer
before the next. Write each answer into `spec.md` as it lands.

## Before step 1

Gate commands in this skill use `--skill spec`.

1. Resume check: after `git fetch`, look for a `spec` branch, local or
   remote. If it exists, switch to it. If it has an open pull request
   (`gh pr list --head spec --state open`), read the latest handoff
   comment and offer to resume at the step it names; with no pull request
   or no comment, propose the step the files show you reached.
2. With no `spec` branch, create it from an up-to-date `main`. Give
   `spec.md` at the repository root these headings, exactly, in this order
   (the tracker reads them): `## Stakeholder and decision`,
   `## Framed questions`, `## Metric definitions`, `## Data sources`,
   `## Screens and interactions`, `## Acceptance criteria`, `## Out of scope`.
3. End every step that changed a file with a commit and a push. After a
   push from a branch with no pull request, open a draft one
   (`gh pr create --draft`).

Then hold the gate for the step you start at.

<!-- gate -->
## Gates

Between steps there is a gate. At every gate, in this order:

1. Run `python tools/progress.py --skill <this skill> --step <next step number>`
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

1. **Stakeholder.** Who reads the dashboard, and what decision will they make
   with it? Done when `## Stakeholder and decision` names the reader, their
   role, and the decision.
2. **Framed questions.** For each high-level question in the brief, propose
   two or three sharp, answerable questions ("Which five product categories
   lost the most revenue year over year?", not "How are sales doing?"). Push
   back on any question that is still vague, cannot be answered from the
   data, or would not change the decision. Done when every brief question
   has framed questions the student accepted, as a numbered list under
   `## Framed questions`.
3. **Metrics.** For every number the framed questions need, pin down a
   definition: formula, granularity (one row per what), filters, and source
   tables and columns. Confirm the tables and columns exist with a short
   read-only query, for example
   `python -c "from dashboard import db, metrics; print(metrics.read_sql(db.engine_from_secrets(), 'SELECT ... LIMIT 5'))"`.
   Done when `## Metric definitions` is a table (metric, formula,
   granularity, filters, source) with every cell filled, every source has
   been confirmed by a query, and `## Data sources` lists each table and the
   columns used.
4. **Screens.** Which screen answers which framed question, and which
   filters the stakeholder needs on it. Done when every framed question sits
   on a screen under `## Screens and interactions` and every screen lists its
   filters (or says it has none).
5. **Acceptance criteria.** For each framed question, plain
   Given / When / Then statements a test can check, with real values where
   you can get them. Number them `AC-1`, `AC-2`, … in one sequence across
   the spec, one per line:
   `- **AC-3** (question 2): Given …, when …, then ….`
   Issues cite these IDs and tests are named after them (`test_ac3_…`), so an
   ID keeps its number once assigned and is never reused. Done when every
   framed question has at least one numbered AC under
   `## Acceptance criteria`.
6. **Out of scope.** What the dashboard deliberately does not do. Done when
   `## Out of scope` lists each item the student agreed to leave out.
7. **Read and agree.** Ask the student to read `spec.md` top to bottom and
   flag anything wrong or missing. Fix each point in the section it belongs
   to; a changed framed question carries through to its metrics, screen,
   and ACs. Done when every framed question has a complete metric definition
   and at least one numbered AC, and the student has typed that they agree.
8. **Merge.** Mark the pull request ready (`gh pr ready`) and ask the team
   to read it. Once they have, the driver merges it
   (`gh pr merge --squash --delete-branch`), then `git switch main` and
   `git pull`. If the team needs time to read, hand off with Merge as the
   step to resume at. Done when the project line of
   `python tools/progress.py --skill spec --step 8` shows ✓ Spec.

**Done when** `spec.md` is merged to `main` and every framed question in it
has a complete metric definition and at least one numbered AC. Tell the
student to `/clear`; the Design Lead runs `/dashkit:design` next.
