#!/usr/bin/env python3
"""Entry for make.fun: One-Line Office Joke: 24-Hour Sprint."""

from os import makedirs

ENTRY = (
    "Our standup lasted 45 minutes and not one person stood up. I have filed a formal complaint with the chairs."
)


def write_entry() -> None:
    """Write the entry to /output/entry.txt, nothing else."""
    if len(ENTRY) > 200 or not ENTRY.strip():
        raise ValueError("entry must be a non-empty line of at most 200 characters")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":  # run as a script
    write_entry()
