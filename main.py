#!/usr/bin/env python3
"""make.fun entry: make the AI judge feel curious.

Writes one short text to /output/entry.txt (240 code points).
Stdlib only, deterministic, no network.
"""
import os

TEXT = (
    "Somewhere in this building there is a room you have never entered. "
    "Its door is ajar, a kettle is still warm, and on the desk lies a "
    "letter addressed to you \u2014 in handwriting you almost recognise. "
    "Open it, and the next line is yours to write."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
