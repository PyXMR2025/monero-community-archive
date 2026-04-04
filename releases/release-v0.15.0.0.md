---
title: Carbon Chamaeleon
type: release
source_url: https://github.com/monero-project/monero/releases/tag/v0.15.0.0
author: luigi1111
tag_name: v0.15.0.0
published_at: '2019-11-12T13:26:34+00:00'
---

# Version: v0.15.0.0

# Release Notes
This is the v0.15.0 release of the Monero software. This major release is due to the November 30th network update, which in turn adds a new PoW, RandomX.

# Overview

Some highlights of this major release are:

- Android builds
- Better readline support
- Info leak fixes when an adversary can perform traffic analysis between a wallet and a node (reported by: Florian Tramèr, Dan Boneh, and Kenneth G. Paterson)
- New PoW based on random instructions, adapted to CPUs
- Pay for service system (either for nodes to offer paid RPC, or third parties to offer services paid for via monero mining)
- Optional Tor/I2P transaction relay for privacy (block relay being done on clearnet)
- New gen_ssl_cert tool to generate SSL certificates suitable for Monero usage
- Difficulty can now range 128 bits
- Windows logging colour support
- SSL timeout fixes
- New wallet commands: public_nodes, restore_height
- New daemon commands: set_bootstrap_daemon
- New daemon RPC: flush_cache, get_public_nodes, set_bootstrap_daemon
- New wallet RPC: edit_address_book
- New wallet command line switches: --no-zmq, --restore-from-seed, --extra-entropy, --rpc-bind-ipv6-address, --rpc-use-ipv6, --rpc-require-ipv4
- New wallet settings: ignore-outputs-above, ignore-outputs-below, export-format
- New dameon commands: --tx-proxy, --p2p-bind-ipv6-address, --p2p-bind-port-ipv6, --rpc-bind-ipv6-address, --p2p-use-ipv6, --rpc-use-ipv6, --p2p-require-ipv4, --rpc-require-ipv4, --keep-alt-blocks
- Fees are now based on median block weight
- Daemons can now optionally sync off pruned data
- Consensus changes: forbid transaction with just one output, use effective median block weight for penalty, enforced 10 block minimum output age for use in rings, reject signatures in coinbase txes, reject v1 coinbase txes
- Python3 compatibility in tests
- Many more tests
- Translations now use Weblate rather than Pootle
- Guard against generating bad block templates in pathological case
- Fix get_reserve_proof when some outputs are sent but not mined yet
- New locked field in get_transfers/get_{bulk_,}_payments
- Fixes for syncing on big endian
- Verification speedups 
- add pruned and publicrpc flags to print_pl 
- Automatic public nodes discovery and bootstrap daemon switching
- New release field to get_version daemon RPC
- Ledger improvements 
- Some protection against isolation by rotating a small amount of nodes
- New seed node
- The wallet can now export data in ASCII (text) format
- Inactivity lock in wallet
- Peer list sanitization
- riscv 64 bit support
- Various networking fixes and improvements
- Better Unicode support in RPC
- IPv6 support
- Standalone payment IDs creation code removed
- Allow blocking whole subnets
- export_key_images and export_outputs can now export incrementally or fully
- Many improvements in depends build system
- Remove dead xiala.net from default DNS resolvers
- RPC connections are now affected by bans
- Misc DoS and robustness fixes
- Fix v1 transaction retrieval from the txpool
- White noise system to frustrate traffic analysis
- delay IGP probing on startup
- Fix committing some data to the database on batch error
- allow exporting blocks.dat format from a pruned blockchain
- Fix wallet SSL cert issues
- alt_chain_info can now display information about a particular alt chain
- Keep alternative blocks in LMDB
- User prompt when a tx sends more than one old output

# Contributors for this Release

This intermediary release was the direct result of 95 people who worked, largely unpaid and altruistically, to put out 706 commits containing 283980 new lines of code. We'd like to thank them very much for their time and effort.

