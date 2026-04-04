---
title: Fluorine Fermi, Point Release 3.1
type: release
source_url: https://github.com/monero-project/monero/releases/tag/v0.18.3.1
author: binaryFate
tag_name: v0.18.3.1
published_at: '2023-10-10T19:18:55+00:00'
---

# Version: v0.18.3.1

# Release Notes
# Overview

This is the v0.18.3.1 release of the Monero software. This release optimizes wallet refresh and contains important bug fixes.

Some highlights of this release are:

- Optimize wallet refresh by reducing periodic RPC calls (#8800)
- Daemon: handle case where a command line flag is not allowed in the config file (#8766)
- Daemon: ensure base fee cannot reach 0 (#8851)
- Daemon: fix high CPU usage on some systems by properly terminating interrupted TCP connection (#8900)
- Daemon: drop peers sending duplicate transactions (#8916)
- Daemon: fix a bug with the long-term block weight cache (#9014)
- Wallet: improve rescanning with `scan_tx` (#8566)
- Wallet: do not use DNS to determine if address is local (#8878)
- Wallet: fix `frozen` function in multisig wallets (#8953)
- Wallet: wallet save and password change related code improvements (#8938, #8999)
- RPC: return ID of submitted block (#8891)
- RPC: allow restore from multisig seed (#8942)
- RPC: add `--no-initial-sync` flag, chunk refresh to keep responding while refreshing (#8941)
- Speed up perf_timer init on x86, reduce monero startup delay by 1s (#8895)
- Fix RandomX initialization when mining from scratch (#8831)
- Fix amount overflow detection on 32-bit systems (#8844)
- Update openssl to 1.1.1u (#8883)
- Add CLSAG serialization to ZMQ (#8908)
- Set SSL SNI even when server verification is disabled (#8899)
- Minor bug fixes and improvements

# Contributors for this Release

This release was the direct result of 12 people who worked, largely unpaid and altruistically, to put out 64 commits containing 2557 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- SChernykh
- Boog900
- moneromooo
- luigi1111
- selsta
- jeffro256
- woodser
- j-berman
- rbrunner7
- vtnerd
- tobtoht
- almalh

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/cli/monero-win-x64-v0.18.3.1.zip)
[Windows, 32-bit](https://downloads.getmonero.org/cli/monero-win-x86-v0.18.3.1.zip)
[macOS, Intel](https://downloads.getmonero.org/cli/monero-mac-x64-v0.18.3.1.tar.bz2)
[macOS, ARM](https://downloads.getmonero.org/cli/monero-mac-armv8-v0.18.3.1.tar.bz2)
[Linux, 64-bit](https://downloads.getmonero.org/cli/monero-linux-x64-v0.18.3.1.tar.bz2)
[Linux, 32-bit](https://downloads.getmonero.org/cli/monero-linux-x86-v0.18.3.1.tar.bz2)
[Linux, armv7](https://downloads.getmonero.org/cli/monero-linux-armv7-v0.18.3.1.tar.bz2)
[Linux, armv8](https://downloads.getmonero.org/cli/monero-linux-armv8-v0.18.3.1.tar.bz2)
[Android, armv7](https://downloads.getmonero.org/cli/monero-android-armv7-v0.18.3.1.tar.bz2)
[Android, armv8](https://downloads.getmonero.org/cli/monero-android-armv8-v0.18.3.1.tar.bz2)
[FreeBSD, 64-bit](https://downloads.getmonero.org/cli/monero-freebsd-x64-v0.18.3.1.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-win-x64-v0.18.3.1.zip, 35dcc4bee4caad3442659d37837e0119e4649a77f2e3b5e80dd6d9b8fc4fb6ad
monero-win-x86-v0.18.3.1.zip, 5bcbeddce32b50ebe18289d0560ebf779441526ec84d73b6a83094f092365271
monero-mac-x64-v0.18.3.1.tar.bz2, 7f8bd9364ef16482b418aa802a65be0e4cc660c794bb5d77b2d17bc84427883a
monero-mac-armv8-v0.18.3.1.tar.bz2, 915288b023cb5811e626e10052adc6ac5323dd283c5a25b91059b0fb86a21fb6
monero-linux-x64-v0.18.3.1.tar.bz2, 23af572fdfe3459b9ab97e2e9aa7e3c11021c955d6064b801a27d7e8c21ae09d
monero-linux-x86-v0.18.3.1.tar.bz2, c8553558dece79a4c23e1114fdf638b15e46899d7cf0af41457f18bbbee83986
monero-linux-armv8-v0.18.3.1.tar.bz2, 445032e88dc07e51ac5fff7034752be530d1c4117d8d605100017bcd87c7b21f
monero-linux-armv7-v0.18.3.1.tar.bz2, 2ea2c8898cbab88f49423f4f6c15f2a94046cb4bbe827493dd061edc0fd5f1ca
monero-android-armv8-v0.18.3.1.tar.bz2, 6d9c7d31942dde86ce39757fd55027448ceb260b60b3c8d32ed018211eb4f1e4
monero-android-armv7-v0.18.3.1.tar.bz2, fc6a93eabc3fd524ff1ceedbf502b8d43c61a7805728b7ed5f9e7204e26b91f5
monero-freebsd-x64-v0.18.3.1.tar.bz2, 3e2d9964a9e52c146b4d26b5eb53e691b3ba88e2468dc4fbfee4c318a367a90e
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys). To ensure that the files you download are those originally posted by the maintainers, you should both check that the hashes of your files match those on the signed list, and that the signature on the list is valid.