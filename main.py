#!/usr/bin/env python3
# Authored for make.fun coolest-art-01.
"""Write the entry image to the harness output directory.

The competition judges exactly the bytes written to /output/entry.png.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def output_dir() -> Path:
    """Return the directory the harness reads the entry from."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    """Copy the image beside this program to the output directory."""
    target = output_dir() / "entry.png"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
