---
title: Sync get stuck
source_url: https://github.com/monero-project/monero/issues/4867
author: ElLamparto
assignees: []
labels: []
created_at: '2018-11-18T18:10:25+00:00'
updated_at: '2018-12-13T01:17:08+00:00'
type: issue
status: closed
closed_at: '2018-12-13T01:17:08+00:00'
---

# Original Description
Monero 'Beryllium Bullet' (v0.13.0.4-release), Debian Stretch 32bit.

DB migration failed: 
[MoneroFailedDBConversion.txt](https://github.com/monero-project/monero/files/2593067/MoneroFailedDBConversion.txt)

Then I synced from scratch. After a couple of weeks, it got stuck at 97.7% at height: 1651112.
I deleted the last 10 blocks: monero-blockchain-import --pop-blocks 10
and restarted monerod. It quickly resynchronized the 10 blocks and got stuck again.

What can I do?
Thanks for any hint.








# Discussion History
## moneromooo-monero | 2018-11-18T18:56:22+00:00
Start monerod with --log-level 2, wait it to get stuck again, post the logs to fpaste.org or similar.

## ElLamparto | 2018-11-20T08:29:42+00:00
[bitmonero.log.zip](https://github.com/monero-project/monero/files/2598757/bitmonero.log.zip)


## moneromooo-monero | 2018-11-20T12:33:14+00:00
If I post a patch adding more logs, can you build with it and post the extra logs to help debug ?

## moneromooo-monero | 2018-11-20T12:59:28+00:00
Here's the patch. Save to PATCH and apply with : patch -p1 \< PATCH

<pre>
diff --git a/src/cryptonote_core/blockchain.cpp b/src/cryptonote_core/blockchain.cpp
index fa23b6bd2..3d6fb3677 100644
--- a/src/cryptonote_core/blockchain.cpp
+++ b/src/cryptonote_core/blockchain.cpp
@@ -638,6 +638,7 @@ block Blockchain::pop_block_from_blockchain()
 
   m_blocks_longhash_table.clear();
   m_scan_table.clear();
+MDEBUG("clearing");
   m_blocks_txs_check.clear();
   m_check_txin_table.clear();
 
@@ -2258,12 +2259,14 @@ bool Blockchain::get_tx_outputs_gindexs(const crypto::hash& tx_id, std::vector<u
 //------------------------------------------------------------------
 void Blockchain::on_new_tx_from_block(const cryptonote::transaction &tx)
 {
+MDEBUG("on_new_tx_from_block: db height " << m_db->height() << ", m_blocks_hash_check size " << m_blocks_hash_check.size() << ", tx " << get_transaction_hash(tx));
 #if defined(PER_BLOCK_CHECKPOINT)
   // check if we're doing per-block checkpointing
   if (m_db->height() < m_blocks_hash_check.size())
   {
     TIME_MEASURE_START(a);
     m_blocks_txs_check.push_back(get_transaction_hash(tx));
+MDEBUG("pushed, now " << m_blocks_txs_check.size());
     TIME_MEASURE_FINISH(a);
     if(m_show_time_stats)
     {
@@ -3450,9 +3453,14 @@ leave:
     {
       // ND: if fast_check is enabled for blocks, there is no need to check
       // the transaction inputs, but do some sanity checks anyway.
+const bool flag = tx_index >= m_blocks_txs_check.size();
       if (tx_index >= m_blocks_txs_check.size() || memcmp(&m_blocks_txs_check[tx_index++], &tx_id, sizeof(tx_id)) != 0)
       {
         MERROR_VER("Block with id: " << id << " has at least one transaction (id: " << tx_id << ") with wrong inputs.");
+MERROR_VER("tx_index: " << tx_index << ", flag " << flag);
+MERROR_VER("tx_id: " << tx_id);
+MERROR_VER("m_blocks_txs_check: " << m_blocks_txs_check.size());
+for (const auto &h: m_blocks_txs_check) MERROR_VER("  : " << h);
         //TODO: why is this done?  make sure that keeping invalid blocks makes sense.
         add_block_as_invalid(bl, id);
         MERROR_VER("Block with id " << id << " added as invalid because of wrong inputs in transactions");
@@ -3468,6 +3476,7 @@ leave:
     cumulative_block_weight += tx_weight;
   }
 
+MDEBUG("clearing");
   m_blocks_txs_check.clear();
 
   TIME_MEASURE_START(vmt);
@@ -3591,6 +3600,7 @@ bool Blockchain::add_new_block(const block& bl_, block_verification_context& bvc
     LOG_PRINT_L3("block with id = " << id << " already exists");
     bvc.m_already_exists = true;
     m_db->block_txn_stop();
+MDEBUG("clearing");
     m_blocks_txs_check.clear();
     return false;
   }
@@ -3602,6 +3612,7 @@ bool Blockchain::add_new_block(const block& bl_, block_verification_context& bvc
     bvc.m_added_to_main_chain = false;
     m_db->block_txn_stop();
     bool r = handle_alternative_block(bl, id, bvc);
+MDEBUG("clearing");
     m_blocks_txs_check.clear();
     return r;
     //never relay alternative blocks
@@ -3759,6 +3770,7 @@ bool Blockchain::cleanup_handle_incoming_blocks(bool force_sync)
   TIME_MEASURE_FINISH(t1);
   m_blocks_longhash_table.clear();
   m_scan_table.clear();
+MDEBUG("clearing");
   m_blocks_txs_check.clear();
   m_check_txin_table.clear();
 
</pre>

## ElLamparto | 2018-11-23T08:44:08+00:00
Do you want me to recompile monerod? If so, I prefer that you give me an executable or you add the extra traces to the next release of monero.

## moneromooo-monero | 2018-11-23T13:43:03+00:00
Yes. I'll PR this to a temp branch so the build machine creates a binary. I'll post again when that's ready.

## moneromooo-monero | 2018-11-23T14:51:18+00:00
What version are you running now ?

## ElLamparto | 2018-11-23T18:47:20+00:00
Monero 'Beryllium Bullet' (v0.13.0.4-release), Debian Stretch 32bit.

## moneromooo-monero | 2018-11-24T00:03:40+00:00
https://build.getmonero.org/downloads/monero-567b5fd9-win32.tar.gz

## moneromooo-monero | 2018-11-24T00:04:40+00:00
Run with: --log-level 2

## ElLamparto | 2018-11-25T16:49:23+00:00
Win32? I am on Linux 32bit. Sorry.

## moneromooo-monero | 2018-11-25T17:22:22+00:00
https://build.getmonero.org/builders/monero-static-ubuntu-i686/builds/5828

## ElLamparto | 2018-11-26T20:31:11+00:00
[bitmonero.zip](https://github.com/monero-project/monero/files/2617220/bitmonero.zip)
Here is the log. Good luck!

## moneromooo-monero | 2018-11-27T00:24:00+00:00
I think https://build.getmonero.org/builders/monero-static-ubuntu-i686/builds/5855 fixes it. <s>The binary is not ready yet, it'll be linked from that page when finished.</s>Binary ready.

## ElLamparto | 2018-11-28T08:18:25+00:00
It is syncing again. Good work!. Thank you.

## moneromooo-monero | 2018-11-30T11:28:22+00:00
Don't close bugs which are fixed by a patch please. They should get closed when the patch gets merged. If you close them like this, chances are I'll forget to PR the patch unless I stumble upon thus bug by chance, like now.

## ElLamparto | 2018-11-30T21:09:22+00:00
Ok, I'll let you the honor...

## moneromooo-monero | 2018-12-13T01:14:30+00:00
Now merged.

+resolved

# Action History
- Created by: ElLamparto | 2018-11-18T18:10:25+00:00
- Closed at: 2018-12-13T01:17:08+00:00