- anonimal
- binaryFate
- cslashm
- Doyle
- dsc
- Dusan Klinec
- erciccione
- Gingeropolous
- Guillaume Le Vaillant
- Harry MacFinned
- HomDX
- Howard Chu
- hyperreality
- iamamyth
- iDunk5400
- Jake Hemmerle
- Jason Rhinelander
- Jesus Ramirez
- JesusRami
- Jethro Grassie
- Jonathan Cross
- Lazaridis
- Lee Clagett
- Lev Sizov
- luigi1111
- Martijn Otto
- Matyas Liptak
- Michal vel m@lbit
- moneromooo-monero
- Mr. Me0w
- Nathan Dorfman
- Nejcraft
- Noel O'Donnell
- pkubaj
- rbrunner7
- redfish
- Riccardo Spagni
- Sarang Noether
- selene
- selsta
- SomaticFanatic
- stoffu
- ston1th
- Tadeas Moravec
- tevador
- TheCharlatan
- TheQuantumPhysicist
- Thomas Winget
- thotbot
- tobtoht
- Tom Smeding
- TrasherDK
- vicsn
- wowario
- xiphon
- Your Name

Special thanks to our translators for this release: Agent LvM, TheFuzzStone, erciccione, Luca Ciavatta, Alessandro Lotta, stefanomarty, Lafudoci, Assumpta Anglada, BennyBeat, Ecron, Joan Montané, Russian Bear, Andrew Onishi, Scott Anecito, el00ruobuob, glv2, Viktor, dskch83, jindouyunz, TE Scott, razorshaman909, Jonathan Heirbaut, siesero, fullmetalScience, Christian, M5M400, Sneaky Squid, Paul Rant, Tim Hartmann

# Official Download Links

- [Windows, 64-bit](https://downloads.getmonero.org/cli/monero-win-x64-v0.15.0.0.zip)
- [Windows, 32-bit](https://downloads.getmonero.org/cli/monero-win-x86-v0.15.0.0.zip)
- [macOS, 64-bit](https://downloads.getmonero.org/cli/monero-mac-x64-v0.15.0.0.tar.bz2)
- [Linux, 64-bit](https://downloads.getmonero.org/cli/monero-linux-x64-v0.15.0.0.tar.bz2)
- [Linux, 32-bit](https://downloads.getmonero.org/cli/monero-linux-x86-v0.15.0.0.tar.bz2)
- [Linux, armv7](https://downloads.getmonero.org/cli/monero-linux-armv7-v0.15.0.0.tar.bz2)
- [Linux, armv8](https://downloads.getmonero.org/cli/monero-linux-armv8-v0.15.0.0.tar.bz2)
- [FreeBSD, 64-bit](https://downloads.getmonero.org/cli/monero-freebsd-x64-v0.15.0.0.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

monero-win-x64-v0.15.0.0.zip, 6b72b3836d179eb517154bbcb8e2119b168ae9d1054866a438aaeab9521f795f
monero-win-x86-v0.15.0.0.zip, b4856d0d3389497bf103d5a4dc4e73c6a39e5be20736b3e0286e76f100c508b6
monero-mac-x64-v0.15.0.0.tar.bz2, bca6b776e7e906fcda4c829aa8666eb9d92014450b87a6723a7c6eda6d6e7de1
monero-linux-x64-v0.15.0.0.tar.bz2, 53d9da55137f83b1e7571aef090b0784d9f04a980115b5c391455374729393f3
monero-linux-x86-v0.15.0.0.tar.bz2, 2197d04f4ffad4e1344b2648273f0be152de637bafc5d940cdf215cbc50e1f79
monero-linux-armv8-v0.15.0.0.tar.bz2, f92f0acbc49076ad57337b5928981cd72c01aabe6a8eb69a1782f7fa1388fb77
monero-linux-armv7-v0.15.0.0.tar.bz2, 326f783ffde78694b2820c95aa310ead00bb5876937ed4edf9c1abd6b6aadc02
monero-freebsd-x64-v0.15.0.0.tar.bz2, hash

A GPG-signed list of the hashes is at https://getmonero.org/downloads/hashes.txt and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)
