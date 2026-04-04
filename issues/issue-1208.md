---
title: History page - search by address
source_url: https://github.com/monero-project/monero-gui/issues/1208
author: sanderfoobar
assignees: []
labels:
- enhancement
created_at: '2018-03-30T01:33:07+00:00'
updated_at: '2018-12-26T22:13:15+00:00'
type: issue
status: closed
closed_at: '2018-12-26T22:13:15+00:00'
---

# Original Description
Would be nice if the GUI could filter the transaction history table by receiving/recipient address.

# Discussion History
## sanderfoobar | 2018-03-30T01:33:13+00:00
+enhancement

## sanderfoobar | 2018-04-09T20:05:59+00:00
For reference:

https://github.com/monero-project/monero-gui/blob/b4353a31ac9cfabd348eb14b4f334918b2abc135/src/model/TransactionHistorySortFilterModel.cpp#L217-L240

This feature might not be worth it, as recipient addresses are only stored in the wallet cache.

# Action History
- Created by: sanderfoobar | 2018-03-30T01:33:07+00:00
- Closed at: 2018-12-26T22:13:15+00:00
