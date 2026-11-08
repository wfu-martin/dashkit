---
name: build-next
description: Take one Issue from red tests to merged code - build, tidy, review, decide findings, merge.
disable-model-invocation: true
argument-hint: "[issue number, optional]"
---

# Build the next task

The second half of a task: start from the Issue's branch with its tests red
(written by `/dashkit:tests-first`) and take it to merged, reviewed code.
State lives in files and on the Issue, never only in chat, so any fresh
session can pick the work up.

Issue: $ARGUMENTS (if empty, step 1 finds it).

**Driver:** the Issue's assignee, who also merges the pull request. Match
`gh api user --jq .login` against `## Our team` in `ROLES.md`. No row for
this login, or an empty table: fill in the student's row (name, GitHub
username, role) first. If the Issue is assigned to someone else, name the
assignee and ask whether to continue; the Delivery Lead reassigns Issues on
GitHub.

Report every step in plain business language: what changed for the person
using the dashboard, and what the student should check.

## Locked tests

The tests from `/dashkit:tests-first` are the contract for this task; the
code changes to meet them. When a test itself looks wrong (not the code),
stop and hold a gate: show the test, explain why it is wrong, and propose
the change. Change it only on the student's approval, and record it in the
pull request body (which test, why, who approved). A test that is wrong
because the spec is wrong goes spec first.

## Spec first

When building shows that `spec.md` is wrong or silent, stop and hold a gate
for the spec change: show what `spec.md` says, what the build needs, and
your recommended wording. Name the Spec Lead (or Stakeholder Lead) from
`ROLES.md` and get their OK; with a single row in `## Our team`, the student
approves. If the approver is not at hand, hand off with this step to resume
at. Once approved, change `spec.md` first, in its own commit on this branch
(the message names the AC and who approved), then the tests (as a locked
test change), then the code. The pull request body calls out the change.

## Before step 1

Gate commands in this skill use `--skill build-next`, plus
`--issue <number>` once the Issue is known. End every step that changed a
file with a commit and a push. Hold the gate for Pick up, then start.

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

1. **Pick up.** After `git fetch`, find the Issue: `$ARGUMENTS` if given;
   otherwise the open Issue assigned to the student
   (`gh issue list --assignee @me --state open`) that has a `<number>-…`
   branch, local or remote (the lowest-numbered if several; confirm it).
   No such branch, or its latest handoff names a `/dashkit:tests-first`
   step: tell the student to run `/dashkit:tests-first` first, and stop.
   Switch to the branch, `git pull`, and read the Issue and its latest
   handoff comment (`gh issue view <number> --comments`). A tests-first
   handoff starts at Build; a build-next handoff names the step to resume
   at; with no comment, propose the step the files show you reached. Then
   read only what the Issue names: its `spec.md` sections, its `design.md`
   section, its files, and its tests. Done when the student has confirmed
   the Issue and the step to start at, the branch is up to date with
   `origin`, and `pytest -rs` shows the Issue's tests in the state the
   handoff describes (red on their stubs' `NotImplementedError`, for a fresh
   start). A skipped test is neither red nor green: if any of the Issue's
   tests skip (usually no `.streamlit/secrets.toml`), set up the connection
   and rerun before going on.
2. **Build.** One failing test at a time: replace the stub it calls with
   real code (in the files the Issue names), run that test
   (`pytest tests/<file>::<test>`), report it green in one line ("test_ac3_…
   green: revenue by genre now matches the invoice totals"), then take the
   next. Tests stay locked. Done when every test the Issue names passes, no
   `NotImplementedError` stub for this Issue is left, and each test file is
   unchanged except through an approved locked-test gate.
3. **Tidy.** Make the new code clearer with the same behavior: plainer
   names, repeated code folded into one function, a short comment where a
   reader would stop. Nothing new is added: no feature, filter, or test. Run
   the Issue's tests after each change. Done when the Issue's tests still
   pass and the student has seen each tidy change in one line, or has been
   told the code already reads clearly.
4. **Full suite.** Run `pytest -rs` on everything. Any failure is fixed in
   the code, with the tests locked, before the next step: nothing merges
   red. Done when `pytest -rs` reports none failed or errored and none of
   the Issue's tests skipped (only the template's vinyl_vault example tests
   may skip, on another database).
5. **Pull request.** Push, then `gh pr create` with a body that says
   `Closes #<number>`, lists what changed on screen in business language,
   and names any spec or test change and who approved it (or says there
   was none). Done when `gh pr view` shows the pull request with all three.
6. **Review.** Launch a separate review agent with fresh context, model
   `sonnet`. Give it the pull request number, the Issue number, `spec.md`,
   and `design.md`, and ask it to check the diff against the spec, the
   Issue's acceptance criteria, and the drawing and style rules in
   `design.md`: wrong numbers, metric definitions not followed, missing
   tests (every AC ID in the Issue has a test named after it), SQL that is
   slow or repeats rows, a screen that departs from its drawing or breaks a
   style rule (quote the rule), secrets, and any box that lets a viewer
   type SQL. It posts its findings as one comment on the pull request
   (`gh pr comment`), most important first, each naming the file and the
   change to make, and returns the same list. Done when
   `gh pr view --comments` shows the review comment and you hold its list.
7. **Decide findings.** Walk the findings one at a time, most important
   first: your recommendation (fix or keep) with a one-line reason, then
   what the finding means for the dashboard. The student decides each.
   Group trivial findings (wording, a label) into one decision. Done when every finding
   has the student's call, fix or keep, with the reason for each keep (or
   the review found nothing).
8. **Fix.** Fix each finding the student chose, with the tests locked and
   spec first. Run the full suite (`pytest -rs`) and push. Then reply on the
   pull request (`gh pr comment`) with one line per finding: fixed (name the
   commit), or kept and why. Done when the full suite meets the Full suite
   step's bar after the last fix, the
   branch is pushed, and the reply covers every finding.
9. **Merge.** `gh pr merge --squash --delete-branch`, then
   `git switch main` and `git pull`. Post the handoff comment on the Issue:
   what changed on screen, what to look at, anything the next tasks should
   know, and the student's name. Tell the student what to check on screen,
   then to `/clear`. Done when `gh issue view <number>` shows the Issue
   closed with the handoff comment on it, and `git branch --show-current`
   prints `main`.

**Done when** the pull request is merged with the full suite green, every
review finding has a recorded decision, and the Issue is closed with its
handoff. After `/clear`, the student starts their next Issue with
`/dashkit:tests-first`.
