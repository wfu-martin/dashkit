---
name: roadmap
description: Turn spec.md into ROADMAP.md and one GitHub Issue per task.
disable-model-invocation: true
---

# Plan the build

Turn the spec into phases and tasks the team can build one at a time, assign
every task to a teammate, and create the tasks as GitHub Issues. Each Issue
carries the acceptance-criterion IDs it covers and the tests that prove
them, so anyone can pick it up in a fresh session.

If `/usage` leaves room, suggest `/model opus`; otherwise Sonnet with
`/effort high`.

**Driver:** the Delivery Lead. Match `gh api user --jq .login` against
`## Our team` in `ROLES.md`. No row for this login, or an empty table: fill
in the student's row (name, GitHub username, role) first. If the row holds
another role, name the driver and ask whether to continue.

**Interview:** inside a step, settle changes one question at a time, each
with your recommendation first and a one-line reason.

## Before step 1

Gate commands in this skill use `--skill roadmap`.

1. Resume check: after `git fetch`, look for a `roadmap` branch, local or
   remote. If it exists, switch to it. If it has an open pull request
   (`gh pr list --head roadmap --state open`), read the latest handoff
   comment and offer to resume at the step it names; with no pull request
   or no comment, propose the step the files show you reached.
2. With no `roadmap` branch, create it from an up-to-date `main`.
3. Read `spec.md`, `design.md`, `ROADMAP.md`, and `ROLES.md`.
4. End every step that changed a file with a commit and a push. After a
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

1. **Phases.** Use the five phases in `ROADMAP.md`, in critical-path order;
   each depends on the one before it, and each matches a label `phase-1` …
   `phase-5`:
   1. Data connection: the app reads the team's database locally and on
      Streamlit Community Cloud (deploy a hello-world early).
   2. Data layer: a tested function in `dashboard/metrics.py` for every
      metric in the spec.
   3. Views: one screen section per framed question, built as `design.md`
      draws it, with the mockup's made-up numbers replaced by the data layer.
   4. Filters: the interactions the spec lists.
   5. Polish and deploy: every style rule in `design.md` holds, `mockup.py`
      is deleted, the live link is in the README.

   Show the student what each phase covers for this spec (which metrics,
   which screens, which filters). Done when the student agrees with what
   each phase covers.
2. **Tasks.** Split each phase into ordered tasks. Size each one to finish
   in a single fresh session: one metric, one view, or one filter is
   typical. A task too big to describe in five acceptance criteria is two
   tasks. Each task's Issue body will have:
   - **Goal**: one sentence in business language.
   - **Acceptance criteria**: the AC IDs from `spec.md` it covers, each with
     its Given / When / Then line.
   - **Tests that prove it**: the reconciliation and acceptance tests to
     write first, named after the AC they prove (`test_ac3_revenue_reconciles_to_invoices`).
   - **Files it touches**, and for a view, the `design.md` section it builds.
   - **Depends on**: the tasks that must merge first.

   Show the tasks as one table (phase · task · AC IDs · tests · depends on)
   and settle changes one question at a time. Write the agreed table under a
   `## Task draft` heading at the end of `ROADMAP.md`. Done when every AC ID
   in `spec.md` belongs to at least one task and every task names its tests.
3. **Assign.** Draft an assignee for every task from `## Our team` in
   `ROLES.md`, role first: Phase 1 → Data Lead; data layer → Data Lead, Spec
   Lead; views → Design Lead, Pitch Lead; filters → Spec Lead, Delivery
   Lead; polish and deploy → Delivery Lead, Design Lead. A Stakeholder Lead
   takes the Spec Lead's and Pitch Lead's leans. Where a phase leans toward
   two roles, alternate between them in task order. Then balance by count:
   while anyone has two or more tasks more than someone else, move the
   busiest person's latest-ordered task to the least busy person. A single
   row in `## Our team` gets every task. Assignment needs every teammate's
   row: add any that are missing with the student first.

   Add an assignee column to the task draft, show it with each person's
   count, and ask the Delivery Lead to approve it. Done when the Delivery
   Lead has approved the table, no one has two or more tasks more than
   anyone else, and every assignee appears in
   `gh api repos/{owner}/{repo}/collaborators --jq '.[].login'`.
4. **Issues.** Create the labels `phase-1` … `phase-5` that `gh label list`
   does not show (`gh label create phase-<n>`). Then create one Issue per
   task in dependency order, so earlier numbers can be cited under
   **Depends on**:
   `gh issue create --title ... --body ... --assignee <username> --label phase-<n>`.
   Record each Issue number in the task draft as it is created. Done when
   `gh issue list` shows one Issue per task, each with its assignee and its
   phase label.
5. **Roadmap file.** Fill `ROADMAP.md`: each phase row's Issue numbers, and
   under `## Critical path`, which Issues block which. Leave
   `## Dashboard review` as it is. The Issues now hold the tasks, so delete
   the `## Task draft` section. Done when every phase row lists its Issues,
   the critical path replaces its placeholder, and `## Task draft` is gone.
6. **Merge.** Mark the pull request ready (`gh pr ready`) and ask the team
   to read it. Once they have, the driver merges it
   (`gh pr merge --squash --delete-branch`), then `git switch main` and
   `git pull`. If the team needs time to read, hand off with Merge as the
   step to resume at. Done when the project line of
   `python tools/progress.py --skill roadmap --step 6` shows ✓ Roadmap.

**Done when** `ROADMAP.md` is merged to `main`, every AC ID in `spec.md`
belongs to at least one Issue, and every Issue names its tests, its assignee,
and its phase label. Tell the student to `/clear`; each assignee starts their
first Issue with `/dashkit:tests-first <issue number>`, in dependency order.
