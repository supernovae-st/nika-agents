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
operate · migrate), 3 subagents, 6 commands (`/nika:check` ·
`/nika:explain` · `/nika:new` · `/nika:trace` · `/nika:permits` ·
`/nika:doctor`), 3 hooks and the read-only MCP oracle (9 tools: `nika_check` ·
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

# Or climb every rung on every surface you have (binary · Cursor ·
# Claude Code · Codex), one gesture — the nika binary itself is lifted
# when it lags the kit's release train · and `--check` reports drift
# read-only (CI-able), reading BOTH rungs per client: the marketplace
# clone AND the install the sessions actually load (claude:
# installed_plugins.json · codex: the per-version cache):
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

# OpenClaude · its plugin loader reads the Claude Code marketplace layout
# (.claude-plugin/marketplace.json), so this kit installs unported:
npm install -g @gitlawb/openclaude
openclaude plugin marketplace add supernovae-st/nika-agents
openclaude plugin install nika@nika

# Grok Build · reads the Claude Code kit natively (marketplace · skills ·
# subagents · commands · hooks · MCP), so this kit installs unported ·
# verified live (grok 0.2.117 · full detail: integrations/grok-build/).
# On a machine already running the Claude Code plugin, grok picks it up
# with zero configuration. Trust is load-bearing: hooks + MCP stay
# inactive without it.
grok plugin marketplace add supernovae-st/nika-agents
grok plugin install nika@nika --trust

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

![nika check audits the workflow (plan, permits, cost, secrets, types, the lethal-trifecta gate), then nika run executes it locally and seals the hash-chained trace — the audit-then-run story](https://raw.githubusercontent.com/supernovae-st/nika/main/media/nika-hero.gif)

<!-- city:map -->
## The city · where this repo sits

```
📜 nika-spec ──── the civil code · the law tables, the corpus, the exam
    │ sync-pack: byte-gated mirror        │ projectors: drift-gated
    ▼                                     ▼
⚙️ nika ───────── the engine + the catalog (the yellow pages)
    │ the release train                  🖥️ nika.sh · 📖 nika-docs
    ▼                                     the showroom · the manual
📦 homebrew-tap · npm · Docker ── the docks
🔌 nika-client · 🎨 nika-vscode · 🤖 nika-agents · ⚡ gh-nika ── the doors   ◀── you are here
🏭 nika-action · 🧪 nika-actions-starter ── the CI district
🏪 nika-registry ── the market · 🏛 nika-estate ── the land registry
```

**This building** · THE AI KIT · agents learn the language here (the authoring skill · the MCP oracle · commands).

**Root** · neither · this building teaches the LANGUAGE. Its corpus is a sha256-pinned mirror of nika-spec and its commands are probed against the released engine · nothing authoritative is typed here.

**Consumes** · the engine's `.agents/plugins/` (mirrored byte-pinned · the heal follows the release train).

**Serves** · Claude Code · Codex · Cursor sessions, one Add each.

**Truth lives** · everything here is a MIRROR · file issues and PRs against the engine.

All the buildings: [nika-spec](https://github.com/supernovae-st/nika-spec) · [nika](https://github.com/supernovae-st/nika) · [nika.sh](https://github.com/supernovae-st/nika.sh) · [nika-docs](https://github.com/supernovae-st/nika-docs) · [nika-client](https://github.com/supernovae-st/nika-client) · [nika-vscode](https://github.com/supernovae-st/nika-vscode) · [nika-agents](https://github.com/supernovae-st/nika-agents) · [gh-nika](https://github.com/supernovae-st/gh-nika) · [homebrew-tap](https://github.com/supernovae-st/homebrew-tap) · [nika-action](https://github.com/supernovae-st/nika-action) · [nika-actions-starter](https://github.com/supernovae-st/nika-actions-starter) · [nika-registry](https://github.com/supernovae-st/nika-registry) · [nika-estate](https://github.com/supernovae-st/nika-estate)

Every fact has one home · everything else is a gated projection.
The living map: [nika.sh/map](https://nika.sh/map).
<!-- /city:map -->

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
  commands/{check,explain,new,trace,permits,doctor}.md
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
integrations/openclaude/              OpenClaude · plugin path + Skill Hub dossier
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
  <sub>Start from a template: <a href="https://github.com/supernovae-st/nika-actions-starter">nika-actions-starter</a> (workflow + editor wiring + CI receipts)<br>
  Docs: <a href="https://docs.nika.sh">docs.nika.sh</a> · Engine (AGPL-3.0): <a href="https://github.com/supernovae-st/nika">nika</a> · 🦋 SuperNovae Studio · Paris</sub>
</p>
