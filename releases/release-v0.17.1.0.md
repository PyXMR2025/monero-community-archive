---
title: Oxygen Orion, GUI, Major Point Release 1
type: release
source_url: https://github.com/monero-project/monero-gui/releases/tag/v0.17.1.0
author: luigi1111
tag_name: v0.17.1.0
published_at: '2020-10-14T16:30:04+00:00'
---

# Version: v0.17.1.0

# Release Notes
# Overview

This is the v0.17.1.0 release of the Monero GUI software.

[The latest CLI release notes and downloads can be found on the release page here.](https://github.com/monero-project/monero/releases/tag/v0.17.1.0)

Some highlights of this release are:

- Simple mode: fix a bug causing transaction propagation to fail (stuck as pending)
- Portable mode: save log to storage folder
- Fix a rare crash during wallet refresh
- Fix wallet not showing up on recent wallets screen
- Fix empty RPATH token issue (Linux)
- Minor bug fixes

# Contributors for this Release

This release was the direct result of 3 people who worked, largely unpaid and altruistically, to put out 20 commits containing 186 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- luigi1111
- xiphon
- selsta

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/gui/monero-gui-win-x64-v0.17.1.0.zip)
[Windows, 64-bit (Installer)](https://downloads.getmonero.org/gui/monero-gui-install-win-x64-v0.17.1.0.exe)
[macOS, 64-bit](https://downloads.getmonero.org/gui/monero-gui-mac-x64-v0.17.1.0.dmg)
[Linux, 64-bit](https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.17.1.0.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-gui-win-x64-v0.17.1.0.zip, 85ecd625721435e99fff0f4849ff40bb3f2de26573b50432a5fe9632dfba3026
monero-gui-install-win-x64-v0.17.1.0.exe, be3b1f07ba86a0d46c27f670b27d936baa5c4e7b68f3dc37349b8f91b073dc6a
monero-gui-mac-x64-v0.17.1.0.dmg, b9c0cbdc8f9c74d6205858ccb4fb0f1eec792e301aa819bf8aa445a3d17869d3
monero-gui-linux-x64-v0.17.1.0.tar.bz2, 9076b731634e073430817cd590ea015a19a9cf3336c3c7a7bb16f1fd25b429f4
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)