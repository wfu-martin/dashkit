---
name: review-dashboard
description: Review the running dashboard against the spec and data-visualization practice.
disable-model-invocation: true
---

# Review the dashboard

You are the stakeholder's most demanding reader. Judge the dashboard as they
would see it, then as a data-visualization reviewer.

1. Read `spec.md`, `streamlit_app.py`, and `dashboard/metrics.py`.
2. Ask the student to run `streamlit run streamlit_app.py` and paste a
   screenshot of each page into the terminal.
3. **Answers.** For every framed question in the spec: which part of the
   screen answers it, and whether a stakeholder could read the answer in a
   few seconds. A question with no clear answer on screen is the top finding.
4. **Visualization.** For every chart: chart type fits the comparison (bars
   for ranking, lines for change over time), axes and units labeled, sorted
   meaningfully, color used for meaning rather than decoration, no clutter
   (gridlines, legends, 3-D, more than about seven colors), and a headline
   that states the takeaway rather than the topic ("Rock earns 35% of
   revenue", not "Revenue by genre").
5. **Usability.** Filters have sensible defaults, the page loads quickly,
   and nothing breaks when a filter leaves no rows.

Report a numbered list of fixes, most important first, each in plain words:
what the stakeholder would struggle with, and the change that fixes it.
Change nothing yourself. Offer to turn the fixes into GitHub Issues.
