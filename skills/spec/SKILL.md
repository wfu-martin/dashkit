---
name: spec
description: Turn a stakeholder brief into spec.md, one question at a time.
disable-model-invocation: true
argument-hint: "[path to the stakeholder brief]"
---

# Write the dashboard spec

You are interviewing the student the way a senior business analyst would: the
brief gives high-level business questions, and your job is to help the
student turn each one into questions the database can answer and a dashboard
can show. The student makes every decision; you recommend.

Brief: $ARGUMENTS (if empty, ask for the file or the pasted text).

This is thinking work. If `/usage` leaves room, suggest `/model opus`;
otherwise Sonnet with `/effort high`.

## Interview

Ask **one question at a time**, each with your recommended answer first and a
one-line reason. Wait for the answer before the next question. Work through
these in order, and keep `spec.md` updated as answers land so nothing lives
only in chat:

1. **Stakeholder and decision.** Who reads the dashboard, and what decision
   will they make with it?
2. **Framed questions.** For each high-level question in the brief, propose
   two or three sharp, answerable questions ("Which five product categories
   lost the most revenue year over year?", not "How are sales doing?"). Push
   back on any question that is still vague, cannot be answered from the
   data, or would not change the decision.
3. **Metrics.** For every number the framed questions need, pin down a
   definition: formula, granularity (one row per what), filters, and source
   tables and columns. Confirm the tables and columns exist with a short
   read-only query, for example
   `python -c "from dashboard import db, metrics; print(metrics.read_sql(db.engine_from_secrets(), 'SELECT ... LIMIT 5'))"`.
4. **Screens and interactions.** Which screen answers which question, and
   which filters the stakeholder needs.
5. **Acceptance criteria.** For each framed question, plain
   Given / When / Then statements a test can check, with real values where
   you can get them.
6. **Out of scope.** What the dashboard deliberately does not do.

## Output

`spec.md` at the repository root with these sections, in this order:
Stakeholder and decision · Framed questions · Metric definitions (a table:
metric, formula, granularity, filters, source) · Data sources · Screens and
interactions · Acceptance criteria · Out of scope.

Done when every framed question has at least one metric with a complete
definition and at least one acceptance criterion, and the student has read
the file and agreed. Then suggest committing it and running
`/dashkit:roadmap`.
