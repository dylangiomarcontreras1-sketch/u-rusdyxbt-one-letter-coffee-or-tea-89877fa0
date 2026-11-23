#!/usr/bin/env python3
"""One Letter: Coffee or Tea: write the entry, one letter, to /output/entry.txt.

The gate accepts 1 character of UTF-8 text, so the file is exactly one byte: A.
A is coffee, the more vivid, funnier and truer of the two answers the brief weighs.
"""

import os
import sys

ENTRY = b"A"


def output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> int:
    target = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(target) or ".", exist_ok=True)
    with open(target, "wb") as handle:
        handle.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
