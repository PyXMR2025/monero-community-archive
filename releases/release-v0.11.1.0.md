---
title: Helium Hydra, Point Release 1 (GUI)
type: release
source_url: https://github.com/monero-project/monero-gui/releases/tag/v0.11.1.0
author: fluffypony
tag_name: v0.11.1.0
published_at: '2017-10-27T10:48:39+00:00'
---

# Version: v0.11.1.0

# Release Notes
# Overview

This is the v0.11.1.0 point release of the Monero GUI software, and it is part of the v0.11 mandatory update. The major release was due to the September 15th hard fork, which in turn increased the minimum ring signature size to 5 across the network, banned duplicate ring members in a ring signature, and enforced the use of ringCT for all transaction outputs. This release of the software presents a number of major improvements to Monero, as well as a large set of bug fixes.

[**The CLI release notes and downloads can be found on the release page here.**](https://github.com/monero-project/monero/releases/tag/v0.11.1.0)

Some highlights of this point release are:

- fixed a bug where, in an edge case, the wallet wouldn't see the first transaction to it
- added an option to change wallet creation height and rescan wallet cache
- changed the default required confirmations to 10
- reworked testnet settings in the wizard
- updated the Windows installer
- made the privacy slider smoother
- the password dialog box is now shown when making a transfer
- added a Romanian translation

Some highlights of the major release this is a part of are:

- Added and updated translations
- Smart mining enabled
- Added 'Rescanning Wallet Balance' feature
- Prep work for iOS and Android 
- displays view/spend keys when viewing Wallet seed on the Settings page
- added a Vulnerability Response Process, with bug bounties available via a dedicated HackerOne portal
- added easylogging option
- added custom blockchain location setting on the Settings page
- history now shows coinbase transactions
- wallet creation height and log file paths are now shown on the Settings page
- wallet will now only prompt for daemon auto start if the wallet is local
- lots of prep work for more streamlined remote node integration
- fixed 32 bit fonts
- bug fixes and performance improvements

# Contributors for this Release

This release was the direct result of 28 people who worked, largely unpaid and altruistically, to put out 211 commits containing 20 744 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- Fabio Nitto
- hesen
- René Brunner
- Nexie Kind
- MaxXor
- Dan Miller
- 8go
- erciccione
- Scott Anecito
- xmr-eric
- Jonathan Cross
- Schnoffel
- anonimal
- Jona
- Riccardo Spagni
- Mike C
- Jaquee
- Lafudoci
- Isaac
- Ordtrogen Översättning
- mastad0n
- Luigi Maselli
- Mandrill Pie
- Medusa
- Nano Akron
- vdo
- L.C. Karssen
- Light3rn
- MoroccanMalinois
- s0ds0ds0d
- redfish
- luigi1111
- ProkhorZ
- louvetic
- stoffu
- Guillaume Le Vaillant
- Helmut Pozimski
- Mattias Eriksson

# Official Download Links

- [Windows, 64-bit](https://downloads.getmonero.org/gui/monero-gui-win-x64-v0.11.1.0.zip)
- [macOS, 64-bit](https://downloads.getmonero.org/gui/monero-gui-mac-x64-v0.11.1.0.tar.bz2)
- [Linux, 64-bit](https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.11.1.0.tar.bz2)
- [Linux, 32-bit](https://downloads.getmonero.org/gui/monero-gui-linux-x86-v0.11.1.0.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

monero-gui-win-x64-v0.11.1.0.zip, 39d16f40fccf532b0193f33afd5a90c817c924e9abad41d4f4990a4c8c50ba97
monero-gui-mac-x64-v0.11.1.0.tar.bz2, 4f63ac3e9c5f87f8d8318ff89cdbfa954716e8addbdc8fcd0352fe678b84f8e2
monero-gui-linux-x64-v0.11.1.0.tar.bz2, e18a13f39a3b4aa87c9afdd9c87dfc087ed4940d99cf18c16ec59037e5f68eaf
monero-gui-linux-x86-v0.11.1.0.tar.bz2, 5df6ebeab728a653eaf64352bc60d8dddbf4d6a47a422856015d7e93ce5dc411

A GPG-signed list of the hashes is at https://getmonero.org/downloads/hashes.txt and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)