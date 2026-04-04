---
title: '[BUG] Incoming transfers to multiple subaddresses in the same tx not showing
  properly on txpool'
source_url: https://github.com/monero-project/monero/issues/2849
author: stoffu
assignees: []
labels: []
created_at: '2017-11-20T23:37:17+00:00'
updated_at: '2017-12-02T09:24:25+00:00'
type: issue
status: closed
closed_at: '2017-12-02T09:24:25+00:00'
---

# Original Description
Sending wallet:
```
[wallet 9xLMUj]: transfer BaXN9bUfbtaaDNZSns3Z4oXdQqyUFQ31tY1Sp5jNz454YJYmJrCwmVEYHoTHVzy68hbeyefFnM9qx2uVFVMLcGULHHbmK7K 0.1 BhGEX2pA8wBCp4mTio25TdSmwptRF6eJL7tKsaLRGoXrVvRkxvaVfMKTdv2ugZeuuf2mB51Fc94LkZ3q1McRiA9FFEkpPk3 0.2

Transaction 1/1:
Spending from address index 0
Sending 0.300000000000.  The transaction fee is 0.027861600000
Is this okay?  (Y/Yes/N/No): y
Transaction successfully submitted, transaction <9a0c37b7bd7e5ad3e3740f0a4c613bbc602ed49bacabc207e57303ce202de914>
You can check its status by using the `show_transfers` command.
```

Receiving wallet:
```
[wallet A1PbM6]: address all
0  A1PbM6kDJs7eJnAjwwE7Bk3DH84iQbfKZF6x5i8KuBrhdZBhKgfwuTPCqTEjPZPKJMG32ioosAHR3KkwG97tDfZS5kSJJRN  Primary address (used)
1  BaXN9bUfbtaaDNZSns3Z4oXdQqyUFQ31tY1Sp5jNz454YJYmJrCwmVEYHoTHVzy68hbeyefFnM9qx2uVFVMLcGULHHbmK7K  (Untitled address) (used)
2  BhGEX2pA8wBCp4mTio25TdSmwptRF6eJL7tKsaLRGoXrVvRkxvaVfMKTdv2ugZeuuf2mB51Fc94LkZ3q1McRiA9FFEkpPk3  (Untitled address) (used)

[wallet A1PbM6]: show_transfers
    pool     in      11:31:17 PM       0.100000000000 9a0c37b7bd7e5ad3e3740f0a4c613bbc602ed49bacabc207e57303ce202de914 0000000000000000 1 - 
```

Once the tx is confirmed, those incoming transfers are recognized correctly.

# Discussion History
## moneromooo-monero | 2017-11-21T17:18:31+00:00
<s>Are you running with 626e80780b3e231705df2d64c44088b551d60d19 ?</s> Nevermind, I have it and I see the bug too.

## moneromooo-monero | 2017-11-21T19:29:29+00:00
https://github.com/monero-project/monero/pull/2850

## moneromooo-monero | 2017-12-02T09:11:09+00:00
+resolved

# Action History
- Created by: stoffu | 2017-11-20T23:37:17+00:00
- Closed at: 2017-12-02T09:24:25+00:00
