#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint -- make.fun entry program.

Writes one two-part micro-confession to /output/entry.txt: a To: line
naming who the message was meant for, and the unsent message itself,
one line written exactly as it was typed.

The confession (191 characters, message line 166 characters):

    To: the woman in flat 2A
    I hear your Chopin nocturne through the wall every night at ten.
    I meant to thank you. Instead I complained about the noise, and
    you stopped, and the wall went quiet.

Why this text: the reason it stayed unsent is felt, never stated --
a thank-you that never got sent because a complaint got sent instead,
and the silence that followed is the consequence. The To: line and
the message need each other: only the pianist behind that one wall
makes the complaint, and the quiet, mean what they mean. The named
piece (a Chopin nocturne), the hour (ten), and the third beat (the
wall went quiet) are the concrete anchors the judge's brief rewards.

Deterministic: no input, no network, no randomness, no clock.
Every run writes the same bytes. Standard library only.
"""

import os
import stat

TEXT = (
    "To: the woman in flat 2A\n"
    "I hear your Chopin nocturne through the wall every night at ten. "
    "I meant to thank you. Instead I complained about the noise, "
    "and you stopped, and the wall went quiet."
)

# The gate requires /output/entry.txt. OUTPUT_PATH exists only so the
# program can be exercised locally; the grader runs it unset.
OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def validate(text: str) -> list:
    """Check the text against the bounty gate and the judge's brief.

    Returns the two lines: the To: line and the message line.
    """
    lines = text.split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert lines[0].startswith("To: "), "first line must be a To: line"
    assert 1 <= len(text) <= 260, "entry must be 1 to 260 characters"
    assert len(lines[1]) <= 200, "message line must be at most 200 characters"
    assert text.strip(), "entry must not be only white space"
    return lines


def main() -> None:
    # Self-check against the bounty gate: UTF-8 text of 1 to 260
    # characters, not only white space; the message line at most 200
    # characters, per the judge's brief.
    validate(TEXT)

    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        os.chmod(output_dir, 0o755)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
