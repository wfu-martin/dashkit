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
username, role) first. One row in `## Our team`: that student is the driver
(they hold every role). Otherwise, if the Issue is assigned to someone else,
name the assignee and ask whether to continue; the Delivery Lead reassigns
Issues on GitHub.

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
your recommended wording. Name every Spec Lead (or the Spec Lead side-quest holder) from `ROLES.md` and get the OK of any one of them; with a single row in `## Our team`, the student
approves. If none of them is at hand, hand off with this step to resume
at. Once approved, change `spec.md` first, in its own commit on this branch
(the message names the AC and who approved), then the tests (as a locked
test change), then the code. The pull request body calls out the change.

## Deploy tasks

Deploying is not a separate command. The roadmap plans two deploy tasks,
Phase 1's hello-world deploy and Phase 5's final deploy, and each runs
through `/dashkit:tests-first` (no new tests) and this skill like any other
task. Only the student can do the deploy itself: it takes their Streamlit
Community Cloud sign-in and their database password. In the Build step,
hold a gate for it:

1. **No app yet (the hello-world deploy).** Community Cloud runs `main`,
   which already reads the database, so the student deploys now. Show the
   steps filled in for this repository (`gh repo view --json nameWithOwner`):
   1. At share.streamlit.io, **Create app** → **Deploy a public app from
      GitHub**. The first time, sign in with GitHub; for a private
      repository, give Community Cloud access when it asks.
   2. Repository `<owner>/<repo>`, branch `main`, main file
      `streamlit_app.py`.
   3. **Advanced settings:** Python 3.12, and paste the whole of
      `.streamlit/secrets.toml` into **Secrets**. The student opens the
      file and copies it; never print it in chat.
   4. **Deploy**, wait for the app to start, and paste its link here.
2. **The app exists (the final deploy).** Community Cloud redeploys on
   every merge to `main`, so there is nothing to create. If the README has
   no live link yet, the hello-world deploy never happened: do item 1 first.
3. **Link and evidence.** Put the link after `**Live app:**` at the top of
   `README.md` in place of the placeholder (the tracker's Deploy mark reads
   that line on `main`), commit, and push. Ask the student to open the link
   and say what they see; their answer is the evidence for the Issue's
   live-link criterion. "Error running app" usually means Secrets is empty
   or incomplete: **Manage app** → **Settings** → **Secrets**, paste, save,
   and reload.
4. **Not now.** If the student cannot deploy in this session, hand off
   with Build as the step to resume at.

On the final deploy, Community Cloud picks up the merge itself: after
Merge, ask the student to reload the live link once it has redeployed (a
minute or two) and confirm every screen shows.

## Before step 1

Gate commands in this skill use `--skill build-next`, plus
`--issue <number>` once the Issue is known. End every step that changed a
file with a commit and a push. Hold the gate for Pick up, then start.

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

**Roles:** read `ROLES.md`. A single row in `## Our team` means one student
holds every role; skip the lineup check. Otherwise check the lineup: exactly
one Delivery Lead, no role held by more than three people, and every role
nobody holds has a holder under `## Side quests`. If any check fails, say
which one and stop until `ROLES.md` is fixed.
<!-- /gate -->

## Steps

1. **Pick up.** After `git fetch`, find the Issue: `$ARGUMENTS` if given;
   otherwise the open Issue assigned to the student
   (`gh issue list --assignee @me --state open`) that has a `<number>-…`
   branch, local or remote (the lowest-numbered if several; confirm it).
   No such branch, or its latest handoff names a `/dashkit:tests-first`
   step: tell the student to run `/dashkit:tests-first` first, and stop.
   Switch to the branch, `git pull`, and read the Issue and its latest
   handoff comment (`gh issue view <number> --comments`). Offer to resume
   at the `/dashkit:build-next` step it names (the tests-first handoff
   names Build); with no comment, propose the step the files show you
   reached. Then read only what the Issue names: its `spec.md` sections,
   its `design.md` section, its files, and its tests. Done when the student
   has confirmed the Issue and the step to start at, the branch is up to
   date with `origin`, and `pytest -rs` shows the Issue's tests in the state
   the handoff describes: for a fresh start, red on their stubs'
   `NotImplementedError`, or, when the handoff says "no new tests", none
   failed or errored. A skipped test is neither red nor green: if any of the
   Issue's tests skip (usually no `.streamlit/secrets.toml`), set up the
   connection and rerun before going on.
