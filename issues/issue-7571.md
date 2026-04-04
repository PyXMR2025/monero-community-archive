---
title: Reduce the number of requests to poll a daemon
source_url: https://github.com/monero-project/monero/issues/7571
author: woodser
assignees: []
labels: []
created_at: '2021-03-14T12:10:50+00:00'
updated_at: '2023-11-25T16:40:54+00:00'
type: issue
status: closed
closed_at: '2023-11-25T16:40:45+00:00'
---

# Original Description
Currently, wallets make up to 4 requests each time a wallet polls a daemon: get_info, get_transaction_pool_hashes, get_transactions, and get_blocks.bin.

As a result, daemons must service up to 4 requests for each client poll, and the user may experience a noticeable delay before their wallet even starts to sync blocks if their connection is slow.

This issue requests reducing the number of requests to poll from 4 to 1 wherein the daemon responds with everything needed:

- Txs in the pool not previously seen by the client
- Txs dropped from the pool
- Current chain height
- New blocks and confirmed txs

The wallet may send a client id to the daemon to track what has been previously served.

@moneromooo suggests this RPC call could piggyback on the existing get_blocks.bin RPC call.

# Discussion History
## hyc | 2021-09-11T18:12:43+00:00
Requiring the monerod to remember clientIDs and their last state is a bad idea. Instead, the client just needs to send the last height & hash of the last block it knows about, plus the timestamp of the last time it saw the txn pool. The timestamp should be one that obtained from monerod itself. (f the block height & hash don't match on monerod side, that means there was a reorg.)

So, extending the get_blocks.bin RPC, should also add monerod's current timestamp.

## j-berman | 2021-09-12T01:33:12+00:00
I'm in to work on this!

Thinking out loud on the reorg case: if it's determined there was a reorg, it seems the monerod side could find the block on an alternate chain, then find the divergent height of that alternate chain from the main chain, then return blocks/transactions (and perhaps just return all tx's in the pool for simplicity) since that height. Wondering if that's how the alternate chain can/should be used.

Note: I included this issue as a bullet in my CCS proposal - it wouldn't make sense for me to take a bounty for it.

## rbrunner7 | 2021-09-12T05:45:36+00:00
If @j-berman changes his mind, or priorities won't allow him to work on it after all, this would also be within reach for me. Don't intend to snatch it from him by submitting faster, however :)

## j-berman | 2021-09-12T07:14:01+00:00
All yours @rbrunner7 :) I've got a fair amount of things to work on

## rbrunner7 | 2021-09-12T07:40:10+00:00
Thanks, @j-berman, kind of you.

Alright, then I will try my luck. I estimate that it might take me 3 calendar weeks or so until PR because working in my spare time.

## erciccione | 2021-09-12T08:10:21+00:00
@rbrunner7 glad to hear that, please comment on https://github.com/haveno-dex/haveno/issues/110 so i can assign the issue to you.

## selsta | 2023-11-25T16:40:52+00:00
Implemented in #8076

# Action History
- Created by: woodser | 2021-03-14T12:10:50+00:00
- Closed at: 2023-11-25T16:40:45+00:00
