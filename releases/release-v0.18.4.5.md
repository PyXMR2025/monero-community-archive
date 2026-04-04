---
title: Fluorine Fermi, Point Release 4.5
type: release
source_url: https://github.com/monero-project/monero/releases/tag/v0.18.4.5
author: binaryFate
tag_name: v0.18.4.5
published_at: '2026-01-11T16:08:32+00:00'
---

# Version: v0.18.4.5

# Release Notes
# Overview

This is the v0.18.4.5 release of the Monero software. This release fixes a bug with Ledger hardware wallet.

Some highlights of this release are:

- Ledger: fix Ledger Monero app crash (#10234)
- Ledger: add support for Ledger Nano Gen5 (#10243)
- Daemon: fix race condition causing dropped connections during sync (#10257)
- Wallet: fix edge case where key images remain marked unspent (#10255)
- Improve terminal color detection (#10268)
- Minor bug fixes and improvements

# Contributors for this Release

This release was the direct result of 7 people who worked to put out 16 commits containing 76 new lines of code. We'd like to thank them very much for their time and effort. In no particular order, they are:

- tobtoht
- plowsof
- nahuhh
- selsta
- laanwj
- iamamyth
- j-berman

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/cli/monero-win-x64-v0.18.4.5.zip)
[Windows, 32-bit](https://downloads.getmonero.org/cli/monero-win-x86-v0.18.4.5.zip)
[macOS, Intel](https://downloads.getmonero.org/cli/monero-mac-x64-v0.18.4.5.tar.bz2)
[macOS, ARM](https://downloads.getmonero.org/cli/monero-mac-armv8-v0.18.4.5.tar.bz2)
[Linux, 64-bit](https://downloads.getmonero.org/cli/monero-linux-x64-v0.18.4.5.tar.bz2)
[Linux, 32-bit](https://downloads.getmonero.org/cli/monero-linux-x86-v0.18.4.5.tar.bz2)
[Linux, armv7](https://downloads.getmonero.org/cli/monero-linux-armv7-v0.18.4.5.tar.bz2)
[Linux, armv8](https://downloads.getmonero.org/cli/monero-linux-armv8-v0.18.4.5.tar.bz2)
[Linux, riscv64](https://downloads.getmonero.org/cli/monero-linux-riscv64-v0.18.4.5.tar.bz2)
[Android, armv7](https://downloads.getmonero.org/cli/monero-android-armv7-v0.18.4.5.tar.bz2)
[Android, armv8](https://downloads.getmonero.org/cli/monero-android-armv8-v0.18.4.5.tar.bz2)
[FreeBSD, 64-bit](https://downloads.getmonero.org/cli/monero-freebsd-x64-v0.18.4.5.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-win-x64-v0.18.4.5.zip, a58132eefdecf6bd5443ae52fc15c0c371499de17223667173e5c81d12bfc2c5
monero-win-x86-v0.18.4.5.zip, 6a0eff6b06fe9b1372a64744900bfe19b47a532b6678d6f7055c2de9999b58d1
monero-mac-x64-v0.18.4.5.tar.bz2, b92a2cebde86bf87ebcdfa9cab8e20ae4b3697798058c3de71945267f361a984
monero-mac-armv8-v0.18.4.5.tar.bz2, f6b91dd7cb06483941945e6a1dc455ed80360092c138a1d1af53dc31985bd8d8
monero-linux-x64-v0.18.4.5.tar.bz2, 423b49f3658e29f70a1d971667dec924c7ee7a107cfc93440456e28500b471a6
monero-linux-x86-v0.18.4.5.tar.bz2, 9960aba30ab2ffc3450a4865e707a60615661ae5c32f3b90da74f1c0a38e4bc0
monero-linux-armv8-v0.18.4.5.tar.bz2, a1667e15307f0dfce2f25f882238c432aee14884219ff0d0be07d7bee959a903
monero-linux-armv7-v0.18.4.5.tar.bz2, 42fbcbcf678794d6b104134bb7218093d6aa2764cc9cfa6fad404a4648a7c38a
monero-linux-riscv64-v0.18.4.5.tar.bz2 ed06d510dc53412362fa22a2149d709eb3b60f973583ebf33bbfbc9edc58f2ab
monero-android-armv8-v0.18.4.5.tar.bz2, 4d48830d0d6494b27bf1144b9546e5e7bccc7eef0f6991a16ae2bf6ac71a69d9
monero-android-armv7-v0.18.4.5.tar.bz2, 3cd6611c5c33ae4c10e52698826560bbb17e00cf2f8a2d7f61e79d28f0f36ef6
monero-freebsd-x64-v0.18.4.5.tar.bz2, a2e924a2293e1d0c192f6e50748dcbcbb58dd9d5ad2b6733ffccefad37c556cf
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys). To ensure that the files you download are those originally posted by the maintainers, you should both check that the hashes of your files match those on the signed list, and that the signature on the list is valid.