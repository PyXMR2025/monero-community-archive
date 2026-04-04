---
title: monero-blockchain-stats underreports size of prunable txs
source_url: https://github.com/monero-project/monero/issues/6732
author: hyc
assignees: []
labels: []
created_at: '2020-08-01T12:29:11+00:00'
updated_at: '2020-08-16T19:56:08+00:00'
type: issue
status: closed
closed_at: '2020-08-16T19:56:08+00:00'
---

# Original Description
Patch coming shortly

# Discussion History
## intj440 | 2020-08-01T13:28:13+00:00
monero-blockchain-stats output for 2020-07-28: Txs/day = 8976, Bytes/day = 3781848.  The ratio is 421 bytes/tx which is ~4-5x smaller than expected (~1.9kB and ~2.5kB for 1in-1out and 2in-2out txs per @SarangNoether).  Coinbase txs could not explain this as they were <10% of the tx for that day (Blocks/day = 760).

# Action History
- Created by: hyc | 2020-08-01T12:29:11+00:00
- Closed at: 2020-08-16T19:56:08+00:00
