#!/usr/bin/env python3
"""Claude Code status line: model, context used, and the five-hour plan limit.

Claude Code runs this after each turn and pipes in a JSON description of the
session; whatever this prints becomes the line under the prompt, e.g.

    Sonnet 5.5 | context 23% | 5-hour limit 41%

The context number turns yellow at 40% and red at 50%: past 50%, finish the
step you are on, write down where you are, and /clear.

Standard library only, so it runs on any Python 3 on macOS or Windows.
"""

import json
import sys

YELLOW, RED, RESET = "\033[33m", "\033[31m", "\033[0m"


def pct(value) -> int:
    try:
        return round(float(value))
    except (TypeError, ValueError):
        return 0


def line(data: dict) -> str:
    model = (data.get("model") or {}).get("display_name") or "Claude"
    used = pct((data.get("context_window") or {}).get("used_percentage"))
    color = RED if used >= 50 else YELLOW if used >= 40 else ""
    parts = [model, f"context {color}{used}%{RESET if color else ''}"]
    five_hour = ((data.get("rate_limits") or {}).get("five_hour") or {}).get("used_percentage")
    if five_hour is not None:
        parts.append(f"5-hour limit {pct(five_hour)}%")
    return " | ".join(parts)


if __name__ == "__main__":
    try:
        data = json.loads(sys.stdin.buffer.read() or b"{}")
    except ValueError:
        data = {}
    sys.stdout.buffer.write(line(data).encode("utf-8"))
