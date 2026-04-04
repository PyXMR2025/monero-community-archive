---
title: 'Unable to make import_multisig_info: Daemon claims reorg below last checkpoint'
source_url: https://github.com/monero-project/monero/issues/3505
author: naughtyfox
assignees: []
labels: []
created_at: '2018-03-27T15:32:14+00:00'
updated_at: '2018-04-28T14:54:56+00:00'
type: issue
status: closed
closed_at: '2018-04-28T14:54:56+00:00'
---

# Original Description
I'm playing around with monero multisignatures and encountered the error in current master:
```
[wallet 49yJuz]: export_multisig_info info1
Wallet password: 
File info1 already exists. Are you sure to overwrite it? (Y/Yes/N/No): y
Multisig info exported to info1
[wallet 49yJuz]: import_multisig_info info2 info3
Wallet password: 
Error: Failed to import multisig info: Daemon claims reorg below last checkpoint
[wallet 49yJuz]: 
```
This happens because wallet wants to `detach_blockchain` on height where the first multisignture output is met (which is 1520XXX), but there is new checkpoint on height 1530000 so sanity check inside the function throws the error. 




# Discussion History
## moneromooo-monero | 2018-03-27T16:06:15+00:00
Good catch!

I can't try it right now, but this should fix it (you'll have to delete the wallet cache first):

```
diff --git a/src/wallet/wallet2.cpp b/src/wallet/wallet2.cpp
index dab2129..d22f72f 100644
--- a/src/wallet/wallet2.cpp
+++ b/src/wallet/wallet2.cpp
@@ -3822,6 +3822,10 @@ void wallet2::load(const std::string& wallet_, const epee::wipeable_string& pass
 void wallet2::trim_hashchain()
 {
   uint64_t height = m_checkpoints.get_max_height();
+  for (const transfer_details &td: m_transfers)
+    if (td.m_block_height < height)
+      height = td.m_block_height;
+
   if (!m_blockchain.empty() && m_blockchain.size() == m_blockchain.offset())
   {
     MINFO("Fixing empty hashchain");
```

## naughtyfox | 2018-03-28T16:40:32+00:00
deleted `mainnet-1` file (is this considered as cache file?), remained only `mainnet-1.keys` and `mainnet-1.address.txt`, repeated on rest 2 wallets, applied the patch, built and this didn't help.


## moneromooo-monero | 2018-03-28T22:39:32+00:00
Yes, that's the cache file.
I'll try to repro when I can then.

# Action History
- Created by: naughtyfox | 2018-03-27T15:32:14+00:00
- Closed at: 2018-04-28T14:54:56+00:00
