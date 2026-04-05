---
title: Idea to speed up first time refresh on wallet open
source_url: https://github.com/seraphis-migration/monero/issues/165
author: j-berman
assignees: []
labels:
- upstream
created_at: '2025-10-11T18:26:10+00:00'
updated_at: '2025-12-18T18:52:17+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Rather than clearing the local pool [here](https://github.com/seraphis-migration/monero/blob/53f94605e7117b3f1622f46f5faff4f6c30c7df9/src/wallet/wallet2.cpp#L4218-L4227) and requiring daemon serve the whole pool again, we could do the following:

- The daemon should only serve pool txs over `/getblocks.bin` `requested_info = BLOCKS_AND_POOL` if the wallet is synced (based on the wallet's requested `start_height` or `block_ids`), or the response will include all blocks that the wallet needs in order to complete sync.
- The wallet should update its pool state **after** processing blocks.
- The first non-incremental request for pool txs in `/getblocks.bin` can **always** return the complete pool state, but limit pool tx blobs in the response to 100, and then place remaining tx hashes in `remaining_added_pool_txids`.
- If the wallet has not already seen the `remaining_added_pool_txids` in `m_scanned_pool_txs` (and the txs aren't already identified as the wallet's), then it can request the remaining tx blobs.
    - This avoids the daemon serving a max of 9,900 txs the wallet has already seen. The wallet will still need to re-download full tx blobs for pools txs >10k.

# Discussion History
## j-berman | 2025-12-18T18:52:17+00:00
To further optimize wallet open with a large pool, we could also implement a set reconciliation algo mentioned by @boog900 over here: https://github.com/seraphis-migration/monero/pull/174#issuecomment-3410945984

The following is worth keeping in mind too:

1) Scanning the pool is currently single threaded.
2) Downloading a large pool doesn't currently work on unrestricted RPC's (https://github.com/monero-project/monero/pull/9473).
3) Downloading over the restricted RPC is pretty slow since it chunks 100 txs at a time.

# Action History
- Created by: j-berman | 2025-10-11T18:26:10+00:00
