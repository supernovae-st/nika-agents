<p align="center">
  <a href="https://nika.sh">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://nika.sh/brand/nika-logo-dark.svg">
      <img src="https://nika.sh/brand/nika-logo-light.svg" alt="Nika" width="220">
    </picture>
  </a>
</p>

<h1 align="center">nika-agents · the Nika plugin marketplace</h1>

<p align="center">
  <a href="https://github.com/supernovae-st/nika-agents/actions/workflows/gate.yml"><img src="https://github.com/supernovae-st/nika-agents/actions/workflows/gate.yml/badge.svg" alt="gate"></a>
  <a href="https://skills.sh/supernovae-st/nika-agents"><img src="https://skills.sh/b/supernovae-st/nika-agents" alt="skills.sh"></a>
</p>

<p align="center"><b>Teach your agent to hand repeatable work to
<a href="https://github.com/supernovae-st/nika">Nika</a>: a plain-text
workflow it can check before a token is spent and verify after.</b><br>
One Add installs the whole suite: 4 skills · 3 subagents · 6 slash commands
· 3 hooks · the read-only MCP oracle (9 tools: <code>nika_check</code> ·
<code>nika_explain</code> · <code>nika_schema</code> · <code>nika_examples</code> ·
<code>nika_template</code> · <code>nika_canon</code> · <code>nika_catalog</code> ·
<code>nika_tools</code> · <code>nika_inspect</code>).</p>