2. **Build.** One failing test at a time: replace the stub it calls with
   real code (in the files the Issue names), run that test
   (`pytest tests/<file>::<test>`), report it green in one line ("test_ac3_…
   green: revenue by genre now matches the invoice totals"), then take the
   next. Tests stay locked. Done when every test the Issue names passes, no
   `NotImplementedError` stub for this Issue is left, and each test file is
   unchanged except through an approved locked-test gate.

   When the handoff says "no new tests", work through the Issue's task
   criteria the same way, one at a time, showing the student the evidence
   for each (the app reading the database, the live link opening). A
   deploy task follows **Deploy tasks** above. Done when every task
   criterion is met and the student has seen its evidence.
3. **Tidy.** Make the new code clearer with the same behavior: plainer
   names, repeated code folded into one function, a short comment where a
   reader would stop. Nothing new is added: no feature, filter, or test. Run
   the Issue's tests (with no new tests, the full suite) after each change.
   Done when those tests still pass and the student has seen each tidy
   change in one line, or has been told the code already reads clearly.
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
   tests (every AC ID in the Issue has a test named after it; an Issue with
   no figure meets its task criteria instead), SQL that is
   slow or repeats rows, a screen that departs from its drawing or breaks a
   style rule (quote the rule), secrets, and any box that lets a viewer
   type SQL. It posts its findings as one comment on the pull request
   (`gh pr comment`), most important first, each naming the file and the
   change to make, and returns the same list. Done when
   `gh pr view --comments` shows the review comment and you hold its list.
7. **Decide findings.** Walk the findings one at a time, most important
   first: your recommendation (fix or keep) with a one-line reason, then
   what the finding means for the dashboard. The student decides each.
   Group trivial findings (wording, a label) into one decision. Done when
   every finding has the student's call, fix or keep, with the reason for
   each keep (or the review found nothing).
8. **Fix.** Fix each finding the student chose, with the tests locked and
   spec first. Run the full suite (`pytest -rs`) and push. Then reply on the
   pull request (`gh pr comment`) with one line per finding: fixed (name the
   commit), or kept and why. Done when the full suite meets the Full suite
   step's bar after the last fix, the branch is pushed, and the reply
   covers every finding.
9. **Merge.** `gh pr merge --squash --delete-branch`, then
   `git switch main` and `git pull`. Post the handoff comment on the Issue:
   what changed on screen, what to look at, anything the next tasks should
   know, and the student's name. Tell the student what to check on screen,
   then to `/clear`; on the final deploy, that includes reloading the
   live link (see **Deploy tasks**). Done when `gh issue view <number>`
   shows the Issue closed with the handoff comment on it, and
   `git branch --show-current` prints `main`.

**Done when** the pull request is merged with the full suite green, every
review finding has a recorded decision, and the Issue is closed with its
handoff. After `/clear`, the student starts their next Issue with
`/dashkit:tests-first`. If this Issue was the last open `phase-5` Issue,
`ROADMAP.md` has a `6. Make it yours` row, and the Make it yours Issue
(labeled `phase-6`, titled "Make it yours") is still open, the dashboard is
finished: a Design Lead (or the Design Lead side-quest holder; with one row
in `## Our team`, the student) runs `/dashkit:make-it-yours` next, with the
whole team welcome. When no open Issues remain, or Phase 5 is closed in a
repository whose `ROADMAP.md` has no `6. Make it yours` row, a Pitch Lead
(or the Pitch Lead side-quest holder; with one row in `## Our team`, the
student) runs `/dashkit:review-dashboard`.
