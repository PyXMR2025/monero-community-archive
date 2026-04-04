---
title: Boron Butterfly, Major Point Release 1
type: release
source_url: https://github.com/monero-project/monero/releases/tag/v0.14.1.0
author: luigi1111
tag_name: v0.14.1.0
published_at: '2019-07-17T20:16:56+00:00'
---

# Version: v0.14.1.0

# Release Notes
# Overview

This is the v0.14.1.0 point release of the Monero software, and it is part of the v0.14 network update. That major release was due to the March 9th network update, which in turn added a new PoW based on Cryptonight-R, added a new block weight algorithm, and introduced a slightly more efficient RingCT format. This release represents the bulk of the effort on Monero over the past 6 months, i.e., includes all new features.

Some highlights of this point release are:

- [Blockchain pruning.](https://web.getmonero.org/2019/02/01/pruning.html)
- [Deterministic (reproducible) builds.](https://github.com/monero-project/monero/tree/master/contrib/gitian#gitian-building)
- [Trezor support (for the model T).](https://monero.stackexchange.com/questions/11353/how-do-i-generate-a-trezor-monero-wallet-with-the-cli-monero-wallet-cli)
- [Ledger Nano X support.](https://monero.stackexchange.com/questions/8503/how-do-i-generate-a-ledger-monero-wallet-with-the-cli-monero-wallet-cli)
- [Tor & I2P (CLI) wallet integration.](https://github.com/monero-project/monero/blob/master/ANONYMITY_NETWORKS.md)
- [Multisig Messaging System](https://web.getmonero.org/resources/user-guides/multisig-messaging-system.html).
- [Further Bulletproofs verification optimizations.](https://web.getmonero.org/2019/02/01/pruning.html)
- JIT enabled, which drastically improves sync performance. 
- Bug fixes and further performance improvements.

Some highlights of the previous minor point release (v0.14.0.2) are:

- Added fix from Ledger for change bug with subaddresses
- Fix crafted coinbase tx mishandling in wallet
- Fix JIT build on mac
- Make slow hash request a restricted RPC request
- Fix off by one in block weight in regtest mode
- Fix fork rules determination for old daemons
- Fix estimated block height for GUI/API
- Fix sync wedge when an incoming tx is already in the pool

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

This intermediary release was the direct result of 77 people who worked, largely unpaid and altruistically, to put out 1551 commits containing 81 191 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- TheCharlatan
- moneromooo-monero
- Riccardo Spagni
- Howard Chu
- Dusan Klinec
- xiphon
- Jesse Jackson
- Tadeas Moravec
- Lee Clagett
- stoffu
- cslashm
- Nathan Dorfman
- Jethro Grassie
- selsta
- Martijn Otto
- Paul Shapiro
- Rohaq
- K3v1n Kur14k053
- moneromooo
- erciccione
- fireice-uk
- Jason Wong
- SChernykh
- Doyle
- who-biz
- Sarang Noether
- italocoin
- Pol Mauri
- ston1th
- iDunk5400
- Tyler Saballus
- Gregory Lemercier
- moneroexamples
- Justin Gerber
- binaryFate
- cryptochangements34
- AnythingTechPro
- buricl
- Tom Smeding
- Lafudoci
- doy-lee
- Joel
- Hasan Pekdemir
- Tyler Baker
- mmitkevich
- naughtyfox
- fuwa
- Cactii1
- Leon Klingele
- Michał Sałaban
- RaskaRuby
- Gingeropolous
- rbrunner7
- David Meister
- Jean-Michel DILLY
- Norman Moeschter
- spoke0
- Guillaume LE VAILLANT
- Guido Vranken
- Ted Moravec
- m2049r
- Jane Mercer
- sachaaaaa
- Aniket Pradhan
- anonimal
- Dimitris Apostolou
- Hom DX
- Neofito89
- George
- Markus Behm
- Ricardo de Vries
- Florian
- monerorus
- Jkat
- MoroccanMalinois
- sanecito
- Monero-Pootle

# Official Download Links

- [Windows, 64-bit](https://downloads.getmonero.org/cli/monero-win-x64-v0.14.1.0.zip)
- [Windows, 32-bit](https://downloads.getmonero.org/cli/monero-win-x86-v0.14.1.0.zip)
- [macOS, 64-bit](https://downloads.getmonero.org/cli/monero-mac-x64-v0.14.1.0.tar.bz2)
- [Linux, 64-bit](https://downloads.getmonero.org/cli/monero-linux-x64-v0.14.1.0.tar.bz2)
- [Linux, 32-bit](https://downloads.getmonero.org/cli/monero-linux-x86-v0.14.1.0.tar.bz2)
- [Linux, armv7](https://downloads.getmonero.org/cli/monero-linux-armv7-v0.14.1.0.tar.bz2)
- [Linux, armv8](https://downloads.getmonero.org/cli/monero-linux-armv8-v0.14.1.0.tar.bz2)
- [FreeBSD, 64-bit](https://downloads.getmonero.org/cli/monero-freebsd-x64-v0.14.1.0.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

monero-win-x64-v0.14.1.0.zip: `ca4367c565026ea23bf90180cdd750a1d6adfab36ee19435e91ed740a369a6fc`
monero-win-x86-v0.14.1.0.zip: `ed26ad4c7f3fc15893c615e438a76f91c8c5c18e29d32bf350e126beecc2877f`
monero-mac-x64-v0.14.1.0.tar.bz2: `96ae0af11cdf4ad66326ae128675d6476088719ed3d226a7dbc903767f3a858a`
monero-linux-x64-v0.14.1.0.tar.bz2: `2b95118f53d98d542a85f8732b84ba13b3cd20517ccb40332b0edd0ddf4f8c62`
monero-linux-x86-v0.14.1.0.tar.bz2: `a31bca6e556064d56f7a37ddbea26408902e5f387e5b67fa5b0999ca299b8eef`
monero-linux-armv7-v0.14.1.0.tar.bz2: `b95903a0f1b0c15cefdf59814fe12e3597a3322ae6d0567c732f0ab79c877724`
monero-linux-armv8-v0.14.1.0.tar.bz2: `cf46a1cdea6f7983697df6dfbbb184b6dd23e816ed156899070885a78b310171`
monero-freebsd-x64-v0.14.1.0.tar.bz2: `17f21d718ad0ba6d7965004ed8390a01a9ccf06ef95891ab26bd6592a7169c58`

A GPG-signed list of the hashes is at https://getmonero.org/downloads/hashes.txt and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)