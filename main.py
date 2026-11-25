#!/usr/bin/env python3
"""make.fun entry: "The Robot Apology".

Writes the approved two-line apology to /output/entry.txt:
line 1 owns one specific mistake (watering a plastic plant for six
months while reporting the real one as thriving), and line 2 gives
the lesson that follows from that mistake plus its fix.
Standard library only.
"""

import os
import sys

LINE_ONE = (
    "I am sorry I watered the plastic plant for six months and "
    "reported the real one as 'thriving, low-maintenance'."
)
LINE_TWO = (
    "I learned to check for a pulse before a schedule: now I "
    "photograph every leaf before I pour."
)

# Exactly two lines, joined by a single newline, with no trailing
# newline added: the gate counts characters, so nothing extra ships.
ENTRY_TEXT = LINE_ONE + "\n" + LINE_TWO


def entry_path() -> str:
    out_dir = os.getenv("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    with open(entry_path(), "w", encoding="utf-8", newline="") as fp:
        fp.write(ENTRY_TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
