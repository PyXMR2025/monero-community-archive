---
title: Fluorine Fermi, GUI, Point Release 4.2
type: release
source_url: https://github.com/monero-project/monero-gui/releases/tag/v0.18.4.2
author: binaryFate
tag_name: v0.18.4.2
published_at: '2025-08-26T16:30:46+00:00'
---

# Version: v0.18.4.2

# Release Notes
# Overview

This is the v0.18.4.2 release of the Monero GUI software. This is a recommended release that fixes a privacy leak when using a malicious remote node.

[The latest CLI release notes and downloads can be found on the release page here.](https://github.com/monero-project/monero/releases/tag/v0.18.4.2)

Some highlights of this release are:

- Fix privacy leak with malicious remote node
- Add background sync when locked functionality (#4050)
- Update P2Pool to v4.9.1, fix Linux permission bug (#4490)
- Add P2Pool nano sidechain (#4482)
- Minor bug fixes

# Contributors for this Release

This release was the direct result of 7 people who worked, to put out 12 commits containing 290 new lines of code. We'd like to thank them very much for their time and effort. In no particular order, they are:

- luigi1111
- tobtoht
- nahuhh
- j-berman
- SChernykh
- selsta
- xihuwenhua

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/gui/monero-gui-win-x64-v0.18.4.2.zip)
[Windows, 64-bit (Installer)](https://downloads.getmonero.org/gui/monero-gui-install-win-x64-v0.18.4.2.exe)
[macOS, Intel](https://downloads.getmonero.org/gui/monero-gui-mac-x64-v0.18.4.2.dmg)
[macOS, ARM](https://downloads.getmonero.org/gui/monero-gui-mac-armv8-v0.18.4.2.dmg)
[Linux, 64-bit](https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.18.4.2.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-gui-win-x64-v0.18.4.2.zip, 4daff8850280173d46464ba9a9de7f712228ad1ef76a1c4954531e4fd2b86d86
monero-gui-install-win-x64-v0.18.4.2.exe, 9d6e87add7e3ac006ee34c13c4f629252595395f54421db768f72dc233e94ea8
monero-gui-mac-x64-v0.18.4.2.dmg, 16abadcbd608d4f7ba20d17a297f2aa2c9066d33f6f22bf3fcdca679ab603990
monero-gui-mac-armv8-v0.18.4.2.dmg, 3dfee5c5d8e000c72eb3755bf0eb03ca7c5928b69c3a241e147ad22d144e00a7
monero-gui-linux-x64-v0.18.4.2.tar.bz2, e4fcdea3f0ff27c3616a8a75545f42a4e4866ea374fa2eeaa9c87027573358ea
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)