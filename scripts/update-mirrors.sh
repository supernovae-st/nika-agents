#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
#
# update-mirrors.sh — every installed nika-kit surface, one gesture.
#
# The staleness ladder is per-client and easy to half-climb (a Claude Code
# install once sat THREE releases behind, silently, with a fresh clone right
# next to it — the clone had updated, the install had not). This script
# climbs every rung on every surface it finds, and says what it did:
#
#   Cursor       ~/.cursor/plugins/local/nika        rsync from this repo
#   Claude Code  marketplace clone + install         BOTH rungs + restart note
#   Codex        marketplace clone (per-version cache refreshes on next run)
#
#   scripts/update-mirrors.sh            # update every surface found
#   scripts/update-mirrors.sh --check    # read-only: report drift, exit 1 if any
#
# A surface that is absent is skipped with a note, never an error — the
# script serves laptops with one client as well as the full triple.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
KIT="$ROOT/.agents/plugins/nika"
CHECK=0
[[ "${1:-}" == "--check" ]] && CHECK=1

repo_version="$(python3 -c "import json;print(json.load(open('$KIT/.claude-plugin/plugin.json'))['version'])")"
echo "kit at this checkout: $repo_version"
drift=0

surface_version() { # $1 = plugin.json path
  [[ -f "$1" ]] && python3 -c "import json;print(json.load(open('$1'))['version'])" 2>/dev/null || echo absent
}

# ── Cursor (local plugin dir · rsync is the only writer) ──────────────
CURSOR_DIR="$HOME/.cursor/plugins/local/nika"
v="$(surface_version "$CURSOR_DIR/.claude-plugin/plugin.json")"
if [[ "$v" == absent ]]; then
  echo "· cursor: no local plugin — skipped (marketplace installs self-manage)"
elif [[ "$v" == "$repo_version" && $CHECK -eq 1 ]]; then
  echo "✔ cursor: $v"
elif [[ $CHECK -eq 1 ]]; then
  echo "✖ cursor: $v (repo has $repo_version)"; drift=1
else
  rsync -a --delete "$KIT/" "$CURSOR_DIR/"
  chmod +x "$CURSOR_DIR"/scripts/*.sh 2>/dev/null || true
  echo "✔ cursor: $v → $(surface_version "$CURSOR_DIR/.claude-plugin/plugin.json")"
fi

# ── Claude Code (TWO rungs: the clone, then the install) ──────────────
if command -v claude >/dev/null 2>&1; then
  CLAUDE_CLONE="$HOME/.claude/plugins/marketplaces/nika/.agents/plugins/nika/.claude-plugin/plugin.json"
  v="$(surface_version "$CLAUDE_CLONE")"
  if [[ "$v" == absent ]]; then
    echo "· claude: plugin not installed — skipped (claude plugin install nika@nika)"
  elif [[ "$v" == "$repo_version" && $CHECK -eq 1 ]]; then
    echo "✔ claude: $v (clone; the INSTALL may still lag — rung 2 is not probeable read-only)"
  elif [[ $CHECK -eq 1 ]]; then
    echo "✖ claude: clone at $v (repo has $repo_version)"; drift=1
  else
    claude plugin marketplace update nika >/dev/null 2>&1 || true       # rung 1: the clone
    out="$(claude plugin update nika@nika 2>&1 | tail -1 || true)"      # rung 2: the install
    echo "✔ claude: $out"
  fi
else
  echo "· claude: CLI absent — skipped"
fi

# ── Codex (one rung: the clone; per-version cache follows on next run) ─
if command -v codex >/dev/null 2>&1; then
  CODEX_CLONE="$HOME/.codex/.tmp/marketplaces/nika/.agents/plugins/nika/.claude-plugin/plugin.json"
  v="$(surface_version "$CODEX_CLONE")"
  if [[ "$v" == absent ]]; then
    echo "· codex: plugin not installed — skipped (codex plugin add nika@nika)"
  elif [[ "$v" == "$repo_version" && $CHECK -eq 1 ]]; then
    echo "✔ codex: $v"
  elif [[ $CHECK -eq 1 ]]; then
    echo "✖ codex: $v (repo has $repo_version)"; drift=1
  else
    codex plugin marketplace upgrade nika >/dev/null 2>&1 || true
    echo "✔ codex: $v → $(surface_version "$CODEX_CLONE") (cache refreshes on next run)"
  fi
else
  echo "· codex: CLI absent — skipped"
fi

if [[ $CHECK -eq 1 ]]; then
  if [[ $drift -eq 0 ]]; then
    echo "no drift"
  else
    echo "drift detected — run scripts/update-mirrors.sh"
    exit 1
  fi
fi
