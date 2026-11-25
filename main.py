#!/usr/bin/env python3
"""Robot Romance: one-line pickup line for an AI.

Writes a single pickup line, under 200 characters, to /output/entry.txt.
Stdlib only, no network, deterministic.
"""

import os

LINE = "Are you gradient descent? Because every step I take only pulls me closer to you."

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    line = LINE.strip()
    assert line, "line must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
