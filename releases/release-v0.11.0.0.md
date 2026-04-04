---
title: Helium Hydra (GUI)
type: release
source_url: https://github.com/monero-project/monero-gui/releases/tag/v0.11.0.0
author: fluffypony
tag_name: v0.11.0.0
published_at: '2017-09-24T13:35:10+00:00'
---

# Version: v0.11.0.0

# Release Notes
# Overview

This is the v0.11.0.0 major release of the Monero GUI software, and it is a mandatory update due to the September 15th hard fork, which in turn increases the minimum ring signature size to 5 across the network, bans duplicate ring members in a ring signature, and enforces use of ringCT for all transaction outputs. This release of the software presents a number of major improvements to Monero, as well as a large set of bug fixes.

[**The CLI release notes and downloads can be found on the release page here.**](https://github.com/monero-project/monero/releases/tag/v0.11.0.0)

Some highlights of this release are:

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

This release was the direct result of 28 people who worked, largely unpaid and altruistically, to put out 169 commits containing 18 169 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- anonimal
- s0ds0ds0d
- Guillaume Le Vaillamt
- Schnoffel
- ProkhorZ
- 8go
- Fabio Nitto
- L.C. Karssen
- Nano Akron
- Mike C
- erciccione
- xmr-eric
- Mattias Eriksson
- Jona
- vdo
- hesen
- louvetic
- MaxXor
- Scott Anecito
- René Brunner
- Medusa
- MoroccanMalinois
- Riccardo "fluffypony" Spagni
- Ordtrogen Översättning
- Lafudoci
- Jonathan Cross
- Jaquee
- Luigi Maselli

# Official Download Links
- [Windows, 64-bit](https://downloads.getmonero.org/gui/monero-gui-win-x64-v0.11.0.0.zip)
- [macOS, 64-bit](https://downloads.getmonero.org/gui/monero-gui-mac-x64-v0.11.0.0.tar.bz2)
- [Linux, 64-bit](https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.11.0.0.tar.bz2)
- [Linux, 32-bit](https://downloads.getmonero.org/gui/monero-gui-linux-x86-v0.11.0.0.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

monero-gui-win-x64-v0.11.0.0.zip, 52edde05fdac17a99441dc7b695ebba40a08fda3d1628d5f1f4424f8ffd531d6
monero-gui-mac-x64-v0.11.0.0.tar.bz2, 5bbb85762811b763f0913706ea7f9de944b042688adb27e828937eb7884fc322
monero-gui-linux-x64-v0.11.0.0.tar.bz2, 25bdeeb9072b679eda4aca2a5dac0351393d6bd8ceed1822bf65495ab6d113bf
monero-gui-linux-x86-v0.11.0.0.tar.bz2, 284b30fe84c92407117b7dcabc324c12050196e520d64ff5601a031dfbc7bb90

A GPG-signed list of the hashes is at https://getmonero.org/downloads/hashes.txt and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)