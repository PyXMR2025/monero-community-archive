---
title: get_transfer_by_txid confusion
source_url: https://github.com/monero-project/monero/issues/5671
author: aaronovz1
assignees: []
labels:
- invalid
created_at: '2019-06-18T17:32:10+00:00'
updated_at: '2019-09-06T13:33:24+00:00'
type: issue
status: closed
closed_at: '2019-09-06T13:33:24+00:00'
---

# Original Description
What would cause `get_transfer_by_txid` to return an object that has no `destinations` field? The `type` of the tx is `in`, and it was created as part of a multisig transaction. The top level `address` and `amount` fields are what I would expect to be in the destinations array.

# Discussion History
## moneromooo-monero | 2019-08-27T15:43:05+00:00
All in transfers have no destinations, since we don't know what they were as we did not send them (if we did them them, they're classed as an out tx).

## moneromooo-monero | 2019-09-06T13:29:16+00:00
Not a bug for in txes. Reopen if you think it is, and give more information if so.

+invalid

# Action History
- Created by: aaronovz1 | 2019-06-18T17:32:10+00:00
- Closed at: 2019-09-06T13:33:24+00:00
