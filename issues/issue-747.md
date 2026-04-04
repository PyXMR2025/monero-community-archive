---
title: Unnamed constant in construct_miner_tx invocation in blockchain.cpp
source_url: https://github.com/monero-project/monero/issues/747
author: tewinget
assignees: []
labels: []
created_at: '2016-03-22T15:43:07+00:00'
updated_at: '2016-12-15T17:55:26+00:00'
type: issue
status: closed
closed_at: '2016-12-15T17:54:44+00:00'
---

# Original Description
https://github.com/monero-project/bitmonero/blob/master/src/cryptonote_core/blockchain.cpp#L1111
https://github.com/monero-project/bitmonero/blob/master/src/cryptonote_core/blockchain.cpp#L1120

construct_miner_tx is passed a parameter it calls "max_outs" which appears to be a limit to the number of digits an output amount should have.  The lines referenced above use a hard-coded amount (11) which should instead be a named constant.


# Discussion History
## luigi1111 | 2016-12-15T17:54:44+00:00
https://github.com/monero-project/monero/commit/c3b3260ae5b5acde445fa88a6f0909f582903754#diff-1279d7b0ddc432573cd2bd8c6e632c1fR1132

# Action History
- Created by: tewinget | 2016-03-22T15:43:07+00:00
- Closed at: 2016-12-15T17:54:44+00:00
