---
title: 'Feature: splitting monero blockchain into block index, chainstate and transaction
  data'
source_url: https://github.com/monero-project/monero-gui/issues/4458
author: godfuture
assignees: []
labels: []
created_at: '2025-06-14T12:51:40+00:00'
updated_at: '2025-08-26T01:09:58+00:00'
type: issue
status: closed
closed_at: '2025-06-14T12:55:08+00:00'
---

# Original Description
Hi guys,
I am running an active, private monero node (active, but no rpc). I understood the idea of pruned blockchain, but this means only a group of pruned nodes can deliver what a full node can do.

On my server I have ssd and hdd storage. Blockchain on hdd storage is slow. ssd storge is scarce. Therefore I seeked some ideas to get the best of both worlds. And I found it on a bitcoin forum (https://bitcointalk.org/index.php?topic=4722244.0).

With bitcoin blockchain we have index, chainstate and data. High IO is needed for chainstate and index, but not pure data. The idea is to move chainstate and index to ssd and link them to blockchain data folder on hdd living next to its transaction data.

This way we have responsive sync and huge amounts of storage.

Could the monero blockchain be split into those different data types as well?

# Discussion History
## godfuture | 2025-06-14T12:55:08+00:00
Wrong project. I moved it to monero core ([#9959](https://github.com/monero-project/monero/issues/9959)).

# Action History
- Created by: godfuture | 2025-06-14T12:51:40+00:00
- Closed at: 2025-06-14T12:55:08+00:00
