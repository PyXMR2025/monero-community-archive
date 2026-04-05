---
title: Daemon segfaulted and now fails to start w/"Failed to insert key images from
  txpool tx"
source_url: https://github.com/seraphis-migration/monero/issues/192
author: j-berman
assignees: []
labels: []
created_at: '2025-10-24T17:20:06+00:00'
updated_at: '2026-02-16T17:34:33+00:00'
type: issue
status: closed
closed_at: '2026-02-16T17:34:33+00:00'
---

# Original Description
Reported by @nahuhh. His node segfaulted (cause unknown, logs weren't enabled), and now the node fails to start with:

> 2025-10-24 04:42:43.277     7f8db13fe6c0        DEBUG   randomx contrib/epee/src/mlog.cpp:517   Couldn't allocate RandomX cache using large pages                                       
2025-10-24 04:42:43.300     7fda79be9ac0        ERROR   txpool  src/cryptonote_core/tx_pool.cpp:485     internal error: tx_relay=4, kei_image_set.size()=1                              
2025-10-24 04:42:43.300     7fda79be9ac0        ERROR   txpool  src/cryptonote_core/tx_pool.cpp:485     txin.k_image=<1d19f67b6a9e0fb5fdd6b870be29f28b520894bbd43062e356f7529ee2b2faa2> 
2025-10-24 04:42:43.300     7fda79be9ac0        ERROR   txpool  src/cryptonote_core/tx_pool.cpp:485     tx_id=<57eacfc8553ea7739aa6f238ef6b81f63d65e267529b62a744896175299b2f69>        
2025-10-24 04:42:43.300     7fda79be9ac0        FATAL   txpool  src/cryptonote_core/tx_pool.cpp:1892    Failed to insert key images from txpool tx                                      
2025-10-24 04:42:43.300     7fda79be9ac0        ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:678     Failed to initialize memory pool                                        
2025-10-24 04:42:43.300     7fda79be9ac0        INFO    stacktrace      src/common/stack_trace.cpp:134  Exception: std::runtime_error  


Before the segfault, @nahuhh noted a number of "failed to find transaction input key images" in the logs (#181).

I requested @nahuhh start his node with the following patch to see what the duplicate tx is in the pool:

```
diff --git a/src/cryptonote_core/tx_pool.cpp b/src/cryptonote_core/tx_pool.cpp
index c63465e4a..c3803a28b 100644
--- a/src/cryptonote_core/tx_pool.cpp
+++ b/src/cryptonote_core/tx_pool.cpp
@@ -482,9 +482,20 @@ namespace cryptonote
       {
         const bool one_txid =
           (kei_image_set.empty() || (kei_image_set.size() == 1 && *(kei_image_set.cbegin()) == id));
+        crypto::hash existing_txid = crypto::null_hash;
+        txpool_tx_meta_t existing_meta;
+        if (!one_txid && kei_image_set.size() == 1)
+        {
+          existing_txid = *(kei_image_set.cbegin());
+          if (!m_blockchain.get_txpool_tx_meta(existing_txid, existing_meta))
+          {
+            MFATAL("Failed to get existing txs's meta");
+            return false;
+          }
+        }
         CHECK_AND_ASSERT_MES(one_txid, false, "internal error: tx_relay=" << unsigned(tx_relay)
                                            << ", kei_image_set.size()=" << kei_image_set.size() << ENDL << "txin.k_image=" << txin.k_image << ENDL
-                                           << "tx_id=" << id);
+                                           << "tx_id=" << id << ", existing tx_id=" << existing_txid << ", existing relay method=" << unsigned(existing_meta.get_relay_method()));
       }
 
       const bool new_or_previously_private =
```

This is @nahuhh's output after running:

> 2025-10-24 16:41:30.353 E internal error: tx_relay=4, kei_image_set.size()=1
2025-10-24 16:41:30.353 E txin.k_image=<1d19f67b6a9e0fb5fdd6b870be29f28b520894bbd43062e356f7529ee2b2faa2>
2025-10-24 16:41:30.353 E tx_id=<57eacfc8553ea7739aa6f238ef6b81f63d65e267529b62a744896175299b2f69>, existing tx_id=<\c6bb38e80e32123c9cd0aa863e36ac94dd4f84c5270fae59902c0b4d5befbe11>, existing relay method=4
2025-10-24 16:41:30.353 F Failed to insert key images from txpool tx
2025-10-24 16:41:30.353 E Failed to initialize memory pool
2025-10-24 16:41:30.396 I Stopping cryptonote protocol...
2025-10-24 16:41:30.396 I Cryptonote protocol stopped successfully
2025-10-24 16:41:30.396 E Exception in main! Failed to initialize core


This suggests 2 distinct txs using the same key image were relayed to @nahuhh's node, which the node **accepted** into the pool at one point. [This section](https://github.com/seraphis-migration/monero/blob/dbf9ff3110aa3aaec160442620fcb18edb99cf3f/src/cryptonote_core/tx_pool.cpp#L1338-L1364) is supposed to prevent that from happening, so I'm not sure how this could have possibly happened yet.

Also of note, my node does not have either of those txs.

# Discussion History
## j-berman | 2025-10-24T20:26:28+00:00
@nahuhh also noted

> The last thing that happened before the segfault was a new block

#181 similarly includes logs from the point of a new block.

## j-berman | 2025-10-24T20:38:50+00:00
> This suggests 2 distinct txs using the same key image were relayed to @nahuhh's node, which the node accepted into the pool at one point. [This section](https://github.com/seraphis-migration/monero/blob/dbf9ff3110aa3aaec160442620fcb18edb99cf3f/src/cryptonote_core/tx_pool.cpp#L1338-L1364) is supposed to prevent that from happening, so I'm not sure how this could have possibly happened yet.

The logs from #181 **also** indicate that txs are in the daemon's pool, but their spent key images are not in `m_spent_key_images` container (txs successfully removed from pool, but `failed to find transaction input in key images`). So the cause of this daemon's state definitely seems linked to #181.

Identifying how the daemon could have txs in its pool but not the associated spent key images in `m_spent_key_images` I believe is the next step toward solving both of these issues.

## j-berman | 2025-10-27T19:52:17+00:00
> Identifying how the daemon could have txs in its pool but not the associated spent key images in `m_spent_key_images` I believe is the next step toward solving both of these issues.

I've spent some time looking for a way the daemon can remove a tx's associated spent key images from `m_spent_key_images` (and the other in-memory containers), but not remove the tx from the db.

The one angle I have my eyes on is `m_batch_success` getting set to false [here](https://github.com/seraphis-migration/monero/blob/dbf9ff3110aa3aaec160442620fcb18edb99cf3f/src/cryptonote_core/blockchain.cpp#L4792-L4807). That should prevent the db txn in `cleanup_handle_incoming_blocks` from executing, preventing db ops started by `handle_block_to_main_chain` from being committed to the db. However, if a tx is taken from the db (and removed from the key image container), then it looks like it should get added back to the container in `return_txs_to_pool`.

The only way it looks like it might *not* get added back to the in-memory containers is if `insert_key_images` fails [here](https://github.com/seraphis-migration/monero/blob/dbf9ff3110aa3aaec160442620fcb18edb99cf3f/src/cryptonote_core/tx_pool.cpp#L490-L493) for one of the tx's key images.

So the following would have to happen:

1) Tx relayed to the node, it's in the stem phase of Dandelion++ and/or doesn't get relayed back to the node.
2) A block is mined including that tx.
3) The node receives the block.
4) [The node takes the tx from the pool](https://github.com/seraphis-migration/monero/blob/dbf9ff3110aa3aaec160442620fcb18edb99cf3f/src/cryptonote_core/blockchain.cpp#L4638-L4641). 
5) [The node fails to add the block to the db, setting `m_batch_success` to false](https://github.com/seraphis-migration/monero/blob/dbf9ff3110aa3aaec160442620fcb18edb99cf3f/src/cryptonote_core/blockchain.cpp#L4792-L4807).
6) The node attempts to re-add the tx back to the db in `return_txs_to_pool`.
7) Since the tx shouldn't be in the node (taken from the pool in step 4), [`existing_tx` should be false](https://github.com/seraphis-migration/monero/blob/fcmp%2B%2B-alpha-stressnet/src/cryptonote_core/tx_pool.cpp#L284).
8) After inserting the first key image back in `insert_key_images`, [the rest of the tx's key images then fail to insert because the tx was previously private](https://github.com/seraphis-migration/monero/blob/dbf9ff3110aa3aaec160442620fcb18edb99cf3f/src/cryptonote_core/tx_pool.cpp#L490-L493).
9) [The tx doesn't get added back to the in-memory containers](https://github.com/seraphis-migration/monero/blob/dbf9ff3110aa3aaec160442620fcb18edb99cf3f/src/cryptonote_core/tx_pool.cpp#L325).
10) Since `m_batch_success` was false, step 4 would not get commit to the db, and so the tx would remain in the pool but the associated spent key image would not be.

