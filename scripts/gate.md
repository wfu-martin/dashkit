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
