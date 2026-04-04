---
title: Boron Butterfly
type: release
source_url: https://github.com/monero-project/monero/releases/tag/v0.14.0.0
author: fluffypony
tag_name: v0.14.0.0
published_at: '2019-02-25T16:39:55+00:00'
---

# Version: v0.14.0.0

# Release Notes
# Overview

This is the v0.14.0 release of the Monero software. This major release is due to the March 9th network update, which in turn adds a new PoW based on Cryptonight-R, adds a new block weight algorithm, and introduces a slightly more efficient RingCT format. This is a intermediary, stable release specifically for the network update, and does not represent the bulk of the effort on Monero over the past 6 months. That effort will be in the 0.14.1 release, which will follow in March after the network update.

Some highlights of this major release are:

- New PoW based on Cryptonight-R
- New block weight algorithm
- New slightly more efficient RingCT format
- Placeholder short payment ID to increase transaction uniformity
- Obsolete long payment IDs are now disabled unless a switch is used
- New event notifications for large block rate changes and blockchain reorgs
- Unmixable outputs can be spent again
- Fix bad pruned transactions JSON in RPC
- Some build fixes for various platforms/setups
- Fix for crash on exit

# Contributors for this Release

This intermediary release was the direct result of 11 people who worked, largely unpaid and altruistically, to put out 72 commits containing 5 981 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- stoffu
- SChernykh
- Lee Clagett
- Pol Mauri
- Tom Smeding
- Riccardo "fluffypony" Spagni
- cslashm
- xiphon
- moneromooo
- Jethro Grassie
- Dusan Klinec

# Official Download Links

- [Windows, 64-bit](https://downloads.getmonero.org/cli/monero-win-x64-v0.14.0.0.zip)
- [Windows, 32-bit](https://downloads.getmonero.org/cli/monero-win-x86-v0.14.0.0.zip)
- [macOS, 64-bit](https://downloads.getmonero.org/cli/monero-mac-x64-v0.14.0.0.tar.bz2)
- [Linux, 64-bit](https://downloads.getmonero.org/cli/monero-linux-x64-v0.14.0.0.tar.bz2)
- [Linux, 32-bit](https://downloads.getmonero.org/cli/monero-linux-x86-v0.14.0.0.tar.bz2)
- [Linux, armv7](https://downloads.getmonero.org/cli/monero-linux-armv7-v0.14.0.0.tar.bz2)
- [Linux, armv8](https://downloads.getmonero.org/cli/monero-linux-armv8-v0.14.0.0.tar.bz2)
- [FreeBSD, 64-bit](https://downloads.getmonero.org/cli/monero-freebsd-x64-v0.14.0.0.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

monero-win-x64-v0.14.0.0.zip, d65a98eec232219c8aee0023510ce162835cc8e567ff2d54fd23cca1e86f4c86
monero-win-x86-v0.14.0.0.zip, ca90d2e7bcc61b5983c38d32cab299e62f5e27a0daa95bf1b5b1e5eae4e60e0e
monero-mac-x64-v0.14.0.0.tar.bz2, 8307432e7a22da197bc5909e8ac5bbefda6ea5f826ebcc284592d3445dd71009
monero-linux-x64-v0.14.0.0.tar.bz2, 1e67163de7a924d65f30da251932ab31fdbccf8042d5e04ef63041709eec7854
monero-linux-x86-v0.14.0.0.tar.bz2, f452f4ab594c8ae7b93bd845dac8d6c0384498736711af2e8fcc8a5b2e628de0
monero-linux-armv8-v0.14.0.0.tar.bz2, 331ca2aa42e849ba0e69d2a2c52b9bec63e3f1793ff6c7a6a137cedc1b0d1980
monero-linux-armv7-v0.14.0.0.tar.bz2, caa37b27f0cd4dbe8a932cb2fee8c7e0713ce55759a72120310da1d675e61cd0
monero-freebsd-x64-v0.14.0.0.tar.bz2, d91c3fff2d120b9ad867e49b4d4834dbeacdfba6e55c9f7cbbc74e72a48d3d66

A GPG-signed list of the hashes is at https://getmonero.org/downloads/hashes.txt and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)