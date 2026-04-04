---
title: Watch-only wallet misreporting transactions.
source_url: https://github.com/monero-project/monero/issues/1994
author: '564765975'
assignees: []
labels: []
created_at: '2017-04-21T11:16:17+00:00'
updated_at: '2017-04-23T06:44:21+00:00'
type: issue
status: closed
closed_at: '2017-04-23T06:44:21+00:00'
---

# Original Description
My watch-only wallet is reporting an outgoing transaction as incoming.

This is an edited printout of the transaction from both full wallet and watch-only:

Full:

1292949 out 09:48:00 PM 0.900000000000 <tx-id removed> 0000000000000000 0.016342040000

Watch-only:

1292949 in 09:48:00 PM 0.083657960000 <tx-id removed> 0000000000000000 - 

# Discussion History
## moneromooo-monero | 2017-04-22T08:14:26+00:00
Did you ever get your hot and cold wallets out of sync ?
Monero distinguishes in and out txes by checking whether a tx spends an output it owns. It can only know that if an outgoing ring has a key image matching one of its own outputs, and only the cold wallet can calculate the key images. So if you rescan the hot wallet without reimporting key images, this will happen.

## 564765975 | 2017-04-23T06:44:18+00:00
Yes I exported/imported the key images and it's working fine now. Thank you.

# Action History
- Created by: 564765975 | 2017-04-21T11:16:17+00:00
- Closed at: 2017-04-23T06:44:21+00:00
