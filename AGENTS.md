# AGENTS.md — nika-agents (the plugin marketplace mirror)

Vendor-neutral agent entry per the AGENTS.md convention (agents.md).

## What this repo is

The lean install surface for the Nika agent plugin — Claude Code and
Codex marketplaces both point here. It carries three things: the plugin
manifests (`.claude-plugin/` · the `.agents/` plugin tree), the
`nika-authoring` skill, and the MCP wiring for the read-only oracle.

## The ONE law — mirror.json is the drift contract

Every content file belongs to one of two classes, declared in
`mirror.json` (the SSOT the gate loops over — never a hardcoded list):

- **engine-mirror** (`.agents/plugins/nika/**`) — a **byte-identical
  mirror of the engine repo** (`supernovae-st/nika`, same paths, `main`),
  pinned by sha256 at the engine SHA it was proven against. Found a
  wording bug in the authoring `SKILL.md`? **Fix it in the engine repo**,
  merge there, then re-sync the bytes AND the pins here. A hand-edit on
  this side is a pin mismatch → hard RED (corruption signal). Engine main
  moving past the pins is a WARNING on PRs and a loud failure on the
  daily cron (re-sync signal) — two different signals, never conflated.
- **kit-native** (`skills/**` — the Hermes delegation skill ·
  `integrations/**` — the per-client wiring packs) — owned HERE, not
  mirrored. Its proof is the released binary: the gate asserts every
  `nika <subcommand>` it teaches ships in the latest release
  (`scripts/check-skill-commands.py`) and every advertised `nika_*` tool
  is served over the wire (`scripts/check-mcp-tools.py`).

Marketplace-specific files owned here: the manifests, `README.md`,
`scripts/`, the gate workflow, `mirror.json`, `listings.yaml` (every
external listing/submission registers there — pinned description from the
bank · cadence class · kill criterion >60d), and this file.

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
python3 scripts/check-mcp-tools.py        # NIKA_BIN=… locally
python3 scripts/check-skill-commands.py   # kit-native skills vs the binary
# pins + upstream + manifest gates run in CI (.github/workflows/gate.yml)
```
