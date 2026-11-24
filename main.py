#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun bounty entry.

Writes one single-line code review comment that approves a pull request
with quiet existential dread to /output/entry.txt.

Pure Python standard library only. Deterministic: the same bytes every run.
"""

import os

ENTRY = "LGTM. It works, the tests pass, and one day this will be someone else's problem in a language we no longer speak."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    line = ENTRY
    if not line or not line.strip():
        raise SystemExit("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(line) <= 140:
        raise SystemExit("entry must be 1-140 characters, got %d" % len(line))
    data = line.encode("utf-8")
    data.decode("utf-8")  # validate UTF-8 round-trip
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    print(line)
    print("chars: %d, bytes: %d" % (len(line), len(data)))


if __name__ == "__main__":
    main()
