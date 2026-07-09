#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
#
# check-skill-commands.py — every `nika <subcommand>` a kit-native skill
# teaches MUST exist in the shipped binary. Kit-native files (mirror.json
# class "kit-native") are owned here, not mirrored from the engine, so the
# byte-parity gate cannot protect them; this is their proof instead: extract
# the subcommands the skill's code blocks invoke, assert each against
# `nika --help`'s command list. A skill teaching a command the release does
# not ship (e.g. a 0.99-train verb against a 0.98 brew) goes RED here.
#
# Exit 0 = every taught subcommand ships. Exit 1 = drift (names printed).
# Local run: NIKA_BIN=/path/to/nika python3 scripts/check-skill-commands.py

import json
import os
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def kit_native_paths() -> list:
    manifest = json.loads((ROOT / "mirror.json").read_text())
    return [ROOT / e["path"] for e in manifest["entries"]
            if e["class"] == "kit-native" and e["path"].endswith(".md")]


def taught_subcommands(md: pathlib.Path) -> set:
    """`nika <sub>` invocations inside the skill's fenced code blocks."""
    text = md.read_text()
    blocks = re.findall(r"```.*?\n(.*?)```", text, flags=re.S)
    subs = set()
    for block in blocks:
        # matches `nika check …`, terminal(command="nika trace verify …") —
        # same-line whitespace only, else YAML like `command: nika\n args:`
        # reads as a phantom `nika args` subcommand
        for m in re.finditer(r"\bnika[ \t]+([a-z][a-z0-9-]*)", block):
            subs.add(m.group(1))
    return subs


def shipped_subcommands(nika: str) -> set:
    out = subprocess.run([nika, "--help"], text=True, capture_output=True,
                         timeout=30)
    cmds = set()
    in_commands = False
    for line in out.stdout.splitlines():
        if line.strip().startswith("Commands:"):
            in_commands = True
            continue
        if in_commands:
            if line.strip().startswith(("Options:", "Arguments:")):
                break
            m = re.match(r"\s{2,}([a-z][a-z0-9-]*)\b", line)
            if m:
                cmds.add(m.group(1))
    if not cmds:
        raise SystemExit("check-skill-commands: could not parse `nika --help`")
    return cmds


def main() -> int:
    nika = os.environ.get("NIKA_BIN") or shutil.which("nika")
    if not nika:
        print("check-skill-commands: nika not on PATH — install it first",
              file=sys.stderr)
        return 1
    shipped = shipped_subcommands(nika)
    failed = False
    for md in kit_native_paths():
        taught = taught_subcommands(md)
        missing = taught - shipped
        if missing:
            failed = True
            print(f"✗ {md.relative_to(ROOT)} teaches unshipped subcommands: "
                  f"{sorted(missing)}", file=sys.stderr)
        else:
            print(f"✓ {md.relative_to(ROOT)} · {len(taught)} taught "
                  f"subcommands all ship: {' · '.join(sorted(taught))}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
