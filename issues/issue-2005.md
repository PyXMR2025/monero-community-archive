---
title: Monero daemon stop working
source_url: https://github.com/monero-project/monero/issues/2005
author: AJIekceu4
assignees: []
labels: []
created_at: '2017-04-25T18:24:58+00:00'
updated_at: '2017-05-07T13:12:33+00:00'
type: issue
status: closed
closed_at: '2017-05-07T13:12:20+00:00'
---

# Original Description
Hello all. Monero 'Wolfram Warptangent' (v0.10.3.1-9ed496b)

This is public node: node.monero.net:13666
I have this problem 3 times for last 7 days (previous 2 don't have log, now i enable it) with my public node.

Last line from log before daemon exit:

> 2017-04-25 05:05:48.549  [P2P1]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:581     Transaction verification failed: <3f9a4e00832ebf56d9e74e119288bb3fede3c4b9157ade9e53a82035a7d74431>

After this line daemon stopped.
https://minergate.com/blockchain/xmr/transaction/3f9a4e00832ebf56d9e74e119288bb3fede3c4b9157ade9e53a82035a7d74431

> Recieved time (UTC)?	2017-03-06 05:57:27 (2 months ago)

# Discussion History
## moneromooo-monero | 2017-04-29T08:48:09+00:00
You likely are on a fork, and it's failing to back off. If you used 0.10.3.0 before, it might have borked the database sligtly, and you can try:
- exit monerod
- monero-blockchain-export
- monero-blockchain-import --verify 0
- restart monerod with log level 1

That should fix up that problem. If it still fails, then it's another problem, and log level 1 will have more info.

## AJIekceu4 | 2017-05-01T18:31:59+00:00
Thank you for info. I decide upgrade server and sync db from 0 and also test not closed connections on different server ;) I will add info later (or close issue if all ok), after some time.

## AJIekceu4 | 2017-05-07T13:12:20+00:00
Seems all ok after resyncing db.

# Action History
- Created by: AJIekceu4 | 2017-04-25T18:24:58+00:00
- Closed at: 2017-05-07T13:12:20+00:00
