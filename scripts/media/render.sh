#!/usr/bin/env bash
# render.sh — render a kit tape against the real released binary in a
# sandboxed HOME (/tmp/you). Sibling of the engine's render-tape.sh ·
# same honesty contract: every command is real, every line of output is
# the binary's own. Usage: bash scripts/media/render.sh [tape-name]
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
NAME="${1:-wire-all}"
TAPE="$ROOT/scripts/media/$NAME.tape"
[ -f "$TAPE" ] || { echo "no tape at $TAPE" >&2; exit 1; }
command -v vhs >/dev/null || { echo "vhs not installed (brew install vhs)" >&2; exit 1; }
command -v nika >/dev/null || { echo "nika not on PATH" >&2; exit 1; }

# The sandbox the tape's `export HOME=/tmp/you` enters: a fresh fake
# home + a git-initialized demo dir (welcome reads the workspace).
rm -rf /tmp/you
mkdir -p /tmp/you/demo
git -C /tmp/you/demo init -q -b main

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK" /tmp/you' EXIT
cp "$TAPE" "$WORK/$NAME.tape"
(cd "$WORK" && vhs "$NAME.tape")

mkdir -p "$ROOT/media"
OUT="$ROOT/media/$NAME.gif"
if command -v gifsicle >/dev/null; then
  gifsicle -O3 --lossy=40 "$WORK/$NAME.gif" -o "$OUT"
else
  cp "$WORK/$NAME.gif" "$OUT"
fi
SIZE_MB=$(du -m "$OUT" | cut -f1)
[ "$SIZE_MB" -le 8 ] || { echo "✖ $OUT is ${SIZE_MB}MB (budget 8MB)" >&2; exit 1; }
echo "→ $OUT (${SIZE_MB}MB · budget 8MB)"
