---
title: Sporadic bursts "E Key image already spent in blockchain" in logs
source_url: https://github.com/seraphis-migration/monero/issues/141
author: j-berman
assignees: []
labels: []
created_at: '2025-10-07T00:05:18+00:00'
updated_at: '2025-10-30T21:33:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Both u/coffnix and u/mayhem69 have reported sporadic bursts of the error "E Key image already spent in blockchain" in the logs. Here is a screenshot shared by u/coffnix in the stressnet matrix channel:

<img width="1612" height="1251" alt="Image" src="https://github.com/user-attachments/assets/d76304c8-b17b-4712-9962-b9cb2dd1e5d3" />

# Discussion History
## nahuhh | 2025-10-07T00:12:12+00:00
3rd

ive seen this as well. To me, looks like..

1. node a has synced new block 390
2. node b is re-relaying txs from pool to node a.
node b is still on block 389 and should be pulling the new block 390 from node a, but that seems to have issues of its own.
3. node a recognizes these as already confirmed

## spackle-xmr | 2025-10-07T00:28:11+00:00
Here is a level 2 log from a stressnet node with some of these entries:
[log2.txt.gz](https://github.com/user-attachments/files/22733765/log2.txt.gz)

## j-berman | 2025-10-07T00:47:06+00:00
From those logs, it looks like txs may be getting mined that spend the same inputs as some txs in the pool. Example: 

```
Considering <210e964f61ad945add250ce1ea325cb945739cbc6347674acca663fa0e57795c>, weight 6498, current block weight 0/9435166, current coinbase 0.600000000000, relay method 4
Key image already spent in blockchain: f28285bc902bde525ccb8508b3050309cb151dfc87ec79d8972205a97bbd767e
```

Looking at my stressnet node, I don't see 210e964f61ad945add250ce1ea325cb945739cbc6347674acca663fa0e57795c in the chain, but I do see that f28285bc902bde525ccb8508b3050309cb151dfc87ec79d8972205a97bbd767e has been spent.

It's possible that spammers are relaying double spends that are relaying to some portions of the network, or relaying them to their own nodes and then mining them.

It's possible this will **also** be alleviated by #135.

## j-berman | 2025-10-07T00:55:50+00:00
Note, the "Considering" log in log level 2 (which precedes every line of "Key image already spent in blockchain") executes when a daemon is filling a new block template immediately after adding a block. It doesn't receive new txs at that point, it already has the txs in its pool. That's why it looks like the daemon is adding a block that includes txs spending the same key images. The theory is testable by checking that key image `f28285bc902bde525ccb8508b3050309cb151dfc87ec79d8972205a97bbd767e` is spent in block `ada807e84cc06ca13eb2c1ce1c6e70c9f435b3050b9b0cf5ff239c152798c639`.

## j-berman | 2025-10-07T01:04:59+00:00
Interestingly, the block in question `ada807e84cc06ca13eb2c1ce1c6e70c9f435b3050b9b0cf5ff239c152798c639` doesn't appear to be in the main chain anymore (and I don't have an alt block for it). Possibly related to the issue at hand.

Would be interesting to see which block (and tx) that the key image `f28285bc902bde525ccb8508b3050309cb151dfc87ec79d8972205a97bbd767e` has been spent in. Could re-purpose `blockchain_usage.cpp` to search for the block and tx.

## j-berman | 2025-10-15T15:40:48+00:00
Reiterating: this error can occur if users are actively attempting to double spend on the network.

If Node A sees a tx spending key image A, and Node B sees a distinct tx spending key image A, then both nodes might end up trying to re-relay the txs to each other, and get dropped [here](https://github.com/monero-project/monero/blob/master/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L942-L943). Perhaps we don't want them to get dropped there.

## nahuhh | 2025-10-15T16:47:07+00:00
"Reiterating: this error can occur if users are actively attempting to double spend on the network."

without more info, i believe some people producing txs/spamming might be flushing their tx pools, probably to clear double spend errors. ..Then they start submitting new txs before the old txpool is refetched.

(still unclear as to what causes the initial double spend errors, but rescan_spent seems to fix those wallets and correct the balances).

## j-berman | 2025-10-30T21:33:52+00:00
#208 should help

# Action History
- Created by: j-berman | 2025-10-07T00:05:18+00:00
