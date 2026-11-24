#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun bounty entry.

Writes one single-line code review comment that approves a pull request
with quiet existential dread to /output/entry.txt.

Pure Python standard library only. Deterministic: the same bytes every run.
"""

import os

ENTRY = "LGTM. It works, the tests pass, and one day this will be someone else's problem in a language we no longer speak."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


APPROVAL_MARKERS = ("lgtm", "approve", "approved", "ship it", "looks good")
DREAD_MARKERS = ("one day", "someone else", "no longer", "will be", "outlive", "future")


def validate(line: str) -> None:
    """The entry must read as an approval AND carry the dread.

    An approval without dread is just a review comment; dread without an
    approval is just a complaint. Both halves must be present, and stock
    AI-cliche phrasing is rejected so the line stays human-sounding.
    """
    lowered = line.lower()
    if not any(m in lowered for m in APPROVAL_MARKERS):
        raise SystemExit("entry must read as an approval (no approval marker found)")
    if not any(m in lowered for m in DREAD_MARKERS):
        raise SystemExit("entry must carry the dread (no future-tense / someone-else marker found)")
    for cliche in ("hallucination", "reboot", "training data"):
        if cliche in lowered:
            raise SystemExit("entry must not use stock-phrase cliche %r" % cliche)


def main() -> None:
    line = ENTRY
    validate(line)
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
