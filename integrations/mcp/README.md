<!-- SPDX-License-Identifier: Apache-2.0 -->
# Wiring the Nika MCP oracle (any client)

The engine serves a read-only MCP oracle over stdio: agents validate
workflows and learn the language without executing anything. One stanza,
every client:

```yaml
# YAML-config clients (hermes, …)
mcp_servers:
  nika:
    command: nika
    args: [mcp]
    timeout: 120
```

```json
{ "mcpServers": { "nika": { "command": "nika", "args": ["mcp"] } } }
```

`nika wire <client>` writes the stanza for you where supported — at 0.106.0
the targets are cursor · vscode · windsurf · claude · claude-desktop · cline
· codex · continue · zed · opencode · hermes · gemini · qwen · lmstudio ·
junie, and `wire all` does the row. `nika wire --help` prints the live list;
per-client pages with exact file paths:
https://docs.nika.sh/integrations/mcp-clients

Docker hosts (directory checkers, sandboxed runners): [`Dockerfile`](Dockerfile)
builds the oracle from the release artifacts (SHA256SUMS-verified, multi-arch
amd64/arm64) — `docker build -t nika-mcp . && docker run -i --rm nika-mcp`
speaks stdio JSON-RPC, introspection-probed in-container.

MCPB hosts (one-click bundle installers, Smithery-class): every engine
release ships `.mcpb` bundles — `nika-mcp-<platform>-<version>.mcpb` next
to the tarballs, checksums in `MCPB.sha256`. `manifest_version 0.2`,
`server.type binary`, entry point `server/nika` with `args: [mcp]` — the
same oracle, zero runtime dependencies, probed from the unpacked bundle
before publish.

## What the oracle serves

Nine tools over `tools/list`, re-asserted against the live wire on every
gate run (`scripts/check-mcp-tools.py` asks the binary, never a remembered
list):

| Tool | Answers |
|---|---|
| `nika_check` | is this workflow valid — the same audit as the CLI |
| `nika_inspect` | its anatomy: tasks · verbs · waves · cost · permits |
| `nika_explain` | one `NIKA-XXXX` code: cause · category · fix-form |
| `nika_schema` | the envelope JSON Schema (thirteen keys · closed) |
| `nika_examples` | the embedded example set |
| `nika_template` | a template skeleton to start from |
| `nika_canon` | the canonical registry (verbs · builtins · providers) |
| `nika_catalog` | provider/model ids · capabilities · required env vars |
| `nika_tools` | the builtins an `invoke` reaches without any MCP server |

`initialize` advertises the `tools` capability and nothing else at 0.106.0:
`prompts/list` answers `-32601 method not found`. So the five `/nika:*`
slash commands do **not** arrive over MCP — they come from the plugin
manifests, in the clients that read one. Wire the oracle for validation;
install the plugin for the commands. Probe it yourself in one line:

```sh
printf '%s\n' \
  '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"probe","version":"1"}}}' \
  '{"jsonrpc":"2.0","method":"notifications/initialized"}' \
  '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}' | nika mcp
```

## The read-only posture (why there is no run tool)

Inspection is safe to hand an agent; execution is not. The oracle answers
*is this valid · what will it cost · what is the syntax* — running stays on
the CLI, where `--max-cost-usd`, effect permits and the trace live. An agent
that wants to run a workflow shells out to `nika run` under your terminal's
permissions, visibly, like any other command you'd review.

Companions in this folder: [`server.json`](server.json) is the MCP Registry
manifest, publishable as-is — its `mcpb` package lanes point at the live
0.99.0 release bundles with their real `fileSha256` (bump both at the
MCP-Registry submission); the npm lane behind
them is the future-revival shape, not a live package yet (install via
brew, the Dockerfile, or the bundles meanwhile);
[`THREAT-MODEL.md`](THREAT-MODEL.md) states plainly what the oracle and the
trace chain do and do not prove.
