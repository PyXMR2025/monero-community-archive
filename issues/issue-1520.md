---
title: FreeBSD Port
source_url: https://github.com/monero-project/monero/issues/1520
author: emc2
assignees: []
labels:
- proposal
created_at: '2017-01-01T15:09:56+00:00'
updated_at: '2022-03-16T15:28:41+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:28:40+00:00'
---

# Original Description
I've created a FreeBSD port for installing Monero.  The repository is [here](https://github.com/emc2/freebsd-ports/tree/monero_port).  The port is found under net-p2p/monero.

I've tested this in an empty jail, built successfully, and am currently syncing up the blockchain.

The port would need someone to add a MAINTAINER entry before FreeBSD would take it.  Also, it currently defaults to LMDB, but it might be good to add an option for BerkeleyDB at some point.

# Discussion History
## moneromooo-monero | 2017-01-01T17:01:51+00:00
The bdb port is now obsolete, and won't work. Only LMDB is supported now.

## danrmiller | 2017-01-01T21:14:02+00:00
I'll test this out too. Whether or not this is eventually included in FreeBSD's ports, maybe we need a directory in contrib or somewhere for packaging metadata, there's been some other discussion and interest in packaging for other platforms, like .deb/.aur/.rpm. 

## anonimal | 2017-01-02T12:58:18+00:00
JFTR: AUR release is [here](https://aur.archlinux.org/packages/monero/). There is also a git-version in the AUR but I'm packaging releases only.

## dEBRUYNE-1 | 2018-01-08T12:36:13+00:00
+proposal

## selsta | 2022-03-16T15:28:40+00:00
https://www.getmonero.org/downloads/#cli offers FreeBSD binaries.

# Action History
- Created by: emc2 | 2017-01-01T15:09:56+00:00
- Closed at: 2022-03-16T15:28:40+00:00
