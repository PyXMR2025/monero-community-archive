---
title: '[Bug] estimate_backlog in wallet2.cpp'
source_url: https://github.com/monero-project/monero/issues/9841
author: Tzadiko
assignees: []
labels: []
created_at: '2025-03-17T03:30:53+00:00'
updated_at: '2025-03-26T13:13:57+00:00'
type: issue
status: closed
closed_at: '2025-03-26T13:13:57+00:00'
---

# Original Description
I think estimate_backlog in wallet2.cpp has a bug that has gone unnoticed because the range of fees passed in is always the same (e.g. get_backlog({min_fee, min_fee}) instead of get_backlog({min_fee, **max**_fee}).

If you take a look, what it does is: For a given range of fees (per byte) determine how many transactions (in terms of weight) pay more than our lower bound, and how many transactions pay more than our higher bound.

We're guaranteed that the number of transactions paying as much as our lowerbound >= the number of transactions paying as much as our higherbound. The code associates the lowerbound fee with the **minimum** number of blocks we'll need to wait, when instead of setting it to the maximum number of blocks we'll need to wait (and vice versa). Put simply, the less fees you pay, the longer you're estimated to wait, but the code has this concept backwards.

_Example_
Say there are 5 transactions in the pool, paying these fee levels per byte: [10, 12, 13, 15, 20] and they each have these weights [2, 3, 2, 2, 4] and the full reward zone weight is 7. When we call estimate_backlog with ({11, 17}), we'll get:

```
Lowerbound Fees = 12 + 13 + 15 + 20
Lowerbound Weights = 3 + 2 + 2 + 4 = 11
Upperbound Fees = 20
Upperbound Weights = 4

Lowerbound Blocks to Wait = (3 + 2 + 2 + 4) / 7 = 1.57 // nblocks_min in the code, when it should be nblocks_max
Upperbound Blocks to Wait = 4 / 7 = 0.57 // nblocks_max in the code, when it should be nblocks_min
```

The code as written has it backwards. It states that upperbound (`nblocks_max`) is 0.57 and lowerbound (`nblock_min`) is 1.57. In other words, it says, _if we pay 17 piconeros per byte (the higher fee), we'll need to wait an estiamted 1.57 blocks, whereas if we pay 11 piconeros per byte (the lower fee), we'll need to wait an estimated 0.57 blocks._ This doesn't make sense.

In an MR I'll open soon, I suggest this change.

![Image](https://github.com/user-attachments/assets/1b5b56bf-fe19-4147-b984-ec91316d3b8a)

# Discussion History
## selsta | 2025-03-26T13:13:57+00:00
Resolved in #9842

# Action History
- Created by: Tzadiko | 2025-03-17T03:30:53+00:00
- Closed at: 2025-03-26T13:13:57+00:00
