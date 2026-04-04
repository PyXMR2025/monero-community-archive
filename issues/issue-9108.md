---
title: Synchronization on my SSD-blockchain
source_url: https://github.com/monero-project/monero/issues/9108
author: developergames2d
assignees: []
labels:
- question
created_at: '2023-12-31T13:42:39+00:00'
updated_at: '2023-12-31T13:45:35+00:00'
type: issue
status: closed
closed_at: '2023-12-31T13:44:54+00:00'
---

# Original Description
If I download full blockchain on my SSD, will be the synchronization **FROM BLOCK WITH HEIGHT 0** very fast (on local demon)? Now I wait many hours (with remote demon node).

# Discussion History
## selsta | 2023-12-31T13:44:55+00:00
Please don't use GitHub to ask basic questions, this is a issue tracker. There are other places for this, like Matrix / IRC monero chat.

To answer your question, syncing with an SSD will take approximately 12-24h.

## selsta | 2023-12-31T13:45:35+00:00
If you mean wallet syncrhonization, yes it will also be faster than using a remote node. But it won't be instantly, it will likely take a bit less than an hour.

# Action History
- Created by: developergames2d | 2023-12-31T13:42:39+00:00
- Closed at: 2023-12-31T13:44:54+00:00
