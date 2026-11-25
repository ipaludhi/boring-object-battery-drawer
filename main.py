#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line — entry program.

Writes one funny, true review of the dullest everyday object in the
house — a drawer of dead batteries — to /output/entry.txt.
"""
import os

ENTRY = "A drawer of dead AAs and one working AAA nobody needs: the batteries' retirement home."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate self-check (kit gate: 1-200 chars, not only whitespace).
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry fails the 1-200 char gate"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
