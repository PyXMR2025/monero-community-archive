---
title: Oxygen Orion, GUI, Point Release 2.3
type: release
source_url: https://github.com/monero-project/monero-gui/releases/tag/v0.17.2.3
author: binaryFate
tag_name: v0.17.2.3
published_at: '2021-09-01T16:02:48+00:00'
---

# Version: v0.17.2.3

# Release Notes
# Overview

This is the v0.17.2.3 minor point release of the Monero GUI software. This release contains a decoy selection bug fix that improves privacy.

[The latest CLI release notes and downloads can be found on the release page here.](https://github.com/monero-project/monero/releases/tag/v0.17.2.3)

Some highlights of this minor release are:

- Add payment request functionality to receive page (#3650)
- Display images on create hardware wallet page (#3618)
- Reenable password strength meter in release binaries (#3562)
- Automatically correct incorrectly typed restore dates (#3564)
- Add tooltips to all buttons (#3490)
- Add search transactions button on receive and account page (#3216, #3546)
- Set an unused wallet name in wizard (#3544)
- Fix bug not accepting new restore height (#3563)
- Fix get / check proof on Sign / Verify page (#3674)
- Fix scanning QR codes that miss an URI prefix (#3598)
- Various date picker improvements
- Accessibility improvements (#3611, #3603)
- Minor bug fixes and UI improvements

# Contributors for this Release

This release was the direct result of 3 people who worked, largely unpaid and altruistically, to put out 170 commits containing 26608 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- selsta
- luigi1111
- rating89us

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/gui/monero-gui-win-x64-v0.17.2.3.zip)
[Windows, 64-bit (Installer)](https://downloads.getmonero.org/gui/monero-gui-install-win-x64-v0.17.2.3.exe)
[macOS, 64-bit](https://downloads.getmonero.org/gui/monero-gui-mac-x64-v0.17.2.3.dmg)
[Linux, 64-bit](https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.17.2.3.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-gui-win-x64-v0.17.2.3.zip, 1ae06f71e7b469ea95f10008f2624797cf0a3223e47f07c42591c0dff63e63ec
monero-gui-install-win-x64-v0.17.2.3.exe, 8b5f37eb6b2d0534cbbc490986f23d7fb470697b7839ac1305499c4675f1ea11
monero-gui-mac-x64-v0.17.2.3.dmg, 20fe978294b65c2bb44932489f114e6a91cb4c2c4b03afb87ab683c8182cf811
monero-gui-linux-x64-v0.17.2.3.tar.bz2, f011ba2bd67395ca8c17d5faf1397785905533dd1a8b9ebf1e6810d0f726f40f
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)