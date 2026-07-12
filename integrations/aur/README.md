# AUR package — `nika-bin` (prepared · operator publishes)

The [AUR](https://aur.archlinux.org) accepts first-party packages; publishing
needs an AUR account + an SSH key (a separate account system — one-time
operator ceremony). `nika-bin` was free at preparation time (2026-07-11).

## One-time publish

```sh
# 1. Create the AUR account at https://aur.archlinux.org/register/
#    and add your SSH public key in the account settings.
# 2. Clone the (empty) package repo — cloning an unclaimed name claims it on push:
git clone ssh://aur@aur.archlinux.org/nika-bin.git && cd nika-bin
cp <this-dir>/PKGBUILD .
# 3. Generate .SRCINFO (on any machine with pacman, or via docker):
docker run --rm -v "$PWD:/pkg" -w /pkg archlinux:base-devel \
  bash -c "useradd -m b && chown -R b /pkg && su b -c 'makepkg --printsrcinfo'" > .SRCINFO
# 4. Sanity build (optional but recommended):
docker run --rm -v "$PWD:/pkg" -w /pkg archlinux:base-devel \
  bash -c "useradd -m b && chown -R b /pkg && pacman -Sy --noconfirm && su b -c 'makepkg -si --noconfirm'"
# 5. Push = publish:
git add PKGBUILD .SRCINFO && git commit -m "nika-bin 0.99.0" && git push
```

## Per-release refresh (agent-preparable)

Bump `pkgver`, refresh the two sha256 lines from the release `SHA256SUMS`,
regenerate `.SRCINFO`, commit, push. Candidate for the release train once
the account exists.

## Notes

- `package()` only installs the binary — running the downloaded binary in
  `package()` would break aarch64 builds on x86_64 build hosts.
- Shell completions: SHIPPED upstream (#487, closed 2026-07-12) — tarballs
  from the next tag carry `completions/`, and package() installs them
  conditionally (present ≥0.100, absent on 0.99.0) without ever executing
  the target-arch binary.
- The ledger entry lives in `listings.yaml` (`queued_operator` until the
  account ceremony happens).

## Release-train auto-bump (wire after the ceremony)

`KSXGitHub/github-actions-deploy-aur@v4.1.3` (verified maintained) in the
engine's release workflow, next to the brew bump: regenerates PKGBUILD
version + sha256s + .SRCINFO and pushes to AUR on every tag — the AUR
« do not submit and forget » maintainer obligation becomes structural.
