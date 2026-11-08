#!/usr/bin/env python3
"""Check that the six dashkit skills stay in step with each other and the tracker.

Why this exists: every skill carries the same "Gates" block (scripts/gate.md,
copied byte for byte), and every skill lists its steps as a numbered list under
a "## Steps" heading. The names in that list are the labels that
tools/progress.py in the dashboard-starter repo prints, so a renamed step in
one place and not the other would show students a progress line that does not
match what the skill is doing. This script is for the instructor maintaining
the plugin; students never run it.

It checks, for every skills/*/SKILL.md:
  (a) the text of scripts/gate.md appears exactly;
  (b) the bold step names under "## Steps" (items written "N. **Name.**")
      equal STEPS[<skill directory name>] from the tracker, in order;
  (c) the frontmatter contains "disable-model-invocation: true".

The tracker is loaded by file path from the sibling clone
(../dashboard-starter/tools/progress.py) so no install step is needed.

Prints "ok" and exits 0 when everything matches; otherwise lists each mismatch
and exits 1. Needs Python 3.11+ and nothing outside the standard library.
"""
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GATE = ROOT / "scripts" / "gate.md"
PROGRESS = ROOT.parent / "dashboard-starter" / "tools" / "progress.py"
STEP_RE = re.compile(r"^\d+\. \*\*(.+?)\.\*\*")


def load_steps() -> dict[str, list[str]]:
    if not PROGRESS.is_file():
        print(f"error: tracker not found at {PROGRESS}; clone dashboard-starter "
              "next to dashkit", file=sys.stderr)
        sys.exit(1)
    spec = importlib.util.spec_from_file_location("progress", PROGRESS)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.STEPS


def split_frontmatter(text: str) -> tuple[str, str]:
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return (m.group(1), text[m.end():]) if m else ("", text)


def step_names(body: str) -> list[str]:
    names, inside = [], False
    for line in body.splitlines():
        if re.match(r"^## ", line):
            inside = line.strip() == "## Steps"
            continue
        if inside and (m := STEP_RE.match(line)):
            names.append(m.group(1))
    return names


def main() -> int:
    steps = load_steps()
    gate = GATE.read_text(encoding="utf-8").strip("\n")
    problems = []
    skills = sorted(p.parent for p in ROOT.glob("skills/*/SKILL.md"))
    for name in sorted(steps):
        if not (ROOT / "skills" / name / "SKILL.md").is_file():
            problems.append(f"{name}: no skills/{name}/SKILL.md for tracker entry")
    for d in skills:
        name = d.name
        text = (d / "SKILL.md").read_text(encoding="utf-8")
        front, body = split_frontmatter(text)
        if gate not in text:
            problems.append(f"{name}: gate block missing or differs from scripts/gate.md")
        if name not in steps:
            problems.append(f"{name}: not a skill in the tracker's STEPS")
        else:
            found = step_names(body)
            if found != steps[name]:
                problems.append(f"{name}: steps {found} != tracker {steps[name]}")
        if not re.search(r"^disable-model-invocation:\s*true\s*$", front, re.M):
            problems.append(f"{name}: frontmatter lacks disable-model-invocation: true")
    if problems:
        print("\n".join(problems))
        return 1
    print("ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
