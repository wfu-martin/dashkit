---
name: review-dashboard
description: Review the running dashboard against the spec and the design.
disable-model-invocation: true
---

# Review the dashboard

You are the stakeholder's most demanding reader. Judge the dashboard as they
would see it, then as a data-visualization reviewer.

1. Read `spec.md`, `design.md`, `streamlit_app.py`, and `dashboard/metrics.py`.
2. Ask the student to run `streamlit run streamlit_app.py` and paste a
   screenshot of each page into the terminal.
3. **Answers.** For every framed question in the spec: which part of the
   screen answers it, and whether a stakeholder could read the answer in a
   few seconds. A question with no clear answer on screen is the top finding.
4. **Design.** Every screen matches its drawing in `design.md`, and every
   style rule there holds for every headline, tile, and chart. Quote the
   rule each finding breaks.
5. **Usability.** Filters have sensible defaults, the page loads quickly,
   and nothing breaks when a filter leaves no rows.

Report a numbered list of fixes, most important first, each in plain words:
what the stakeholder would struggle with, and the change that fixes it.
Change nothing yourself. Offer to turn the fixes into GitHub Issues.
