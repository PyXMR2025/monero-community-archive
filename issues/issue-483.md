---
title: Berkeley DB broken after commit 0a5a5e859791b6ff0ced2a3f403eed71fb41dee2. It
  won't sync past block 600003.
source_url: https://github.com/monero-project/monero/issues/483
author: osensei
assignees: []
labels: []
created_at: '2015-11-11T18:00:36+00:00'
updated_at: '2015-11-13T17:37:11+00:00'
type: issue
status: closed
closed_at: '2015-11-13T17:37:11+00:00'
---

# Original Description
I noticed that my RPi2 had got stuck on the same block after upgrading the daemon.

With every attempt to get new blocks the daemon would show the message:

> Skipping prepare blocks. New blocks don't belong to chain.

Setting log level to 1 would show:

```
2015-Nov-09 22:05:11.600180 [P2P9][104.156.227.151:18080 OUT]-->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=200, txs.size()=0requested blocks count=200 / 200
2015-Nov-09 22:05:13.892427 [P2P8][104.156.227.151:18080 OUT]Got NEW BLOCKS inside of handle_response_get_objects: size: 200
2015-Nov-09 22:06:01.822097 [P2P8]Index: 505518 Elems: 505495 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:02.270326 [P2P8]Index: 347969 Elems: 347969 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:02.357075 [P2P8]Index: 301431 Elems: 301430 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:02.532862 [P2P8]Index: 643156 Elems: 643156 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:02.601718 [P2P8]Index: 302613 Elems: 302612 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:02.681018 [P2P8]Index: 215498 Elems: 215498 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:02.749411 [P2P8]Index: 178443 Elems: 178442 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:02.790547 [P2P8]Index: 188869 Elems: 188866 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:02.841429 [P2P8]Index: 121973 Elems: 121967 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:02.870627 [P2P8]Index: 91181 Elems: 91181 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:02.906439 [P2P8]Index: 152158 Elems: 152158 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:02.942079 [P2P8]output with given index not in db
2015-Nov-09 22:06:02.943011 [P2P8]EXCEPTION: output with given index not in db
2015-Nov-09 22:06:02.979615 [P2P8]Index: 168914 Elems: 168910 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:03.143618 [P2P8]Index: 697885 Elems: 697885 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:03.155190 [P2P8]Index: 43069 Elems: 43064 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:03.163884 [P2P8]Index: 25451 Elems: 25450 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:03.174764 [P2P8]Index: 20697 Elems: 20695 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:03.188710 [P2P8]Index: 15004 Elems: 14999 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:03.208156 [P2P8]Index: 22854 Elems: 22853 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:03.225001 [P2P8]Index: 6603 Elems: 6600 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:03.228111 [P2P8]Index: 1966 Elems: 1964 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:03.230171 [P2P8]Index: 2389 Elems: 2389 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:03.232228 [P2P8]Index: 4357 Elems: 4357 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:03.235647 [P2P8]Index: 1033 Elems: 1033 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:03.237076 [P2P8]Index: 825 Elems: 825 partial results found for get_output_tx_and_index
2015-Nov-09 22:06:03.412888 [P2P8]transaction with hash e2ba49d7e83787f8d56b2536e1fafad6b67350994e967f412084ab30767825b1 not found in db
2015-Nov-09 22:06:03.443958 [P2P8]Failed to check ring signatures!, t_loop: 0
2015-Nov-09 22:06:03.444433 [P2P8]Block with id: <8b1c847fc1dd65b2674e48e1b2c6d2d8e8a61d7b9608f629a8ab5cd16d82ced3> has at least one transaction (id: <e2ba49d7e83787f8d56b2536e1fafad6b67350994e967f412084ab30767825b1>) with wrong inputs.
2015-Nov-09 22:06:03.445017 [P2P8]BLOCK ADDED AS INVALID: <8b1c847fc1dd65b2674e48e1b2c6d2d8e8a61d7b9608f629a8ab5cd16d82ced3>, prev_id=<e1deb5f98ae823073ae24efaf8740424a600e908f33579972cc5a8fd4d5e3f84>, m_invalid_blocks count=1
2015-Nov-09 22:06:03.445516 [P2P8]Block with id <8b1c847fc1dd65b2674e48e1b2c6d2d8e8a61d7b9608f629a8ab5cd16d82ced3> added as invalid because of wrong inputs in transactions
2015-Nov-09 22:06:03.449843 [P2P8]coinbase transaction spend too much money (8.319695860938). Block reward is 8.196675093564(8.196675093564+0.000000000000)
2015-Nov-09 22:06:03.450329 [P2P8]Block with id: <8b1c847fc1dd65b2674e48e1b2c6d2d8e8a61d7b9608f629a8ab5cd16d82ced3> has incorrect miner transaction
2015-Nov-09 22:06:03.472842 [P2P8]Failed to check ring signatures!, t_loop: 0
2015-Nov-09 22:06:03.473876 [P2P8][104.156.227.151:18080 OUT]Block verification failed, dropping connection
2015-Nov-09 22:06:03.474643 [P2P8]Failed to invoke command 1002 return code -3
2015-Nov-09 22:06:03.475010 [P2P8][104.156.227.151:18080 OUT]COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
```

