<p align="center">
  <a href="https://nika.sh">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="media/hero-dark.svg">
      <img src="media/hero-light.svg" alt="nika-agents · the Nika plugin marketplace · one Add teaches your agent the language" width="100%">
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://github.com/supernovae-st/nika-agents/actions/workflows/gate.yml"><img src="https://github.com/supernovae-st/nika-agents/actions/workflows/gate.yml/badge.svg" alt="gate"></a>
  <a href="https://github.com/supernovae-st/nika/releases/latest"><img src="https://img.shields.io/github/v/release/supernovae-st/nika?label=engine&color=ff7a3c" alt="engine release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/supernovae-st/nika-agents?color=5b8cff&label=license" alt="license"></a>
  <a href="https://skills.sh/supernovae-st/nika-agents"><img src="https://skills.sh/b/supernovae-st/nika-agents" alt="skills.sh"></a>
</p>

<h1 align="center">One Add · your agent learns the language</h1>

<p align="center"><b>Teach your agent to hand repeatable work to
<a href="https://github.com/supernovae-st/nika">Nika</a>: a plain-text
workflow it can check before a token is spent and verify after.</b><br>
One Add installs the whole suite: 4 skills · 3 subagents · 6 slash commands
· 3 hooks · the read-only MCP oracle (9 tools: <code>nika_check</code> ·
<code>nika_explain</code> · <code>nika_schema</code> · <code>nika_examples</code> ·
<code>nika_template</code> · <code>nika_canon</code> · <code>nika_catalog</code> ·
<code>nika_tools</code> · <code>nika_inspect</code>).</p>

![A fresh machine: nika wire all previews the MCP config for every agent client, one confirmation applies the sweep, then nika welcome confirms every editor wired, local models first, zero keys needed · the one-command wiring story, recorded against the released binary](media/wire-all.gif)

## Pick your door

