---
title: Oxygen Orion
type: release
source_url: https://github.com/monero-project/monero/releases/tag/v0.17.0.0
author: luigi1111
tag_name: v0.17.0.0
published_at: '2020-09-29T02:50:39+00:00'
---

# Version: v0.17.0.0

# Release Notes
# Overview

This is the v0.17.0.0 release of the Monero software. This major release is due to the October 17th network upgrade, which in turn adds support for the CLSAG transaction format which improves verification speed and reduces transaction size.

Some highlights of this release are:

- Support for CLSAG transaction format
- Deterministic unlock times
- Enforce claiming maximum coinbase amount
- Serialization format changes
- Remove most usage of Boost library
- Always send raw transactions through P2P, don't use bootstrap daemon
- Update InProofV1, OutProofV1, and ReserveProofV1 to V2
- ASM optimizations for wallet refresh (macOS / Linux)
- Randomized delay when forwarding txes from i2p/tor -> ipv4/6
- New show_qr_code wallet command for CLI
- Add ZMQ/Pub support for txpool_add and chain_main events
- Various bug fixes and performance improvements

# Contributors for this Release

This release was the direct result of 30 people who worked, largely unpaid and altruistically, to put out 292 commits containing 11523 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- stoffu
- François Colas
- TheCharlatan
- koe
- Lee Clagett
- Jean Pierre Dudey
- MaxXor
- rbrunner7
- luigi1111
- xiphon
- erciccione
- mj-xmr
- thomasvaughan
- Age Bosma
- cohcho
- sumogr
- moneromooo-monero
- woodser
- cryptographicfool
- Jason Rhinelander
- Norman Moeschter
- Sarang Noether
- Dusan Klinec
- SomaticFanatic
- cslashm
- selsta
- tevador
- ArqTras
- russoj88
- Reinaldulin

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/cli/monero-win-x64-v0.17.0.0.zip)
[Windows, 32-bit](https://downloads.getmonero.org/cli/monero-win-x86-v0.17.0.0.zip)
[macOS, 64-bit](https://downloads.getmonero.org/cli/monero-mac-x64-v0.17.0.0.tar.bz2)
[Linux, 64-bit](https://downloads.getmonero.org/cli/monero-linux-x64-v0.17.0.0.tar.bz2)
[Linux, 32-bit](https://downloads.getmonero.org/cli/monero-linux-x86-v0.17.0.0.tar.bz2)
[Linux, armv7](https://downloads.getmonero.org/cli/monero-linux-armv7-v0.17.0.0.tar.bz2)
[Linux, armv8](https://downloads.getmonero.org/cli/monero-linux-armv8-v0.17.0.0.tar.bz2)
[Android, armv7](https://downloads.getmonero.org/cli/monero-android-armv7-v0.17.0.0.tar.bz2)
[Android, armv8](https://downloads.getmonero.org/cli/monero-android-armv8-v0.17.0.0.tar.bz2)
[FreeBSD, 64-bit](https://downloads.getmonero.org/cli/monero-freebsd-x64-v0.17.0.0.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-win-x64-v0.17.0.0.zip, 8b84b4c9820a9b0f5e010079ceaf622936cbf4a5cec6de099c2dbbaf3cf47b73
monero-win-x86-v0.17.0.0.zip, bd92b31b82d4349416f2bac6d9d76404c526f9e546f90cc9806084badccd9de8
monero-mac-x64-v0.17.0.0.tar.bz2, b07ca7a00373c4b7f151133e5ecd47da8a2ab65bdaa00154311cee8be735fd07
monero-linux-x64-v0.17.0.0.tar.bz2, 29a1a3d2d4a6bcbaccba0a8016be43c36c88523c358c721d9886e1f0c5ae662d
monero-linux-x86-v0.17.0.0.tar.bz2, 390125abd93ad7640e5033a88c34cda618fa4a78eb38156d9f9a29742968f44e
monero-linux-armv8-v0.17.0.0.tar.bz2, 47d7a24a15457ddca2bd5151805f35f000c92d8d216a0aaa31a982d1a68e31c3
monero-linux-armv7-v0.17.0.0.tar.bz2, 95b424be406346acd0422d2a12598d5f7d7033e20dfdb0e123fd75e185bcf76c
monero-android-armv8-v0.17.0.0.tar.bz2, ff9c51f03be4728614a6c4b9ceefe60334dee118c1cd3a96be9af3db30b80cb0
monero-android-armv7-v0.17.0.0.tar.bz2, 620c10c940eb9480f1004b80de6cdf0db0ff402d45ebda07b0677f556d3d8535
monero-freebsd-x64-v0.17.0.0.tar.bz2, a183c9729b4fcf53b29207c218ae39a01f59d4788620bf4227aa3a4adc4312ad
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys). To ensure that the files you download are those originally posted by the maintainers, you should both check that the hashes of your files match those on the signed list, and that the signature on the list is valid.