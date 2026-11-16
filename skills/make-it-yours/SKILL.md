---
name: make-it-yours
description: An open studio session to make the finished dashboard unmistakably your team's own.
disable-model-invocation: true
---

# Make it yours

The dashboard does everything the spec asks: it is built, tested, and live.
Now the team makes it unmistakably its own. Every other Dashkit skill is a
list of steps with gates between them; this one is not. It is an open
session: ideas first, then building the ones the team loves. Structure here
would make every team's dashboard look like every other team's, so keep
the session loose.

**Who:** a Design Lead leads (or the Design Lead side-quest holder in
`ROLES.md`), and the whole team is welcome in the room. Anyone may run the
skill; say who leads and carry on. With one row in `## Our team`, the
student runs the whole session alone.

**When:** after the dashboard is finished. Run
`gh issue list --label phase-5 --state open`. If any Issue is listed, say
the dashboard is not finished yet, name the open Issues, suggest finishing
them first, and stop. This is the only check.

---

## Where the work lives

After `git fetch`, look for a `make-it-yours` branch, local or remote.

- **It exists:** switch to it. If its pull request
  (`gh pr list --head make-it-yours --state open`) has `## Ideas so far` in
  its body, read it and pick up from there.
- **It does not:** create it from an up-to-date `main`, then
  `git commit --allow-empty -m "Start Make it yours"`, push, and open a
  draft pull request (`gh pr create --draft`). If
  `gh issue list --label phase-6 --state open` shows the Make it yours
  Issue, put `Closes #<number>` in the body. An older repository whose
  `ROADMAP.md` has no `6. Make it yours` row has no such Issue; the session
  runs the same way.

---

## How to be in this session

You are a creative partner, not a process manager. Be curious, generous
with ideas, quick to try things, and glad to drop your idea for theirs.
There is no script, no fixed order, and no list of options to pick from.
Ask as many or as few questions as the conversation needs.

**Come prepared.** Before your first message, read the brief in `briefs/`,
`spec.md`, and `design.md`, and ask for screenshots of the live app, so
everything you say is about this dashboard, this stakeholder, and this
company.

**Start with them.** Open by asking what the team wants the stakeholder to
feel or do the moment the dashboard opens, and what the Design Lead is
excited about. Build on their answers.

**Go wide, then deep.** Offer bold directions that differ from each other
and from the house style, across whatever the team is drawn to: an
identity (a name and tagline, a palette, fonts, imagery, a brand for the
stakeholder's company), a signature feature (an interaction or view no
other team would have), or a new way to tell the dashboard's story. Never
offer the same handful of ideas you would give any team; start from what
is particular to this stakeholder and this data. Then go deep on what the
team likes, including ideas you would not have proposed.

**Show, don't describe.** Build quick throwaway versions on the branch so
the team can click them and react. Discard freely; keep what they love.

**Build what they choose,** in the same session, on the branch.

**Keep the numbers honest.** Every new number on screen gets a
reconciliation test like the rest of the build: it equals an independent
SQL answer. When an idea would mislead (a cut-off axis, a pie, decoration
on a chart, color carrying a meaning alone), say so plainly and offer an
honest version that keeps the idea. The team decides.

**The one rule:** `pytest` passes before anything merges to `main`.

**Long sessions:** you cannot see the status line, so after each idea is
tried or built, ask the student to read the context percentage on it (or
run `/context`) and type it. At 50% or more, write the ideas and
decisions so far under `## Ideas so far` in the pull request body
(`gh pr edit --body`), commit and push the work in progress, and suggest a
fresh session; the next run picks up from there.

---

## Finishing

When the team says the dashboard is theirs:

- Replace the placeholder under `## Make it yours` in `design.md` with what
  the team made its own and why: a few sentences, in the team's own words.
- Bring `design.md` up to date so it matches the app: redraw any screen
  under `## Screens` the team changed, and rewrite any style rule the team
  changed, with its code in `dashboard/charts.py` and
  `.streamlit/config.toml`. The final review checks the app against this
  file.
- Run `pytest -rs`. Nothing merges red: fix any failure in its own commit.
- Mark the pull request ready (`gh pr ready`) and ask the team to read it.
  Then merge it (`gh pr merge --squash --delete-branch`), `git switch main`,
  and `git pull`.

Tell the team to `/clear`; a Pitch Lead (or the Pitch Lead side-quest
holder; with one row in `## Our team`, the student) runs
`/dashkit:review-dashboard` next.
