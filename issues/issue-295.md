---
title: error adding block
source_url: https://github.com/monero-project/monero/issues/295
author: Gingeropolous
assignees: []
labels: []
created_at: '2015-05-29T21:40:09+00:00'
updated_at: '2015-05-31T11:46:52+00:00'
type: issue
status: closed
closed_at: '2015-05-31T11:46:52+00:00'
---

# Original Description
I just did a git pull, compiled, running on mainnet, got this:

2015-May-29 17:38:19.896276 [P2P3][78.194.26.60:18080 OUT]-->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=200, txs.size()=0requested blocks count=200 / 200
2015-May-29 17:38:20.724617 [P2P8][217.23.2.242:18080 OUT]Sync data returned unknown top block: 583974 -> 585310 [1336 blocks (0 days) behind]
SYNCHRONIZATION started
2015-May-29 17:38:21.725372 [P2P9][83.212.114.252:18080 OUT]Sync data returned unknown top block: 583974 -> 585310 [1336 blocks (0 days) behind]
SYNCHRONIZATION started
2015-May-29 17:38:22.157302 [P2P6][61.90.204.244:18080 OUT]Got NEW BLOCKS inside of handle_response_get_objects: size: 200
2015-May-29 17:38:22.888067 [P2P6]Failed to add tx blob to db transaction
2015-May-29 17:38:22.888360 [P2P6]ERROR /home/e5405/bitmonero_latest2/bitmonero/src/cryptonote_core/blockchain.cpp:2195 Error adding block with hash: <094397ace0327d4fc01146fb24acc5739008db5915025ef7209da0b619de15a9> to blockchain, what = Failed to add tx blob to db transaction
2015-May-29 17:38:23.631213 [P2P3][217.23.2.242:18080 OUT]-->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=200, txs.size()=0requested blocks count=200 / 200
2015-May-29 17:38:25.270475 [P2P6][80.71.13.36:18080 OUT]Sync data returned unknown top block: 583974 -> 585310 [1336 blocks (0 days) behind]
SYNCHRONIZATION started
2015-May-29 17:38:28.722489 [P2P9][94.23.55.211:18080 OUT]Got NEW BLOCKS inside of handle_response_get_objects: size: 200
2015-May-29 17:38:29.456353 [P2P9]Failed to add tx blob to db transaction


# Discussion History
## Gingeropolous | 2015-05-29T22:47:09+00:00
and it just keeps on doing it. Its stuck on that block. 

I've tried reboot and clearing out the p2pstate.bin and poolstate.bin, nothing changed. 


## warptangent | 2015-05-30T16:24:28+00:00
Thanks for this.
Fixed in #297.


# Action History
- Created by: Gingeropolous | 2015-05-29T21:40:09+00:00
- Closed at: 2015-05-31T11:46:52+00:00
