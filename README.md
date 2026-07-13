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

**Teach your agent to hand repeatable work to [Nika](https://github.com/supernovae-st/nika):
a plain-text workflow it can check before a token is spent and verify
after.** This repo is the install surface: 4 skills (author · debug ·
operate · migrate), 3 subagents, 5 commands (`/nika:check` ·
`/nika:explain` · `/nika:new` · `/nika:trace` · `/nika:permits`),
3 hooks and the read-only MCP oracle (9 tools: `nika_check` ·
`nika_explain` · `nika_schema` · `nika_examples` · `nika_template` ·
`nika_canon` · `nika_catalog` · `nika_tools` · `nika_inspect`), for the plugin
ecosystems:

```sh
brew install supernovae-st/tap/nika   # the binary first; plugins invoke it

# Codex
codex plugin marketplace add supernovae-st/nika-agents
codex plugin add nika@nika
codex plugin marketplace upgrade nika   # later: pull a new kit version
                                        # (the per-version cache refreshes on the next run)

# Claude Code · updating is TWO rungs (proven live: an install sat 3 releases
# behind, silently, with a fresh clone right next to it):
claude plugin marketplace add supernovae-st/nika-agents
claude plugin install nika@nika
claude plugin marketplace update nika   # rung 1: refresh the CLONE
claude plugin update nika@nika          # rung 2: move the INSTALL, then restart

# Or climb every rung on every surface you have (Cursor · Claude Code ·
# Codex), one gesture · and `--check` reports drift read-only (CI-able):
scripts/update-mirrors.sh

# Cursor · search "nika" in the marketplace (Settings → Plugins), one Add
# installs the full bundle: rule + skill + subagent + commands + hooks + MCP.
# Or wire this repo as a team marketplace: Dashboard → Plugins → add
# supernovae-st/nika-agents
# (A manual drop into ~/.cursor/plugins/local/ loads MCP + skills ONLY —
# Cursor's local loader ignores the other components. Until the marketplace
# listing serves you: `nika init` equips the repo fully · rules · mcp ·
# the three subagents · delegation rule · the three seatbelt hooks, all
# project-side and byte-identical to this kit (engine ≥0.101).)

# Hermes, or any skills.sh-compatible client
hermes skills tap add supernovae-st/nika-agents      # then: hermes skills list
hermes skills install https://raw.githubusercontent.com/supernovae-st/nika-agents/main/skills/autonomous-ai-agents/nika/SKILL.md
# or: npx skills add supernovae-st/nika-agents
```

The Hermes-facing skill (`skills/autonomous-ai-agents/nika/SKILL.md` ·
agentskills.io shape) teaches the delegation idiom: Hermes orchestrates,
Nika runs the repeatable work as a checkable file with receipts: check
before run, budget caps on paid models, `trace verify` after.

Other install paths (script, manual download): [nika.sh](https://nika.sh).
One-click MCP wiring where the client supports it (binary still required):

[![Install in VS Code](https://img.shields.io/badge/VS_Code-install%20nika%20mcp-0098FF?logo=githubcopilot)](https://insiders.vscode.dev/redirect/mcp/install?name=nika&config=%7B%22command%22%3A%20%22nika%22%2C%20%22args%22%3A%20%5B%22mcp%22%5D%7D)
[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en/install-mcp?name=nika&config=eyJjb21tYW5kIjogIm5pa2EiLCAiYXJncyI6IFsibWNwIl19)

> 🗺️ **Every door in one page**: install paths, IDEs, agents, skills, MCP, CI, SDKs: [docs.nika.sh/integrations/everywhere](https://docs.nika.sh/integrations/everywhere).

## How the pieces fit (the three layers)

```
ENGINE  supernovae-st/nika              the source of truth
  ├─ .agents/plugins/nika/              THE plugin kit (skills · subagents ·
  │    3 manifests: claude · codex ·     commands · rules · hooks · MCP · logo)
  │    cursor                            · mirrored HERE, byte-pinned
  ├─ nika init                          per-REPO scaffold (AGENTS.md ·
  │                                      .cursor/{rules,mcp.json} · .vscode ·
  │                                      copilot brief · CLAUDE.md · skill)
  └─ nika wire <client>                 per-MACHINE wiring (cursor · zed ·
                                         cline · continue · claude · …)

THIS REPO  supernovae-st/nika-agents    the install surface (light clone —
                                         marketplaces clone their target)
   Claude Code · Codex · Cursor          the mirrored plugin, one Add each
   Hermes / skills.sh · opencode ·       kit-native integrations
   MCP registries (Glama · server.json)

nika-vscode  supernovae-st/nika-vscode  the IDE product (compiled extension:
                                         LSP · live DAG canvas · replay
                                         debugger · runs view · VS Code ·
                                         Cursor · Windsurf, one build)
```

Three mechanisms, no overlap: the **plugin** teaches any agent the
language (per-agent) · **`nika init`** equips one repository (per-repo)
· **`nika wire`** configures one machine's clients (per-machine). The
extension is not a plugin: it is the full IDE surface, and on Cursor it
nudges you to the plugin for the agent side.

## Why a separate repo

`plugin marketplace add` clones its target. The engine repo carries the full
Rust workspace and media; this repo carries the plugin only, so the install
is instant. The files are mirrored verbatim from the engine's
[`.agents/plugins/`](https://github.com/supernovae-st/nika/tree/main/.agents/plugins).
File issues and PRs against [supernovae-st/nika](https://github.com/supernovae-st/nika).

## What's inside

```
.agents/plugins/marketplace.json      Codex marketplace manifest
.agents/plugins/nika/                 the plugin (the full suite, one bundle)
  .codex-plugin/plugin.json           Codex manifest
  .claude-plugin/plugin.json          Claude Code manifest
  .cursor-plugin/plugin.json          Cursor manifest (logo + all components)
  skills/{nika-authoring,nika-debugging,nika-operating,nika-migration}/
                                      author · run forensics · day-2 ops · script porting
  agents/{nika-author,nika-debugger,nika-migrator}.md
                                      the three subagents (write · root-cause · port)
  commands/{check,explain,new,trace,permits}.md
                                      the /nika:* slash commands
  hooks/{cursor,claude}-hooks.json    the three seatbelts, one file per dialect:
                                      session map · check-on-edit · guard-run (a nika
                                      run must pass nika check · the deny teaches)
  rules/nika-workflow-language.mdc    the language rule (the init template, verbatim)
  rules/nika-delegation.mdc           WHEN to propose a workflow, WHICH surface to use
  assets/nika-logo.png                the marketplace logo
  .mcp.json                           the read-only oracle wiring
.claude-plugin/marketplace.json       Claude Code marketplace manifest
.cursor-plugin/marketplace.json       Cursor marketplace manifest
skills/autonomous-ai-agents/nika/     the Hermes delegation skill (kit-native)
integrations/opencode/                opencode wiring (live-verified · pinned)
integrations/mcp/                     generic MCP wiring + registry manifest + threat model
integrations/description-bank.md      the words every listing copies
mirror.json                           the drift contract (classes + pins)
```

You want to support Nika in your client? Copy the matching `integrations/`
folder. Each one is self-contained, version-pinned, and gate-checked
against the live binary.

Two content classes, one contract (`mirror.json`): **engine-mirror** files
are byte-identical projections of the engine repo, pinned by sha256 at the
engine SHA they were proven against: a pin mismatch means corruption (hard
fail), upstream movement means a re-sync is due (warning, loud on the daily
cron). **kit-native** files are owned here and proven against the latest
released binary instead: the gate asserts every taught `nika <subcommand>`
and every advertised `nika_*` tool actually ships.

Docs · https://docs.nika.sh/getting-started/agents · License ·
AGPL-3.0-or-later (mirrored engine content); per-file declarations win
where present (the Hermes delegation skill is MIT, the Hermes catalog norm).

<p align="center">
  <sub>Start from a template: <a href="https://github.com/supernovae-st/nika-starter">nika-starter</a> (authoring) · <a href="https://github.com/supernovae-st/nika-actions-starter">nika-actions-starter</a> (CI receipts)<br>
  Docs: <a href="https://docs.nika.sh">docs.nika.sh</a> · Engine (AGPL-3.0): <a href="https://github.com/supernovae-st/nika">nika</a> · 🦋 SuperNovae Studio · Paris</sub>
</p>
