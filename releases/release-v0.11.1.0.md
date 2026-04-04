---
title: Helium Hydra, Point Release 1
type: release
source_url: https://github.com/monero-project/monero/releases/tag/v0.11.1.0
author: fluffypony
tag_name: v0.11.1.0
published_at: '2017-10-25T15:27:26+00:00'
---

# Version: v0.11.1.0

# Release Notes
# Overview

This is the v0.11.1.0 point release of the Monero software, and it is part of the v0.11 mandatory update. The major release was due to the September 15th hard fork, which in turn increased the minimum ring signature size to 5 across the network, banned duplicate ring members in a ring signature, and enforced the use of ringCT for all transaction outputs. This release of the software presents a number of major improvements to Monero, as well as a large set of bug fixes.

[**The GUI release notes and downloads can be found on the release page here.**](https://github.com/monero-project/monero-core/releases/tag/v0.11.1.0)

Some highlights of this point release are:

- fixed an occasional sync failure that occurred when a transaction was already in the mempool
- added an underflow check on low block heights
- added a guard against a mined block not finding all the transactions in the mempool
- fixed the transaction size estimator for transactions with a large number of inputs
- fixed an LMDB issue on 32-bit systems
- the get_tx_backlog RPC call was unrestricted
- threads now guard against exceptions during transaction verification
- fixed a crash that could occur when checking pre-validated transactions
- various other bug fixes and improvements

Some highlights of the major release this is a part of are:

- major synchronisation speed-up from reducing bandwidth used
- massively improved the blockchain import function
- changed terminology from "mixin" to "ring size"
- add a --fluffy-blocks option to relay blocks as fluffy blocks if possible
- allow for password verification without loading the subsequently unencrypted wallet into RAM
- reduced privacy leak risks when using untrusted remote nodes
- added an Esperanto wordlist for mnemonic seed choices
- decreased memory demands for the getblocks RPC call
- added a "fee" command to display fee information
- transfer CLI command warns if there's a tx backlog for selected fee
- add average seconds per block in bc\_dyn\_stats
- added an on\_get\_alt\_blocks\_hashes RPC call 
- added an Italian translation for the CLI
- return the per-tx amount in the transfer\_split RPC call
- switched to readline for the CLI
- automatically switch to SAFE db-sync-mode once daemon catches up to network
- added a histogram to poolstats
- major speed-up for poolstats and coinbase\_tx\_sum
- enable support for macOS smart mining
- added the ability to build a Snap package
- added a Vulnerability Response Process, with bug bounties available via [a dedicated HackerOne portal](https://hackerone.com/monero)
- added support for payment proving via key derivation instead of tx key reveal
- changed output selection for ring signatures to heavily weight newer outputs
- added a sweep\_below function to sweep small amounts
- moved the mempool to a database on disk instead of keeping it all in memory
- fully enable iOS and Android full node support
- enabled support for ppc64le architectures
- added the ability to create and open wallets via RPC
- added ability to relay transactions manually after creating them
- better AC / battery power detection for Linux smart mining
- getblocktemplate now indicates the expected total reward
- as always, loads of bug fixes and performance improvements

# Contributors for this Release

This release was the direct result of 39 people who worked, largely unpaid and altruistically, to put out 583 commits containing 60 350 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- moneromooo
- kenshi84
- Roberto Oliveira
- Lee Clagett
- Eugene Otto
- MoroccanMalinois
- Michael Shick
- JollyMort
- Erik de Castro Lopo
- anonimal
- erciccione
- Guillaume Le Vaillant
- rbrunner7
- binaryFate
- Riccardo "fluffypony" Spagni
- Jaquee
- Julien Klepatch
- moneroexamples
- Nano Akron
- Antti Keränen
- Jethro Grassie
- xmr-eric
- schnerchi
- MaxXor
- Andrei Muresan
- Jkat
- stoffu
- Mike C
- Gingeropolous
- Jonathan Cross
- m2049r
- Miguel Herranz
- Randi Joseph
- assylias
- Martin Wimpress
- Ryan Mehta
- Gentian
- Robby Weinberg
- Howard Chu

# Official Download Links

- [Windows, 64-bit](https://downloads.getmonero.org/cli/monero-win-x64-v0.11.1.0.zip)
- [Windows, 32-bit](https://downloads.getmonero.org/cli/monero-win-x86-v0.11.1.0.zip)
- [macOS, 64-bit](https://downloads.getmonero.org/cli/monero-mac-x64-v0.11.1.0.tar.bz2)
- [Linux, 64-bit](https://downloads.getmonero.org/cli/monero-linux-x64-v0.11.1.0.tar.bz2)
- [Linux, 32-bit](https://downloads.getmonero.org/cli/monero-linux-x86-v0.11.1.0.tar.bz2)
- [Linux, armv7](https://downloads.getmonero.org/cli/monero-linux-armv7-v0.11.1.0.tar.bz2)
- [Linux, armv8](https://downloads.getmonero.org/cli/monero-linux-armv8-v0.11.1.0.tar.bz2)
- [FreeBSD, 64-bit](https://downloads.getmonero.org/cli/monero-freebsd-x64-v0.11.1.0.tar.bz2)
- [DragonflyBSD, 64-bit](https://downloads.getmonero.org/cli/monero-dragonflybsd-x64-v0.11.1.0.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

monero-win-x64-v0.11.1.0.zip, 81f80876b5ce95b4c94b858bd4b57d2ac808e52e7b98819ab5c33be8ecbc09ae
monero-win-x86-v0.11.1.0.zip, d1c1c2e75211143f935c2e06cf09892e7118e46fbb1d5fc240cde9cb1d3b92c9
monero-mac-x64-v0.11.1.0.tar.bz2, 75b12623760574688572adfb10504d872d60ca7c4ac7571011d62429d6288e50
monero-linux-x64-v0.11.1.0.tar.bz2, 6581506f8a030d8d50b38744ba7144f2765c9028d18d990beb316e13655ab248
monero-linux-x86-v0.11.1.0.tar.bz2, ef212bda6b9a30af2a3e7e94cb2af4dd6e01eb0f54a4d1c0eb25abe75316e2ae
monero-linux-armv7-v0.11.1.0.tar.bz2, 72d48a83189e3f99e7bd3d0ceab34e7466d99ec4ca85bb8e7b81ed338c692a46
monero-linux-armv8-v0.11.1.0.tar.bz2, f1f0850e37eb65595d8e92eb2b84f5119165f418ab54a72dfa8a149e0efa810b
monero-freebsd-x64-v0.11.1.0.tar.bz2, bd2090f643d212a4031edbf44a8f1425cf335b6b63c6527a7e82f5bc6a83db67
monero-dragonflybsd-x64-v0.11.1.0.tar.bz2, 30e2d50db8e1738a72d3a06ec106c1a3f157de057efad344bd12151b6bbd3019

A GPG-signed list of the hashes is at https://getmonero.org/downloads/hashes.txt and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)