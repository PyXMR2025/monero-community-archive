---
title: Smaller testnet
source_url: https://github.com/monero-project/monero/issues/6200
author: dd1982
assignees: []
labels: []
created_at: '2019-11-30T17:43:40+00:00'
updated_at: '2022-02-19T04:43:56+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:43:56+00:00'
---

# Original Description
There might be good reason for the current situation but I'm wondering whether it might be a good idea to purge the testnet regularily and start over or have a separate testnet that does that in order to keep the size of the chain reasonable for _most_ testing purposes? I just started a node there to test something and the sync looks like it's going to take it's sweet time - after 30-ish minutes I've only progressed to ~30% and I guess like the main chain it will only go slower the further I get. So it seems it might take hours before I can do my "quick" check - I would guess that for a large portion of the testnets use cases having to store and sync such a large blockchain for testing is more trouble than it's worth.

Maybe I'm missing some good reason for the current situation - I'm mostly miffed because I wanted to check something before the fork happens but since I hadn't anticipated having to wait for hours before my node was synced to the testnet it seems like that might not be happening. Gonna try and see if I can find a remote testnet-node.

# Discussion History
## moneromooo-monero | 2019-11-30T19:22:03+00:00
You can use --regtest if you want a quick check. Typically with --fixed-difficulty. It starts a new chain on startup.

## moneroexamples | 2019-12-02T00:36:44+00:00
There is also stagenet. Alternatively can also setup your own private network (e.g., https://github.com/moneroexamples/private-testnet). 

# Action History
- Created by: dd1982 | 2019-11-30T17:43:40+00:00
- Closed at: 2022-02-19T04:43:56+00:00
