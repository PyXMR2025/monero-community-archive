---
title: I forked Monero, it wont stop trying to sync?
source_url: https://github.com/monero-project/monero/issues/8185
author: kvthweatt
assignees: []
labels: []
created_at: '2022-02-19T09:17:02+00:00'
updated_at: '2022-02-19T13:04:30+00:00'
type: issue
status: closed
closed_at: '2022-02-19T13:04:30+00:00'
---

# Original Description
I mined --offline to block height 140 or so.

Why isn't the daemon picking up the existing chain?

When I start my daemon online, it says "Syncing with the network, this may take a long time"
Also when started online, using print_block 100 gives the appropriate block, so my daemon
knows the blocks are there.

# Discussion History
## moneromooo-monero | 2022-02-19T09:34:19+00:00
Just give it time to find other peers.

## kvthweatt | 2022-02-19T09:39:57+00:00
Oh so the only problem is there's no one else mining? Or is it because there's no other wallet trying to sync?

## kvthweatt | 2022-02-19T10:14:59+00:00
The problem I'm having because of it is I can't mine locally, because the miner daemon says "BUSY"

## selsta | 2022-02-19T13:04:30+00:00
This isn't the correct place to get fork help, I would recommend to search on Google or ask other projects that have forked monero.

# Action History
- Created by: kvthweatt | 2022-02-19T09:17:02+00:00
- Closed at: 2022-02-19T13:04:30+00:00
