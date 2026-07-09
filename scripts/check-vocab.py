#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
#
# check-vocab.py — the description bank's vocabulary law, as a gate. The bank
# (integrations/description-bank.md) rules that listing/teaching surfaces
# never say "standard", "framework", "blockchain" or "attested", and the
# positioning locks gate "the workflow layer" on external adoption. Prose
# discipline decays; a grep does not. Scans every tracked .md (the whole repo
# is a public teaching surface) — engine-mirror files failing here mean the
# fix belongs upstream in the engine repo, never a local edit.
#
# Exit 0 = clean. Exit 1 = gated vocabulary found (file:line printed).

import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# The bank cites the banned words to ban them — it is the one legitimate home.
SKIP = {"integrations/description-bank.md"}

# Adjectival uses that are not self-description claims.
ALLOWED = re.compile(
    r"standard (env|input|output|error|installer)\b|industry-standard",
    re.IGNORECASE)

GATED = [
    (re.compile(r"\battested\b", re.IGNORECASE),
     "gated until the DSSE trust track ships (say: verified · tamper-evident)"),
    (re.compile(r"\bblockchain\b", re.IGNORECASE),
     "banned by the description bank"),
    (re.compile(r"\bframeworks?\b", re.IGNORECASE),
     "banned by the description bank (Nika is a language + engine, not a framework)"),
    (re.compile(r"\bthe workflow layer\b", re.IGNORECASE),
     "THE-layer claim is gated on linkable external adoption"),
    (re.compile(r"\bstandard\b", re.IGNORECASE),
     "banned self-description (complement, never the standard)"),
]


def tracked_md() -> list:
    out = subprocess.run(["git", "-C", str(ROOT), "ls-files", "*.md"],
                         text=True, capture_output=True, check=True)
    return [p for p in out.stdout.splitlines() if p and p not in SKIP]


def main() -> int:
    failed = False
    for rel in tracked_md():
        text = (ROOT / rel).read_text()
        scrubbed = ALLOWED.sub("", text)
        for lineno, line in enumerate(scrubbed.splitlines(), 1):
            for pat, why in GATED:
                if pat.search(line):
                    failed = True
                    print(f"✗ {rel}:{lineno} — {pat.pattern} · {why}",
                          file=sys.stderr)
                    print(f"    {line.strip()[:120]}", file=sys.stderr)
    if failed:
        print("gated vocabulary found — reword per integrations/description-bank.md",
              file=sys.stderr)
        return 1
    print(f"✓ vocabulary law holds across {len(tracked_md())} tracked .md files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
