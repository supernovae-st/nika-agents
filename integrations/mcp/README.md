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
vscode · windsurf · claude · codex — `wire all` does the row); per-client
pages with exact file paths: https://docs.nika.sh/reference/mcp-clients

## The read-only posture (why there is no run tool)

Inspection is safe to hand an agent; execution is not. The oracle answers
*is this valid · what will it cost · what is the syntax* — running stays on
the CLI, where `--max-cost-usd`, effect permits and the trace live. An agent
that wants to run a workflow shells out to `nika run` under your terminal's
permissions, visibly, like any other command you'd review.

Companions in this folder: [`server.json`](server.json) is the MCP Registry
manifest shape we publish from; [`THREAT-MODEL.md`](THREAT-MODEL.md) states
plainly what the oracle and the trace chain do and do not prove.
