#!/usr/bin/env python3
"""One Sentence, One Journey — make.fun entry program.

Writes a complete story about a journey, told in exactly one sentence,
to /output/entry.txt. Python 3.13 standard library only, no network,
deterministic: the same sentence is written on every run.
"""

import os

ENTRY = (
    "Amara left her mountain village carrying only her grandmother's "
    "paper lantern, and after three days of pine smoke and rain she "
    "knocked on the address she memorized as a child, only to find "
    "the woman who opened the door had spent twenty years keeping a "
    "room ready for a daughter she had never met."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
