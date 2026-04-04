---
title: ERROR blockchain, Error Retrieving Blocks
source_url: https://github.com/monero-project/monero/issues/3258
author: notmike-5
assignees: []
labels: []
created_at: '2018-02-13T17:59:04+00:00'
updated_at: '2018-06-18T15:09:25+00:00'
type: issue
status: closed
closed_at: '2018-06-18T15:09:25+00:00'
---

# Original Description
Version: Helium Hydra (v0.11.1.0-master-ed67e5c0)

Daemon start normally, indicates that it is synced with the network, but then I just get this error repeated over and over. Did the local copy of the blockchain become corrupted?

2018-02-13 17:55:08.242	[P2P8]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:1552	Error retrieving blocks, missed 1 transactions for block with hash: <1bad8acfad69bff2ea6394bfbb46d831e2f9357484891fb2bdd1bfc0bd8e4e48>

2018-02-13 17:56:33.398	[P2P2]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:1552	Error retrieving blocks, missed 1 transactions for block with hash: <9dc8aa9dd89f44e8f721be55a384cdeed560232e1d9b6bf01ce5cceaf188271b>

# Discussion History
## moneromooo-monero | 2018-02-13T18:33:07+00:00
Yes, it looks like DB corruption. At least one block in the DB is referencing a tx that's not in the DB.

## notmike-5 | 2018-02-13T18:44:42+00:00
Oh no, https://youtu.be/tpD00Q4N6Jk

## moneromooo-monero | 2018-06-18T14:54:23+00:00
There was a bug in the code which switched lmdb to safe mode after sync. This is now fixed. Corruption can still happen while the initial sync is going on though, but fixing that would kill performance so it won't be done by default, though you can set safe mode anyway with --db-sync-mode if you want.

+resolved

# Action History
- Created by: notmike-5 | 2018-02-13T17:59:04+00:00
- Closed at: 2018-06-18T15:09:25+00:00
