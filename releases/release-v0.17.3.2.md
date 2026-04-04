---
title: Oxygen Orion, GUI, Point Release 3.2
type: release
source_url: https://github.com/monero-project/monero-gui/releases/tag/v0.17.3.2
author: binaryFate
tag_name: v0.17.3.2
published_at: '2022-04-29T19:22:31+00:00'
---

# Version: v0.17.3.2

# Release Notes
# Overview

This is the v0.17.3.2 point release of the Monero GUI software. This release contains support for P2Pool mining and Ledger Nano S Plus.

[The latest CLI release notes and downloads can be found on the release page here.](https://github.com/monero-project/monero/releases/tag/v0.17.3.2)

Some highlights of this minor release are:

- Integrate experimental support for P2Pool mining (#3829)
- Warn against high fees during transaction creation (#3897)
- Improvements against wallet getting stuck on exit (#3890, #3889)
- Add support for Ledger Nano S Plus
- Add support for reserve proof (#3828)
- Add a lock wallet button to the title bar (#3859)
- Fix offline signing (#3862)
- Fix adding a new address book entry (#3865)
- Update translations, add support for 5 new languages (#3832)
- Minor bug fixes and UI improvements

# Contributors for this Release

This release was the direct result of 22 people who worked, largely unpaid and altruistically, to put out 76 commits containing 31625 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- selsta
- luigi1111
- rating89us
- netrik182
- devhyper
- mj-xmr
- jeffro256
- reemuru

A special thanks to translators

Miguel Medina, jaime diaz, Dynse Clyde Sacote, Robbie Monero, Gilberto F da Silva, Malek Atwiz, nanostos, ambercookie, Patix0331, Paul Janowitz, Trendyne, siptruk, tuknag, Marta Kozera

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/gui/monero-gui-win-x64-v0.17.3.2.zip)
[Windows, 64-bit (Installer)](https://downloads.getmonero.org/gui/monero-gui-install-win-x64-v0.17.3.2.exe)
[macOS, 64-bit](https://downloads.getmonero.org/gui/monero-gui-mac-x64-v0.17.3.2.dmg)
[Linux, 64-bit](https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.17.3.2.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-gui-win-x64-v0.17.3.2.zip, a0fa78c62a97b91db3d225c37c33d8185891600930dddd694d01635b825c2bff
monero-gui-install-win-x64-v0.17.3.2.exe, 92541cc74ac7afbe771292f6a94127dfaf5163627a750226bff10abd431e5086
monero-gui-mac-x64-v0.17.3.2.dmg, acaabe36002ae66bee4d4ded1fbcca4b34688cb702231aea26afe49f3f284fbe
monero-gui-linux-x64-v0.17.3.2.tar.bz2, ad4b4be60548cddcade3cf8874579256805559d61a68e6102e4dde71284a2039
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)