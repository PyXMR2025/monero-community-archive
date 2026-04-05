---
title: Sync stops, no peers connected
source_url: https://github.com/seraphis-migration/monero/issues/244
author: thankfulfornever
assignees: []
labels: []
created_at: '2025-11-21T20:35:27+00:00'
updated_at: '2025-12-14T02:40:01+00:00'
type: issue
status: closed
closed_at: '2025-12-14T02:40:00+00:00'
---

# Original Description
My setup:

Debian 13 vps
8gb RAM (utilizing 6gb, no OOM crash after 48 hours)
75GB SSD NVMe
4 vCPUs (probably shared)
Nothing else installed except fail2ban on ssh

Daemon command: `./monerod --testnet --restricted-rpc --max-connections-per-ip=10 --log-level 2`

After 24 hours was steady syncing 4.5 tx/min, but after 36 hours `status` showed sync at 100%, but zero connections:

`Height: 2880860/2880860 (100.0%) on testnet, mining info unavailable, net hash 1.35 kH/s, v18, 0(out)+0(in) connections`

Attached log

[log.log](https://github.com/user-attachments/files/23683873/log.log)

# Discussion History
## j-berman | 2025-11-21T21:08:17+00:00
u/mayhem69 reported the same in the stressnet channel

## j-berman | 2025-11-22T19:28:50+00:00
Of note both @thankfulfornever and u/mayhem69 were using this build: https://github.com/j-berman/monero/commit/a40a18c5625364d196209af6651761d5056c2a7d

I've experienced this now a couple times with that build as well. For me the cause is the following:

```
2025-11-22 04:50:41.802	[P2P6]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1855	Transaction removed from pool: txid <8c059e9aca6f6e7e7c238a04e22ec787002300c60cca0fbc61b85393975c4f1c>, total entries in removed list now 2221
2025-11-22 04:50:41.802	[P2P6]	INFO	perf.blockchain	src/common/perf_timer.cpp:125	PERF             ----------
2025-11-22 04:50:41.802	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3919	No previously valid verID provided for tx <8c059e9aca6f6e7e7c238a04e22ec787002300c60cca0fbc61b85393975c4f1c>, continuing to input verification as normal...
2025-11-22 04:50:41.802	[P2P6]	INFO	perf.blockchain	src/common/perf_timer.cpp:161	PERF        1      expand_transaction_2
2025-11-22 04:50:41.802	[P2P6]	ERROR	verify	src/cryptonote_core/tx_verification_utils.cpp:72	Mismatched key images to inputs after expanding FCMP tx
2025-11-22 04:50:41.802	[P2P6]	ERROR	verify	src/cryptonote_core/tx_verification_utils.cpp:195	Failed post-expansion FCMP++ checks
2025-11-22 04:50:41.802	[P2P6]	ERROR	verify	src/cryptonote_core/blockchain.cpp:3937	Failed to verify input FCMP++ signatures for tx <8c059e9aca6f6e7e7c238a04e22ec787002300c60cca0fbc61b85393975c4f1c>
2025-11-22 04:50:41.802	[P2P6]	INFO	perf.blockchain	src/common/perf_timer.cpp:161	PERF      114    check_tx_inputs
2025-11-22 04:50:41.802	[P2P6]	ERROR	verify	src/cryptonote_core/blockchain.cpp:4678	Block with id: <88c44ad2480e1221f8c31e12e0fde674b0e0c40007b594ff3d53255e8ff9bc19> has at least one transaction (id: <8c059e9aca6f6e7e7c238a04e22ec787002300c60cca0fbc61b85393975c4f1c>) with wrong inputs.
2025-11-22 04:50:41.802	[P2P6]	INFO	blockchain	src/cryptonote_core/blockchain.cpp:3136	BLOCK ADDED AS INVALID: <88c44ad2480e1221f8c31e12e0fde674b0e0c40007b594ff3d53255e8ff9bc19>
2025-11-22 04:50:41.802	[P2P6]	INFO	blockchain	src/cryptonote_core/blockchain.cpp:3136	, prev_id=<7dfd25997b5685c093d7605f7184fed625d997fdf1119b26de24c983b0486f78>, m_invalid_blocks count=1
2025-11-22 04:50:41.802	[P2P6]	ERROR	verify	src/cryptonote_core/blockchain.cpp:4682	Block with id <88c44ad2480e1221f8c31e12e0fde674b0e0c40007b594ff3d53255e8ff9bc19> added as invalid because of wrong inputs in transactions
```

Once a block gets added as an invalid block, it doesn't get removed as invalid. So something is up with tx expansion, not sure exactly what yet. My immediate guess is maybe the key images are getting consumed over the FFI here https://github.com/j-berman/monero/commit/741bddfdeecec6cabc667eef0cdfdaa766a52d88

## j-berman | 2025-11-22T19:29:09+00:00
Accidental close

## thankfulfornever | 2025-11-27T13:58:31+00:00
Restarted and seem to hit the same problem. Strangely, the block height is changing with no peers:

`Height: 1991156/2885056 (69.0%) on testnet, mining info unavailable, net hash 1.69 kH/s, v16, 0(out)+0(in) connections`

`Height: 1991756/2885056 (69.0%) on testnet, mining info unavailable, net hash 3.57 kH/s, v16, 0(out)+0(in) connections`

`Height: 1992656/2885056 (69.1%) on testnet, mining info unavailable, net hash 2.19 kH/s, v16, 0(out)+0(in) connections`

## j-berman | 2025-12-03T04:42:24+00:00
The root cause of this issue is the pool exceeding max weight, and a fairly complex sequence of events where a tx that was already validated gets re-validated. When txs get added *back* to the pool, they'd also re-expand (incorrectly), causing a block to fail to verify and then get stuck as an invalid block. Nodes that send invalid blocks then get dropped.

#251 / #252 should prevent valid blocks from getting stuck as invalid from broken re-expansion, thus addressing the reported connection drops.

The fix doesn't entirely address behavior when the pool exceeds max weight, however. I think nodes should probably only attempt to add a tx to the pool if the tx won't be immediately pruned upon adding (i.e. don't `prune` a tx after doing all validation / adding to the db, and instead just short-circuit reject the tx if it's not a high enough fee and the pool is at capacity already). That is an upstream issue. EDIT: also need careful DoS protection for this sort of thing too...

## j-berman | 2025-12-04T00:09:38+00:00
#251 prevents nodes from entering a 100% broken state when pool exceeds max weight

#253 ensures more stable sync when pool exceeds max weight

I think both would be nice to have in before closing this issue

# Action History
- Created by: thankfulfornever | 2025-11-21T20:35:27+00:00
- Closed at: 2025-12-14T02:40:00+00:00
