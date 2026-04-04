---
title: Generate genesis block in testnet.
source_url: https://github.com/monero-project/monero/issues/2167
author: p1gd0g
assignees: []
labels: []
created_at: '2017-07-12T00:57:20+00:00'
updated_at: '2017-07-12T01:30:34+00:00'
type: issue
status: closed
closed_at: '2017-07-12T01:29:21+00:00'
---

# Original Description
https://github.com/monero-project/monero/blob/master/src/cryptonote_core/cryptonote_tx_utils.cpp#L484
This should be genesis_tx, right?

# Discussion History
## p1gd0g | 2017-07-12T01:30:34+00:00
Coin base is different in testnet, this caused another bug.

# Action History
- Created by: p1gd0g | 2017-07-12T00:57:20+00:00
- Closed at: 2017-07-12T01:29:21+00:00
