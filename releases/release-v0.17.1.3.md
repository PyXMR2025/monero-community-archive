---
title: Oxygen Orion, Point Release 1.3
type: release
source_url: https://github.com/monero-project/monero/releases/tag/v0.17.1.3
author: binaryFate
tag_name: v0.17.1.3
published_at: '2020-11-16T18:19:26+00:00'
---

# Version: v0.17.1.3

# Release Notes
# Overview

This is the v0.17.1.3 minor point release of the Monero software.
This is a recommended release that improves overall network perfomance.

Some highlights of this minor release are:

- Add support for I2P and Tor seed nodes (--tx-proxy)
- Add --ban-list daemon option to ban a list of IP addresses
- Switch to Dandelion++ fluff mode if no out connections for stem mode
- Fix a bug with relay_tx
- Fix a rare readline related crash
- Use /16 filtering on IPv4-within-IPv6 addresses
- Give all hosts the same chance of being picked for connecting
- Minor bugfixes

# Contributors for this Release

This release was the direct result of 5 people who worked, largely unpaid and altruistically, to put out 40 commits containing 367 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- luigi1111
- selsta
- moneromooo-monero
- xiphon
- vtnerd

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/cli/monero-win-x64-v0.17.1.3.zip)
[Windows, 32-bit](https://downloads.getmonero.org/cli/monero-win-x86-v0.17.1.3.zip)
[macOS, 64-bit](https://downloads.getmonero.org/cli/monero-mac-x64-v0.17.1.3.tar.bz2)
[Linux, 64-bit](https://downloads.getmonero.org/cli/monero-linux-x64-v0.17.1.3.tar.bz2)
[Linux, 32-bit](https://downloads.getmonero.org/cli/monero-linux-x86-v0.17.1.3.tar.bz2)
[Linux, armv7](https://downloads.getmonero.org/cli/monero-linux-armv7-v0.17.1.3.tar.bz2)
[Linux, armv8](https://downloads.getmonero.org/cli/monero-linux-armv8-v0.17.1.3.tar.bz2)
[Android, armv7](https://downloads.getmonero.org/cli/monero-android-armv7-v0.17.1.3.tar.bz2)
[Android, armv8](https://downloads.getmonero.org/cli/monero-android-armv8-v0.17.1.3.tar.bz2)
[FreeBSD, 64-bit](https://downloads.getmonero.org/cli/monero-freebsd-x64-v0.17.1.3.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-win-x64-v0.17.1.3.zip, 3eee0d0e896fb426ef92a141a95e36cb33ca7d1e1db3c1d4cb7383994af43a59
monero-win-x86-v0.17.1.3.zip, c9e9dde61b33adccd7e794eba8ba29d820817213b40a2571282309d25e64e88a
monero-mac-x64-v0.17.1.3.tar.bz2, 79557c8bee30b229bda90bb9ee494097d639d60948fc2ad87a029359b56b1b48
monero-linux-x64-v0.17.1.3.tar.bz2, cf3fb693339caed43a935c890d71ecab5b89c430e778dc5ef0c3173c94e5bf64
monero-linux-x86-v0.17.1.3.tar.bz2, d107384ff7b1f77ee4db93940dbfda24d6045bf59c43169bc81a0118e3986bfa
monero-linux-armv8-v0.17.1.3.tar.bz2, a0419993fbc6a5ca11bcd2e825acef13e429824f4d8c7ba4ec73ac446d2af2fb
monero-linux-armv7-v0.17.1.3.tar.bz2, 57d6f9c25bd1dbc9d6b39fcfb13260b21c5594b4334e8ed3b8922108730ee2f0
monero-android-armv8-v0.17.1.3.tar.bz2, 0e94f58572646992ee21f01d291211ed3608e8a46ecb6612b378a2188390dba0
monero-android-armv7-v0.17.1.3.tar.bz2, 38a04a7bd00733e9d943edba3004e44730c0848fe5e8a4fca4cb29c12d1e6b2f
monero-freebsd-x64-v0.17.1.3.tar.bz2, ae1a1b61d7b4a06690cb22a3389bae5122c8581d47f3a02d303473498f405a1a
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)