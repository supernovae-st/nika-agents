#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
#
# resync-mirror.py — the re-sync ritual as one command. When the daily cron
# goes loud ("engine main moved past the pins"), run this: it fetches every
# engine-mirror file from engine main, rewrites the local bytes, recomputes
# the sha256 pins, and stamps the engine SHA the sync was proven against.
# Review the diff, commit. Never hand-edit a mirrored file or a pin.
#
#   python3 scripts/resync-mirror.py                 # network sync + re-pin
#   python3 scripts/resync-mirror.py --dry           # show what would change
#   python3 scripts/resync-mirror.py --engine <dir>  # sync from a local clone
#   NIKA_ENGINE_CLONE=<dir> python3 scripts/resync-mirror.py   # same, via env
#
# Resilience (each rule earned by a live failure, 2026-07-12):
# - A local clone is FETCHED before it is read (git fetch origin main) —
#   an unfetched clone pins pre-merge bytes and stamps a stale SHA, and
#   the versions-agree gate only catches it one CI round later.
# - The raw API rate-limits (HTTP 403/429) mid-run. With a local clone
#   available the script FALLS BACK to it automatically; without one it
#   names the exact remedy instead of dying half-synced.
# - Bytes and the stamped SHA always come from the SAME source.

import hashlib
import json
import os
import pathlib
import subprocess
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = "https://raw.githubusercontent.com/{repo}/main/{path}"
API = "https://api.github.com/repos/{repo}/commits/main"


class Source:
    """Where mirror bytes come from — network raw API or a fetched local clone."""

    def __init__(self, repo: str, clone: pathlib.Path | None):
        self.repo = repo
        self.clone = clone
        if clone is not None:
            self._fetch_clone()

    def _fetch_clone(self) -> None:
        # The stale-clone trap: reading origin/main without fetching pins
        # yesterday's bytes. Fetch is mandatory, not polite.
        r = subprocess.run(
            ["git", "-C", str(self.clone), "fetch", "--quiet", "origin", "main"],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            sys.exit(f"engine clone at {self.clone}: git fetch failed: {r.stderr.strip()}")

    @classmethod
    def resolve(cls, repo: str, argv: list[str]) -> "Source":
        clone = None
        if "--engine" in argv:
            clone = pathlib.Path(argv[argv.index("--engine") + 1])
        elif os.environ.get("NIKA_ENGINE_CLONE"):
            clone = pathlib.Path(os.environ["NIKA_ENGINE_CLONE"])
        if clone is not None and not (clone / ".git").exists():
            sys.exit(f"--engine {clone}: not a git clone")
        return cls(repo, clone)

    def head(self) -> str:
        if self.clone is not None:
            r = subprocess.run(
                ["git", "-C", str(self.clone), "rev-parse", "origin/main"],
                capture_output=True, text=True, check=True,
            )
            return r.stdout.strip()
        with urllib.request.urlopen(API.format(repo=self.repo), timeout=30) as resp:
            return json.loads(resp.read())["sha"]

    def read(self, path: str) -> bytes:
        if self.clone is not None:
            r = subprocess.run(
                ["git", "-C", str(self.clone), "show", f"origin/main:{path}"],
                capture_output=True,
            )
            if r.returncode != 0:
                sys.exit(f"engine clone: origin/main:{path} unreadable")
            return r.stdout
        with urllib.request.urlopen(RAW.format(repo=self.repo, path=path), timeout=30) as resp:
            return resp.read()

    def try_local_fallback(self) -> bool:
        """Rate-limited mid-run: switch to a discoverable clone if one exists."""
        for candidate in (
            os.environ.get("NIKA_ENGINE_CLONE"),
            str(ROOT.parent / "nika"),          # sibling checkout
        ):
            if candidate and (pathlib.Path(candidate) / ".git").exists():
                self.clone = pathlib.Path(candidate)
                self._fetch_clone()
                print(f"  ! raw API rate-limited — continuing from the local clone at {self.clone}")
                return True
        return False


def main() -> int:
    dry = "--dry" in sys.argv
    manifest_path = ROOT / "mirror.json"
    manifest = json.loads(manifest_path.read_text())
    # One canonical stamp field — a hand-rolled sync once wrote a stray
    # sibling key; drop any impostor so the manifest never carries two truths.
    manifest.pop("engine_sha", None)
    repo = manifest["engine_repo"]
    source = Source.resolve(repo, sys.argv)

    changed = 0
    for e in manifest["entries"]:
        if e["class"] != "engine-mirror":
            continue
        path = e.get("source", e["path"])
        try:
            upstream = source.read(path)
        except urllib.error.HTTPError as err:
            if err.code in (403, 429) and source.try_local_fallback():
                upstream = source.read(path)
            else:
                sys.exit(
                    f"raw API answered {err.code} on {path} and no local clone "
                    f"was found — re-run with --engine <path-to-nika-clone> "
                    f"(or set NIKA_ENGINE_CLONE)"
                )
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
            if str(local).endswith(".sh"):
                local.chmod(0o755)
            e["sha256"] = digest

    head = source.head()
    if changed and not dry:
        manifest["synced_at_engine_sha"] = head
        manifest_path.write_text(json.dumps(manifest, indent=2,
                                            ensure_ascii=False) + "\n")
        print(f"re-pinned {changed} file(s) at engine {head[:9]} — review the "
              f"diff, then commit")
    elif changed:
        print(f"--dry: {changed} file(s) would re-sync (engine head {head[:9]})")
    else:
        # A clean pass still heals a polluted stamp field.
        if not dry and json.loads(manifest_path.read_text()).get("engine_sha") is not None:
            manifest_path.write_text(json.dumps(manifest, indent=2,
                                                ensure_ascii=False) + "\n")
        print(f"mirror already current with engine {head[:9]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
