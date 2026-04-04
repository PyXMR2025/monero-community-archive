---
title: '[master] Ledger transfer broken'
source_url: https://github.com/monero-project/monero/issues/4917
author: selsta
assignees: []
labels: []
created_at: '2018-11-30T05:19:22+00:00'
updated_at: '2018-12-13T01:33:04+00:00'
type: issue
status: closed
closed_at: '2018-12-13T01:33:04+00:00'
---

# Original Description
Using git-bisect, d6937e373b32628fff414c7d8a07e4323593c6a0 broke transfer using Ledger.

```
[wallet xxxxx]: transfer xxx 0.1
Wallet password: 
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y
Error: unexpected error: Wrong Device Status : SW=6911 (EXPECT=9000, MASK=ffff)
```

# Discussion History
## moneromooo-monero | 2018-11-30T11:54:36+00:00
Does this come with an exception (and stack) in the log ?

## selsta | 2018-11-30T11:57:53+00:00
The wallet does not crash.

Edit: Do you mean log with --log-level 4?

## moneromooo-monero | 2018-11-30T12:04:18+00:00
I forgot the logs are off by default now. Log level 0 should be enough.

## moneromooo-monero | 2018-11-30T13:35:26+00:00
https://github.com/monero-project/monero/pull/4921

## moneromooo-monero | 2018-12-13T01:16:30+00:00
+resolved

# Action History
- Created by: selsta | 2018-11-30T05:19:22+00:00
- Closed at: 2018-12-13T01:33:04+00:00
