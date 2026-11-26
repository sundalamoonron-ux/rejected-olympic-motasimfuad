"""Rejected Olympic Sports.

Writes the winning rejected Olympic sport one-liner to /output/entry.txt.
The line was picked by a full pairwise round-robin tournament over 10
candidate lines, judged on the competition's own criteria: a funny
one-line rejected Olympic sport, landing in one read, sounding like a
real event a broadcaster would have to explain, wasting no words, and
staying quotable. The winner went 9-0.
"""

import os

# Winning line (109 characters, one line, UTF-8):
# "Speed Folding: athletes fold a fitted sheet against the clock;
#  the judges have never seen one done correctly."
LINE = (
    "Speed Folding: athletes fold a fitted sheet against the clock; "
    "the judges have never seen one done correctly."
)


def main() -> None:
    # Gate self-check (mirrors the competition gate): 1-200 chars,
    # exactly one line, not only whitespace, valid UTF-8.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    LINE.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
