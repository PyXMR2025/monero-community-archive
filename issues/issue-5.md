---
title: use `TransactionPruned` in `TxBlobEntry`
source_url: https://github.com/Cuprate/cuprate/issues/5
author: Boog900
assignees: []
labels:
- A-storage
- C-bug
created_at: '2023-03-08T00:09:36+00:00'
updated_at: '2024-05-27T01:01:07+00:00'
type: issue
status: closed
closed_at: '2023-04-26T20:11:10+00:00'
---

# Original Description
`TxBlobEntry` should be a pruned transaction:
https://github.com/SyntheticBird45/cuprate/blob/265fb3e895e97b3027651121b646d0f202fd3b19/net/monero-wire/src/messages/common.rs#L103

However monero-rs does not currently support pruned transactions. So for now I have just made it a normal transaction (which means it will error if anyone tries to de-serialize a `BlockCompleteEntry` with pruned txs).

A PR is already open to add pruned txs to monero-rs: [#138](https://github.com/monero-rs/monero-rs/pull/138)



# Discussion History
## Boog900 | 2023-04-26T20:11:10+00:00
monero-rs has been removed from monero-wire, now all block/transaction data is kept as bytes 

# Action History
- Created by: Boog900 | 2023-03-08T00:09:36+00:00
- Closed at: 2023-04-26T20:11:10+00:00
