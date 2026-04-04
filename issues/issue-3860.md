---
title: Node getting stuck
source_url: https://github.com/monero-project/monero/issues/3860
author: emesik
assignees: []
labels: []
created_at: '2018-05-25T11:29:50+00:00'
updated_at: '2018-06-05T11:08:57+00:00'
type: issue
status: closed
closed_at: '2018-06-05T11:08:57+00:00'
---

# Original Description
My node which I use to get stats from to create [mempool graphs](https://pooldata.xmrlab.com/) apparently got stuck and suffered a mempool swell.

After restarting, it synced up blocks and cleared the pool. [This picture](https://imgur.com/a/bnqj72J) shows the mempool swell and cleanup after restart.

[Here on reddit](https://www.reddit.com/r/Monero/comments/8m0lao/mempool_is_swelling/dzjvbej/) I made a hypothesis on what could have happened, but it's not supported by log analysis, just a guess.

The node is running 0.12.0.0

Logs covering that period, including the restart: [1](http://salaban.info/~emes/monero.1.log.gz) and [2](http://salaban.info/~emes/monero.2.log.gz)

# Discussion History
## moneromooo-monero | 2018-05-25T11:39:26+00:00
Believed fixed in 0.12.1.0.

## moneromooo-monero | 2018-06-05T11:00:56+00:00
+resolved

# Action History
- Created by: emesik | 2018-05-25T11:29:50+00:00
- Closed at: 2018-06-05T11:08:57+00:00
