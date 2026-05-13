---
title: Red "Failed to verify input FCMP++ signatures" spam after deep reporg
source_url: https://github.com/seraphis-migration/monero/issues/372
author: j-berman
assignees: []
labels: []
created_at: '2026-05-11T23:39:39+00:00'
updated_at: '2026-05-13T04:47:09+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Around the time of a very deep reorg (~200 blocks), lots of stressnet daemon operators started complaining about unresponsiveness in the node coupled with a huge number of red `Failed to verify input FCMP++ signatures for tx <hash>` in their logs. Continued logging for hours. If anyone has log level 2 during this period of spam, sharing that log file would be very much appreciated to help fix this.

Obviously, it seems the node is re-verifying all these txs that were reorged out of the chain.

Here are a few theories for issues reported during that time:

1) Nodes used to mine or create block templates are re-verifying all the txs in their daemon, including these txs that will never pass verification.
2) Nodes are re-relaying these txs even though they're guaranteed to fail verification (and thus cause the nodes to drop).
3) The pool reaches capacity.

### 1) Mining nodes re-verifying bad txs

Immediately upon switching to a reorged chain and adding the reorged txs back to the pool, the txs wouldn't re-verify because we pop blocks one-by-one and re-add popped txs to the pool. Those txs would *all* still use the expected tree state for when they entered the chain, and thus have "correct" `verID` saved when re-added to the pool. However, if the reorg is >10 blocks, the `verID` will actually be rendered incorrect and future re-verifications of those txs would fail because the referenced FCMP++ tree is expected to change after a 10+ block reorg), and we re-verify said txs [because of this](https://github.com/seraphis-migration/monero/blob/d2eeda9f3cdcea0e829a3b70ed42e0ed608c38a6/src/cryptonote_core/blockchain.cpp#L3931-L3932).

We know that nodes may re-verify these reorged out txs via `is_transaction_ready_to_go` when creating block templates, and `create_block_template` grabs the `m_blockchain_lock`. Thus node unresponsiveness definitely makes sense while this is happening.

A solution for this is to **never** modify an already saved `verID`, and immediately fail without attempting to re-verify if it's incorrect.

However, so far this is the only known potential cause for the red `Failed to verify` spam. But there are some users who have reported they saw the spam even when not using the node to mine. I'm not sure yet what could have caused such nodes to attempt to re-verify these txs. Logs would help show why the nodes were doing that, though I'm continuing to investigate anyway.

### 2) Re-relaying bad txs

A node will re-broadcast the txs in its pool to its peers in a loop [here](https://github.com/seraphis-migration/monero/blob/d2eeda9f3cdcea0e829a3b70ed42e0ed608c38a6/src/cryptonote_core/tx_pool.cpp#L838). If their peers don't already have those txs saved in their pools (nor the key images from those txs already spent in the pool), then verification will fail and the re-relaying node will get dropped. @rucknium mentioned reduced peer counts after this, so it's possible this was a factor.

Perhaps we'd like to re-tune this logic for re-broadcasting `block` relayed txs. Either to not do it at all, or to avoid it if the `verID != calculated`.

I don't think this is a potential cause of the red `Failed to verify` spam because the node would immediately drop the peer on first fail [here](https://github.com/seraphis-migration/monero/blob/d2eeda9f3cdcea0e829a3b70ed42e0ed608c38a6/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L1071-L1074), rather than continue to try to verify these unverifiable txs.

### 3) Pool is at capacity

Reorged out txs count toward the pool weight. They can linger for 7 days and don't get kicked as the pool takes in new txs. The max pool weight allowed is 600mb. This means it's possible nodes can't accept very many new txs since the reorged out txs are taking up space.

Also an unlikely cause of the red spam, but an issue to consider regardless.

# Discussion History
## j-berman | 2026-05-13T03:14:30+00:00
Related to issue 2: it's possible that txs that were *already* in the pool (and never in the chain) become invalidated by the reorg.

Then nodes attempt to re-relay said txs and get dropped.

That appears to be what's happening with the latest deep reorg. My node kicked a tx from the pool (because my pool was at capacity and another ~~tx had higher fee~~ block tx replaced it), and then later a node is attempting to re-relay that tx to me:

```
2026-05-13 02:22:21.325	[P2P8]	INFO	txpool	src/cryptonote_core/tx_pool.cpp:354	Transaction added to pool: txid <547a8b3978ad55233b7a0ba761e198b28b44afa850071e960f0456e506620551> weight: 7650 fee/byte: 77000, count: 78578, pool total weight: 648000286
2026-05-13 02:22:21.331	[P2P8]	INFO	txpool	src/cryptonote_core/tx_pool.cpp:478	Pruning tx <00772980f591f2e63daeb12e2ac96eb8abe5eb2ae26a4a52458da2581e7d7428> from txpool: weight: 7650, fee/byte: 77000
2026-05-13 02:22:21.331	[P2P8]	INFO	txpool	src/cryptonote_core/tx_pool.cpp:482	Pruned tx <00772980f591f2e63daeb12e2ac96eb8abe5eb2ae26a4a52458da2581e7d7428> from txpool: weight: 7650, fee/byte: 77000
2026-05-13 02:22:21.331	[P2P8]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1870	Transaction removed from pool: txid <00772980f591f2e63daeb12e2ac96eb8abe5eb2ae26a4a52458da2581e7d7428>, total entries in removed list now 15692
...
2026-05-13 02:42:11.554	[P2P8]	ERROR	verify	src/cryptonote_core/blockchain.cpp:3956	Failed to verify input FCMP++ signatures for tx <00772980f591f2e63daeb12e2ac96eb8abe5eb2ae26a4a52458da2581e7d7428>
2026-05-13 02:42:11.554	[P2P8]	INFO	perf.blockchain	src/common/perf_timer.cpp:161	PERF    32482      check_tx_inputs
2026-05-13 02:42:11.554	[P2P8]	INFO	txpool	src/cryptonote_core/tx_pool.cpp:271	tx used wrong inputs, rejected
2026-05-13 02:42:11.554	[P2P8]	INFO	perf.txpool	src/common/perf_timer.cpp:161	PERF    39004    add_tx
2026-05-13 02:42:11.554	[P2P8]	INFO	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1082	[<IP> OUT] Tx verification failed, dropping connection
2026-05-13 02:42:11.554	[P2P8]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:3060	[<IP> OUT] dropping connection id c92085b3-4438-4ade-9480-1f4a67a30b6a (pruning seed 0), score 0, flush_all_spans 0
```

I have 35 of those over a 20min span. So that helps explain poor node connectivity after a deep reorg.

That would be solved by avoiding relaying if the tx's `verID != calculated`. 

## j-berman | 2026-05-13T03:25:34+00:00
EDIT: ignore, I was reading the wrong code. #204 *is* applied to beta, and does not impact the above issues.

~~#204 is also not applied to beta :/ that would make this issue 2 a no-drop-offense.~~

# Action History
- Created by: j-berman | 2026-05-11T23:39:39+00:00
