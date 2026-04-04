---
title: Sync on v0.12.0 after accidental sync on v0.11.1 consuming all available memory,
  causing OOM
source_url: https://github.com/monero-project/monero/issues/3792
author: conscott
assignees: []
labels: []
created_at: '2018-05-10T08:33:18+00:00'
updated_at: '2018-06-16T00:29:08+00:00'
type: issue
status: closed
closed_at: '2018-05-20T20:26:44+00:00'
---

# Original Description
Apologies if this is a duplicated, I tried to check. 

A few days ago I restarted my v0.11.1.0 node, forgetting about the PoW change fork. The wallet happily synced to what a assume is some other fork (Classic or Original?) that didn't modify PoW. After seeing my balance has not been updated, I downloaded v0.12.0 and started the deamon back up. In order to resync with the right chain, I am getting the expected alternative chain messages...
```
[P2P2]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1547479
```

Starting from the fork height 1546000, however, as the alternative chain grows, so does the memory consumption of monerod, until it consumes all of my 16 GB of RAM. monerod doesn't actually ever die, but at some point it detects a fault in the sync, and the alt chain progress resets back to block height 1546000. So basically it gets to the point where it's got like 80% of the fork chain info, runs out of memory, and the thread crashes, and restarts back for fork height 1546000.

I am guessing that monerod doesn't have a way to save progress on a fork (must keep it all in memory), so the question is then: Is there a command I should be using to limit memory consumption, or is there a startup command for monerod that can help it sync to the right fork without trying to keep progress on the _actual_ alt chain (which I am currently synced to)?

# Discussion History
## dEBRUYNE-1 | 2018-05-10T09:37:26+00:00
>or is there a startup command for monerod that can help it sync to the right fork without trying to keep progress on the actual alt chain (which I am currently synced to)?

You can use this guide:

https://monero.stackexchange.com/questions/7989/i-forgot-to-upgrade-from-cli-or-gui-v0-11-to-cli-or-gui-v0-12-and-as-a-result

## moneromooo-monero | 2018-05-10T09:58:25+00:00
For any crash, please supply the crash stack trace.

## moneromooo-monero | 2018-05-20T13:10:37+00:00
> at some point it detects a fault in the sync, and the alt chain progress resets back to block height 1546000.

Such sync bugs are now fixed in the release-v0.12 branch. Maybe that also takes care of the excessive memory usage at the same time.


## conscott | 2018-05-20T20:26:44+00:00
Thanks!

## mmortal03 | 2018-06-16T00:29:08+00:00
> Maybe that also takes care of the excessive memory usage at the same time.

@moneromooo-monero , unfortunately, I'm still seeing that, at least on Windows, with 0.12.2.0, as you've seen discussed at the following: https://github.com/monero-project/monero/issues/2732

Might a workaround be to significantly lower or raise the batch-size, block-sync-size, and/or the nblocks_per_sync parameters? It's not clear to me which of these I'd want to lower and which of these I'd want to raise.

# Action History
- Created by: conscott | 2018-05-10T08:33:18+00:00
- Closed at: 2018-05-20T20:26:44+00:00
