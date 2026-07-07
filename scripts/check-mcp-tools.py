#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
#
# check-mcp-tools.py — the documented MCP tool set MUST equal what the binary
# serves. The marketplace README advertises "8 tools: nika_check · nika_explain
# · …"; those names are hand-written, so a future engine that adds or drops a
# tool would leave the marketplace lying. This asserts the README's `nika_*`
# names are exactly the tools `nika mcp` exposes over the wire — no drift, no
# stale count. Runs in CI after the pinned nika is installed; also runnable
# locally: NIKA_BIN=/path/to/nika python3 scripts/check-mcp-tools.py
#
# Exit 0 = README ⟺ binary agree. Exit 1 = drift (names printed).

import json
import os
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def documented_tools() -> set:
    """The `nika_*` tool names the marketplace README advertises."""
    readme = (ROOT / "README.md").read_text()
    return set(re.findall(r"nika_[a-z]+", readme))


def served_tools(nika: str) -> set:
    """The tool names `nika mcp` actually exposes (JSON-RPC tools/list)."""
    handshake = "\n".join(json.dumps(m) for m in [
        {"jsonrpc": "2.0", "id": 1, "method": "initialize",
         "params": {"protocolVersion": "2025-06-18", "capabilities": {},
                    "clientInfo": {"name": "gate", "version": "1"}}},
        {"jsonrpc": "2.0", "method": "notifications/initialized"},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}},
    ]) + "\n"
    out = subprocess.run([nika, "mcp"], input=handshake, text=True,
                         capture_output=True, timeout=30)
    for line in out.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        if msg.get("id") == 2 and "result" in msg:
            return {t["name"] for t in msg["result"].get("tools", [])}
    raise SystemExit("check-mcp-tools: no tools/list reply from `nika mcp` "
                     f"(stderr: {out.stderr.strip()[:160]})")


def main() -> int:
    nika = os.environ.get("NIKA_BIN") or shutil.which("nika")
    if not nika:
        print("check-mcp-tools: nika not on PATH — install it first", file=sys.stderr)
        return 1
    documented = documented_tools()
    served = served_tools(nika)
    if documented == served:
        print(f"✓ README ⟺ nika mcp agree · {len(served)} tools: "
              f"{' · '.join(sorted(served))}")
        return 0
    print("✗ MCP tool drift — the README and `nika mcp` disagree", file=sys.stderr)
    if missing := documented - served:
        print(f"  README claims, binary does NOT serve: {sorted(missing)}", file=sys.stderr)
    if extra := served - documented:
        print(f"  binary serves, README does NOT list: {sorted(extra)}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
