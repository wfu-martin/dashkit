# dashkit

Six Claude Code skills for building a dashboard the way a disciplined team
does: a spec that turns a stakeholder's questions into testable
requirements, a design signed off on a mockup, a roadmap of small tasks,
tests before code, one task at a time with a separate review, and a final
review of the dashboard itself.

Each skill is a short list of numbered steps, and Claude stops at a gate
between every two of them. At each gate it shows two progress lines (where
the whole project stands, and where you are in the current skill), asks you
to read the context percentage off your status line and recommends handing
off at 50%, says in a sentence or two what the next step is for, and waits
for your go-ahead. Work is saved in the repository and on GitHub, never only
in the chat, so a teammate or a fresh session can pick it up from the last
handoff comment. Every team member holds a role from `ROLES.md`; the role
that owns a planning skill runs it and merges it, and each task is run and
merged by the teammate it is assigned to.

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
| `/dashkit:build-next` | Second half of a task, from red to merged: builds one test at a time, tidies, runs the full suite, opens the pull request, has it reviewed separately, settles each finding with you, and merges |
| `/dashkit:review-dashboard` | Checks every spec question is answered on screen and every rule in `design.md` holds, then turns the fixes you choose into assigned Issues |

Each task takes two commands, each in a fresh session: `/dashkit:tests-first`
and then `/dashkit:build-next`.

## Extras

| File | What it is |
|---|---|
| `extras/CLAUDE.md` | A starter for `~/.claude/CLAUDE.md`: plain business language, one question at a time, token habits |
| `extras/statusline.py` | A status line showing the model, context used, and the five-hour plan limit |

## For maintainers

`python scripts/check_skills.py` checks that every skill carries the gate
block from `scripts/gate.md` word for word, that each skill's step names
match the tracker in `dashboard-starter` (cloned next to this repository),
and that every skill stays user-invoked. It prints `ok` when they agree. Run
it before every push.
