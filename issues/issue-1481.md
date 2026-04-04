---
title: Wallet gets stuck at "Starting refresh... Height 810359 / 810360", or whatever
  the highest blocks are.
source_url: https://github.com/monero-project/monero/issues/1481
author: RandomRun
assignees: []
labels:
- invalid
created_at: '2016-12-21T02:28:53+00:00'
updated_at: '2017-09-02T12:54:19+00:00'
type: issue
status: closed
closed_at: '2017-09-02T12:54:19+00:00'
---

# Original Description
This was observed in testnet, I didn't check on the mainnet. After starting a wallet, the command line interface is unusable due to the wallet being stuck in the refreshing phase. Sometimes, pressing escape, or ctrl+c, or typing exit seems to make it stop, but it would be good to have that fixed. Thanks!

# Discussion History
## moneromooo-monero | 2016-12-21T11:59:16+00:00
It will fix itself when the daemon stops seeing a larger chain. At the moment, when started the daemon will spend quite a lot of time syncing blocks from that chain, then do a reorg to it, then realize it's not a good idea, then reorg back. And that takes quite some time, due to the size of the reorg (~10k blocks I think).
Might be fixable by adding a checkpoint though, not sure where in the reorg proces this'd get checked...


## moneromooo-monero | 2016-12-22T11:27:32+00:00
The following bodge will ignore the bad chain. Use only on testnet or it will stop mainnet from syncing.

diff --git a/src/cryptonote_protocol/cryptonote_protocol_handler.inl b/src/cryptonote_protocol/cryptonote_protocol_handler.inl
index b13c1f4..d154e9d 100644
--- a/src/cryptonote_protocol/cryptonote_protocol_handler.inl
+++ b/src/cryptonote_protocol/cryptonote_protocol_handler.inl
@@ -274,6 +274,7 @@ namespace cryptonote
         on_connection_synchronized();
       return true;
     }
+if (hshd.current_height > 855000) return true;
 
     /* As I don't know if accessing hshd from core could be a good practice,
     I prefer pushing target height to the core at the same time it is pushed to the user.


## gituser | 2016-12-22T13:21:32+00:00
I've stumbled across the same issue: https://github.com/monero-project/monero/issues/1476#issuecomment-268272104

The quickest way is to re-import your wallet via deterministic seed into new wallet file.

## moneromooo-monero | 2017-09-02T12:47:28+00:00
I'll close as invalid, since it's really a freak scenario (3 months of reorg IIRC). There was another case where scanning the txpool was pretty slow, and that one's now fixed.

+invalid

# Action History
- Created by: RandomRun | 2016-12-21T02:28:53+00:00
- Closed at: 2017-09-02T12:54:19+00:00
