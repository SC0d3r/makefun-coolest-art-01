Coolest art entry for make.fun.

`main.py` finds `entry.png` beside itself, copies it byte for byte into the
directory given by `MAKEFUN_OUTPUT_DIR` (default `/output`), creating that
directory if needed, then prints the output path and the byte count.

Run it locally:

    MAKEFUN_OUTPUT_DIR=out python3 main.py

`entry.png` is the entry itself, and `out/entry.png` will be an exact copy of it.
