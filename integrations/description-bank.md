<!-- SPDX-License-Identifier: Apache-2.0 -->
# Description bank — the words every listing copies

One truth, three lengths per surface. Submissions (MCP directories, awesome
lists, marketplaces) copy from HERE — never improvise a description in a PR
form. Rules: name **verifiable capabilities** (check · cost floor · traces ·
receipts), never "AI workflow tool"; no counts (they drift — the gate checks
tool names against the live binary instead); local-first examples; the words
"standard", "framework", "blockchain" and "attested" do not appear.

## One line (≤160 chars — awesome lists, directory taglines)

> Nika — intent-as-code for AI workflows: author a reviewable DAG in YAML,
> audit cost/permits **before** running, keep tamper-evident traces after.

## Three lines (MCP directories, marketplace cards)

> Nika is a workflow language for AI — one file, four verbs, one Rust
> binary. Its MCP server is a read-only oracle: agents validate workflows
> (`nika_check`, `nika_explain`) and learn the language (schema, templates,
> examples, catalogs) without executing anything. Running stays on the CLI,
> budget-capped and trace-verified — inspect freely, execute deliberately.

## Ten lines (README sections, submission long-forms)

> Nika turns repeatable AI work into files you can run, review, diff and
> share. A workflow is a `.nika.yaml` DAG — LLM steps, shell steps, tool
> calls — statically checkable before a single token is spent: `nika check`
> audits the schema, the DAG, the cost floor (unpriced is never $0), the
> secret flows and the effect permits. Runs are budget-capped
> (`--max-cost-usd`) and leave a tamper-evident trace (`nika trace verify`).
> Agents meet it through the surfaces they already read: `AGENTS.md` and a
> repo skill (`nika init`), a read-only MCP oracle (`nika mcp`), and a
> GitHub Action that posts the plan with receipts on every PR. Local-first:
> the mock and Ollama paths need no API key. Engine AGPL-3.0-or-later ·
> spec and SDK Apache-2.0.

## Per-surface first lines (when the form asks "what is this?")

| surface | lead |
|---|---|
| MCP directories | the three-line block (the oracle IS the listing) |
| awesome-mcp lists | one line + `read-only oracle: validate + learn, no execution` |
| skills registries | `Author → check → repair loop for Nika workflows — teaches agents to write valid .nika.yaml, never invent syntax` |
| GitHub Action marketplace | `Plan with receipts: check verdict, honest cost floor, permits and the DAG on every PR — static, zero secrets` |
| Hermes/agent catalogs | `The deterministic workflow worker: Hermes orchestrates, Nika runs repeatable work budget-capped with verifiable receipts` |

Companion: `listings.yaml` (every live submission registers there with its
pinned description + cadence + kill criterion — see AGENTS.md).
