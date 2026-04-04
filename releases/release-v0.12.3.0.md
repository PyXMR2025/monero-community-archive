---
title: Lithium Luna, Point Release 3
type: release
source_url: https://github.com/monero-project/monero-gui/releases/tag/v0.12.3.0
author: luigi1111
tag_name: v0.12.3.0
published_at: '2018-07-26T22:19:27+00:00'
---

# Version: v0.12.3.0

# Release Notes
# Overview

This is the v0.12.3.0 point release of the Monero GUI software, and it is part of the v0.12 network wide update. This major release is due to the April 6th network update, which in turn increases the minimum ring signature size, sorts inputs so as not to leak wallet choice by inference, and slightly changes the proof-of-work algorithm to prevent DoS attacks by ASICs. This release of the software presents a number of major improvements to Monero, as well as a large set of bug fixes.

[**The CLI release notes and downloads can be found on the release page here.**](https://github.com/monero-project/monero/releases/tag/v0.12.3.0)

Some highlights of this release are:

- Fix for overly abrupt remote node timeouts
- Fix for edge case where a wallet might incorrectly report received Monero

# Official Download Links

- [Windows GUI, 64-bit](https://downloads.getmonero.org/gui/monero-gui-win-x64-v0.12.3.0.zip)
- [macOS GUI, 64-bit](https://downloads.getmonero.org/gui/monero-gui-mac-x64-v0.12.3.0.tar.bz2)
- [Linux GUI, 64-bit](https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.12.3.0.tar.bz2)
- [Linux GUI, 32-bit](https://downloads.getmonero.org/gui/monero-gui-linux-x86-v0.12.3.0.tar.bz2)

# Download Hashes
If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

monero-gui-linux-x64-v0.12.3.0.tar.bz2, dcf0a103589b8e71cdb8298dec96610f9f50b25e8f48afef5186d4c460a4ecae
monero-gui-linux-x86-v0.12.3.0.tar.bz2, 6858519657add070aeedb03a22d4661ec1b868acdd0b3437fe45e6b640ea4e3b
monero-gui-mac-x64-v0.12.3.0.tar.bz2, 90a9fa02e7bcef653b034f8a0365f16ec96cd553791546df2200a3c2591d5104
monero-gui-win-x64-v0.12.3.0.zip, 947efb72418d9ee60ccb0a2afa1f85553fa6a777a0a4e0f89f353592c84e00dc

A GPG-signed list of the hashes is at https://getmonero.org/downloads/hashes.txt and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)