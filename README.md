# nika-agents · the Nika plugin marketplace

The lean install surface for the [Nika](https://github.com/supernovae-st/nika)
agent plugin — the `nika-authoring` skill (author → check → repair loop) and
the read-only MCP oracle (`nika_check` + `nika_explain`), for both plugin
ecosystems:

```sh
# Codex
codex plugin marketplace add supernovae-st/nika-agents
codex plugin add nika@nika

# Claude Code
claude plugin marketplace add supernovae-st/nika-agents
claude plugin install nika@nika
```

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
```

Docs · https://docs.nika.sh/getting-started/agents · License · AGPL-3.0-or-later

🦋 SuperNovae Studio · Paris
