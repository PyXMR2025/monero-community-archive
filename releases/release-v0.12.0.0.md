---
title: Lithium Luna
type: release
source_url: https://github.com/monero-project/monero-gui/releases/tag/v0.12.0.0
author: luigi1111
tag_name: v0.12.0.0
published_at: '2018-04-04T06:27:07+00:00'
---

# Version: v0.12.0.0

# Release Notes
# Overview

This is the v0.12.0.0 release of the Monero GUI software, and it is part of the v0.12 network wide update. This major release is due to the April 6th network update, which in turn increases the minimum ring signature size, sorts inputs so as not to leak wallet choice by inference, and slightly changes the proof-of-work algorithm to prevent DoS attacks by ASICs. This release of the software presents a number of major improvements to Monero, as well as a large set of bug fixes.

[**The CLI release notes and downloads can be found on the release page here.**](https://github.com/monero-project/monero/releases/tag/v0.12.0.0)

Some highlights of this release are:

- new black theme!
- add a second progress bar to show both daemon sync status and wallet refresh status
- added or improved the following translations: Russian, Ukrainian, Turkish, Portuguese, Esperanto, Arabic, Japanese, Polish, Dutch, Serbian, Hebrew, Romanian, Swedish, Croatian, Slovenian, Spanish, Egyptian, Italian, Taiwanese, French, Catalan, Chinese, Czech, German, Slovak, and Danish
- new "bootstrap daemon" mode
- initial subaddress support
- added some mitigations for privacy-threatening key reusing forks
- automatically use lower fee if no network congestion
- added a way to prove you were the originator of a transaction, even if you didn't save the transaction key
- minimum ringsize 7, sorted inputs, and altered POW (see CLI release notes above for more details and other changes)
- many other bugfixes and performance improvements

# Contributors for this Release

This release was the direct result of 59 people who worked, largely unpaid and altruistically, to put out 483 commits containing 52,853 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- Jaquee
- Keksoj
- erciccione
- Bas Joe
- stoffu
- luigi1111
- xc
- fungible-crypto
- Sander Ferdinand
- xmr-eric
- lancillotto
- Anton Krylov
- Jonathan Cross
- AJIekceu4
- René Brunner
- Tim L
- jacobzipper
- xmr-eric
- cryptobench
- Robert Fridzema
- medusadigital
- Wojciech Gomoła
- Vasile
- Schnoffel
- potatored
- MoroccanMalinois
- Evan Klitzke
- Ruzicka Pavel
- fero-sk
- 3b7ameed
- kenshi84
- Neozaru
- Miguel Herranz
- hqwrong
- cryptochangements34
- Guillaume LE VAILLANT
- jernejml
- Ordtrogen Översättning
- milargos
- TasmaniaKrama
- Mario Kralj
- ProkhorZ
- xmronadaily
- Takuto Hayashi
- mandrill-pie
- einsteinsfool
- netrik182
- moneromooo-monero
- Lafudoci
- EdwardLow
- rtonline
- i3visio
- pazos
- Agent LvM
- MB
- cryptochangements34
- Dan Miller
- dEBRUYNE-1
- iDunk5400
- lh1008

# Official Download Links

- [Windows, 64-bit](https://downloads.getmonero.org/gui/win64)
- [macOS, 64-bit](https://downloads.getmonero.org/gui/mac64)
- [Linux, 64-bit](https://downloads.getmonero.org/gui/linux64)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

monero-gui-win-x64-v0.12.0.0.zip, 4b9f31686ecaad97cdb175e6574bf307f8d1c410427825f4304c21da8aac1864
monero-gui-mac-x64-v0.12.0.0.tar.bz2, f74c108d16bd70b6f0052ba4b3ce91fa3ca59622a0aee7d523a1f43967814c12
monero-gui-linux-x64-v0.12.0.0.tar.bz2, fb0f43387b31202f381c918660d9bc32a3d28a4733d391b1625a0e15737c5388

A GPG-signed list of the hashes is at https://getmonero.org/downloads/hashes.txt and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)