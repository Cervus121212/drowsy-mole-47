#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message -- entry program.

Writes one commit message for a bug fix that made everything worse
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Standard library only. Fully deterministic: the same bytes on every run.
"""

import os
import sys

ENTRY = "fix: bots kept passing the captcha, made it harder; humans fail it now, bots still pass"


def main() -> int:
    if not 1 <= len(ENTRY) <= 100:
        print(
            "entry must be 1-100 characters, got %d" % len(ENTRY),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
