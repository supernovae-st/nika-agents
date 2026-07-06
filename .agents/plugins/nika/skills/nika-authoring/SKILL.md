---
name: nika-authoring
description: Author, check and repair Nika workflows (.nika.yaml files — the workflow language for AI). Use when writing or editing a *.nika.yaml file, converting a repeated AI task or prompt chain into a workflow, or when nika check reports NIKA-XXXX findings to fix.
---

# Authoring Nika workflows

Nika turns repeatable AI work into files: one `.nika.yaml`, four verbs,
audited **before** it runs. You author the file; `nika check` is the
oracle; the human runs it.

## The loop (always)

1. **Start from a template or example**, never from scratch:
   `nika examples list` · `nika examples show <slug>` ·
   `nika new --from <template> <file>.nika.yaml`
2. **Write the file.** Envelope is always `nika: v1` +
   `workflow: <kebab-id>` + `tasks:`.
3. **Check it**: `nika check <file>`. Exit 0 = clean · 2 = findings.
   `nika inspect <file>` shows the anatomy (tasks · waves · cost floor).
4. **Repair from the diagnostics** — they name the exact task, reference
   and fix. Unknown code? `nika explain NIKA-XXXX`.
5. Repeat 3–4 until clean. **Never hand a file to the human that does
   not pass `nika check`.**
6. The human (or CI) runs it: `nika run <file>`. Preview offline with
   `--model mock/echo` (the mock synthesizes schema-conformant output,
   so schema workflows preview offline too); run locally with
   `--model ollama/<model>`.
7. **Pin the contract**: `nika test <file> --update` writes
   `<file>.golden.json` (the typed outputs under the deterministic
   mock) — commit it; from then on `nika test <file>` is the offline CI
   gate (a red test = the output contract changed).

## The four verbs (exactly one per task)

- `infer:` — an LLM call (`prompt`, `schema?` for typed output,
  `max_tokens?`)
- `exec:` — a shell command (`command`, `capture: text|structured`)
- `invoke:` — a builtin or MCP tool (`tool`, `args`) · HTTP fetch is
  `tool: "nika:fetch"`, a tool, not a verb
- `agent:` — a bounded multi-turn loop (`prompt`, `tools` allowlist,
  `max_turns`, `max_tokens_total`)

## Discipline

- References: `${{ tasks.<id>.output }}` · `${{ vars.x }}` ·
  `${{ env.KEY }}` · `${{ secrets.X }}` (never inline a credential).
- A task that reads another task's output MUST declare it in
  `depends_on: [<id>]`.
- Models are `provider/name` (`ollama/llama3.2:3b` local-first ·
  `mock/echo` offline preview).
- Declare the blast radius: `nika check --infer-permits <file>` prints
  the tightest `permits:` block — paste it in (default-deny from then on).
- Structured output: give `infer:` a `schema:`; add
  `additionalProperties: false` for a deterministic shape.
- Vars at launch: declare `vars:` with `default:` for the zero-arg run;
  the human overrides with `nika run <file> --var key=value`
  (repeatable · unknown keys are refused before anything runs).
- Timeouts are quoted Go-durations (`timeout: "7m"`, never a bare
  number). Local models get a 300s provider deadline by default —
  thinking models legitimately exceed 30s.
- Long runs are resumable: `nika run <file> --resume <trace>` skips
  journaled successes (visible cache hits). A blocking `nika:prompt`
  pauses durably (exit 4) — re-arm with `--resume … --answer <task>=…`
  (confirm prompts take booleans: `approve=true`).
- Debugging a run: `nika trace show <.nika/traces/…ndjson>` renders the
  storyboard + waterfall; `nika explain NIKA-XXXX` teaches any code.
