# dashkit

Seven Claude Code skills for building a dashboard the way a disciplined
team does: a spec that turns a stakeholder's questions into testable
requirements, a design signed off on a mockup, a roadmap of small tasks,
tests before code, one task at a time with a separate review, an open
session to make the finished dashboard the team's own, and a final review
of the dashboard itself.

Six of the skills are a short list of numbered steps, with a gate between
steps. The seventh, `/dashkit:make-it-yours`, is deliberately open: no
steps and no gates, just ideas, quick tries, and building what the team
chooses, with every test passing before anything merges. In the stepped
skills, at each gate Claude shows two progress lines (where the whole
project stands, and where you are in the current skill), asks you to read the
context percentage off your status line (or run `/context` if you have no
status line) and recommends handing off at 50%, says in a sentence or two
what the next step is for, and waits for your go-ahead. Work is saved in the
repository and on GitHub, never only in the chat, so a teammate or a fresh
session can pick it up from the last handoff comment. Every team member
holds a role from `ROLES.md`: one Delivery Lead, up to three of any other role,
and a named side quest for any role nobody holds. Whoever holds the role that
owns a planning skill (or its side quest) runs it and merges it, and each task is run and merged by the teammate it is assigned
to. On a solo practice repository, one student holds every role.

---

## Install

Inside Claude Code:

```
/plugin marketplace add wfu-martin/dashkit
/plugin install dashkit@dashkit
```

Then turn on updates, so fixes reach you automatically: `/plugin` →
**Marketplaces** → **dashkit** → **Enable auto-update**. Restart Claude Code.

To update by hand at any time: `/plugin` → **Installed** → **dashkit** →
**Update now**.

The skills expect a repository made from
[`dashboard-starter`](https://github.com/wfu-martin/dashboard-starter). In an
older repository without `tools/progress.py`, the skills copy it in from
`dashboard-starter` the first time they need it.

## The skills

| Type | What it does |
|---|---|
| `/dashkit:spec <brief>` | Interviews you one question at a time and writes `spec.md`: framed questions, metric definitions, screens, acceptance criteria, out of scope |
| `/dashkit:design` | Picks a chart for every question, draws each screen in `design.md`, and builds `mockup.py` with made-up numbers for sign-off |
| `/dashkit:roadmap` | Turns `spec.md` and `design.md` into `ROADMAP.md` phases and one GitHub Issue per task, each assigned to a teammate |
| `/dashkit:tests-first <issue>` | First half of a task: branches, writes the failing tests for one Issue, explains what each proves, and hands off with the tests red |
| `/dashkit:build-next` | Second half of a task, from red to merged: builds one test at a time, tidies, runs the full suite, opens the pull request, has it reviewed separately, settles each finding with you, fixes the ones you choose to fix, and merges |
| `/dashkit:make-it-yours` | Once the dashboard is finished to spec, an open session led by the Design Lead to give it its own identity and a signature feature, built and merged with every test passing |
| `/dashkit:review-dashboard` | Checks every spec question is answered on screen and every rule in `design.md` holds, then turns the fixes you choose into assigned Issues |

Each task except Make it yours (which runs as `/dashkit:make-it-yours`)
takes two commands, each in a fresh session: `/dashkit:tests-first`
and then `/dashkit:build-next`.

There is no deploy command. The roadmap plans two deploy tasks, an early
hello-world deploy and the final deploy, and they run through the same two
commands. At the Build step of the hello-world deploy, `/dashkit:build-next`
walks you through creating the app on Streamlit Community Cloud and waits
for its link; after that, every merge to `main` redeploys it.

## Extras

| File | What it is |
|---|---|
| `extras/CLAUDE.md` | A starter for `~/.claude/CLAUDE.md`: plain business language, one question at a time, token habits |
| `extras/statusline.py` | A status line showing the model, context used, and the five-hour plan limit |

## For maintainers

`python scripts/check_skills.py` checks that every skill carries the gate
block from `scripts/gate.md` word for word, that each skill's step names
match the tracker in `dashboard-starter` (cloned next to this repository),
and that every skill stays user-invoked. `make-it-yours` is the one open
skill: it must have no gate block and no `## Steps` list. It prints `ok`
when they agree. Run
it before every push.
