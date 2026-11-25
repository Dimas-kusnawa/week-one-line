#!/usr/bin/env python3
"""Write the week-in-one-line entry to /output/entry.txt."""

import os

# 94 characters, inside the 1-100 gate. No trailing newline: the file
# holds exactly the line, so the byte count is the character count.
LINE = "Monday said 'one last thing'. It's Friday, 214 tabs open, and the last thing is still loading."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
