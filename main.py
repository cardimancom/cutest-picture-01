"""Cutest picture entry: copy the bundled image to the output path.

The image (art.png) is a fluffy baby penguin chick, generated for this
entry and stored in this repository. The program writes it byte-for-byte
to $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png), so the
two runs make.fun performs produce identical bytes.

Limits the entry respects (RULES.txt): PNG, at most 1,048,576 bytes and
at most 1024x1024 pixels; art.png is 1,048,179 bytes at 1024x1024.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "art.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
