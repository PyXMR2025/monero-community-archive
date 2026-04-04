---
title: Unable to sync blocks since yesterday due to transaction already in db
source_url: https://github.com/monero-project/monero/issues/3922
author: rex4539
assignees: []
labels: []
created_at: '2018-06-04T08:22:00+00:00'
updated_at: '2018-06-04T13:30:27+00:00'
type: issue
status: closed
closed_at: '2018-06-04T13:30:26+00:00'
---

# Original Description
Logs from 0.12.0.0

```
2018-06-04 08:14:08.401	  0x7fff9bbcd380	WARN 	daemon	src/daemon/executor.cpp:61	Monero 'Lithium Luna' (v0.12.0.0-master-release) Daemonised

...

2018-06-04 08:14:33.553	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[51.254.122.128:18080 OUT] Sync data returned a new top block candidate: 1586875 -> 1587494 [Your node is 619 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-06-04 08:14:38.369	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[113.196.177.100:29671 OUT] Sync data returned a new top block candidate: 1586875 -> 1587495 [Your node is 620 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-06-04 08:15:07.132	[P2P7]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3534	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 08:15:12.555	[P2P4]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3534	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 08:15:13.737	[P2P6]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3534	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 08:15:15.082	[P2P4]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3534	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 08:15:15.669	[P2P2]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3534	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 08:15:18.218	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[185.157.161.152:48011 OUT] Sync data returned a new top block candidate: 1586875 -> 1587495 [Your node is 620 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-06-04 08:15:28.777	[P2P3]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3534	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
```

Logs from 0.12.2.0

```
2018-06-04 06:32:44.042	  0x7fff9bbcd380	INFO 	global	src/daemon/main.cpp:279	Monero 'Lithium Luna' (v0.12.2.0-release)

...

2018-06-04 06:33:00.567	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[68.8.43.22:18080 OUT] Sync data returned a new top block candidate: 1586875 -> 1587447 [Your node is 572 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-06-04 06:33:09.186	[P2P8]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3578	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 06:33:14.742	[P2P7]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3578	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 06:33:21.002	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[14.202.191.220:18080 OUT] Sync data returned a new top block candidate: 1586875 -> 1587447 [Your node is 572 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-06-04 06:33:29.766	[P2P3]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3578	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 06:35:32.510	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[83.7.26.85:18080 OUT] Sync data returned a new top block candidate: 1586875 -> 1587447 [Your node is 572 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-06-04 06:35:42.696	[P2P8]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3578	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 07:01:50.500	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[83.7.26.85:18080 OUT] Sync data returned a new top block candidate: 1586875 -> 1587457 [Your node is 582 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-06-04 07:01:57.904	[P2P8]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3578	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 07:03:59.726	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[80.101.35.68:18080 OUT] Sync data returned a new top block candidate: 1586875 -> 1587459 [Your node is 584 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-06-04 07:04:09.269	[P2P0]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3578	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 07:04:12.582	[P2P1]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3578	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 07:04:19.546	[P2P6]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3578	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 07:04:23.968	[P2P8]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3578	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 07:04:27.772	[P2P5]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3578	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 07:17:21.519	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[51.254.122.128:18080 OUT] Sync data returned a new top block candidate: 1586875 -> 1587466 [Your node is 591 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-06-04 07:17:33.880	[P2P1]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3578	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 07:23:44.542	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[113.196.177.100:29671 OUT] Sync data returned a new top block candidate: 1586875 -> 1587468 [Your node is 593 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-06-04 07:23:50.629	[P2P6]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3578	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 07:28:13.258	[P2P2]	INFO 	global	src/cryptonote_core/blockchain.cpp:1534	[1;34m----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581881
id:	<7109e6c518717d56f4ea9eb58812f03b98363dbcf78cd8a613df74523d854886>
PoW:	<d3c693d2083888c03bc8dfbca4f32d9692e094722d8cbf4a90aa4c1400000000>
difficulty:	50454937567[0m
2018-06-04 07:28:13.286	[P2P2]	INFO 	global	src/cryptonote_core/blockchain.cpp:1534	[1;34m----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581882
id:	<fade9c6c28337e945198e747d391f9e57d725e1def6d9c7cf99edfb7e32865ac>
PoW:	<c1ca2169cf89d7d4dc76fc7b86c1dc012c4567ff5eb0651ee8736a0b00000000>
difficulty:	50327383695[0m
2018-06-04 07:28:13.309	[P2P2]	INFO 	global	src/cryptonote_core/blockchain.cpp:1534	[1;34m----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581883
id:	<21bd3e12be99b5155193797996a77c96de2fe55bafdb60abcb6a6957abe22232>
PoW:	<7f4089a4d9c01173c77e9bb506fbadd8810bd43520f2371da7cb540200000000>
difficulty:	50328137674[0m
2018-06-04 07:28:13.343	[P2P2]	INFO 	global	src/cryptonote_core/blockchain.cpp:1534	[1;34m----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581884
id:	<869782996021166249c8894afd91eeff6b4fc981c42e58a44e80c23db503f625>
PoW:	<e3ee2aa3cf476db4362a03dfb445ebc50868827de74c9a47c379be0700000000>
difficulty:	50287474850[0m
2018-06-04 07:28:13.375	[P2P2]	INFO 	global	src/cryptonote_core/blockchain.cpp:1534	[1;34m----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581885
id:	<1a3573e19dd618d463feb05ac131924c487e0ffe427e475c0a28ac3d78567265>
PoW:	<83023ae3dae254d2294305b304d930007c69c209ac82745b273a560000000000>
difficulty:	50232957166[0m
2018-06-04 07:28:15.098	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1561	[1;32mSYNCHRONIZED OK[0m
2018-06-04 07:32:09.022	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[194.12.69.213:18080 OUT] Sync data returned a new top block candidate: 1586875 -> 1587299 [Your node is 424 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-06-04 07:32:19.332	[P2P7]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3578	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 07:34:16.148	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[188.209.49.33:18080 OUT] Sync data returned a new top block candidate: 1586875 -> 1587475 [Your node is 600 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-06-04 07:34:27.041	[P2P8]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3578	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 07:56:35.467	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[68.10.30.158:18080 OUT] Sync data returned a new top block candidate: 1586875 -> 1587487 [Your node is 612 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-06-04 07:56:44.336	[P2P1]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3578	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 07:56:53.847	[P2P0]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3578	Error adding block with hash: <3ccbc29d872cca08007ce313b026e2a9ad069847dc7a4cb7dfe12491d2046b39> to blockchain, what = Attempting to add transaction that's already in the db (tx id 4501774)
2018-06-04 07:58:57.415	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[165.227.26.165:18080 OUT] Sync data returned a new top block candidate: 1586875 -> 1587488 [Your node is 613 blocks (0 days) behind] 
```

# Discussion History
## moneromooo-monero | 2018-06-04T09:08:55+00:00
That is a corrupt DB.

## moneromooo-monero | 2018-06-04T10:38:25+00:00
Also, do you have interesting messages in the log from around the time it stopped keeping up ?

## rex4539 | 2018-06-04T13:30:26+00:00
After restoring a db backup, it synced fine.

# Action History
- Created by: rex4539 | 2018-06-04T08:22:00+00:00
- Closed at: 2018-06-04T13:30:26+00:00
