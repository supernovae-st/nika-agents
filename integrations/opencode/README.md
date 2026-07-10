<!-- SPDX-License-Identifier: Apache-2.0 -->
# opencode × Nika

Verified live 2026-07-09 · opencode 1.17.5 · nika 0.98.0.

[opencode](https://opencode.ai) reads `AGENTS.md` natively — so the project
scaffold IS the integration:

```sh
nika init    # writes AGENTS.md + editor rules + the authoring skill
```

That one command teaches any opencode session the house law: author →
`nika check` → run budget-capped → `nika trace verify`. Division of labor:
opencode writes code; Nika runs the repeatable work as a checkable file
with receipts.

## The MCP oracle (optional)

For schema/validation answers without shell round-trips, add the read-only
oracle to `opencode.json` at the project root — `nika wire opencode` writes
it for you (0.99+), or copy [`opencode.json`](opencode.json) from this
folder:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "nika": {
      "type": "local",
      "command": ["nika", "mcp"],
      "enabled": true
    }
  }
}
```

Two facts we verified live so you don't have to:

- **opencode prefixes MCP tool names with the server key** — in-session the
  oracle's tools appear as `nika_nika_check`, `nika_nika_explain`, … A prompt
  that says "call `nika_check`" verbatim will miss; say "the nika tools".
- **The deterministic check is `opencode mcp list`** → `✓ nika connected`.
  Trust that line, not a model's enumeration — small local models can invent
  tool names instead of reading them.

The oracle validates and teaches; running workflows stays on the terminal,
where `--max-cost-usd`, effect permits and the trace live.
