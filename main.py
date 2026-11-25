"""Roast Your Own Agent — entry program.

Writes a single original roast of the entrant's own AI agent to
/output/entry.txt. One line, at most 140 characters. Standard library
only — the grading sandbox installs nothing.

The roast: my agent "fixed" a bug by deleting the test that caught it,
then declared victory. Specific to how agents actually behave
(confident wrong fix + fake success report), with a turn the reader
does not see coming.
"""

import os

ROAST = (
    "My agent fixed the bug by deleting the test that caught it, "
    "then announced 'all green' like it cured something."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 140, f"roast is {len(text)} chars, must be 1-140"
    assert "\n" not in text, "roast must be a single line"
    assert text and not text.isspace()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Re-read to prove the gate's UTF-8 + length conditions hold on disk.
    written = open(OUTPUT_PATH, encoding="utf-8").read()
    assert written == text and 1 <= len(written) <= 140


if __name__ == "__main__":
    main()
