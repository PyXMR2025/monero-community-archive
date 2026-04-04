---
title: Oxygen Orion, GUI, Point Release 1.1
type: release
source_url: https://github.com/monero-project/monero-gui/releases/tag/v0.17.1.1
author: luigi1111
tag_name: v0.17.1.1
published_at: '2020-10-22T04:01:27+00:00'
---

# Version: v0.17.1.1

# Release Notes
# Overview

This is the v0.17.1.1 minor point release of the Monero GUI software. This is a highly recommended release that fixes an issue with nodes getting stuck at block 2210720.

[The latest CLI release notes and downloads can be found on the release page here.](https://github.com/monero-project/monero/releases/tag/v0.17.1.1)

Some highlights of this minor release are:

- Fix sync past block 2210720
- Add "pending" and "failed" transaction status
- Simple mode: improve start / stop splash screen
- Simple mode: set default out peers to 16
- Add armv8-linux release target
- Fix wallet getting stuck on close
- Minor bug fixes

# Contributors for this Release

This release was the direct result of 4 people who worked, largely unpaid and altruistically, to put out 22 commits containing 62 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- Snipa
- bjacquin
- xiphon
- selsta

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/gui/monero-gui-win-x64-v0.17.1.1.zip)
[Windows, 64-bit (Installer)](https://downloads.getmonero.org/gui/monero-gui-install-win-x64-v0.17.1.1.exe)
[macOS, 64-bit](https://downloads.getmonero.org/gui/monero-gui-mac-x64-v0.17.1.1.dmg)
[Linux, 64-bit](https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.17.1.1.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-gui-win-x64-v0.17.1.1.zip, a64fe57d2f0cf6bab49f78c5ae298f71e3fc44777da4e0cd89cd660facce14c2
monero-gui-install-win-x64-v0.17.1.1.exe, 318cec037990d89cec62f2d29ac5827a459d15a638abc5c25cbc3b910337e50f
monero-gui-mac-x64-v0.17.1.1.dmg, ebaecd3b4072c1ef22009dd69290208b5c83b9b597de1a1116bc05564a08a916
monero-gui-linux-x64-v0.17.1.1.tar.bz2, 14f5667e57603f05872a0dcd31a81acd7ffa31b71eb83ba22661bd05e2fc53d1
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)