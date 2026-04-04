---
title: monerod errors preventing syncing
source_url: https://github.com/monero-project/monero-gui/issues/854
author: Engelberg
assignees: []
labels: []
created_at: '2017-09-05T00:07:59+00:00'
updated_at: '2017-09-06T02:03:14+00:00'
type: issue
status: closed
closed_at: '2017-09-06T02:03:14+00:00'
---

# Original Description
Using the monero-gui-0.10.3.1-beta2 Windows release, when running monerod, I get the following errors about missed transactions and no signs of any progress syncing:

```
2017-09-04 16:52:34.936	[P2P7]	WARN 	net.dns	src/common/dns_utils.cpp:531	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-09-04 16:52:56.152	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:293	[78.156.107.88:18080 OUT] Sync data returned a new top block candidate: 1384583 -> 1391986 [Your node is 7403 blocks (10 days) behind] 
SYNCHRONIZATION started
2017-09-04 16:53:35.811	[P2P5]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:1505	Error retrieving blocks, missed 1 transactions for block with hash: <332b8fa36465b400b317782c8426ac67d7da6e648362bc04063bfaa261dab68e>

2017-09-04 16:54:26.179	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:293	[124.160.224.28:18080 OUT] Sync data returned a new top block candidate: 1384583 -> 1391987 [Your node is 7404 blocks (10 days) behind] 
SYNCHRONIZATION started
2017-09-04 16:54:53.363	[P2P7]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:1505	Error retrieving blocks, missed 1 transactions for block with hash: <3d8feee76a5f22759c81a351b2a4bd63de3157819d5691b6abb97d5d8cfb307d>

2017-09-04 16:55:02.989	[P2P9]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:1505	Error retrieving blocks, missed 1 transactions for block with hash: <4ab37f9b1e1323c578984c83553098afe969a81187b1c808884c2fe2ea99fcf8>

2017-09-04 16:55:24.855	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:293	[174.101.167.205:18080 OUT] Sync data returned a new top block candidate: 1384583 -> 1391988 [Your node is 7405 blocks (10 days) behind] 
SYNCHRONIZATION started
2017-09-04 16:56:44.114	[P2P5]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:1505	Error retrieving blocks, missed 1 transactions for block with hash: <c66e3cced64899972a96941fc73e0c41d76ad5a0c2db47f8b66f1f07dc6f1cb4>

2017-09-04 16:57:05.464	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:293	[89.103.10.174:18080 OUT] Sync data returned a new top block candidate: 1384583 -> 1391989 [Your node is 7406 blocks (10 days) behind] 
SYNCHRONIZATION started
2017-09-04 16:57:15.704	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:293	[212.55.82.48:18080 OUT] Sync data returned a new top block candidate: 1384583 -> 1391990 [Your node is 7407 blocks (10 days) behind] 
SYNCHRONIZATION started
2017-09-04 16:58:02.139	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:293	[213.152.161.149:30997 OUT] Sync data returned a new top block candidate: 1384583 -> 1391991 [Your node is 7408 blocks (10 days) behind] 
SYNCHRONIZATION started
2017-09-04 16:58:45.924	[P2P5]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:1505	Error retrieving blocks, missed 1 transactions for block with hash: <e0a44b14383560e87cc1f123e840ef61a64dde5168db2c60d3acd94c74687698>

2017-09-04 16:58:49.970	[P2P5]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:1505	Error retrieving blocks, missed 1 transactions for block with hash: <26c16dbcf366fdb6de6ae8614ad0496a8f7e73f0ff28447de876de5fa97cfe77>

```

I have tried deleting p2pstate.bin and I have tried popping several blocks from the database, but neither had any effect.

# Discussion History
## dEBRUYNE-1 | 2017-09-05T09:49:42+00:00
Could you try this:

https://monero.stackexchange.com/questions/4462/my-blockchain-is-stuck-how-do-i-unstuck-it

## Engelberg | 2017-09-05T19:05:56+00:00
Thanks for the suggestion, but no, that didn't help.   That post's suggestions are: 
1) Use the latest release (which I am)
2) Delete p2pstate.bin (which I did again, but had already done)
3) --block-sync-size 20 (didn't help)

I have observed that it works if I blow away the database, so I'm beginning to conclude that this is a database corruption issue, which would necessitate starting over.  That's a no-go for me because not having a solid state drive, it took me weeks to build this database the first time, and I won't go through that again.  If it is in fact a database problem, it's a shame that:

a) The error message implies that the problem is with the p2p network, not with the database.
b) Monerod can't backtrack or repair the problem with the database.

## Engelberg | 2017-09-06T02:03:14+00:00
Closing issue, assuming it is database corruption with a misleading error message.

# Action History
- Created by: Engelberg | 2017-09-05T00:07:59+00:00
- Closed at: 2017-09-06T02:03:14+00:00
