<!-- SPDX-License-Identifier: Apache-2.0 -->
# Threat model — the oracle & the trace chain

Plain statements, scoped to what the machinery proves. Nothing more.

## The oracle (`nika mcp`)

- **Read-only by design.** The tools validate, explain and teach; there is
  no execute/run tool over MCP. Execution requires the CLI.
- **Local stdio subprocess.** No listening port, no network egress of its
  own; it answers from the vendored spec and the workflow text a client
  passes it.
- **Tool outputs are data, not instructions.** A workflow file can contain
  hostile text; the oracle returns findings *about* it. Clients should
  treat everything inside a workflow as untrusted content.
- **No key values.** Provider keys are read by the CLI at run time; the
  oracle's answers never depend on, nor contain, a secret value.

## The trace chain (`nika trace verify`)

- **Tamper-evident, not producer-honest.** Each event links to the previous
  by sha256; editing a trace after the fact breaks the chain (exit 2). That
  proves the file was not altered since it was written — it does NOT prove
  the writer told the truth at write time. A malicious runner could log
  consistent lies; an honest chain from a trusted binary is the pairing
  that means something.
- **Costs are list-rate estimates.** Uncataloged models meter as $0 and are
  flagged as unpriced, never silently priced.

## What never happens

- No telemetry — neither surface phones home.
- No secret leaves your machine through the oracle.
- No workflow executes because an agent asked politely over MCP.
