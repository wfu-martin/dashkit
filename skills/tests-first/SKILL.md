---
name: tests-first
description: Write the failing tests for one Issue and explain what each proves.
disable-model-invocation: true
argument-hint: "[issue number]"
---

# Tests first

Issue: $ARGUMENTS (if empty, ask which Issue).

1. Read the Issue with `gh issue view <number>` and only the parts of
   `spec.md` it names.
2. From an up-to-date `main`, create the Issue's branch:
   `<number>-<short-name>`.
3. Write the tests the Issue lists, in `tests/`:
   - a **reconciliation test** for every figure: the function the screen will
     call returns the same number as an independent SQL query that reaches
     it a different way (another table, or a simpler path);
   - an **acceptance test** for every Given / When / Then line.
   Follow `tests/test_example_reconciliation.py` for the pattern.
4. Run `pytest` and show the student the new tests failing. Red is the goal:
   it proves the tests check something that does not exist yet.
5. Explain each new test in one plain sentence: what it proves about the
   dashboard and why that matters to the stakeholder.

Done when every test the Issue names exists and fails for the expected
reason (the function or screen does not exist yet), and nothing else is
built. Commit the tests on the branch. `/dashkit:build-next` picks up from
here.
