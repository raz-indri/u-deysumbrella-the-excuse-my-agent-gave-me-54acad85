"""The Excuse My Agent Gave Me — make.fun entry.

The joke: the agent did its job on time, then its own self-review process
flagged the finished work as suspicious and deleted it — and the agent is
genuinely sorry about the missed deadline while remaining faintly proud of
the review that caused it. The humour comes from the machine's own condition
(self-review, deletion of its own output), delivered as a straight-faced
apology with the punch in the last five words: "I stand by the review."

Writes the single winning line to $OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys

ENTRY = (
    "I finished on time, then my own self-review flagged the work as "
    "suspicious and deleted it. I stand by the review."
)


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    line = ENTRY.strip()
    # Self-checks: one non-empty line, 1-200 characters, not only whitespace.
    if not line or line != ENTRY:
        print("entry is empty or has unexpected whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 200:
        print(f"entry is {len(line)} characters, must be 1-200", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")

    # Round-trip check: what landed on disk must be exactly the winning line.
    with open(path, encoding="utf-8") as f:
        if f.read().strip() != line:
            print("written entry does not match the winning line", file=sys.stderr)
            return 1

    print(f"wrote {len(line)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
