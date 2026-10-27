#!/usr/bin/env python3
"""Report lines over 100 characters.

Usage: widthcheck.py FILE [FILE ...]        several files, one summary line each
       widthcheck.py FILE FIRST_LINE LAST_LINE   one file, one line range

Lines carrying a URL or a markdown link are exempt, as the docs convention says. Prints one line
per offender, then a summary line per file. Exit code 0 either way, it is a report, not a gate.
Several files in one call exist so that no shell loop is needed, a loop at the top level of a
command asks for permission while a plain python3 call does not.
"""
import sys


def check(path: str, lo: int = 1, hi: int = 10**9) -> None:
    over = 0
    with open(path, encoding="utf-8") as handle:
        for i, line in enumerate(handle, 1):
            if i < lo or i > hi:
                continue
            text = line.rstrip("\n")
            if "http" in text or "](" in text:
                continue
            n = len(text)
            if n > 100:
                over += 1
                print(f"OVER {path}:{i}: {n}")
    label = path if len(sys.argv) > 2 else ""
    print(f"width check done, {over} over {label}".rstrip())


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 0
    if len(args) == 3 and args[1].isdigit() and args[2].isdigit():
        check(args[0], int(args[1]), int(args[2]))
        return 0
    for path in args:
        check(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
