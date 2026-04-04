---
title: blockchain verification question
source_url: https://github.com/monero-project/monero/issues/5219
author: JustFranz
assignees: []
labels:
- invalid
created_at: '2019-03-03T21:17:43+00:00'
updated_at: '2019-03-05T13:41:31+00:00'
type: issue
status: closed
closed_at: '2019-03-05T13:41:31+00:00'
---

# Original Description
lets say you have a blockchain of 1 million blocks and you want to verify it multithreaded

Could you start up 9 threads and start asking other nodes for blocks, starting at 1, 100K, 200K ... 900K
and temporarily assume the first blocks to be valid and verify next blocks against the assumed to be true initial block.

Once the first chunk 1-99,999 finishes and block 100,000 verifies against it then all of the blocks that have been verified in the 100K starting chunk are confirmed to be valid.

If a chunk finishes in the middle then it can be verified against the first block of the next chunk and those can be confirmed to be valid against each other.

If 1-100K finishes and 900K is at 950K then the first thread can request the block 975K and start a new chunk.

A database of missing transaction continuity between the chunks could be created and that can be processed once two chunks are joined or as chunks get a continuous line of verification to the genesis block.

# Discussion History
## moneromooo-monero | 2019-03-03T22:47:55+00:00
It's a blockchain. Every block depends on the block before it.

That said, you can do things like checking PoW independently. You can also assume a block is valid and process it, and "undo" if you later find you assumed too much.

But still, if you want to verify multithreaded, it's probably best to do it chunked in order, as monerod currently does. If you want to improve that, it's probably the way to go.

Currently, blocks are downloaded in advance (network throughput permitting).

## moneromooo-monero | 2019-03-05T13:38:52+00:00
Not a bug.

+invalid

# Action History
- Created by: JustFranz | 2019-03-03T21:17:43+00:00
- Closed at: 2019-03-05T13:41:31+00:00
