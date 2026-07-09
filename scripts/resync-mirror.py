#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
#
# resync-mirror.py — the re-sync ritual as one command. When the daily cron
# goes loud ("engine main moved past the pins"), run this: it fetches every
# engine-mirror file from engine main, rewrites the local bytes, recomputes
# the sha256 pins, and stamps the engine SHA the sync was proven against.
# Review the diff, commit. Never hand-edit a mirrored file or a pin.
#
#   python3 scripts/resync-mirror.py          # sync + re-pin
#   python3 scripts/resync-mirror.py --dry    # show what would change

import hashlib
import json
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = "https://raw.githubusercontent.com/{repo}/main/{path}"
API = "https://api.github.com/repos/{repo}/commits/main"


def fetch(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=30) as r:
        return r.read()


def main() -> int:
    dry = "--dry" in sys.argv
    manifest_path = ROOT / "mirror.json"
    manifest = json.loads(manifest_path.read_text())
    repo = manifest["engine_repo"]

    head = json.loads(fetch(API.format(repo=repo)))["sha"]
    changed = 0
    for e in manifest["entries"]:
        if e["class"] != "engine-mirror":
            continue
        upstream = fetch(RAW.format(repo=repo, path=e["path"]))
        digest = hashlib.sha256(upstream).hexdigest()
        local = ROOT / e["path"]
        same_bytes = local.is_file() and local.read_bytes() == upstream
        same_pin = e["sha256"] == digest
        if same_bytes and same_pin:
            print(f"  = {e['path']}")
            continue
        changed += 1
        print(f"  ~ {e['path']}  pin {e['sha256'][:9]} → {digest[:9]}"
              f"{'' if same_bytes else '  (bytes updated)'}")
        if not dry:
            local.parent.mkdir(parents=True, exist_ok=True)
            local.write_bytes(upstream)
            e["sha256"] = digest
    if changed and not dry:
        manifest["synced_at_engine_sha"] = head
        manifest_path.write_text(json.dumps(manifest, indent=2,
                                            ensure_ascii=False) + "\n")
        print(f"re-pinned {changed} file(s) at engine {head[:9]} — review the "
              f"diff, then commit")
    elif changed:
        print(f"--dry: {changed} file(s) would re-sync (engine head {head[:9]})")
    else:
        print(f"mirror already current with engine {head[:9]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
