---
title: Fluorine Fermi, GUI, Major Point Release 1
type: release
source_url: https://github.com/monero-project/monero-gui/releases/tag/v0.18.1.0
author: binaryFate
tag_name: v0.18.1.0
published_at: '2022-08-11T19:33:20+00:00'
---

# Version: v0.18.1.0

# Release Notes
# Overview

This is the v0.18.1.0 release of the Monero GUI software. This release adds v0.18 network upgrade compatibility for Ledger and Trezor hardware wallets.

[The latest CLI release notes and downloads can be found on the release page here.](https://github.com/monero-project/monero/releases/tag/v0.18.1.0)

Some highlights of this release are:

- Add Ledger support for v0.18, requires app v1.8.0
- Add Trezor support for v0.18, requires firmware v2.5.2
- Speed up time between wallet opening and refresh (#3994)
- Add option to skip stop local node screen (#3734)
- Minor bug fixes and UI improvements

# Contributors for this Release

This release was the direct result of 7 people who worked, largely unpaid and altruistically, to put out 18 commits containing 27 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- selsta
- luigi1111
- reemuru
- tobtoht
- garth-xmr
- plowsof
- rbrunner7

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/gui/monero-gui-win-x64-v0.18.1.0.zip)
[Windows, 64-bit (Installer)](https://downloads.getmonero.org/gui/monero-gui-install-win-x64-v0.18.1.0.exe)
[macOS, 64-bit](https://downloads.getmonero.org/gui/monero-gui-mac-x64-v0.18.1.0.dmg)
[Linux, 64-bit](https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.18.1.0.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-gui-win-x64-v0.18.1.0.zip, 39c4290a01072cc8fe8eabaa2c61598421a72eac6011eccd16a2a63e89323fa2
monero-gui-install-win-x64-v0.18.1.0.exe, 9b2c8978f96e8c9662373b427ef320ccd9d652d346435a8487a756bf55cf43ff
monero-gui-mac-x64-v0.18.1.0.dmg, 0b06351b370863dce8fff9d8659a8235b98505c61c7e4f5af23843b161d92186
monero-gui-linux-x64-v0.18.1.0.tar.bz2, 6c993b622516d85555d8962767b39c79a3b3614cbdf0ab9f62fa07e3826498d0
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)