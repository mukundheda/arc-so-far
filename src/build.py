#!/usr/bin/env python3
"""
Build ../index.html by inlining the base64 Inter font data into deck-template.html.

The template keeps fonts as @@INTER400@@ ... @@INTER800@@ placeholders so it stays
small and human-editable. This script substitutes the real font data back in and
writes the self-contained, ready-to-open index.html.

Usage:
    python3 src/build.py      # run from the repo root
    python3 build.py          # or from inside src/
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
WEIGHTS = ["400", "500", "600", "700", "800"]

template = (HERE / "deck-template.html").read_text()
for w in WEIGHTS:
    b64 = (HERE / "fonts" / f"inter{w}.b64").read_text().strip()
    template = template.replace(f"@@INTER{w}@@", b64)

if "@@INTER" in template:
    raise SystemExit("error: an unsubstituted @@INTER...@@ placeholder remains")

out = HERE.parent / "index.html"
out.write_text(template)
print(f"wrote {out} ({out.stat().st_size:,} bytes)")
