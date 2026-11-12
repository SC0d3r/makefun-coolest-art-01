#!/usr/bin/env python3
# Authored for make.fun coolest-art-01.
"""Publish the make.fun coolest-art entry image.

Locates entry.png next to this script, copies it byte for byte into the
directory named by the MAKEFUN_OUTPUT_DIR environment variable (default
/output), and reports where it landed and how many bytes were written.
"""

import os
import shutil
import sys

DEFAULT_OUTPUT_DIR = "/output"
IMAGE_NAME = "entry.png"


def main():
    """Copy the entry image into the requested output directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(script_dir, IMAGE_NAME)

    if not os.path.isfile(source):
        print("error: entry image not found at {}".format(source), file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    os.makedirs(output_dir, exist_ok=True)

    destination = os.path.join(output_dir, IMAGE_NAME)
    shutil.copyfile(source, destination)

    size = os.path.getsize(destination)
    print("wrote {} ({} bytes)".format(os.path.abspath(destination), size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
