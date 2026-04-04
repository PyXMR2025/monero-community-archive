---
title: Cache grows even for wallets without transactions
source_url: https://github.com/monero-project/monero/issues/8366
author: onionltd
assignees: []
labels: []
created_at: '2022-05-30T19:23:18+00:00'
updated_at: '2022-07-20T00:36:58+00:00'
type: issue
status: closed
closed_at: '2022-07-20T00:36:58+00:00'
---

# Original Description
I made a new wallet in monero-wallet-gui. The size of a the cache file was initially around 400kB. Once the wallet was synced with the daemon, the cache has grown to around 5MB and continues to grow as time passes, though much slower. I've made no transaction to or from the wallet. Why is the cache growing so much?

# Discussion History
## moneromooo-monero | 2022-05-31T21:22:37+00:00
The wallet cache keeps a list of block hashes, to know when it needs to reorg. When you update to next version, it'll be able to cut off old block hashes and reduce the cache size a lot, which will then continue slowly growing again.

## Cactii1 | 2022-07-20T00:35:27+00:00
This issue should be closed.

# Action History
- Created by: onionltd | 2022-05-30T19:23:18+00:00
- Closed at: 2022-07-20T00:36:58+00:00
