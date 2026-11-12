# Coolest Art Entry

`main.py` copies the entry image beside it (`entry.png`) into the harness output
directory, which is `/output` inside the grader's container or the directory named
by `MAKEFUN_OUTPUT_DIR` anywhere else.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`entry.png` is the entry: the generated artwork the judges score.