![nika check audits the workflow (plan, permits, cost, secrets, types, the lethal-trifecta gate), then nika run executes it locally and seals the hash-chained trace · the audit-then-run story](https://raw.githubusercontent.com/supernovae-st/nika/main/media/nika-hero.gif)

## Pick your door

The binary first, everywhere: `brew install supernovae-st/tap/nika`
([other paths](https://nika.sh)). Then one Add for your client:

```sh
# Claude Code · updating is TWO rungs (clone, then install, then restart)
claude plugin marketplace add supernovae-st/nika-agents
claude plugin install nika@nika
```

```sh
# Codex · the per-version cache refreshes on your next run
codex plugin marketplace add supernovae-st/nika-agents
codex plugin add nika@nika
```

```sh
# Grok Build · reads the Claude Code kit natively; --trust activates hooks + MCP
grok plugin marketplace add supernovae-st/nika-agents
grok plugin install nika@nika --trust
```

```sh
# OpenClaude · its loader reads the same marketplace layout, unported
openclaude plugin marketplace add supernovae-st/nika-agents
openclaude plugin install nika@nika
```

```sh
# Hermes, or any skills.sh-compatible client
npx skills add supernovae-st/nika-agents
```

**Cursor** · search "nika" in Settings → Plugins, one Add installs the full
bundle. **Everyone else** (opencode · Kimi Code · Gemini CLI · Zed · Cline ·
Copilot CLI · Warp · 30+ clients): `nika init` equips the repo, `nika wire
<client>` wires the machine, and the read-only oracle rides any MCP client.
Every door on one page: [docs.nika.sh/integrations/everywhere](https://docs.nika.sh/integrations/everywhere).

## Your first minute

Once installed, paste one of these into your agent:

> Turn this repeatable task into a checked Nika workflow.

> Validate this .nika.yaml file and repair every finding.

> Diagnose this failed Nika run from its trace.

The plugin proposes the command; you type it. Spend is capped at the call
that would cross the cap, the effect boundary is declared in the file and
reviewable in a diff, and every run leaves a hash-chained trace you can
verify afterwards. Running stays yours.

## Proven where you work

Coverage is a machine-checked contract, not a claims list:
[`clients.yaml`](clients.yaml) tracks 31 clients across 9 component classes
(CI-gated both ways against the shipped binary). The proven rows, each with
a deterministic receipt:

| Client | The receipt |
|---|---|
| **Claude Code** | full suite loads in-session: skills · subagents · `/nika:*` · hooks · oracle |
| **Codex** | marketplace page live (interface block · try-now prompts) · plugin cache enabled |
| **Grok Build** | `grok inspect --json` lists every component with origins · `grok mcp doctor --json`: handshake OK, 9 tools ([fiche](integrations/grok-build/)) |
| **Kimi Code** | a stream-json run emits `tool_calls: mcp__nika__nika_canon` · the oracle loaded AND called ([fiche](integrations/kimi-code/)) |
| **opencode** | `opencode mcp list` → `✓ nika connected` ([fiche](integrations/opencode/)) |
| **Hermes / skills.sh** | e2e-proven skill pack, listed live ([skills.sh](https://skills.sh/supernovae-st/nika-agents)) |
| **Any MCP client** | the containerized oracle answers `initialize` + `tools/list` on every CI run ([integrations/mcp](integrations/mcp/)) |

One-click MCP wiring where the client supports it (binary still required):

[![Install in VS Code](https://img.shields.io/badge/VS_Code-install%20nika%20mcp-0098FF?logo=githubcopilot)](https://insiders.vscode.dev/redirect/mcp/install?name=nika&config=%7B%22command%22%3A%20%22nika%22%2C%20%22args%22%3A%20%5B%22mcp%22%5D%7D)
[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en/install-mcp?name=nika&config=eyJjb21tYW5kIjogIm5pa2EiLCAiYXJncyI6IFsibWNwIl19)

## Keeping the suite fresh

Every surface invokes the binary and the plugin kits ride its release train,
but no surface updates another: brew never touches a plugin, a marketplace
never touches the binary.

| Surface | Update gesture |
|---|---|
| Binary | `brew upgrade nika` |
| Claude Code plugin | `claude plugin marketplace update nika` **then** `claude plugin update nika@nika` (two rungs · restart after) |
| Codex plugin | `codex plugin marketplace upgrade nika` |
| Every surface at once | `scripts/update-mirrors.sh` (`--check` reports drift read-only, CI-able) |

`nika doctor` is the coherence oracle: it reads what each client actually
loads, names any kit lagging the binary's train, and prints the exact
per-client fix. Drift is advisory (warn · exit 0).

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
   Claude Code · Codex · Cursor ·        the mirrored plugin, one Add each
   Grok Build · OpenClaude
   Hermes / skills.sh · opencode ·       kit-native integrations
   Kimi Code · MCP registries

nika-vscode  supernovae-st/nika-vscode  the IDE product (compiled extension:
                                         LSP · live DAG canvas · replay
                                         debugger · runs view · VS Code ·
                                         Cursor · Windsurf, one build)
```

Three mechanisms, no overlap: the **plugin** teaches any agent the language
(per-agent) · **`nika init`** equips one repository (per-repo) · **`nika
wire`** configures one machine's clients (per-machine). The extension is not
a plugin: it is the full IDE surface, and on Cursor it nudges you to the
plugin for the agent side.

## Why a separate repo

`plugin marketplace add` clones its target. The engine repo carries the full
Rust workspace and media; this repo carries the plugin only, so the install
is instant. The files are mirrored verbatim from the engine's
[`.agents/plugins/`](https://github.com/supernovae-st/nika/tree/main/.agents/plugins).
File issues and PRs against [supernovae-st/nika](https://github.com/supernovae-st/nika).

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

**Serves** · Claude Code · Codex · Cursor · Grok Build sessions, one Add each (OpenClaude rides the same layout).

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
clients.yaml                          the client × component matrix (the coverage SSOT)
skills/autonomous-ai-agents/nika/     the Hermes delegation skill (kit-native)
integrations/{grok-build,kimi-code,opencode,openclaude,mcp}/
                                      per-client fiches · live-verified, version-pinned
integrations/description-bank.md      the words every listing copies
listings.yaml                         the public submissions ledger
mirror.json                           the drift contract (classes + pins)
```

Two content classes, one contract (`mirror.json`): **engine-mirror** files
are byte-identical projections of the engine repo, pinned by sha256 at the
engine SHA they were proven against: a pin mismatch means corruption (hard
fail), upstream movement means a re-sync is due. **kit-native** files are
owned here and proven against the latest released binary instead: the gate
asserts every taught `nika <subcommand>` and every advertised `nika_*` tool
actually ships. The oracle is read-only by design:
[threat model](integrations/mcp/THREAT-MODEL.md).

## Add your client · ask for a workflow

You want to support Nika in your client? Copy the matching
[`integrations/`](integrations/) folder: each one is self-contained,
version-pinned, and gate-checked against the live binary. Missing a
workflow for your use case?
[Ask for one](https://github.com/supernovae-st/nika-agents/issues/new?template=request-a-workflow.yml)
· the answer ships as a checked file, receipts included.

<p align="center">
  <sub>Start from a template: <a href="https://github.com/supernovae-st/nika-actions-starter">nika-actions-starter</a> (workflow + editor wiring + CI receipts)<br>
  Docs: <a href="https://docs.nika.sh">docs.nika.sh</a> · Engine (AGPL-3.0): <a href="https://github.com/supernovae-st/nika">nika</a> · 🦋 SuperNovae Studio · Paris</sub>
</p>
