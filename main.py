#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — make.fun Growth entry.

Writes the GPS's one-line excuse for sending the driver down the
wrong road to /output/entry.txt. Pure Python standard library.
"""

import os

ENTRY = (
    "That cul-de-sac was a shortcut \u2014 the map just never told me "
    "the lake moved in after the road did."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Validation gate: re-read what was written and assert the
    # competition's constraints — 1 to 200 characters, not only
    # whitespace, exactly one line, no trailing newline.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written text differs from ENTRY"
    assert 1 <= len(written) <= 200, f"length {len(written)} outside 1-200"
    assert written.strip(), "entry is only whitespace"
    assert "\n" not in written, "entry must be exactly one line"
    assert not written.endswith("\n"), "no trailing newline allowed"
    print(f"Wrote {len(written)} characters to /output/entry.txt (gate passed)")


if __name__ == "__main__":
    main()
