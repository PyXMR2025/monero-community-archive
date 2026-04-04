---
title: Fluorine Fermi, Point Release 3.2
type: release
source_url: https://github.com/monero-project/monero/releases/tag/v0.18.3.2
author: binaryFate
tag_name: v0.18.3.2
published_at: '2024-03-10T19:58:53+00:00'
---

# Version: v0.18.3.2

# Release Notes
# Overview

This is the v0.18.3.2 release of the Monero software. This is a recommended release that adds support for RISC-V and contains important bug fixes.

Some highlights of this release are:

- Add RISC-V (riscv64) support (#9029)
- Daemon: multiple ZMQ bug fixes (#9053, #9080)
- Daemon: disable ports with I2P (#9142)
- Daemon: fix a bug that causes transactions to remain in the txpool (#9226)
- Daemon: fix `--max-txpool-weight` feature (#9226)
- Daemon: avoid slow fee RPC call response in edge cases (#9188)
- Wallet: adjust fee during backlog when set to `default` (#9220)
- Wallet: fix `set priority` getting ignored during transfers (#9220)
- Wallet: transfer amount with fee included (#8945)
- Wallet: mitigate statistical dependence for decoy selection within rings (#9130)
- Wallet: ensure transfers and sweeps use same fee calc logic (#9022)
- Wallet: better errors for small malformed multisig key exchange mesages (#9039)
- Wallet: fix multisig key memory leak (#9051)
- Add a workaround for a GCC compiler bug in JH hash (#9043)
- Add support for NO_COLOR enviroment variable (#9047)
- Reduce number of network packets sent for small HTTP bodies (#9020)
- Update RandomX to 1.2.1, fix a potential crash on macOS ARM (#9027)
- Update OpenSSL to 3.0.13, unbound to 1.19.1 (#9178)
- Minor bug fixes and improvements

# Contributors for this Release

This release was the direct result of 12 people who worked, largely unpaid and altruistically, to put out 65 commits containing 996 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- SChernykh
- moneromooo
- luigi1111
- selsta
- Crypto City
- tevador
- woodser
- jeffro256
- j-berman
- vtnerd
- tobtoht
- 0xFFFC0000

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/cli/monero-win-x64-v0.18.3.2.zip)
[Windows, 32-bit](https://downloads.getmonero.org/cli/monero-win-x86-v0.18.3.2.zip)
[macOS, Intel](https://downloads.getmonero.org/cli/monero-mac-x64-v0.18.3.2.tar.bz2)
[macOS, ARM](https://downloads.getmonero.org/cli/monero-mac-armv8-v0.18.3.2.tar.bz2)
[Linux, 64-bit](https://downloads.getmonero.org/cli/monero-linux-x64-v0.18.3.2.tar.bz2)
[Linux, 32-bit](https://downloads.getmonero.org/cli/monero-linux-x86-v0.18.3.2.tar.bz2)
[Linux, armv7](https://downloads.getmonero.org/cli/monero-linux-armv7-v0.18.3.2.tar.bz2)
[Linux, armv8](https://downloads.getmonero.org/cli/monero-linux-armv8-v0.18.3.2.tar.bz2)
[Linux, riscv64](https://downloads.getmonero.org/cli/monero-linux-riscv64-v0.18.3.2.tar.bz2)
[Android, armv7](https://downloads.getmonero.org/cli/monero-android-armv7-v0.18.3.2.tar.bz2)
[Android, armv8](https://downloads.getmonero.org/cli/monero-android-armv8-v0.18.3.2.tar.bz2)
[FreeBSD, 64-bit](https://downloads.getmonero.org/cli/monero-freebsd-x64-v0.18.3.2.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-win-x64-v0.18.3.2.zip, 61ae870024036f2000eaa0da72dfddbbfc494d7c0b9432ef656183e6ba3978cf
monero-win-x86-v0.18.3.2.zip, c84d94208cfdcd6af9ec541f8b2ea66fcfc8911c56dd21d7e313e8384c45b205
monero-mac-x64-v0.18.3.2.tar.bz2, 994d4ef86dde41ef6c61083806a8a2e4ae5c37cd56375f24e950c8765368e236
monero-mac-armv8-v0.18.3.2.tar.bz2, 1e43364b18edd2be913f80cd9ed4c7c42d61873c9557486a4c59b74366a1c5a0
monero-linux-x64-v0.18.3.2.tar.bz2, 9dafd70230a7b3a73101b624f3b5f439cc5b84a19b12c17c24e6aab94b678cbb
monero-linux-x86-v0.18.3.2.tar.bz2, 9857719c4dc35c3e38a7289b49f890d25ad62aba44a82fbcde194db1720d5cb2
monero-linux-armv8-v0.18.3.2.tar.bz2, 72f5c90955a736d99c1a645850984535050ebddd42c39a27eec1df82bd972126
monero-linux-armv7-v0.18.3.2.tar.bz2, 5df3a1390960c1632c797b8dfb46e93ebb2e93498e4e5e517be0bda6ff5b719b
monero-linux-riscv64-v0.18.3.2.tar.bz2 43bcb395cff51d90016bd34d75c7a339b1f0c3ea369b2258057d2b8ef972df81
monero-android-armv8-v0.18.3.2.tar.bz2, 7598672d552af3b711c3811683315c9661ff4c8059574afbbbf57abb71d029cd
monero-android-armv7-v0.18.3.2.tar.bz2, e61bf3d80de1d7ce92074570ce4d87316f7083de338e92d83f8987b4e3f4496d
monero-freebsd-x64-v0.18.3.2.tar.bz2, 0a07ff7697dad610d7b65ad7f2b083e4a50ce2d9c56736d20823786540840abc
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys). To ensure that the files you download are those originally posted by the maintainers, you should both check that the hashes of your files match those on the signed list, and that the signature on the list is valid.