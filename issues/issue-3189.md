---
title: Possible Mempool spam attack
source_url: https://github.com/monero-project/monero/issues/3189
author: cmaves
assignees: []
labels: []
created_at: '2018-01-26T21:29:52+00:00'
updated_at: '2018-02-18T19:28:34+00:00'
type: issue
status: closed
closed_at: '2018-02-18T19:28:34+00:00'
---

# Original Description
Currently if somebody makes a simple modification to the monero-wallet, they can generate a transaction that is about 360kb in size. If this transaction is low priority, the transaction will be relayed as valid but will not be confirmed unless the median blocksize grows. One could use this to flood the mempool with transactions.

After doing a bit of math it appears that a normal priority transaction of this size would be confirmed, so the nodes just fail to account for the case where a transaction is both large and low priority.

# Discussion History
## anonimal | 2018-01-27T10:45:41+00:00
In the future, please respect [responsible disclosure](https://en.wikipedia.org/wiki/Responsible_disclosure) by using use our [Vulnerability Response Process](https://github.com/monero-project/meta/blob/master/VULNERABILITY_RESPONSE_PROCESS.md) regardless of whether this issue is a confirmed vulnerability or not. Thank you.

## moneromooo-monero | 2018-01-27T11:40:36+00:00
There's been some talk about limiting txes to a percentage of the block size for this reason. Not done, though. I also wanted to start dumping the lowest fee/byte txes from the txpool as new txes are received.
The first one would be consensus, the second one not.

## moneromooo-monero | 2018-01-30T09:41:10+00:00
https://github.com/monero-project/monero/pull/3205

## moneromooo-monero | 2018-02-18T19:21:23+00:00
+resolved

# Action History
- Created by: cmaves | 2018-01-26T21:29:52+00:00
- Closed at: 2018-02-18T19:28:34+00:00
