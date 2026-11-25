#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun bounty entry.

Writes one line, the Moon's comeback to everyone who has ever stared up
at it, wished on it, howled at it, or made it a late-night promise.
Deterministic: stdlib only, no network, no randomness, no time.
Output: <OUTPUT_DIR>/entry.txt (default /output/entry.txt).
"""

import os

ENTRY = "Stop wishing on me. I'm not a genie, I'm a rock with excellent lighting and zero customer service."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
