#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
#
# derive-hero-light.py — media/hero-light.svg is a projection of
# media/hero-dark.svg: same geometry, same animations, only the THEME
# block (CSS custom properties between the THEME:START/END markers)
# differs. Editing the light file by hand is the drift; run this after
# any change to the dark twin.

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
PAIRS = [
    (ROOT / "media/hero-dark.svg", ROOT / "media/hero-light.svg"),
    (ROOT / "media/update-rungs-dark.svg", ROOT / "media/update-rungs-light.svg"),
]

LIGHT_THEME = """\
    /* THEME:START */
    :root {
      --bg0: #fbfcfe; --bg1: #eef2f8;
      --ink: #0b0d12; --tag: #4a5568; --cmd: #1a2233;
      --legend: #5a6b80; --legend-dim: #5a6b80;
      --accent: #c2410c;
      --mark: #04050d; --glow: #5b8cff;
      --star: #5b8cff; --star-op: 0.5; --tw-lo: 0.1; --tw-hi: 0.55;
      --pulse-lo: 0.15; --pulse-hi: 0.38; --halo-op: 0.18;
      --chip-bg: #f0f3f9; --chip-stroke: #d8dfeb;
      --frame: #0b0d12; --frame-op: 0.1;
      --v-infer: #3b5bdb; --v-exec: #c2410c; --v-invoke: #0b7285; --v-agent: #862e9c;
      --wm-op: 0.05;
    }
    /* THEME:END */"""

BLOCK = re.compile(r"[ ]*/\* THEME:START \*/.*?/\* THEME:END \*/", re.S)


def main() -> int:
    for dark, light in PAIRS:
        src = dark.read_text()
        if not BLOCK.search(src):
            print(f"derive-hero-light: THEME markers missing in {dark.name}",
                  file=sys.stderr)
            return 1
        light.write_text(BLOCK.sub(LIGHT_THEME, src, count=1))
        print(f"→ {light.relative_to(ROOT)} (theme block swapped · rest identical)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
