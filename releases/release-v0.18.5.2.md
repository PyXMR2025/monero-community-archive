---
title: Fluorine Fermi, GUI, Point Release 5.2
type: release
source_url: https://github.com/monero-project/monero-gui/releases/tag/v0.18.5.2
author: binaryFate
tag_name: v0.18.5.2
published_at: '2026-07-21T21:20:25+00:00'
---

# Version: v0.18.5.2

# Release Notes
# Overview

This is the v0.18.5.2 release of the Monero GUI software. This release fixes wallet generation during first use.

[The latest CLI release notes and downloads can be found on the release page here.](https://github.com/monero-project/monero/releases/tag/v0.18.5.1)

Some highlights of this release are:

- Fix wallet generation during first use (#4657)
- Warn when adjusting KDF rounds (#4641)
- Fix precision loss when generating payment requests with large amounts (#4649)
- Create wallets in memory in wizard (#4654)
- Minor bug fixes

# Contributors for this Release

This release was the direct result of 6 people who worked to put out 50 commits containing 1120 new lines of code. We'd like to thank them very much for their time and effort. In no particular order, they are:

- tobtoht
- selsta
- jpk68
- munzzyy
- thomasbuilds
- SNeedlewoods

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/gui/monero-gui-win-x64-v0.18.5.2.zip)
[Windows, 64-bit (Installer)](https://downloads.getmonero.org/gui/monero-gui-install-win-x64-v0.18.5.2.exe)
[macOS, Intel](https://downloads.getmonero.org/gui/monero-gui-mac-x64-v0.18.5.2.dmg)
[macOS, ARM](https://downloads.getmonero.org/gui/monero-gui-mac-armv8-v0.18.5.2.dmg)
[Linux, 64-bit](https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.18.5.2.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-gui-win-x64-v0.18.5.2.zip, e7a11d2faa6c4f223984b4064965fd1f37aea6b3c1d1658ce7150fe84680713f
monero-gui-install-win-x64-v0.18.5.2.exe, e3c5f1f2661b624d1fd3d264c01c23cf2c1f774cbd6555251abe37dd23868573
monero-gui-mac-x64-v0.18.5.2.dmg, b57cef077a3d5db26a3b3ed0831f879d6c8cbd67e7cffd8091865b90e86b1335
monero-gui-mac-armv8-v0.18.5.2.dmg, 26efb1be1a409b4dd9090b1c0ca2ee95ef4a3d0a42fdfb83cddbba6c048e1cc0
monero-gui-linux-x64-v0.18.5.2.tar.bz2, 294017a5aa1ee86420b0c62fe4046000f42438375a8559d9ff55e41e5c6cbbcd
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in `/utils/gpg_keys`)