---
title: Info messages in log could be improved during sync periods
source_url: https://github.com/monero-project/monero/issues/1632
author: ghost
assignees: []
labels: []
created_at: '2017-01-25T23:44:54+00:00'
updated_at: '2017-02-24T06:11:37+00:00'
type: issue
status: closed
closed_at: '2017-02-24T06:11:37+00:00'
---

# Original Description
Example messages at log level = 0 (*INFO):

```
2017-01-25 23:39:45.739	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:288	[195.154.207.151:18092 OUT] Sync data returned a new top block candidate: 1230953 -> 1231802 [Your node is 849 blocks (1 days) behind] 
SYNCHRONIZATION started
2017-01-25 23:39:46.665	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:288	[192.110.160.146:18080 OUT] Sync data returned a new top block candidate: 1230953 -> 1231802 [Your node is 849 blocks (1 days) behind] 
SYNCHRONIZATION started
2017-01-25 23:39:47.382	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:288	[78.83.66.202:18080 OUT] Sync data returned a new top block candidate: 1230953 -> 1231802 [Your node is 849 blocks (1 days) behind] 
SYNCHRONIZATION started
2017-01-25 23:39:47.654	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:288	[37.97.177.81:18085 OUT] Sync data returned a new top block candidate: 1230953 -> 1220528 [Your node is 10425 blocks (14 days) ahead] 
SYNCHRONIZATION started
2017-01-25 23:40:00.768	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:288	[23.250.10.250:43686 INC] Sync data returned a new top block candidate: 1230953 -> 1009962 [Your node is 220991 blocks (306 days) ahead] 
SYNCHRONIZATION started
2017-01-25 23:40:00.769	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:288	[51.175.81.209:47874 INC] Sync data returned a new top block candidate: 1230953 -> 1220528 [Your node is 10425 blocks (14 days) ahead] 
SYNCHRONIZATION started
2017-01-25 23:40:00.823	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:288	[173.234.159.236:55497 INC] Sync data returned a new top block candidate: 1230953 -> 1220528 [Your node is 10425 blocks (14 days) ahead] 
SYNCHRONIZATION started
2017-01-25 23:40:00.879	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:288	[163.172.76.47:40314 INC] Sync data returned a new top block candidate: 1230953 -> 1231802 [Your node is 849 blocks (1 days) behind] 
SYNCHRONIZATION started
2017-01-25 23:40:00.880	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:288	[199.231.85.122:39592 INC] Sync data returned a new top block candidate: 1230953 -> 1231802 [Your node is 849 blocks (1 days) behind] 
SYNCHRONIZATION started
```

Instead an example of a 'block added' message at log level = 2:

```
2017-01-25 23:37:41.371	[P2P9]	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:3328	+++++ BLOCK SUCCESSFULLY ADDED
id:	<51fe60098da66df83f509005b9c74b6c2e04afbf7e19df20f82213b348a86d18>
PoW:	<32e189c2d0b7ddc5bf704f98232bb3aec60232bc840ac59a68e8203b00000000>
HEIGHT 1230918, difficulty:	6120952500
block reward: 8.870328683619(8.753689736511 + 0.116638947108), coinbase_blob_size: 95, cumulative size: 65796, 334(0/253)ms
```

This seems to be far more interesting to people watching their nodes during an initial sync, but it's flooded with loads of extra stuff.

Is it possible to add 'block successfully added' messages at a lower log level?

# Discussion History
## moneromooo-monero | 2017-01-27T20:44:03+00:00
Feel free to twiddle what you think should be.

## ghost | 2017-01-27T21:04:24+00:00
Ok thanks :)

## moneromooo-monero | 2017-01-27T21:50:52+00:00
Subject to review, of course :P

## ghost | 2017-01-29T02:42:21+00:00
I wouldn't trust my code without review!

# Action History
- Created by: ghost | 2017-01-25T23:44:54+00:00
- Closed at: 2017-02-24T06:11:37+00:00
