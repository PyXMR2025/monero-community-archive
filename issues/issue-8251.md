---
title: 'Feature: resubmit a failed tx from the wallet'
source_url: https://github.com/monero-project/monero/issues/8251
author: j-berman
assignees: []
labels: []
created_at: '2022-04-10T08:51:05+00:00'
updated_at: '2022-05-29T21:24:47+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
### Overview

My wallet is connected to my node via tor, my node uses the tx proxy over tor. This happened the other day:

1. I created a tx in a mobile wallet and hit send. It submit successfully and entered the "pending" state in my wallet, then after several minutes the tx entered the "failed" state. The other person didn't see the tx in their wallet, nor did I see the tx on a global block explorer (i.e. my node apparently didn't broadcast it to the rest of the network).
2. I tried to create another tx and got a "rejected because of double spend" error.
3. I created another tx from a separate account (same wallet same node) that broadcast to the rest of the network and confirmed on chain without issue. I knew this 2nd tx was risky but I wanted to pay the guy and I wanted to use my node.
4. Some number of minutes later, the first failed tx from step 1 ended up on chain without action on my part.

So I ended up paying someone twice and never saw them again unfortunately (the one that got away). I figure there could probably be some fail-safe to protect against this scenario better. I think the best fail-safe is enabling the user to resubmit a failed tx to a node from their wallet in a cleaner way. I don't see an RPC endpoint for this particular scenario.

### My investigation so far

First off, this issue happens to me sporadically and I've yet to capture it in useful logs, but I'm hoping I will soon.

This is what I believe is happening: upon initial successful tx submission, my tx first enters my node's pool with the [`relay_method::local`](https://github.com/monero-project/monero/blob/9a124f681119855949f6406ecd69c2ad91da9770/src/rpc/core_rpc_server.cpp#L1291) state, and then *sporadically* it takes quite a bit of time before the tx reaches the `relay_method::fluff` state (which AFAIU occurs after another node tells mine it knows about the tx and [Dandellion++ has completed](https://github.com/monero-project/monero/blob/f49fc9b4876382d5c6f08fd7a6125b554c49e260/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L1006)). So on occasion, before the tx reaches the fluff state on my node, in my wallet it enters the "failed" state from [this 500 second propagation timeout here](https://github.com/monero-project/monero/blob/f49fc9b4876382d5c6f08fd7a6125b554c49e260/src/wallet/wallet2.cpp#L3035-L3040), and my wallet indicates this to me in the UI.

Note [this TODO inside `core_rpc_server::on_send_raw_tx`](https://github.com/monero-project/monero/blob/9a124f681119855949f6406ecd69c2ad91da9770/src/rpc/core_rpc_server.cpp#L1292):

> //TODO: make sure that tx has reached other nodes here, probably wait to receive reflections from other nodes

Because my node responds successfully to the RPC server call to `send_raw_tx` even before knowing other nodes have seen the tx, the client thinks the tx submit successfully (naturally), even though it has not broadcast to the rest of the network.

I'm able to repro the failed state consistently by submitting a tx to my node, then immediately setting `out_peers 0` to cut my node off from the rest of the network *before* the tx enters the `relay_method::fluff` state, which eventually triggers the propagation timeout that causes the failure to appear in my wallet.

### My takes

1. First and foremost, ideally it wouldn't take so long for my node to broadcast the tx to other nodes in those apparent edge cases. Solving that will take more investigation that the logs may help with, and I suspect #7760 and related work may help with this too. However, at the end of the day, I still think it is optimal to have a stronger fail-safe UX under not-so-great network conditions.

2. It would have been nice to be able to re-submit the failed tx from my wallet, exactly as is. If a node receives a re-submission attempt for a tx that is already in the pool but not in `relay_method::fluff` state, the node can attempt to rebroadcast, and indicate to the wallet it's retrying (or still trying) the broadcast flow, then the tx can re-enter a pending state in the wallet.

3. More debatable, but I don't think the user should get a "successfully sent" indicator in the wallet until the tx has been confirmed broadcast to the rest of the network. Either [this TODO](https://github.com/monero-project/monero/blob/9a124f681119855949f6406ecd69c2ad91da9770/src/rpc/core_rpc_server.cpp#L1292) should be solved in that exact spot/line above, or alternatively, after the node responds successfully from `on_send_raw_tx`, the client should wait until it sees the tx in the pool before indicating to the user the tx sent successfully. I lean toward the latter as safer because otherwise traffic analysis might be easier to determine that a tx was broadcast from a particular node, by observing timing of payloads going into and out of a node.

4. I think the wallet was failing to recognize the node eventually did broadcast the tx. At some point the tx should have re-entered the "pending" state since the tx eventually did broadcast, but I don't think there was any logic handling it re-entering the "pending" state after it had already failed. Could be wrong on this. Still looking.


# Discussion History
## selsta | 2022-04-10T17:06:05+00:00
Could https://github.com/monero-project/monero/issues/6929 be related?

## j-berman | 2022-04-11T04:22:12+00:00
Looks like the same thing I was running into to me!

And duh.. seems `relay_tx` is the daemon RPC endpoint that should enable re-submitting the tx. I think there could be a wallet API hook that enables the user to re-submit the tx id, which calls the daemon RPC's `relay_tx`. On success, the wallet places the tx back into the "pending" state.

I'll see if I can capture more useful logs to help get to the bottom of why it's not broadcasting in the first place. I'll include any useful logs over in that issue.

## reemuru | 2022-04-12T03:40:19+00:00
I think I may have had a similar issue when using i2p tx routing, but even relay didn't work. I had to flush the tx pool before re-submitting. Maybe *also have an option to 'cancel' a stuck tx and API hook into flushing the tx pool before creating another one?

## j-berman | 2022-04-12T05:01:10+00:00
It seems both [`relay_tx`](https://github.com/monero-project/monero/blob/f49fc9b4876382d5c6f08fd7a6125b554c49e260/src/rpc/core_rpc_server.h#L179) and [`flush_txpool`](https://github.com/monero-project/monero/blob/f49fc9b4876382d5c6f08fd7a6125b554c49e260/src/rpc/core_rpc_server.h#L173) are restricted endpoints. `flush_txpool` makes sense to me to keep restricted for DoS protection (edit: can't allow anyone to cancel transactions in your pool). I didn't assume `relay_tx` is restricted. Not sure why that is/what that is protecting (also confused especially considering [this explicitly looks like logic allowing restricted nodes to expose relay_tx](https://github.com/monero-project/monero/blob/f49fc9b4876382d5c6f08fd7a6125b554c49e260/src/rpc/core_rpc_server.cpp#L3144).. maybe this has something to do with the bug? idk going to continue investigating to try to understand this).

In any case, I figure ideally some re-submission flow should work for someone connected to a public ~un~restricted node as well who wants to re-submit a tx from their wallet. I think it may make sense that if a node receives a request to submit a tx that is already in its pool and the tx is not yet in the `relay_method::fluff` state, the node could asynchronously evict it from its pool and attempt to re-broadcast (or just attempt the broadcast flow again asynchronously). Just need to be careful not to reveal to the caller that this tx was in the pool.

# Action History
- Created by: j-berman | 2022-04-10T08:51:05+00:00
