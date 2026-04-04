---
title: Lithium Luna, Point Release 2
type: release
source_url: https://github.com/monero-project/monero/releases/tag/v0.12.2.0
author: fluffypony
tag_name: v0.12.2.0
published_at: '2018-06-04T19:16:07+00:00'
---

# Version: v0.12.2.0

# Release Notes
# Overview

This is the v0.12.2.0 point release of the Monero software, and it is part of the v0.12 network wide update. The major release was due to the April 6th network update, which in turn increased the minimum ring signature size, sorted inputs so as not to leak wallet choice by inference, and slightly changed the proof-of-work algorithm to prevent DoS attacks by ASICs. This release of the software presents a number of major improvements to Monero, as well as a large set of bug fixes.

Some highlights of this point release are:

- mention announcement mailing list in README.md (lists.getmonero.org)
- fix PCSC on windows (for Ledger support)
- various build fixes
- fix fee display unit when the unit is not the default
- fixes for lengthy waits (and timeouts) when sending transactions and parsing ring history
- automatically pop old version blocks if the user failed to update in time
- fix sweep_unmixable output selection after the recent min ring size bump
- sync fixes
- document the need for building dependencies with -fPIC
- fix bandwidth limit commands scaling
- fix disabling logs (--log-level "")
- reuse connections in the wallet API
- fix reading some arguments from the config file
- log stack trace on crash (wonky on windows)
- fix loading the txpool with colliding key images
- fix errors when the shared ringdb fails to initialize
- fix destination ordering
- fix endianness dependence in subaddress generation
- fast scan mode for Ledger (exposes view key to the host computer)

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

- [Windows, 64-bit](https://downloads.getmonero.org/cli/monero-win-x64-v0.12.2.0.zip)
- [Windows, 32-bit](https://downloads.getmonero.org/cli/monero-win-x86-v0.12.2.0.zip)
- [macOS, 64-bit](https://downloads.getmonero.org/cli/monero-mac-x64-v0.12.2.0.tar.bz2)
- [Linux, 64-bit](https://downloads.getmonero.org/cli/monero-linux-x64-v0.12.2.0.tar.bz2)
- [Linux, 32-bit](https://downloads.getmonero.org/cli/monero-linux-x86-v0.12.2.0.tar.bz2)
- [Linux, ARMv7](https://downloads.getmonero.org/cli/monero-linux-armv7-v0.12.2.0.tar.bz2)
- [Linux, ARMv8](https://downloads.getmonero.org/cli/monero-linux-armv8-v0.12.2.0.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

monero-win-x64-v0.12.2.0.zip, 188e122e4ec84994cfb8f8f1582514359c0e9e7b121a288362016565ba9d58da
monero-win-x86-v0.12.2.0.zip, 4a1718e75e2467f9a4b02b5c342b702999c97b1c0f8a1cdd5a63d7c2b21f849a
monero-mac-x64-v0.12.2.0.tar.bz2, 31568fdedf9557e5d8398013137266afe0e7ed46011691fef1b40ea7cd94e090
monero-linux-x64-v0.12.2.0.tar.bz2, cb97e3f8b700a81e1b0f1a77509eefbfb415aa6013f23685f8933b559309c580
monero-linux-x86-v0.12.2.0.tar.bz2, 99de2b8b5c60ce3d0fceda8607e5b1fcac22c2971f2b8f9016c5acb207587513
monero-linux-armv7-v0.12.2.0.tar.bz2, f4b7f3fe46d95f8499253c515401c01efb707a7362fec49ca4527ee5839331b3
monero-linux-armv8-v0.12.2.0.tar.bz2, 5ff435057d87952e70a5be4e7edf62440eeeb532734e739e208a9eca67c569c6

A GPG-signed list of the hashes is at https://getmonero.org/downloads/hashes.txt and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)