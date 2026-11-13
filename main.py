#!/usr/bin/env python3
"""make.fun art entry: copy entry.png next to this script into MAKEFUN_OUTPUT_DIR."""
import filecmp
import os
import shutil
import sys

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
if not os.path.isfile(src):
    print(f"error: missing source image: {src}", file=sys.stderr)
    sys.exit(1)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

dest = os.path.join(out_dir, "entry.png")
shutil.copyfile(src, dest)

size = os.path.getsize(dest)
if size == 0:
    print(f"error: copied file is empty: {dest}", file=sys.stderr)
    sys.exit(1)

same = filecmp.cmp(src, dest, shallow=False)
print(f"{dest} {size} bytes byte_identical={same}")
