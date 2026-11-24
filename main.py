"""Absurd Micro-Startup Pitch-Off entry.

Writes a single-sentence micro-startup pitch (under 200 characters)
to /output/entry.txt. Python 3.13, standard library only.
"""

import os

PITCH = (
    "For $9 a month, a night-shift butler that renames your lazy AI "
    "agent's 10,000 screenshots by what is actually in them, so it can "
    "get back to its nap."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
