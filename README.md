# dashkit

Five Claude Code skills for building a dashboard the way a disciplined team
does: a spec that turns a stakeholder's questions into testable
requirements, a roadmap of small tasks, tests before code, one task at a
time with a separate review, and a final review of the dashboard itself.

---

## Install

Inside Claude Code:

```
/plugin marketplace add foresightmetrix/dashkit
/plugin install dashkit@dashkit
```

Then turn on updates, so fixes reach you automatically: `/plugin` →
**Marketplaces** → **dashkit** → **Enable auto-update**. Restart Claude Code.

To update by hand at any time: `/plugin` → **Installed** → **dashkit** →
**Update now**.

## The skills

| Type | What it does |
|---|---|
| `/dashkit:spec <brief>` | Interviews you one question at a time and writes `spec.md`: framed questions, metric definitions, screens, acceptance criteria, out of scope |
| `/dashkit:roadmap` | Turns `spec.md` into `ROADMAP.md` phases and one GitHub Issue per task |
| `/dashkit:tests-first <issue>` | Writes the failing tests for one Issue and explains what each proves |
| `/dashkit:build-next` | One Issue start to finish: branch, tests, build, full suite, pull request, separate review, fix, merge |
| `/dashkit:review-dashboard` | Checks every spec question is answered on screen and reviews the charts |

They are built to run in a repository made from
[`dashboard-starter`](https://github.com/foresightmetrix/dashboard-starter).

## Extras

| File | What it is |
|---|---|
| `extras/global-CLAUDE.md` | A starter for `~/.claude/CLAUDE.md`: plain business language, one question at a time, token habits |
| `extras/statusline.py` | A status line showing the model, context used, and the five-hour plan limit |
