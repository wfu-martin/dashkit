---
name: tests-first
description: Write the failing tests for one Issue, explain what each proves, and hand off at red.
disable-model-invocation: true
argument-hint: "[issue number, optional]"
---

# Tests first

The first half of a task: write the tests that will prove the Issue is done,
watch them fail, and hand off. Red is the goal: a test that fails before the
code exists proves it checks something real. `/dashkit:build-next` takes the
branch from red to merged in a fresh session.

Issue: $ARGUMENTS (if empty, step 2 finds it).

**Driver:** the Issue's assignee. Match `gh api user --jq .login` against
`## Our team` in `ROLES.md`. No row for this login, or an empty table: fill
in the student's row (name, GitHub username, role) first. If the Issue is
assigned to someone else, name the assignee and ask whether to continue;
the Delivery Lead reassigns Issues on GitHub.

Report in plain business language: what each test proves for the person
using the dashboard.

## Spec first

When writing a test shows that `spec.md` is wrong or silent (a metric
definition that cannot be tested as written, an AC with no value to check),
stop and hold a gate for the spec change: show what `spec.md` says, what the
test needs, and your recommended wording. Name the Spec Lead (or Stakeholder
Lead) from `ROLES.md` and get their OK; with a single row in `## Our team`,
the student approves. If the approver is not at hand, hand off with this
step to resume at. Once approved, change `spec.md` in its own commit on this
branch (the message names the AC and who approved), then write the test.

## Before step 1

Gate commands in this skill use `--skill tests-first`, plus
`--issue <number>` once the Issue is known.

1. Resume check: after `git fetch`, look for a `<number>-…` branch, local or
   remote, for the Issue in `$ARGUMENTS` or, with none given, for each open
   Issue assigned to the student (`gh issue list --assignee @me --state open`).
   If one exists, switch to it and read the Issue's latest handoff comment
   (`gh issue view <number> --comments`). Offer to resume at the step it
   names; with no comment, propose the step the files show you reached. A
   handoff that names `/dashkit:build-next` means this half is done: tell
   the student to run `/dashkit:build-next` and stop.
2. End every step that changed a file with a commit and a push.

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

1. **Start clean.** Run `git status`, then `git switch main && git pull`.
   Uncommitted changes or another branch's work in the way: tell the student
   what they are and settle them first. Done when `git status` shows a clean
   working tree on `main`, up to date with `origin/main`.
2. **Pick the Issue.** `$ARGUMENTS` if given; otherwise the lowest-numbered
   open Issue assigned to the student (`gh issue list --assignee @me --state open`)
   whose **Depends on** Issues are all closed. Read it with
   `gh issue view <number>` and confirm it with the student. Done when the
   student has confirmed the Issue and `gh issue view` shows every Issue it
   depends on as closed.
3. **Branch.** `git switch -c <number>-<short-name>`, the short name two to
   four words of the Issue title in lowercase with hyphens. Done when
   `git branch --show-current` prints the new branch.
4. **Write tests.** Read only the `spec.md` sections and the files the Issue
   names. In `tests/`, write:
   - a **reconciliation test** for every figure: the function the screen
     will call returns the same number as an independent SQL query that
     reaches it a different way (another table, or a simpler path);
   - an **acceptance test** for every AC the Issue lists, checking its
     Given / When / Then line.

   Name each test after the AC it proves, `test_ac<n>_…`: AC-3 gives
   `test_ac3_revenue_reconciles_to_invoices`. Follow
   `tests/test_example_reconciliation.py` for the pattern. Write tests only;
   the functions and screens they call are built in `/dashkit:build-next`.
   Done when every AC ID the Issue lists has a test named after it, every
   figure those ACs show has a reconciliation test, and every test under the
   Issue's **Tests that prove it** exists.
5. **Tests red.** Run `pytest`. Each new test must fail because the function
   or screen it calls does not exist yet. Fix any other failure first: a
   typo, a wrong fixture or query, a test that already passes. Then explain
   each new test in one plain sentence: what it proves about the dashboard
   and why that matters to the stakeholder. Done when `pytest` shows every
   new test failing for that one reason, every test already on `main` still
   passing, and the student has heard a sentence for each new test.
6. **Commit and hand off.** Commit the tests, push the branch
   (`git push -u origin <branch>`), and post the handoff comment on the
   Issue: the tests written, that they are red, any spec change and who
   approved it, `/dashkit:build-next` as the next step, and the student's
   name. Tell the student to `/clear`. Done when `git status` shows a clean
   tree up to date with its `origin` branch and
   `gh issue view <number> --comments` shows the handoff naming
   `/dashkit:build-next`.

**Done when** the Issue's branch is on GitHub with every test the Issue
names failing for the expected reason, only tests (and any approved spec
change) committed on it, and the handoff on the Issue. After `/clear`, the
student runs `/dashkit:build-next`.
