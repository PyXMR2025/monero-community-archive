---
title: Stale block template cache
source_url: https://github.com/monero-project/monero/issues/5553
author: hyc
assignees: []
labels: []
created_at: '2019-05-18T08:40:20+00:00'
updated_at: '2019-06-01T18:20:54+00:00'
type: issue
status: closed
closed_at: '2019-06-01T18:20:54+00:00'
---

# Original Description
If multiple daemons are mining and sharing the same DB, the block template cache can become stale because it only gets invalidated by successful add_block, and since the DB is shared, the block doesn't get added on the daemons that didn't mine the current block. (It's already in the DB.) I guess this is a stupid use case, and will only occur in testing. Just wanted to document it in case anyone else runs into it. Can be fixed like so:
````
diff --git a/src/cryptonote_core/blockchain.cpp b/src/cryptonote_core/blockchain.cpp
index 5c6e5de98..4abc70f29 100644
--- a/src/cryptonote_core/blockchain.cpp
+++ b/src/cryptonote_core/blockchain.cpp
@@ -1367,10 +1367,14 @@ bool Blockchain::create_block_template(block& b, const crypto::hash *from_block,
   size_t median_weight;
   uint64_t already_generated_coins;
   uint64_t pool_cookie;
+  uint64_t b_height;
 
   m_tx_pool.lock();
   const auto unlock_guard = epee::misc_utils::create_scope_leave_handler([&]() { m_tx_pool.unlock(); });
   CRITICAL_REGION_LOCAL(m_blockchain_lock);
+  b_height = m_db->height();
+  if (b_height != m_btc_height)
+    m_btc_valid = false;
   if (m_btc_valid && !from_block) {
     // The pool cookie is atomic. The lack of locking is OK, as if it changes
     // just as we compare it, we'll just use a slightly old template, but
````


# Discussion History
## moneromooo-monero | 2019-05-18T09:40:11+00:00
Easy fix, definitely worth merging. Though in that case we probably need to store the tip hash, rather than just the height, or the "ghost" monerod might pop once then push another.

## hyc | 2019-05-18T13:54:51+00:00
Could we just check
````
get_tail_id() != m_btc.prev_id
````

## moneromooo-monero | 2019-05-18T18:01:03+00:00
I think so, yes.

# Action History
- Created by: hyc | 2019-05-18T08:40:20+00:00
- Closed at: 2019-06-01T18:20:54+00:00
