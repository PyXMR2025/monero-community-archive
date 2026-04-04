---
title: Failed to parse transaction from blob
source_url: https://github.com/monero-project/monero/issues/6854
author: aaronovz1
assignees: []
labels: []
created_at: '2020-10-01T00:47:35+00:00'
updated_at: '2020-10-05T23:23:10+00:00'
type: issue
status: closed
closed_at: '2020-10-05T23:23:10+00:00'
---

# Original Description
Trying to create a new wallet or import an existing one using seed on stagenet using 0.16.0.3 is failing recently.

```
2020-10-01 00:44:58.312	T READ ENDS: Success. bytes_tr: 4038
2020-10-01 00:44:58.312	T READ ENDS: Success. bytes_tr: 989
2020-10-01 00:44:58.348	D Pulled blocks: blocks_start_height 674994, count 1000, height 675994, node height 676343
2020-10-01 00:44:58.360	E Failed to parse transaction from blob

---
2020-10-01 00:45:23.265	E pull_blocks failed, try_count=3
2020-10-01 00:45:23.266	D refreshed
2020-10-01 00:45:23.266	T refreshThreadFunc: waiting for refresh...
2020-10-01 00:45:23.268	D >>> wallet refreshed
2020-10-01 00:45:23.268	D Checking connection status
2020-10-01 00:45:23.268	D >>> wallet updated
```

I tried using 0.17 release but get similar issues with wallets not being able to fully sync.

I am using remote node from https://community.xmr.to/nodes.html

# Discussion History
## aaronovz1 | 2020-10-05T23:23:10+00:00
Looks like it might have been a sync issue with node and wallet versions. Since the 0.17.0.1 GUI release the problem has resolved.

# Action History
- Created by: aaronovz1 | 2020-10-01T00:47:35+00:00
- Closed at: 2020-10-05T23:23:10+00:00
