#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
#
# check-dead-forms.py — the kit-native half of the drift ratchet.
#
# The engine side already refuses a mirrored kit that teaches a form the
# engine rejects (nika-onboard's `the_kit_never_teaches_a_form_the_engine
# _refuses`). The kit-native surfaces here — the Hermes delegation skill,
# every integrations/ pack, the root README — had no equivalent, and they
# teach the same language to the same agents.
#
# Why it exists: the 2026-07-28 audit found the plugin teaching `vars:`,
# `${{ env.X }}`, a scalar `workflow:`, a `tasks:` sequence and
# `capture: text` — three engine releases after each became a refusal. A
# file written from those instructions died at PARSE. Prose discipline
# decays; a grep does not.
#
# USING a dead form is banned everywhere. NAMING one is legitimate where
# porting or history is the subject — a migration table has to spell what
# it migrates. That asymmetry is the whole exemption list below.
#
# Exit 0 = clean. Exit 1 = a dead form is being taught (file:line printed).

import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Engine-mirrored files are proven by the ENGINE's own test + the sha256
# pins in mirror.json; re-judging them here would report an upstream
# problem as a local one.
SKIP_PREFIXES = (".agents/plugins/",)

# (regex, why) — banned in every kit-native teaching surface, no exemption.
DEAD_USAGE = [
    (re.compile(r"\$\{\{\s*vars\."),
     "NIKA-VALUES-001 · the vars namespace is dead — read inputs: or const:"),
    (re.compile(r"\$\{\{\s*env\."),
     "NIKA-VALUES-002 · the env namespace is dead — read config: or secrets:"),
    (re.compile(r"\bcapture:\s*text\b"),
     "capture is stdout · stderr · combined · structured"),
    (re.compile(r"^\s*workflow:\s*[A-Za-z<][^\s:]*\s*$", re.MULTILINE),
     "NIKA-PARSE-020 · the envelope is an OBJECT carrying id:"),
    (re.compile(r":\s*succeeded\b"),
     "NIKA-DAG-005 · the predicate is `success`"),
    (re.compile(r":\s*failed\b"),
     "NIKA-DAG-005 · the predicate is `failure`"),
    # `type: boolean` is NOT listed here on purpose. It is dead under the
    # value authorities (NIKA-TYPE-001 wants `bool`) but perfectly correct
    # inside a `schema:` block, which is JSON Schema and not Nika's type
    # grammar. A regex cannot tell those apart from one line, and a gate
    # that reds a legitimate schema example teaches people to ignore it.
    # Column 0 inside a fence is the ENVELOPE level, where both blocks are
    # dead. An INDENTED `env:` is a task's own environment map and is very
    # much alive, which is why the anchor matters more than the word.
    (re.compile(r"^vars:\s*$", re.MULTILINE),
     "NIKA-VALUES-001 · the vars envelope block is dead — inputs: / const:"),
    (re.compile(r"^env:\s*$", re.MULTILINE),
     "NIKA-VALUES-002 · the env envelope block is dead — config: / secrets:"),
]

# Legitimate only where porting or history is the subject.
DEAD_NAMING = [
    (re.compile(r"`vars:`"), "NIKA-VALUES-001 · classify into inputs: / const:"),
    (re.compile(r"`depends_on`"), "dead edge form — with: / after:"),
]
MAY_NAME_THE_RETIRED = {
    "integrations/openclaude/SUBMISSION.md",
}


def tracked_teaching_files() -> list:
    out = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "*.md", "*.mdc", "*.yaml", "*.yml"],
        text=True, capture_output=True, check=True)
    return [p for p in out.stdout.splitlines()
            if p and not p.startswith(SKIP_PREFIXES)]


def main() -> int:
    failed = False
    scanned = 0
    for rel in tracked_teaching_files():
        text = (ROOT / rel).read_text()
        scanned += 1
        rules = list(DEAD_USAGE)
        if rel not in MAY_NAME_THE_RETIRED:
            rules += DEAD_NAMING
        for pat, why in rules:
            for m in pat.finditer(text):
                lineno = text[:m.start()].count("\n") + 1
                failed = True
                print(f"✗ {rel}:{lineno} — {why}", file=sys.stderr)
                print(f"    {text.splitlines()[lineno - 1].strip()[:110]}",
                      file=sys.stderr)
    if failed:
        print("\na kit-native surface teaches a form the engine refuses — "
              "fix the teaching, never the engine", file=sys.stderr)
        return 1
    # An empty sweep prints the same ✓ as a clean one. The kit always has
    # kit-native surfaces (README · integrations · skills); a harvest near
    # zero means the file walk moved, and this gate is blind rather than
    # satisfied.
    if scanned < 5:
        print(f"✗ swept only {scanned} kit-native file(s) — the walk moved, "
              "this gate is blind (expected the README, integrations/ and "
              "skills/ surfaces)", file=sys.stderr)
        return 1
    print(f"✓ no dead language forms across {scanned} kit-native teaching files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
