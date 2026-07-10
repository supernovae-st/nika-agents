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

`nika wire <client>` writes the stanza for you where supported (cursor ·
vscode · windsurf · claude · codex · opencode · hermes — `wire all` does
the row); per-client pages with exact file paths:
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

## The read-only posture (why there is no run tool)

Inspection is safe to hand an agent; execution is not. The oracle answers
*is this valid · what will it cost · what is the syntax* — running stays on
the CLI, where `--max-cost-usd`, effect permits and the trace live. An agent
that wants to run a workflow shells out to `nika run` under your terminal's
permissions, visibly, like any other command you'd review.

Companions in this folder: [`server.json`](server.json) is the MCP Registry
manifest, publishable as-is — its `mcpb` package lanes point at the live
v0.98.0 release bundles with their real `fileSha256`; the npm lane behind
them is the future-revival shape, not a live package yet (install via
brew, the Dockerfile, or the bundles meanwhile);
[`THREAT-MODEL.md`](THREAT-MODEL.md) states plainly what the oracle and the
trace chain do and do not prove.
