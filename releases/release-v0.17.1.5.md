---
title: Oxygen Orion, Point Release 1.5
type: release
source_url: https://github.com/monero-project/monero/releases/tag/v0.17.1.5
author: binaryFate
tag_name: v0.17.1.5
published_at: '2020-11-26T18:29:31+00:00'
---

# Version: v0.17.1.5

# Release Notes
# Overview

This is the v0.17.1.5 minor point release of the Monero software. This is a recommended release that improves Dandelion++ perfomance.

Some highlights of this minor release are:

- Change Dandelion++ fluff probability to 20%, and embargo timeout to 39s 
- Fix timeout checks for forwarded and Dandelion++ stem txes
- Improve peer selection in Dandelion++ stem phase
- Skip non-synced bootstrap daemons in --no-sync mode
- Check imported multisig curve points are in main subgroup
- Better log message for unusable anonymity networks
- Minor bug fixes

# Contributors for this Release

This release was the direct result of 7 people who worked, largely unpaid and altruistically, to put out 25 commits containing 203 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- luigi1111
- Snipa
- moneromooo
- xiphon
- hyc
- vtnerd
- selsta

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/cli/monero-win-x64-v0.17.1.5.zip)
[Windows, 32-bit](https://downloads.getmonero.org/cli/monero-win-x86-v0.17.1.5.zip)
[macOS, 64-bit](https://downloads.getmonero.org/cli/monero-mac-x64-v0.17.1.5.tar.bz2)
[Linux, 64-bit](https://downloads.getmonero.org/cli/monero-linux-x64-v0.17.1.5.tar.bz2)
[Linux, 32-bit](https://downloads.getmonero.org/cli/monero-linux-x86-v0.17.1.5.tar.bz2)
[Linux, armv7](https://downloads.getmonero.org/cli/monero-linux-armv7-v0.17.1.5.tar.bz2)
[Linux, armv8](https://downloads.getmonero.org/cli/monero-linux-armv8-v0.17.1.5.tar.bz2)
[Android, armv7](https://downloads.getmonero.org/cli/monero-android-armv7-v0.17.1.5.tar.bz2)
[Android, armv8](https://downloads.getmonero.org/cli/monero-android-armv8-v0.17.1.5.tar.bz2)
[FreeBSD, 64-bit](https://downloads.getmonero.org/cli/monero-freebsd-x64-v0.17.1.5.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-win-x64-v0.17.1.5.zip, 4bb0fca53bc58c1167bc0a258f61dd69a54507fd83ad37edf4213b4f30df8c94
monero-win-x86-v0.17.1.5.zip, 7dc0565a2880b38e73d85599153a31bbed85965963c6f74e1a5cf6dbd06f619e
monero-mac-x64-v0.17.1.5.tar.bz2, adfc663b2b36b0cb2fdfcc35185b3d93c8c2256de06da01521e555b7b20ee292
monero-linux-x64-v0.17.1.5.tar.bz2, 95666508e695637830b4c1700538c717ff97f02f181fbb337a109763372c8d34
monero-linux-x86-v0.17.1.5.tar.bz2, c5b19fa1db2de6a66e475e634b07f2b5f74d5cd41e968aa0ed34ffd8f91f527f
monero-linux-armv8-v0.17.1.5.tar.bz2, 50f113959bcc230860ff77cbac03a2713db772a72e80afe50f511418f9e9d97f
monero-linux-armv7-v0.17.1.5.tar.bz2, 99fa5eb56616c1b7b6aef69572b8c51efa813bfaff2f2336ac982b449e8ee2a1
monero-android-armv8-v0.17.1.5.tar.bz2, 01998179f2c39d97f4e204b1323c17ca35c5797c558a9c51ad3f8a21c23620fe
monero-android-armv7-v0.17.1.5.tar.bz2, 972f4ed467e34ea783fb66ad6f50749c2b7b3d9f77bb2825e70a8763d84b00f2
monero-freebsd-x64-v0.17.1.5.tar.bz2, 8fead098417cd4d3896012e485494efec8851c28abcb1883c3a1716652390321
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)