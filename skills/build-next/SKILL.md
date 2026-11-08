---
name: build-next
description: Build the next Issue start to finish - branch, tests, code, review, merge.
disable-model-invocation: true
argument-hint: "[issue number, optional]"
---

# Build the next task

One Issue, start to finish. State lives in files and Issues, never in chat,
so any fresh session can pick the work up.

## Steps

1. **Start clean.** `git status` is clean and `main` is up to date
   (`git switch main && git pull`). If not, stop and tell the student what
   is in the way. Already on an Issue's branch (from `/dashkit:tests-first`
   or a handoff comment)? Read the Issue's latest comment and resume at the
   step it names.
2. **Pick the Issue.** $ARGUMENTS if given; otherwise the lowest-numbered open
   Issue assigned to the student whose dependencies are closed
   (`gh issue list --assignee @me`). Confirm it with the student.
3. **Branch** `<number>-<short-name>`.
4. **Read only what the Issue names**: its spec sections, its `design.md`
   section, and its files.
5. **Tests first.** Write the Issue's tests, run them, and confirm they fail.
6. **Build** until they pass, then run the **full** suite. Nothing merges red.
7. **Commit, push, open a pull request** whose body says `Closes #<number>`
   and lists what changed on screen.
8. **Review.** Launch a separate review agent with fresh context, model
   `sonnet`. Give it the pull request number, the Issue number, and
   `spec.md`, and ask it to check the diff against the spec and the
   Issue's acceptance criteria: wrong numbers, metric definitions not
   followed, missing tests, SQL that is slow or repeats rows, secrets, and
   any box that lets a viewer type SQL. It reports findings, most important
   first.
9. **Fix** what the review found; re-run the full suite; push.
10. **Merge** (`gh pr merge --squash --delete-branch`), switch to `main`,
    pull, and post a short handoff comment on the Issue: what changed, what
    to look at on screen, anything the next tasks should know.
11. Tell the student what to check on screen, then to `/clear` before the
    next task.

## Stop rule

When context passes about 50% before the task is done (the student's status
line, or `/context`), or the student says so: post a handoff comment on the Issue (what is done,
what is left, the next step number), commit the work in progress on the
branch, push, and stop. The next fresh session resumes from that comment.

Report every step in plain business language: what changed for the person
using the dashboard, and what the student should check.
