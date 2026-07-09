# AGENTS.md — nika-agents (the plugin marketplace mirror)

Vendor-neutral agent entry per the AGENTS.md convention (agents.md).

## What this repo is

The lean install surface for the Nika agent plugin — Claude Code and
Codex marketplaces both point here. It carries three things: the plugin
manifests (`.claude-plugin/` · the `.agents/` plugin tree), the
`nika-authoring` skill, and the MCP wiring for the read-only oracle.

## The ONE law — the mirror is never hand-edited

The plugin content under `.agents/plugins/nika/` is a **byte-identical
mirror of the engine repo** (`supernovae-st/nika`, same paths, `main`).
CI diffs every mirrored file against engine main on push, PR, and a
daily cron; the nightly engine coherence bot watches it too.

- Found a wording bug in `SKILL.md` here? **Fix it in the engine repo**
  (`.agents/plugins/nika/skills/nika-authoring/SKILL.md`), merge there,
  then copy the merged bytes here. A hand-edit on this side goes RED
  within 24 hours and reads as drift, not as a fix.
- Only the marketplace-specific files are owned here: the manifests,
  `README.md`, `scripts/`, the gate workflow, and this file.

## Load-bearing facts (verify in-repo · never from memory)

- The three plugin manifests MUST agree on one version (gate-checked).
- The README's advertised `nika_*` tool names MUST equal what the
  pinned `nika mcp` binary actually serves — asserted by
  `scripts/check-mcp-tools.py` against the live wire, never a
  remembered count.
- Counts live in the engine/spec canon; prose here stays count-free or
  gate-checked.

## Verify before any PR

```sh
python3 scripts/check-mcp-tools.py   # NIKA_BIN=… locally
# the byte-parity + manifest gates run in CI (.github/workflows/gate.yml)
```
