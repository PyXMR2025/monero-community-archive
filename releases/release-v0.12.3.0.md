---
title: Lithium Luna, Point Release 3
type: release
source_url: https://github.com/monero-project/monero/releases/tag/v0.12.3.0
author: fluffypony
tag_name: v0.12.3.0
published_at: '2018-07-23T20:45:10+00:00'
---

# Version: v0.12.3.0

# Release Notes
# Overview

This is the v0.12.3.0 point release of the Monero software, and it is part of the v0.12 network wide update. The major release was due to the April 6th network update, which in turn increased the minimum ring signature size, sorted inputs so as not to leak wallet choice by inference, and slightly changed the proof-of-work algorithm to prevent DoS attacks by ASICs. This release of the software presents a number of major improvements to Monero, as well as a large set of bug fixes.

Some highlights of this point release are:

- Fix for overly abrupt remote node timeouts
- Fix for edge case where a wallet might incorrectly report received Monero

Some highlights of this major release are:

- tweaked PoW to block DoS attacks from ASICs
- added input ordering to prevent wallet inference
- increased minimum ring size from 5 to 7
- subaddress support added, with addresses starting with a prefix of 8
- added multisig support
- added support for SunOS / Solaris
- initial support for Ledger Nano S hardware wallet
- added seed encryption by password
- securely erase keys from memory, for most cases, when no longer in use
- initial Bulletproofs implementation live on testnet
- added accounts, tags, and labels, via subaddresses
- added initial, quite rough support for 0MQ
- added some mitigations for privacy-threatening key reusing forks
- added a new network, stagenet, which mirrors mainnet's features
- added SSL support for light wallet API
- added CORS support to the RPC stack
- added a --generate-from-spend-key flag to the CLI wallet
- added a --disable-dns-checkpoints flag to the daemon
- massive improvements to build hardening
- added native fuzz testing for user input
- added the ability to limit inbound connections
- enabled "fluffy blocks" by default
- added a --max-txpool-size mempool size limit flag
- allow a remote node to temporarily process RPC requests during IBD
- added a relay_tx command to the RPC wallet
- allow for spend key retrieval via RPC wallet call
- made libraries use position independent code
- improvements made to Docker image
- added a sweep_single command to the CLI wallet
- made RPC error codes more specific
- improved stack trace printing, and noted stack trace lib in output
- split and refactored wallet_api from wallet code
- added priority arguments to sweep_all and donate CLI wallet commands
- added a --do-not-relay option to the CLI wallet
- made the hashchain unit tests work again
- added tests for subaddress expansion
- added RingCT performance tests
- added package installation instructions for Void Linux
- made changes to ensure no sensitive data is logged accidentally
- added a Croatian mnemonic word list
- added a Lojban mnemonic word list
- added a Swedish CLI translation
- added stoffu's GPG key to the source code
- added an timeoue for connections which don't complete a handshake
- moved test building to the end of the CMake build process
- as always, loads of bug fixes and performance improvements

# Contributors for this Release

This release was the direct result of 87 people who worked, largely unpaid and altruistically, to put out 1 649 commits containing 56 735 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- Onur Altun
- Leon Klingele
- Jean Pierre Dudey
- vasi
- Howard Chu
- Thaer Khawaja
- flozilla
- Bertrand Jacquin
- 0xB44EFD8751077F97
- Gene Peters
- erciccione
- ston1th
- luigi1111
- cryptochangements34
- Ordtrogen Översättning
- kenshi84
- Calvin Liang
- Dimitris Apostolou
- MaxXor
- Jan Beich
- Pavel Maryanov
- Orestis Konstantinidis
- Alexander Azarov
- stoffu
- landergate
- Gingeropolous
- AnythingTechPro
- MoroccanMalinois
- Thomas Winget
- Timothy D. Prime
- Michał Sałaban
- anonimal
- guzzijones
- Jethro Grassie
- rbrunner7
- Jaquee
- Guillaume Le Vaillant
- xmr-eric
- moneroexamples
- AJIekceu4
- whythat
- Riccardo "fluffypony" Spagni
- selsta
- Neozaru
- Mike C
- damir
- iDunk5400
- Mikhail Mitkevichl
- Edward Betts
- Helmut Pozimski
- Nano Akron
- h908714124
- m2049r
- Jonny Heggheim
- Maxithi
- lancillotto
- Maxime Thiebaut
- vdo
- dEBRUYNE-1
- Bruno Clermont
- Tobias Hoffmann
- Lee Clagett
- Nick Johnson
- aivve
- cslashm
- Tim L
- Erik de Castro Lopo
- sneurlax
- Tadeas Moravec
- binaryFate
- Emilien Devos
- Gareth Hayes
- moneromooo
- Dmitriy Plekhanov
- Matt Smith
- Dusan Klinec
- Maximilian Lupke
- SChernykh
- Matthew Campassi
- Vasil Dimov
- redfish
- Serhack
- Matt Little
- Cifrado
- Cole Lightfighter
- Dyrcona
- Wei Tang

# Official Download Links

- [Windows, 64-bit](https://downloads.getmonero.org/cli/monero-win-x64-v0.12.3.0.zip)
- [macOS, 64-bit](https://downloads.getmonero.org/cli/monero-mac-x64-v0.12.3.0.tar.bz2)
- [Linux, 64-bit](https://downloads.getmonero.org/cli/monero-linux-x64-v0.12.3.0.tar.bz2)
- [Linux, 32-bit](https://downloads.getmonero.org/cli/monero-linux-x86-v0.12.3.0.tar.bz2)
- [Linux, ARMv7](https://downloads.getmonero.org/cli/monero-linux-armv7-v0.12.3.0.tar.bz2)
- [Linux, ARMv8](https://downloads.getmonero.org/cli/monero-linux-armv8-v0.12.3.0.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

monero-win-x64-v0.12.3.0.zip, 5c06097acebf643857672e673258d16d66a71de504377399b7407318f9887ee3
monero-mac-x64-v0.12.3.0.tar.bz2, 39d40e2001ca9948f434637c28b3933c0d79c66e2db07ffc4274711ab2d2ae66
monero-linux-x64-v0.12.3.0.tar.bz2, 72fe937aa2832a0079767914c27671436768ff3c486597c3353a8567d9547487
monero-linux-x86-v0.12.3.0.tar.bz2, 41d68f66a43098754de0d2ead0eaeb125fc7eb05ecf3eb6a48c96ce6874052f3
monero-linux-armv7-v0.12.3.0.tar.bz2, 839bddb01214acb8f7bc12181b206e1e8d99314337addef7ba850b15c32dc685
monero-linux-armv8-v0.12.3.0.tar.bz2, a6e994dc9fcec7259b656752a6fc0f9686bad47da9deec0f50398718cd9b9be8

A GPG-signed list of the hashes is at https://getmonero.org/downloads/hashes.txt and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)