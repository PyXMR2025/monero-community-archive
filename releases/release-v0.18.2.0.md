---
title: Fluorine Fermi, Major Point Release 2
type: release
source_url: https://github.com/monero-project/monero/releases/tag/v0.18.2.0
author: binaryFate
tag_name: v0.18.2.0
published_at: '2023-03-01T05:46:20+00:00'
---

# Version: v0.18.2.0

# Release Notes
# Overview

This is the v0.18.2.0 release of the Monero software. This release contains various bugfixes as well as improvements to block propagation time.

Some highlights of this release are:

- Daemon: add RingCT cache for huge block propagation speedup (#8676)
- Daemon: refactored `rx-slow-hash`, add `MONERO_RANDOMX_FULL_MEM` env var to force use the full dataset for PoW verification (#8678)
- Daemon: fix back ping to discover healthy peers to connect to (#8641)
- Daemon: fix Dandelion++ fluff/stem bug with local transactions (#8628)
- Daemon: fix exclusive node DNS resolution for certain hosts (#8644)
- Daemon: cleanup and add new seed nodes (#8721)
- Wallet: update `hidapi`/`libusb` dependencies, fix Trezor connectivity issues on Windows (#8714)
- Fix monero-blockchain-stats omits data from final day (#8723)
- Update `OpenSSL` to 1.1.1t (#8738)
- Minor bug fixes and improvements

# Contributors for this Release

This release was the direct result of 11 people who worked, largely unpaid and altruistically, to put out 44 commits containing 865 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- SChernykh
- j-berman
- vtnerd
- woodser
- LocalMonero
- UkoeHB
- luigi1111
- selsta
- jeffro256
- tobtoht
- hyc

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/cli/monero-win-x64-v0.18.2.0.zip)
[Windows, 32-bit](https://downloads.getmonero.org/cli/monero-win-x86-v0.18.2.0.zip)
[macOS, Intel](https://downloads.getmonero.org/cli/monero-mac-x64-v0.18.2.0.tar.bz2)
[macOS, ARM](https://downloads.getmonero.org/cli/monero-mac-armv8-v0.18.2.0.tar.bz2)
[Linux, 64-bit](https://downloads.getmonero.org/cli/monero-linux-x64-v0.18.2.0.tar.bz2)
[Linux, 32-bit](https://downloads.getmonero.org/cli/monero-linux-x86-v0.18.2.0.tar.bz2)
[Linux, armv7](https://downloads.getmonero.org/cli/monero-linux-armv7-v0.18.2.0.tar.bz2)
[Linux, armv8](https://downloads.getmonero.org/cli/monero-linux-armv8-v0.18.2.0.tar.bz2)
[Android, armv7](https://downloads.getmonero.org/cli/monero-android-armv7-v0.18.2.0.tar.bz2)
[Android, armv8](https://downloads.getmonero.org/cli/monero-android-armv8-v0.18.2.0.tar.bz2)
[FreeBSD, 64-bit](https://downloads.getmonero.org/cli/monero-freebsd-x64-v0.18.2.0.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-win-x64-v0.18.2.0.zip, 112c0647baaa5c7e42f8b121ad633222f608200f9a402dbf2b5cd6b95ee555cd
monero-win-x86-v0.18.2.0.zip, dac24fa46581987041ea3e9d89d745c643afab23a6d74385cdddd1231fe92514
monero-mac-x64-v0.18.2.0.tar.bz2, 25965adf64e20b1fc7e6b4c8839390de90eb2ec702b7fc07271be81ae592bd5c
monero-mac-armv8-v0.18.2.0.tar.bz2, 46e793b1401e3b3b1d7308bacede021ec45af7df70e277530079386abb3915da
monero-linux-x64-v0.18.2.0.tar.bz2, 83e6517dc9e5198228ee5af50f4bbccdb226fe69ff8dd54404dddb90a70b7322
monero-linux-x86-v0.18.2.0.tar.bz2, 22e73cfe0bd8fbd37f9e74b8e3ed78d4682a7c2489b30ba00cd3e70644dfefc2
monero-linux-armv8-v0.18.2.0.tar.bz2, fb20eaf9b04020abdf883eb339258814742a1452653c1f5d8705d16e90413f35
monero-linux-armv7-v0.18.2.0.tar.bz2, 1312afd0dde3262ff89554e278c0130c0ced6bdbeec8bf614fbb40bd03c6a0d2
monero-android-armv8-v0.18.2.0.tar.bz2, 29ea258ff6c213b276dd97432f3ba7f03834c5a3c6787a16af36d15544b60c44
monero-android-armv7-v0.18.2.0.tar.bz2, d72064d7df1ed0e4f5d37eca69a457cb56bb505c32e1a48f4d25480aaecfe1ce
monero-freebsd-x64-v0.18.2.0.tar.bz2, 0647ebc921315d3e2c31de7e1ba6d3bd9f42b582f7b0d2761a61375291cf3307
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys). To ensure that the files you download are those originally posted by the maintainers, you should both check that the hashes of your files match those on the signed list, and that the signature on the list is valid.