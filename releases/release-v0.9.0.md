---
title: Hydrogen Helix
type: release
source_url: https://github.com/monero-project/monero/releases/tag/v0.9.0
author: fluffypony
tag_name: v0.9.0
published_at: '2016-01-01T08:47:39+00:00'
---

# Version: v0.9.0

# Release Notes
# Overview

Too much to describe. Represents a major release in Monero's history, over a year-and-a-half in the making. Some highlights:
- moved from in-RAM database to a backend-agnostic blockchain database
- created an LMDB blockchainDB implementation (with the help of Howard Chu, the creator of LMDB)
- created a BerkeleyDB blockchainDB implementation
- created an OS-agnostic raw blockchain format
- built tools to convert between blockchain implementations, as well as import and export them
- added ARM support
- brought back 32-bit support (WIP)
- added QoS (bandwidth control)
- added [OpenAlias](https://openalias.org) support
- fixed all (previously broken) unit tests and core tests
- implemented daemonize for proper backgrounding of the Monero daemon
- drastically increased sync speed
- included block headers in the source
- designed and implemented a stealth payment ID scheme
- designed and implemented a unified address+payment ID scheme
- implemented a hard fork mechanism
- changed the block time to 2 minutes
- implemented the [MRL-0001](https://lab.getmonero.org/pubs/MRL-0001.pdf) and [MRL-0004](https://lab.getmonero.org/pubs/MRL-0004.pdf) recommendations
- added tons of simplewallet / rpcwallet / daemon commands
- added a dust handler to simplewallet
- created a multilanguage mechanism, implemented in simplewallet
- bug fixes, bug fixes, bug fixes
- completely overhauled the CMake (with the help of Kitware, the creators of CMake)
- added a bad peer auto-banning mechanism
- refactored a ton of code, added a ton of comments
- added a core crypto implementation based on SUPERCOP ref10
- switched to a triangular distribution for output selection
- added multiple new mnemonic wordlists, including Russian and Italian
- created a "trusted daemon" system for remote daemon use

In total this represents 922 commits worth of work by 9 contributors. This will probably be the biggest release in Monero's history, everything from here on out can be done as faster point releases.

# Updating: Blockchain Conversion

It is highly recommended that you delete the contents of your Monero working directory and sync from scratch. This directory can be found in ~/.bitmonero on Linux and OS X, and on Windows in \Users\username\AppData\Roaming\bitmonero or \ProgramData\bitmonero.

Syncing from scratch is EXTREMELY fast in this version, pretty much at bittorrent speeds, and will leave you with a fully verified blockchain.

_Alternatively_: if you want to grab the bootstrap (NOTE: there is a new bootstrap format!) off the website then you can get it at https://downloads.getmonero.org/blockchain.raw - once downloaded you can import it with `blockchain_import --input-file /path/to/your/download.raw`. If you're particularly brave you can pass the `--verify 0` flag to skip verification during import.

_If you REALLY want to convert your old blockchain_: you can either use the `blockchain_converter` tool, or you can use `blockchain_export` to create a blockchain.raw, followed by `blockchain_import` to import it into the new LMDB format.

# Official Download Links
- [Windows, 64-bit](https://downloads.getmonero.org/monero.win.x64.v0-9-0-0.zip)
- [OS X, 64-bit](https://downloads.getmonero.org/monero.mac.x64.v0-9-0-0.tar.bz2)
- [Linux, 64-bit](https://downloads.getmonero.org/monero.linux.x64.v0-9-0-0.tar.bz2)
