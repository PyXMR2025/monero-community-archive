---
title: '"Refresh" logic not resuming refresh from correct height causing excessive
  bandwidth / processing for nodes'
source_url: https://github.com/monero-project/monero/issues/9358
author: AlwaysCompile
assignees: []
labels:
- bug
- discussion
- more info needed
created_at: '2024-06-11T01:14:14+00:00'
updated_at: '2024-06-14T07:40:36+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I have discovered in my testing that the RPC wallet (and likely all wallets) are not correctly resuming after "refresh". Here is the sequence of steps where this is observed using the RPC wallet:

1) A) restart wallet RPC connected to remote daemon. B) call "refresh" C) call "store" and look at "Pulled blocks" to see result in the log

> Pulled blocks: blocks_start_height **3168255**, count 295, height 3168550, node height 3168550, pool info 2

2) A) restart wallet RPC connected to remote daemon. B) call "refresh" C) call "store" and look at "Pulled blocks" to see result in the log. Observe, it started at the same 3168255 start height.

> Pulled blocks: blocks_start_height **3168255**, count 304, height 3168559, node height 3168559, pool info 2

3) A) restart wallet RPC connected to remote daemon. B) call "height" and observe wallet height is 3168561 B) call "refresh" C) call "store" D) wait for "refresh" E) call height and observe wallet height is now 3168561 and look at "Pulled blocks" to see result in the log.

> Pulled blocks: blocks_start_height **3168255**, count 310, height 3168565, node height 3168565, pool info 2


After this I decided there is something seriously broken with how the wallet maintains it's state. Keep in mind, during this the wallet's reporetd height via "height" is hundreds of blocks ahead of where it is resuming to pull blocks from . So, I decided to manually specify the "start_height" in the "refresh" command and see what the result is:

> Pulling blocks: start_height 0
.....
> Pulled blocks: blocks_start_height **3168255**, count 310, height 3168565, node height 3168572, pool info 2

During this time I ran stat on the wallet to verify it was in fact storing the wallet during the "store" command. In addition, like I said, **the wallet itself reports a greater height when running the "height" command than the block it is starting to pull from.** And "height" is called before any refreshing starts. 

So, in other words, it is continually refreshing from a height that is less than the reported wallet height. The constant unnecessary refreshing is now causing about a 30 minute start-up penalty before the wallet is usable because already refreshed blocks must be downloaded and processed.


Unfortunately I am not a programmer, so I cannot really follow the code base.  But, I do know that this likely has serious consequences for remote nodes in terms of bandwidth costs and in terms of usability as users must constantly re-download the same blocks. There is some condition that will eventually get Monero to advance the block it will start from because it is a block that is greater than the restore height of the wallet, but it seems like that condition is not being met, so it constantly restarts from 3168255.

# Discussion History
# Action History
- Created by: AlwaysCompile | 2024-06-11T01:14:14+00:00
