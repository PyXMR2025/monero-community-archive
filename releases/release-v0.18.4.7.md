---
title: Fluorine Fermi, GUI, Point Release 4.7
type: release
source_url: https://github.com/monero-project/monero-gui/releases/tag/v0.18.4.7
author: binaryFate
tag_name: v0.18.4.7
published_at: '2026-03-11T05:08:48+00:00'
---

# Version: v0.18.4.7

# Release Notes
# Overview

This is the v0.18.4.7 release of the Monero GUI software. This release contains bug fixes.

[The latest CLI release notes and downloads can be found on the release page here.](https://github.com/monero-project/monero/releases/tag/v0.18.4.6)

Some highlights of this release are:

- Fix GUI getting stuck during exit on macOS (#4558)
- Fix lack of focus during password dialog (#4549)
- Set password for temporary wallet during wizard wallet creation (#4556, #4571)
- Improve blockchain size estimate accuracy (#4552)
- Update Qt to 5.15.18 (#4565)
- Update p2pool to v4.14 (#4570)
- Minor bug fixes

# Contributors for this Release

This release was the direct result of 4 people who worked to put out 29 commits containing 163 new lines of code. We'd like to thank them very much for their time and effort. In no particular order, they are:

- tobtoht
- selsta
- SChernykh
- luigi1111

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/gui/monero-gui-win-x64-v0.18.4.7.zip)
[Windows, 64-bit (Installer)](https://downloads.getmonero.org/gui/monero-gui-install-win-x64-v0.18.4.7.exe)
[macOS, Intel](https://downloads.getmonero.org/gui/monero-gui-mac-x64-v0.18.4.7.dmg)
[macOS, ARM](https://downloads.getmonero.org/gui/monero-gui-mac-armv8-v0.18.4.7.dmg)
[Linux, 64-bit](https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.18.4.7.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-gui-win-x64-v0.18.4.7.zip, b06dde8291aa03c4ac89efe19568c22eba2854af18a39163ed6d4a1fb88f1a20
monero-gui-install-win-x64-v0.18.4.7.exe, adf679471c5a619a6e1f484672c883de097ba55caecaf85a6b040d7190d38576
monero-gui-mac-x64-v0.18.4.7.dmg, 23a09caf2430f1e2b4809bd52ca2477de6acbe8db45890942975e757fb8096db
monero-gui-mac-armv8-v0.18.4.7.dmg, 5685e948ea070c4a7b9450a576da00b4037168b2f0645aa27437fa6d2e609095
monero-gui-linux-x64-v0.18.4.7.tar.bz2, 4573defcf21b0daeea0e9c7213540012c7d1186e829daf991fa8edfc5033dc08
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)