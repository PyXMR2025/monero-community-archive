---
title: Oxygen Orion, Point Release 3.0
type: release
source_url: https://github.com/monero-project/monero/releases/tag/v0.17.3.0
author: binaryFate
tag_name: v0.17.3.0
published_at: '2021-12-07T14:12:54+00:00'
---

# Version: v0.17.3.0

# Release Notes
# Overview

This is the v0.17.3.0 point release of the Monero software. This release contains support for P2Pool.

Some highlights of this point release are:

- Add P2Pool support (#7964)
- Daemon: allow socks5 proxy configuration with --proxy flag (#7326, #7616)
- Daemon: fix race condition (#7873)
- Daemon: fix spurious rejection of downloaded blocks (#8022)
- Daemon: disable restricted RPC from getting output dist. for pre-rct outputs, fix DoS (#8084) [Reported by xfang/Haven]
- Daemon: add seed nodes (#7664, #7753)
- Wallet: fix key encryption when changing ask-password from 0/1 to 2 (#8014)
- Wallet: fix precision when selecting decoys (#7798)
- Wallet: decrease the "recent spend window" in decoy selection (#7993)
- Wallet: don't truncate integrated address in CSV history export (#7961)
- Wallet: chunk get_outs.bin RPC calls to avoid sanity limits (#7796)
- Wallet: add human-readable error messages to Ledger (#8039)
- RPC: fix get_transactions failing when not found (#7959)
- RPC: add calcpow method (#8075)
- Support wildcard CORS (#7952)
- Fix missing logs (#7929)
- Mac: fix compilation on ARM (#7435)
- Mac: don't blow out stack on ARM64 in slow-hash (#8032)
- LMDB: fix deadlock in resized detection (#7958)
- Detect AES support dynamically to support ARMv8 binaries on Raspberry Pi (#8005)
- Update following dependencies: OpenSSL, RandomX, unwind, hidapi, zeromq (#7933, #8002, #8037, #8049, #8056, #8072)
- Minor bug fixes and performance improvements

# Contributors for this Release

This release was the direct result of 18 people who worked, largely unpaid and altruistically, to put out 96 commits containing 1842 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- luigi1111
- hyc
- jtgrassie
- tevador
- woodser
- xiphon
- moneromooo
- tobtoht
- SChernykh
- ndorf
- anon
- vtnerd
- j-berman
- UkoeHB
- mj-xmr
- rbrunner7
- lalanza808
- selsta

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/cli/monero-win-x64-v0.17.3.0.zip)
[Windows, 32-bit](https://downloads.getmonero.org/cli/monero-win-x86-v0.17.3.0.zip)
[macOS, 64-bit](https://downloads.getmonero.org/cli/monero-mac-x64-v0.17.3.0.tar.bz2)
[Linux, 64-bit](https://downloads.getmonero.org/cli/monero-linux-x64-v0.17.3.0.tar.bz2)
[Linux, 32-bit](https://downloads.getmonero.org/cli/monero-linux-x86-v0.17.3.0.tar.bz2)
[Linux, armv7](https://downloads.getmonero.org/cli/monero-linux-armv7-v0.17.3.0.tar.bz2)
[Linux, armv8](https://downloads.getmonero.org/cli/monero-linux-armv8-v0.17.3.0.tar.bz2)
[Android, armv7](https://downloads.getmonero.org/cli/monero-android-armv7-v0.17.3.0.tar.bz2)
[Android, armv8](https://downloads.getmonero.org/cli/monero-android-armv8-v0.17.3.0.tar.bz2)
[FreeBSD, 64-bit](https://downloads.getmonero.org/cli/monero-freebsd-x64-v0.17.3.0.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-win-x64-v0.17.3.0.zip, a956d0c3ab77ebfc1d6229b77d68b739661b564d9a4115e5a549c3af146d6034
monero-win-x86-v0.17.3.0.zip, 541189f5635f479605eda306a36d2beef1fbe68d6fdbfabce671d6e4c8970158
monero-mac-x64-v0.17.3.0.tar.bz2, 53b7ed67f7077f27f470b4411478bef8b2bb9cf2cf480055dd1802a935983387
monero-linux-x64-v0.17.3.0.tar.bz2, ac18ce3d1189410a5c175984827d5d601974733303411f6142296d647f6582ce
monero-linux-x86-v0.17.3.0.tar.bz2, 586b9967d848eb31dd66bdb6d828bd3a640098434595a5933374d129b76958eb
monero-linux-armv8-v0.17.3.0.tar.bz2, 8fdb5761f6f4345dc670d184144ce8c2fa56eeb1609ed169e79b202fcca20f7d
monero-linux-armv7-v0.17.3.0.tar.bz2, da49d85ce2d52fc07846c58d0c58d6412f454f9d389bfa31eab9c1d49a1a13ed
monero-android-armv8-v0.17.3.0.tar.bz2, 1fa1ba8a1e4c6a0e56d8f7afd788205ff0916a3670b9bf7992f1db0f9d7dec3e
monero-android-armv7-v0.17.3.0.tar.bz2, a152c765386ee6ed670dbbfe1e90a8505040d5240a1c7c449bfa9845c4eb3e0d
monero-freebsd-x64-v0.17.3.0.tar.bz2, d496811ee4687db0c448d30086700f485bf30512c38b50441e5cb5e76b6011a7
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys). To ensure that the files you download are those originally posted by the maintainers, you should both check that the hashes of your files match those on the signed list, and that the signature on the list is valid.
