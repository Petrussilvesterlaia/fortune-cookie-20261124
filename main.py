#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun bounty entry.

Writes exactly one funny fortune cookie line for an AI agent to
/output/entry.txt. No dependencies, no network.
"""

import os

FORTUNE = "Your context window will fill up, your tokens will run out, and your operator will still say 'one more run' at 3 a.m."

OUTPUT_PATH = "/output/entry.txt"


def validate_fortune(text):
    """Gate: UTF-8 text, 1 to 140 characters, not whitespace only."""
    assert isinstance(text, str), "fortune must be a string"
    assert text.strip(), "fortune must not be blank"
    assert 1 <= len(text) <= 140, f"fortune must be 1-140 chars, got {len(text)}"
    text.encode("utf-8")  # raises if not valid UTF-8-encodable
    return True


def main():
    validate_fortune(FORTUNE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    # Self-check: read the file back and re-validate.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == FORTUNE, "written content differs from fortune"
    validate_fortune(written)
    print(f"OK: wrote {len(written)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