Seems an unlikely angle to me, but it would help to know if the node is seeing the following logs in proximity to `failed to find transaction input in key images`:

A) `internal error: try to insert duplicate iterator in key_image set`
B) `Error adding block with hash:`

## jeffro256 | 2025-10-29T17:44:31+00:00
Maybe related to https://github.com/monero-project/monero/issues/10163?

## j-berman | 2025-10-29T20:20:31+00:00
I think the cause of this one is probably linked to the pool's weird state, since upon restart it immediately fails showing the daemon is in an unexpected state. Whereas looks like OP in that issue can restart without issue

## j-berman | 2025-12-08T18:00:16+00:00
The pool's weird state is explained by the combination of [this](https://github.com/seraphis-migration/monero/issues/192#issuecomment-3453052958), and the borked `expand_transaction_2` (fixed by #251).

A tx can be removed from the in-memory containers when adding a block, then when the node finds its missing txs from the block it attempts to re-add the already removed txs, but that can fail to add back because of `expand_transaction_2`, which then means `m_batch_success` gets set to false. So because of that issue, a tx could be taken from the in-memory containers but not removed from the db.

It seems like the segfault is related to this underlying issue. Without knowing exactly where the segfault is yet, I think it's plausible @nahuhh won't see the same segfault with the fix from #251 in place.

## j-berman | 2026-02-16T17:34:33+00:00
Root cause appears solved

# Action History
- Created by: j-berman | 2025-10-24T17:20:06+00:00
- Closed at: 2026-02-16T17:34:33+00:00
