---
title: Fluorine Fermi, GUI, Point Release 5.1
type: release
source_url: https://github.com/monero-project/monero-gui/releases/tag/v0.18.5.1
author: binaryFate
tag_name: v0.18.5.1
published_at: '2026-07-08T20:26:52+00:00'
---

# Version: v0.18.5.1

# Release Notes
# Overview

This is the v0.18.5.1 release of the Monero GUI software. This recommended release includes a large number of bug fixes.

[The latest CLI release notes and downloads can be found on the release page here.](https://github.com/monero-project/monero/releases/tag/v0.18.5.1)

Some highlights of this release are:

- Fix a memory safety issue during QR code scanning (#4597)
- Fix wallet freeze on shutdown edge case (#4603)
- Prevent CSV formula injection during export (#4609)
- Apply consistent text escaping across rich text views (#4610)
- Fix console log spam on startup (#4615)
- Check wallet file directory is writable during wallet creation (#4617)
- Add confirmation dialog for unauthenticated OpenAlias (#4618)
- Fix generic name in .desktop file (#4590)
- Hide update popup during device passphrase prompt (#4623)
- Set desktop entry ID for the application (#4625)
- Update P2Pool to v4.17.1 (#4620)
- Minor bug fixes

# Contributors for this Release

This release was the direct result of 8 people who worked to put out 48 commits containing 192 new lines of code. We'd like to thank them very much for their time and effort. In no particular order, they are:

- tobtoht
- selsta
- SChernykh
- jpk68
- City-busz
- SNeedlewoods
- plowsof
- thomasbuilds

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/gui/monero-gui-win-x64-v0.18.5.1.zip)
[Windows, 64-bit (Installer)](https://downloads.getmonero.org/gui/monero-gui-install-win-x64-v0.18.5.1.exe)
[macOS, Intel](https://downloads.getmonero.org/gui/monero-gui-mac-x64-v0.18.5.1.dmg)
[macOS, ARM](https://downloads.getmonero.org/gui/monero-gui-mac-armv8-v0.18.5.1.dmg)
[Linux, 64-bit](https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.18.5.1.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-gui-win-x64-v0.18.5.1.zip, 9241bb617bc4de37b0c3b2481c234ce39984ba2615fc65991979c189f092c918
monero-gui-install-win-x64-v0.18.5.1.exe, 0c0880b62edf00ee4291b37c4ba32227fd1bc31433d84929eeec1e2862bd1c0f
monero-gui-mac-x64-v0.18.5.1.dmg, 1f7b2c3a0e83180267d4c09cbb4f4d14b35c4f3c218abae585f0bb288f8bf01c
monero-gui-mac-armv8-v0.18.5.1.dmg, c40a9125a976d7f063216f286976a252eb5a7f26206bd034f25782691786f18c
monero-gui-linux-x64-v0.18.5.1.tar.bz2, ecf7f734fb0048896b12f7e04e4f69a0257271f8411c06d30cd701371d2fd155
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in `/utils/gpg_keys`)
