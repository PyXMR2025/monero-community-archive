---
title: wallet should construct transactions below the minimum block size limit by
  default
source_url: https://github.com/monero-project/monero/issues/2010
author: iamsmooth
assignees: []
labels: []
created_at: '2017-05-01T07:24:04+00:00'
updated_at: '2017-09-25T18:54:25+00:00'
type: issue
status: closed
closed_at: '2017-09-25T18:54:25+00:00'
---

# Original Description
Currently it allows some extra size above the current block size. This causes two problems:

1. TXs much above the block limit don't get mined even in an empty block because most miners now reject unless enough fee is paid to cover the penalty, and these generally don't (at least not at the standard fee level)

2. Block size may shrink, making transactions that were previously mineable unmineable.

Solution is to limit transactions to the minimum block size limit (300KB) by default (or possibly even somewhat smaller so as not to require an empty block for it to fit), with anything larger being split. The protocol allows larger, but the conditions where that would be useful are unclear and the standard wallet shouldn't do it by default.


# Discussion History
## ghost | 2017-05-01T19:01:59+00:00
Transaction size seems to be tested independently in two different locations:

1. Line 155 in `src/cryptonote_core/tx_pool.cpp`, which looks at the minimum block size for the version  (300kB) * 1.25, minus the coinbase blob size, so approx. 370kB

and

2. The (mis-spelled) function `get_upper_tranaction_size_limit` on line 4776 in `src/wallet/wallet2.cpp`, which will usually return `m_upper_transaction_size_limit` which is set to zero on line 352 of `src/wallet/wallet2.h`, so it falls through and returns the value of the full reward zone (300kB) * 1.25, minus the coinbase blob size, so approx. 370kB

## iamsmooth | 2017-05-01T19:58:52+00:00
correction, should stop at 300KB-estimated coinbase size (or even a bit less so as to not require a 100% empty block to fit)

## iamsmooth | 2017-05-02T00:34:55+00:00
#2011 sets the wallet limit at block_minimum-estimated_coinbase, which might or might not solve the problem. It depends how often: a) the wallet fully packs a tx up to the limit; b) people end up with these large txs at the low end of the fee/byte range that won't ever be mined unless the tx pool is completely empty (not counting lower fee levels), c) how often the block size is at the minimum; and d) how often the tx pool is completely empty. Its not the same sort of issue as now, but still may end up being bad UX.

If we go with this fix then we can close this issue and open a new one if that problem appears in practice.

## moneromooo-monero | 2017-09-25T18:44:30+00:00
For the record, the wallet aims at starting a new tx at about 2/3 of the max block size. It's estimating the size though, so might be a bit off in practice.

The patch in 2011 was just merged, so closing.

+resolved

# Action History
- Created by: iamsmooth | 2017-05-01T07:24:04+00:00
- Closed at: 2017-09-25T18:54:25+00:00
