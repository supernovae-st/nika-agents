<p align="center">
  <a href="https://nika.sh">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://nika.sh/brand/nika-logo-dark.svg">
      <img src="https://nika.sh/brand/nika-logo-light.svg" alt="Nika" width="220">
    </picture>
  </a>
</p>

# nika-agents · the Nika plugin marketplace

[![gate](https://github.com/supernovae-st/nika-agents/actions/workflows/gate.yml/badge.svg)](https://github.com/supernovae-st/nika-agents/actions/workflows/gate.yml)
[![skills.sh](https://skills.sh/b/supernovae-st/nika-agents)](https://skills.sh/supernovae-st/nika-agents)

The lean install surface for the [Nika](https://github.com/supernovae-st/nika)
agent plugin — the `nika-authoring` skill (author → check → repair loop) and
the read-only MCP oracle (8 tools: `nika_check` · `nika_explain` ·
`nika_schema` · `nika_examples` · `nika_template` · `nika_canon` ·
`nika_catalog` · `nika_tools`), for the plugin ecosystems:

```sh
# Codex
codex plugin marketplace add supernovae-st/nika-agents
codex plugin add nika@nika

# Claude Code
claude plugin marketplace add supernovae-st/nika-agents
claude plugin install nika@nika

# Hermes — or any skills.sh-compatible client
hermes skills tap add supernovae-st/nika-agents      # then: hermes skills list
hermes skills install https://raw.githubusercontent.com/supernovae-st/nika-agents/main/skills/autonomous-ai-agents/nika/SKILL.md
# or: npx skills add supernovae-st/nika-agents
```

The Hermes-facing skill (`skills/autonomous-ai-agents/nika/SKILL.md` ·
agentskills.io shape) teaches the delegation idiom: Hermes orchestrates,
Nika runs the repeatable work as a checkable file with receipts — check
before run, budget caps on paid models, `trace verify` after.

The plugin expects the `nika` binary on your PATH:

```sh
brew install supernovae-st/tap/nika    # or: curl -LsSf https://nika.sh/install.sh | sh
```

## Why a separate repo

`plugin marketplace add` clones its target. The engine repo carries the full
Rust workspace and media; this repo carries the plugin only, so the install
is instant. The files are mirrored verbatim from the engine's
[`.agents/plugins/`](https://github.com/supernovae-st/nika/tree/main/.agents/plugins)
— file issues and PRs against [supernovae-st/nika](https://github.com/supernovae-st/nika).

## What's inside

```
.agents/plugins/marketplace.json      Codex marketplace manifest
.agents/plugins/nika/                 the plugin (skill + MCP bundle)
  .codex-plugin/plugin.json           Codex manifest
  .claude-plugin/plugin.json          Claude Code manifest
  skills/nika-authoring/SKILL.md      the authoring skill (agentskills.io shape)
  .mcp.json                           the read-only oracle wiring
.claude-plugin/marketplace.json       Claude Code marketplace manifest
skills/autonomous-ai-agents/nika/     the Hermes delegation skill (kit-native)
mirror.json                           the drift contract (classes + pins)
```

Two content classes, one contract (`mirror.json`): **engine-mirror** files
are byte-identical projections of the engine repo, pinned by sha256 at the
engine SHA they were proven against — a pin mismatch means corruption (hard
fail), upstream movement means a re-sync is due (warning, loud on the daily
cron). **kit-native** files are owned here and proven against the latest
released binary instead: the gate asserts every taught `nika <subcommand>`
and every advertised `nika_*` tool actually ships.

Docs · https://docs.nika.sh/getting-started/agents · License ·
AGPL-3.0-or-later (mirrored engine content) — per-file declarations win
where present (the Hermes delegation skill is MIT, the Hermes catalog norm).

🦋 SuperNovae Studio · Paris
