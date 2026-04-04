---
title: Possible issue with genesis block generation
source_url: https://github.com/monero-project/monero/issues/790
author: tewinget
assignees: []
labels: []
created_at: '2016-04-03T08:09:00+00:00'
updated_at: '2016-04-03T08:56:14+00:00'
type: issue
status: closed
closed_at: '2016-04-03T08:56:06+00:00'
---

# Original Description
https://github.com/monero-project/bitmonero/blob/master/src/cryptonote_core/cryptonote_format_utils.cpp#L838

to create the genesis block, the above line calls create_miner_tx, which has an issue with the max_outs parameter being passed as 0 on the below line.

https://github.com/monero-project/bitmonero/blob/master/src/cryptonote_core/cryptonote_format_utils.cpp#L148

construct_miner_tx returns false before finishing, and this may or may not affect genesis block generation.  Warrants looking into, I think.


# Discussion History
## tewinget | 2016-04-03T08:56:05+00:00
Turns out this was known and is resolved by #782.  Marking closed.


# Action History
- Created by: tewinget | 2016-04-03T08:09:00+00:00
- Closed at: 2016-04-03T08:56:06+00:00
