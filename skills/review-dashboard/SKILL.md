---
name: review-dashboard
description: Review the running dashboard against the spec and the design, and turn the fixes into Issues.
disable-model-invocation: true
---

# Review the dashboard

You are the stakeholder's most demanding reader. Judge the dashboard as they
would see it, then as a data-visualization reviewer, and turn what the
student decides to fix into Issues the team builds like any other task. This
skill changes only `spec.md` and `ROADMAP.md`; every fix to the app becomes
an Issue for `/dashkit:tests-first` and `/dashkit:build-next`.

If `/usage` leaves room, suggest `/model opus`; otherwise Sonnet with
`/effort high`.

**Driver:** the Pitch Lead, or the Stakeholder Lead on a team of four. Match
`gh api user --jq .login` against `## Our team` in `ROLES.md`. No row for
this login, or an empty table: fill in the student's row (name, GitHub
username, role) first. One row in `## Our team`: that student is the driver
(they hold every role). Otherwise, if the row holds another role, name the
driver and ask whether to continue.

**Findings:** each one in plain words: what the stakeholder would struggle
with, and the change that fixes it. Number them in one list, most important
first, and keep the list in the pull request body under `## Findings`
(`gh pr edit --body`) as each step adds to it, so a fresh session can pick
the review up.

## Before step 1

Gate commands in this skill use `--skill review-dashboard`.

1. Resume check: after `git fetch`, look for a `review` branch, local or
   remote. If it exists, switch to it. If it has an open pull request
   (`gh pr list --head review --state open`), read its findings and the
   latest handoff comment and offer to resume at the step it names; with
   no pull request or no comment, propose the step the files show you
   reached. Resuming after Screens: ask for the screenshots again first.
2. With no `review` branch, create it from an up-to-date `main`, then
   `git commit --allow-empty -m "Start the dashboard review"`, push, and
   open a draft pull request (`gh pr create --draft`) whose body holds an
   empty `## Findings` list. The handoffs go on it.
3. Read `spec.md`, `design.md`, `ROADMAP.md`, `ROLES.md`,
   `streamlit_app.py`, and `dashboard/metrics.py`.
4. End every step that changed a file with a commit and a push.

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
is done, what is left, the skill and step to resume at, and the student's
name) on the Issue for a task, or on this skill's draft pull request for a
planning skill.

**Roles:** read `ROLES.md`. A single row means one student holds every role.
<!-- /gate -->

## Steps

1. **Screens.** Ask the student to run `streamlit run streamlit_app.py` and
   paste a screenshot of each page into the terminal. A page that shows an
   error or will not load is the first finding. Done when you hold a
   screenshot of every screen listed under `## Screens and interactions` in
   `spec.md`, or a finding for each one that would not show.
2. **Answers.** For every framed question in the spec: which part of the
   screen answers it, and whether a stakeholder could read the answer in
   five seconds. A question with no clear answer on screen is the top
   finding. Done when every framed question has a line, shown to the
   student, naming the section that answers it or the finding it became.
3. **Design.** Compare every screen with its drawing in `design.md`, and
   check every style rule there against every headline, tile, and chart.
   Quote the rule each finding breaks. Done when every screen has been
   compared with its drawing, every style rule has been checked, and each
   break is a finding that quotes its rule.
4. **Usability.** With the student at the controls: every filter starts on a
   sensible default, each page loads in a few seconds, and setting a filter
   so it leaves no rows shows a plain message instead of an error or an
   empty chart. Done when every filter in the spec has been tried, including
   one setting that leaves no rows, and each problem is a finding.
5. **Findings to Issues.** Walk the findings one at a time, most important
   first: your recommendation (Issue or leave) with a one-line reason, then
   the finding in plain words. The student decides each; group trivial
   findings (wording, a label) into one decision.

   A finding the spec does not ask for is a new requirement and goes spec
   first: show your recommended wording for a new AC at the next unused
   number, `- **AC-n** (question q): Given …, when …, then ….`, and get the
   Spec Lead's (or Stakeholder Lead's) OK, named from `ROLES.md`; with a
   single row in `## Our team`, the student approves. If the approver is
   not at hand, hand off with this step to resume at. Once approved, add it
   under `## Acceptance criteria` in `spec.md`, in its own commit (the
   message names the AC and who approved), before its Issue exists.

   Each chosen finding becomes one Issue with the same body as a roadmap
   task: **Goal**, **Acceptance criteria** (the AC IDs it covers, with their
   Given / When / Then lines), **Tests that prove it** (named
   `test_ac<n>_…`), **Files it touches** (and the `design.md` section, for a
   view), and **Depends on** (any Issues it needs, plus the line "Start
   this Issue after review pull request #<n> merges.", since its new ACs
   reach `main` only then). Label it with the phase it belongs to
   (`phase-1` … `phase-5`; `gh label create` any that `gh label list` lacks).

   Draft an assignee for every one of these Issues from `## Our team` in
   `ROLES.md`, role first: Phase 1 → Data Lead; data layer → Data Lead, Spec
   Lead; views → Design Lead, Pitch Lead; filters → Spec Lead, Delivery
   Lead; polish and deploy → Delivery Lead, Design Lead. A Stakeholder Lead
   takes the Spec Lead's and Pitch Lead's leans. Where a phase leans toward
   two roles, alternate between them in Issue order. Then balance by count:
   while anyone has two or more of these Issues more than someone else, move
   the busiest person's latest-ordered Issue to the least busy person. A
   single row in `## Our team` gets every Issue. Assignment needs every
   teammate's row: add any that are missing with the student first.

   Show the table (finding · Issue title · AC IDs · phase · assignee) with
   each person's count, and get the Delivery Lead's OK, named from
   `ROLES.md`; with a single row in `## Our team`, the student approves. If
   the Delivery Lead is not at hand, hand off with this step to resume at.
   Once approved, create each with
   `gh issue create --title ... --body ... --assignee <username> --label phase-<n>`.

   Record the run in `ROADMAP.md`: add each new Issue number to its phase
   row, and under `## Dashboard review` replace the
   `<Filled in by /dashkit:review-dashboard …>` placeholder (or, on a later
   review, add below the last line) with
   `- YYYY-MM-DD: fixes in #n, #n` (today's date; `- YYYY-MM-DD: no fixes`
   when the student chose none). Commit and push. Done when every finding
   has the student's call, the Delivery Lead has approved the assignment
   table, `gh issue list` shows one Issue per chosen finding with its AC
   IDs, assignee, and phase label, every assignee appears in
   `gh api repos/{owner}/{repo}/collaborators --jq '.[].login'`, and
   `## Dashboard review` in `ROADMAP.md` ends with today's dated line.
6. **Merge.** Mark the pull request ready (`gh pr ready`) and ask the team
   to read it. Once they have, the driver merges it
   (`gh pr merge --squash --delete-branch`), then `git switch main` and
   `git pull`. If the team needs time to read, hand off with Merge as the
   step to resume at, and say in the handoff that the fix Issues start
   after this pull request merges. Done when the project line of
   `python tools/progress.py --skill review-dashboard --step 6` shows
   ✓ Review.

**Done when** the review is merged to `main`, every finding has the
student's recorded call, every chosen finding is an assigned Issue that
lists its AC IDs, and `ROADMAP.md` carries the dated review line. Tell the
student to `/clear`; each assignee starts their fix Issues with
`/dashkit:tests-first <issue number>`, and the Delivery Lead finishes the
deploy once they are closed.
