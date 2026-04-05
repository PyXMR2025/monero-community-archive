---
title: '`monerod` killed by OOM while syncing'
source_url: https://github.com/seraphis-migration/monero/issues/147
author: j-berman
assignees: []
labels:
- upstream
created_at: '2025-10-08T20:28:03+00:00'
updated_at: '2026-03-27T17:36:10+00:00'
type: issue
status: closed
closed_at: '2026-03-27T17:36:10+00:00'
---

# Original Description
We've had a few reports of `monerod` getting killed by OOM. Currently under investigation.

# Discussion History
## j-berman | 2025-10-10T17:37:41+00:00
@SNeedlewoods has reported an OOM kill on a machine with 8GB RAM and 1GB swap, not mining, `--out-peers 1`

## j-berman | 2025-10-23T17:58:57+00:00
Of note, looks like there are 2 distinct OOM-related errors being reported:

1) Node is already synced.

    - Possible memory leak, cause currently unknown.

2) While syncing.

    - @samsunggalaxyplayer reported the issue in the stressnet channel.
    - @nahuhh and @boog900 raised suspicion surrounding the block download queuing too many blocks and filling up memory (related: https://hackerone.com/reports/2693786).
    - At @nahuhh's request, sgp used `sync_info` which showed `1022 spans, 2128.43 MB`.
    - "even with 6 GB of free memory, monerod keeps getting killed to the point I can't really sync more than a few blocks at a time" - sgp

## Boog900 | 2025-10-25T15:57:51+00:00
I _think_ I might have a plausible explanation for the run away block queue. Copying here my explanation of `stripe_proceed_main`, the varible that decides if we should ignore the queue's size and download anyway:

```cpp
bool stripe_proceed_main =
    (
        (m_sync_pruned_blocks && local_stripe && add_stripe != local_stripe) // True if we should sync pruned blocks, we are pruned and the peer has the next blocks pruned.
        || add_stripe == 0 // True if the next block is within the tip-blocks which won't be pruned.
        || peer_stripe == 0 // True if the peer does no pruning.
        || add_stripe == peer_stripe // True if the peer is pruned and has the next block un-pruned.
    )
    && 
    (
        next_block_height < bc_height + BLOCK_QUEUE_FORCE_DOWNLOAD_NEAR_BLOCKS // True if next_block_height is less than 1000 blocks above our blockchain
        || next_needed_height < bc_height + BLOCK_QUEUE_FORCE_DOWNLOAD_NEAR_BLOCKS // True if next_needed_heightis less than 1000 blocks above our blockchain
    );
```
`next_block_height` is the height of the next block we expect from the peer.
`next_needed_height` is got from `get_next_needed_height`: https://github.com/monero-project/monero/blob/d32b5bfe18e2f5b979fa8dc3a8966c76159ca722/src/cryptonote_protocol/block_queue.cpp#L151

As you can see it will download the first 1000 blocks above our chain always, this in itself is enough to get the queue pretty big if blocks are big enough. 

However, as I mentioned in that H1 report, `get_next_needed_height` will sometimes give a height way below what it should if the heights in the queue don't line up perfectly. Copying it here:

```cpp
uint64_t block_queue::get_next_needed_height(uint64_t blockchain_height) const
{
  boost::unique_lock<boost::recursive_mutex> lock(mutex);
  if (blocks.empty())
    return blockchain_height;
  uint64_t last_needed_height = blockchain_height;
  bool first = true;
  for (const auto &span: blocks)
  {
    if (span.start_block_height + span.nblocks - 1 < blockchain_height)
      continue;
    if (span.start_block_height != last_needed_height || (first && span.blocks.empty()))
      return last_needed_height;
    last_needed_height = span.start_block_height + span.nblocks;
    first = false;
  }
  return last_needed_height;
}
```

Now, when we go to add blocks we do not remove the entry before adding all the blocks to the chain here: https://github.com/monero-project/monero/blob/d32b5bfe18e2f5b979fa8dc3a8966c76159ca722/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L1363-L1584 

So this means while we add blocks to the chain the entry will still be in the queue.

Now, if another thread calls `get_next_needed_height` after the first block in the batch has been added to the chain it will call the function with a `blockchain_height` that wont line up with the `span.start_block_height` of the first block in the batch causing `get_next_needed_height` to return the `blockchain_height` as the next needed block. This would then cause `stripe_proceed_main` to be true as the height is less than 1000 above our chain, meaning the queue limit is ignored. 





## nahuhh | 2026-03-25T16:27:45+00:00
I think this is resolved

# Action History
- Created by: j-berman | 2025-10-08T20:28:03+00:00
- Closed at: 2026-03-27T17:36:10+00:00
