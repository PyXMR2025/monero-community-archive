---
title: Fluorine Fermi, GUI, Point Release 3.2
type: release
source_url: https://github.com/monero-project/monero-gui/releases/tag/v0.18.3.2
author: binaryFate
tag_name: v0.18.3.2
published_at: '2024-03-10T20:00:06+00:00'
---

# Version: v0.18.3.2

# Release Notes
# Overview

This is the v0.18.3.2 release of the Monero GUI software. This is a recommended release that fixes automatic fee selection.

[The latest CLI release notes and downloads can be found on the release page here.](https://github.com/monero-project/monero/releases/tag/v0.18.3.2)

Some highlights of this release are:

- Fix automatic fee selection (#4283)
- Add support for Trezor Safe 3 (#4255)
- OpenAlias domains starting with a digit can now be recognized (#4243)
- Fix Tails detection (#4281)
- Fix a crash on macOS ARM (#4283)
- Update Qt to 5.15.12 (#4261)
- Update p2pool to v3.10 (#4260)
- Minor bug fixes and UI improvements

# Contributors for this Release

This release was the direct result of 6 people who worked, largely unpaid and altruistically, to put out 35 commits containing 198 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- luigi1111
- tobtoht
- selsta
- SChernykh
- inson1
- sausagenoods

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/gui/monero-gui-win-x64-v0.18.3.2.zip)
[Windows, 64-bit (Installer)](https://downloads.getmonero.org/gui/monero-gui-install-win-x64-v0.18.3.2.exe)
[macOS, Intel](https://downloads.getmonero.org/gui/monero-gui-mac-x64-v0.18.3.2.dmg)
[macOS, ARM](https://downloads.getmonero.org/gui/monero-gui-mac-armv8-v0.18.3.2.dmg)
[Linux, 64-bit](https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.18.3.2.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-gui-win-x64-v0.18.3.2.zip, 42f14a477524e60b7fb6addef8b18f6a99a0008755c56aaa0628fd611a7f6909
monero-gui-install-win-x64-v0.18.3.2.exe, e6a1f267d6e07ee72576bc942cfa74c7eeaa47b73a5d30291eb03e722448b79e
monero-gui-mac-x64-v0.18.3.2.dmg, 8f18d3a63f0f52c6ae61de1881e420c6c8c2bf3296084c3d30b529430cdd9896
monero-gui-mac-armv8-v0.18.3.2.dmg, 3c48b77e0b5258350a40d8cf23c2f6fda56a7ba0193fc368473ce1e0bf59342f
monero-gui-linux-x64-v0.18.3.2.tar.bz2, 98772e56afe5509ed4bd3d36ee2ea3c70c019cb4325c18d3508291fcdc784d4f
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)