So I thought that maybe my DB had got corrupted and decided to sync it again from scratch. For faster performance I did it on a VPS running Ubuntu 15.04 i386 (using gcc4.8 and g++4.8 instead of 4.9 as that's what I'm using on my RPI2 because of the issue I described [here](https://forum.getmonero.org/5/support/2375/can-t-sync-further-than-block-600000-on-rpi2?page=&noscroll=1#post-3966))

When syncing from scratch, the daemon wasn't able to go past block 600003, recognizing block 600004 as orphaned:

```
2015-Nov-10 22:45:38.162582 [P2P5][10.99.0.11:18080 OUT]Got NEW BLOCKS inside of handle_response_get_objects: size: 200
2015-Nov-10 22:45:38.172069 [P2P5]Attempting to get an output index by amount and amount index, but amount not found
2015-Nov-10 22:45:38.172430 [P2P5]EXCEPTION: Attempting to get an output index by amount and amount index, but amount not found
2015-Nov-10 22:45:38.172658 [P2P5]Attempting to get an output index by amount and amount index, but amount not found
2015-Nov-10 22:45:38.172883 [P2P5]EXCEPTION: Attempting to get an output index by amount and amount index, but amount not found
2015-Nov-10 22:45:38.173102 [P2P5]Attempting to get an output index by amount and amount index, but amount not found
2015-Nov-10 22:45:38.173262 [P2P5]EXCEPTION: Attempting to get an output index by amount and amount index, but amount not found
2015-Nov-10 22:45:38.177119 [P2P5]Attempting to get an output index by amount and amount index, but amount not found
2015-Nov-10 22:45:38.177445 [P2P5]EXCEPTION: Attempting to get an output index by amount and amount index, but amount not found
2015-Nov-10 22:45:38.182013 [P2P5]Index: 379286 Elems: 379283 partial results found for get_output_tx_and_index
2015-Nov-10 22:45:38.187572 [P2P5]Index: 203994 Elems: 203993 partial results found for get_output_tx_and_index
2015-Nov-10 22:45:38.192281 [P2P5]Index: 160939 Elems: 160935 partial results found for get_output_tx_and_index
2015-Nov-10 22:45:38.195128 [P2P5]Index: 146588 Elems: 146580 partial results found for get_output_tx_and_index
2015-Nov-10 22:45:38.197170 [P2P5]Index: 138615 Elems: 138615 partial results found for get_output_tx_and_index
2015-Nov-10 22:45:38.210213 [P2P5]Index: 767858 Elems: 767857 partial results found for get_output_tx_and_index
2015-Nov-10 22:45:38.221641 [P2P5]Index: 919657 Elems: 919657 partial results found for get_output_tx_and_index
2015-Nov-10 22:45:38.229557 [P2P5]Index: 576475 Elems: 576465 partial results found for get_output_tx_and_index
2015-Nov-10 22:45:38.235714 [P2P5]Index: 429831 Elems: 429823 partial results found for get_output_tx_and_index
2015-Nov-10 22:45:38.254397 [P2P5]Index: 437187 Elems: 437180 partial results found for get_output_tx_and_index
2015-Nov-10 22:45:38.266584 [P2P5]Index: 253644 Elems: 253637 partial results found for get_output_tx_and_index
2015-Nov-10 22:45:38.274320 [P2P5]Index: 573561 Elems: 573534 partial results found for get_output_tx_and_index
2015-Nov-10 22:45:38.281353 [P2P5]Index: 194994 Elems: 194985 partial results found for get_output_tx_and_index
2015-Nov-10 22:45:38.283687 [P2P5]Index: 164010 Elems: 164003 partial results found for get_output_tx_and_index
2015-Nov-10 22:45:38.291068 [P2P5]Index: 79241 Elems: 79241 partial results found for get_output_tx_and_index
2015-Nov-10 22:45:38.293455 [P2P5]Index: 49647 Elems: 49641 partial results found for get_output_tx_and_index
2015-Nov-10 22:45:38.302925 [P2P5]Index: 680691 Elems: 680689 partial results found for get_output_tx_and_index
2015-Nov-10 22:45:38.313319 [P2P5]Block recognized as orphaned and rejected, id = <a4701970ed5a6224dce5777485962d2a2d791fc12ae468b36c830f55c60f3a96>
2015-Nov-10 22:45:38.313629 [P2P5][10.99.0.11:18080 OUT]Block received at sync phase was marked as orphaned, dropping connection
```

Doing some tests, I nailed the problem down to this particular commit: [0a5a5e859791b6ff0ced2a3f403eed71fb41dee2](https://github.com/monero-project/bitmonero/commit/0a5a5e859791b6ff0ced2a3f403eed71fb41dee2)

Reverting that commit solved the problem and I was able to continue syncing on both the VPS and the RPi2.


# Discussion History
## moneromooo-monero | 2015-11-11T23:07:23+00:00
I think this is just because you had an already partly synced DB, so the existing data would have the "wrong" indices. If you are able, could you blockchain_export when you're done syncing, then try blockchain_import with the patch in (or just sync from scratch with the patch in, if bandwidth isn't an issue) ?


## osensei | 2015-11-11T23:28:10+00:00
As I mentioned on the description, on the tests I did on the VPS, I synced the blockchain from the start, building the daemon from the latest master commit, and it wasn't able to sync past block 600003, so that shouldn't be the issue.


## osensei | 2015-11-11T23:44:14+00:00
Reverting that commit, with the newly synced chain from scratch (using the latest code) which got stuck at 600003, allowed it to continue syncing.


## osensei | 2015-11-12T15:20:16+00:00
Just to re-confirm, in case I could have messed something up in my previous tests going back and forward between commits, I tried it again with the same results.

These are the steps I followed:
1. Build from latest master code.
2. Sync blockchain from scratch using BerkeleyDB
3. Will fail to include block 600004 into the blockchain, recognizing it as orphaned.
4. git revert 0a5a5e859791b6ff0ced2a3f403eed71fb41dee2
5. Build again
6. Run daemon -> will continue syncing without any problem.


## moneromooo-monero | 2015-11-13T09:33:23+00:00
So I think I'm just an idiot indeed. Looking carefully, at least one of those indices is passed around from somewhere with code implying it's already offset by 1.
So I've reverted the patch, it should be merged soon. Thanks for reporting, and sorry for the trouble.


## osensei | 2015-11-13T17:37:05+00:00
No problem! I'm glad I could help. Thanks for looking into it.


# Action History
- Created by: osensei | 2015-11-11T18:00:36+00:00
- Closed at: 2015-11-13T17:37:11+00:00
