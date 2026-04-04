---
title: 'Error: Reason: double spend'
source_url: https://github.com/monero-project/monero/issues/1960
author: ghost
assignees: []
labels: []
created_at: '2017-04-07T15:27:33+00:00'
updated_at: '2017-08-08T17:36:15+00:00'
type: issue
status: closed
closed_at: '2017-08-08T17:36:15+00:00'
---

# Original Description
I'm trying to send money, but I get Error: Reason: double spend. I issued a rescan_bc twice and I still get the error. Any ideas on what I can do to fix this?

# Discussion History
## moneromooo-monero | 2017-04-08T05:45:10+00:00
That's probably because you ran rescan_bc. Don't run this unless you really need it.
Anyway, if you ran rescan_bc and you had an outgoing tx waiting to be mined, then you need to run rescan_spent after it as well to sync to the txpool.


## moneromooo-monero | 2017-08-08T17:34:41+00:00
Known reasons for the wallet to get out of sync with real spent state are now gone, except the case where a wallet crsahes or is killed after sending, but before saving. I'm calling it fixed, the remaining case will be fixed with the lmdb wallet file.

+resolved

# Action History
- Created by: ghost | 2017-04-07T15:27:33+00:00
- Closed at: 2017-08-08T17:36:15+00:00