The binary first, everywhere ([other paths](https://nika.sh)):

```sh
brew install supernovae-st/tap/nika
```

Then one Add for your client:

<p align="center">
  <a href="#claude-code"><img src="https://img.shields.io/badge/Claude_Code-ff7a3c?style=for-the-badge" alt="Claude Code"></a>
  <a href="#codex"><img src="https://img.shields.io/badge/Codex-5b8cff?style=for-the-badge" alt="Codex"></a>
  <a href="#grok-build"><img src="https://img.shields.io/badge/Grok_Build-22d3ee?style=for-the-badge" alt="Grok Build"></a>
  <a href="#openclaude"><img src="https://img.shields.io/badge/OpenClaude-b07bff?style=for-the-badge" alt="OpenClaude"></a>
  <a href="#hermes-or-any-skillssh-client"><img src="https://img.shields.io/badge/Hermes-9fd0ff?style=for-the-badge" alt="Hermes"></a>
  <a href="#cursor"><img src="https://img.shields.io/badge/Cursor-0a1226?style=for-the-badge" alt="Cursor"></a>
  <a href="#everyone-else"><img src="https://img.shields.io/badge/30%2B_more-5a6d8a?style=for-the-badge" alt="30+ more"></a>
</p>

### Claude Code

```sh
claude plugin marketplace add supernovae-st/nika-agents
claude plugin install nika@nika
```

Updating is TWO rungs: marketplace first, plugin second, restart after.

### Codex

```sh
codex plugin marketplace add supernovae-st/nika-agents
codex plugin add nika@nika
```

<sub>The per-version cache refreshes on your next run.</sub>

### Grok Build

```sh
grok plugin marketplace add supernovae-st/nika-agents
grok plugin install nika@nika --trust
```

<sub>Reads the Claude Code kit natively; <code>--trust</code> activates hooks + MCP.</sub>

### OpenClaude

```sh
openclaude plugin marketplace add supernovae-st/nika-agents
openclaude plugin install nika@nika
```

<sub>Its loader reads the same marketplace layout, unported.</sub>

### Hermes, or any skills.sh client

```sh
npx skills add supernovae-st/nika-agents
```

<sub>The kit-native skill pack, e2e-proven and listed live on
<a href="https://skills.sh/supernovae-st/nika-agents">skills.sh</a>.</sub>

### Cursor

Search "nika" in Settings → Plugins, one Add installs the full bundle (a
manual drop into `~/.cursor/plugins/local/` loads MCP + skills ONLY · until
the listing serves you, `nika init` equips the repo fully).

### Everyone else

opencode · Kimi Code · Gemini CLI · Zed · Cline · Copilot CLI · Amp · Warp ·
30+ clients: `nika init` equips the repo, `nika wire <client>` wires the
machine, and the read-only oracle rides any MCP client. Every door on one
page: [docs.nika.sh/integrations/everywhere](https://docs.nika.sh/integrations/everywhere).

### One-click doors

Where the client supports a one-click MCP install, one button wires the
read-only oracle — the oracle only: the full plugin still arrives through
your client's Add above (binary still required):

<p align="center">
  <a href="https://vscode.dev/redirect/mcp/install?name=nika&config=%7B%22command%22%3A%20%22nika%22%2C%20%22args%22%3A%20%5B%22mcp%22%5D%7D"><img src="https://img.shields.io/badge/VS_Code-install%20nika%20mcp-0098FF?style=for-the-badge&logo=githubcopilot" alt="Install in VS Code"></a>
  <a href="https://insiders.vscode.dev/redirect/mcp/install?name=nika&config=%7B%22command%22%3A%20%22nika%22%2C%20%22args%22%3A%20%5B%22mcp%22%5D%7D"><img src="https://img.shields.io/badge/VS_Code_Insiders-install%20nika%20mcp-24bfa5?style=for-the-badge&logo=githubcopilot" alt="Install in VS Code Insiders"></a>
  <a href="https://cursor.com/en/install-mcp?name=nika&config=eyJjb21tYW5kIjogIm5pa2EiLCAiYXJncyI6IFsibWNwIl19"><img src="https://cursor.com/deeplink/mcp-install-dark.svg" alt="Install MCP Server in Cursor"></a>
</p>

## Your first minute

Once installed, paste one of these into your agent:

> Turn this repeatable task into a checked Nika workflow.

> Validate this .nika.yaml file and repair every finding.

> Diagnose this failed Nika run from its trace.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="media/loop-dark.svg">
    <img src="media/loop-light.svg" alt="The loop: you describe the job in plain words, the agent writes the .nika.yaml, nika check audits it before a token is spent, nika run stays yours to type, nika trace verify seals the receipt · the file is the repeatable part" width="100%">
  </picture>
</p>

The plugin proposes the command; you type it. Spend is capped at the call
that would cross the cap, the effect boundary is declared in the file and
reviewable in a diff, and every run leaves a hash-chained trace you can
verify afterwards. Running stays yours:

![nika check audits the workflow (plan, permits, cost, secrets, types, the lethal-trifecta gate), then nika run executes it locally and seals the hash-chained trace · the audit-then-run story](https://raw.githubusercontent.com/supernovae-st/nika/main/media/nika-hero.gif)

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

<sub>Listed across the ecosystem:
<a href="https://skills.sh/supernovae-st/nika-agents">skills.sh</a> ·
<a href="https://claudepluginhub.com">ClaudePluginHub</a> ·
<a href="https://github.com/davila7/claude-code-templates">aitmpl.com</a> ·
<a href="https://crates.io/crates/nika">crates.io</a> ·
<a href="https://github.com/SchemaStore/schemastore">SchemaStore</a> (<code>*.nika.yaml</code> in every IDE) ·
<a href="https://www.libhunt.com/r/nika">LibHunt</a> ·
<a href="https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/supernovae-st/nika">Software Heritage</a>
· every submission lives in <a href="listings.yaml"><code>listings.yaml</code></a>, verified on a cadence.</sub>

## Keeping the suite fresh

The binary moved and a kit stayed behind? One command names it:

```sh
nika doctor    # reads what each client actually loads · names any kit
               # lagging the binary's train · prints the exact per-client fix
```

Every surface invokes the binary and the plugin kits ride its release train,
but no surface updates another: brew never touches a plugin, a marketplace
never touches the binary. The gestures, per surface:

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="media/update-rungs-dark.svg">
    <img src="media/update-rungs-light.svg" alt="Updating: brew upgrade nika for the binary · then the two rungs for the Claude Code plugin: marketplace update, plugin update, restart" width="100%">
  </picture>
</p>

| Surface | Update gesture |
|---|---|
| Binary | `brew upgrade nika` |
| Claude Code plugin | `claude plugin marketplace update nika` **then** `claude plugin update nika@nika` (two rungs · restart after) |
| Codex plugin | `codex plugin marketplace upgrade nika` |
| Cursor plugin | Settings → Plugins → nika (the listing serves the current train) |
| Every surface at once (maintainers) | `scripts/update-mirrors.sh` (`--check` reports drift read-only, CI-able) |

Drift is advisory (`nika doctor` warns · exit 0) and every fix line it
prints is copy-paste ready.

## How the pieces fit (the three layers)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="media/layers-dark.svg">
    <img src="media/layers-light.svg" alt="Three layers: the engine supernovae-st/nika is the source of truth, mirrored byte-pinned into this repo, one Add per client · nika init equips one repository · nika wire wires one machine · nika-vscode is the IDE product, not a plugin" width="100%">
  </picture>
</p>

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

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="media/suite-dark.svg">
    <img src="media/suite-light.svg" alt="One Add installs the whole suite: 4 skills, 3 subagents, 6 commands, 3 hooks and the read-only oracle" width="100%">
  </picture>
</p>

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
