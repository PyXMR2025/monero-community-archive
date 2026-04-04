---
title: Fluorine Fermi, GUI, Point Release 3.1
type: release
source_url: https://github.com/monero-project/monero-gui/releases/tag/v0.18.3.1
author: binaryFate
tag_name: v0.18.3.1
published_at: '2023-10-10T19:20:02+00:00'
---

# Version: v0.18.3.1

# Release Notes
# Overview

This is the v0.18.3.1 release of the Monero GUI software. This release adds support for macOS ARM.

[The latest CLI release notes and downloads can be found on the release page here.](https://github.com/monero-project/monero/releases/tag/v0.18.3.1)

Some highlights of this release are:

- Add macOS ARM support
- Display error when `Scan Transaction` is used on older tx via untrusted daemon (#4051)
- Add image when Ledger Stax is selected in wizard (#4146)
- Add more detailed P2Pool failure messages, fix a rare crash (#4147)
- Update Qt to 5.15.10 (#4143)
- Update p2pool to v3.7 (#4219)
- Minor bug fixes and UI improvements

# Contributors for this Release

This release was the direct result of 10 people who worked, largely unpaid and altruistically, to put out 60 commits containing 605 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- luigi1111
- tobtoht
- j-berman
- Botspot
- plowsof
- Dvd-Znf
- web3d3v
- BigmenPixel0
- selsta
- SChernykh

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/gui/monero-gui-win-x64-v0.18.3.1.zip)
[Windows, 64-bit (Installer)](https://downloads.getmonero.org/gui/monero-gui-install-win-x64-v0.18.3.1.exe)
[macOS, Intel](https://downloads.getmonero.org/gui/monero-gui-mac-x64-v0.18.3.1.dmg)
[macOS, ARM](https://downloads.getmonero.org/gui/monero-gui-mac-armv8-v0.18.3.1.dmg)
[Linux, 64-bit](https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.18.3.1.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-gui-win-x64-v0.18.3.1.zip, f263ce5863fd87ea959f79420e28ef0002649fa02bd57ae34efda926bdcf1a70
monero-gui-install-win-x64-v0.18.3.1.exe, 792271147ad71a2eaa02fc37d61d72cd92f2f9857dcc09ea032f48481f87e279
monero-gui-mac-x64-v0.18.3.1.dmg, 8ae53f0908f9bc03452f23d5092bf1eb1d2ad9f1224580486b486cf0a2020401
monero-gui-mac-armv8-v0.18.3.1.dmg, b0c8d07f8d8ade49d08419b196ddb9f691717ef05cae066e220db707e4dfedc4
monero-gui-linux-x64-v0.18.3.1.tar.bz2, 06f6e600db51205116d52522964cf9b96337d7b5cb1e101730ccb0039b30e15b
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)