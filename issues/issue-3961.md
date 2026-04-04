---
title: the monerod stops moving forward on blocks and get stuck on the current block,
  it has been happening every several days
source_url: https://github.com/monero-project/monero/issues/3961
author: WebCodiyapa
assignees: []
labels: []
created_at: '2018-06-08T15:31:55+00:00'
updated_at: '2025-12-19T16:51:14+00:00'
type: issue
status: closed
closed_at: '2025-12-19T16:51:14+00:00'
---

# Original Description
the monerod stops moving forward on blocks and get stuck on the current block, it has been happening every several days

# Discussion History
## moneromooo-monero | 2018-06-08T16:35:04+00:00
Use >= 0.12.1.0, a sync bug got fixed.


## WebCodiyapa | 2018-06-08T16:47:21+00:00
now i am using 12.2 version

## moneromooo-monero | 2018-06-08T19:17:19+00:00
Then exit monerod, then run it again with --log-level 0,net.cn:DEBUG,net.p2p*:DEBUG,sync-info:DEBUG
After's it's started doing this again, upload the relevant part of the log to fpaste.org. The relevant part of the log starts a minute before the first error adding a block/tx, up until a minute later, so 2 minutes' worth of log.


## moneromooo-monero | 2018-07-03T14:40:25+00:00
ping

# Action History
- Created by: WebCodiyapa | 2018-06-08T15:31:55+00:00
- Closed at: 2025-12-19T16:51:14+00:00
