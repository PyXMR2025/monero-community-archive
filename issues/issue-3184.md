---
title: 'read error: "end of file"'
source_url: https://github.com/xmrig/xmrig/issues/3184
author: WindowsMEMZ
assignees: []
labels: []
created_at: '2022-12-25T11:24:33+00:00'
updated_at: '2022-12-25T17:13:58+00:00'
type: issue
status: closed
closed_at: '2022-12-25T17:13:57+00:00'
---

# Original Description
I always see this issus, it just like this:
[2022-12-25 19:17:27.366]  cpu      accepted (8/1) diff 120001 (245 ms)
[2022-12-25 19:17:41.139]  cpu      accepted (9/1) diff 120001 (242 ms)
[2022-12-25 19:17:43.726]  cpu      accepted (10/1) diff 120001 (243 ms)
[2022-12-25 19:18:15.264]  miner    speed 10s/60s/15m 3160.8 3114.5 n/a H/s max 3435.9 H/s
[2022-12-25 19:18:16.894]  net      xmr.2miners.com:2222 read error: "end of file"
[2022-12-25 19:18:16.894]  net      no active pools, stop mining
[2022-12-25 19:18:22.603]  net      use pool xmr.2miners.com:2222  127.0.0.1
[2022-12-25 19:18:22.604]  net      new job from xmr.2miners.com:2222 diff 120001 algo rx/0 height 2784995 (14 tx)
[2022-12-25 19:19:16.302]  miner    speed 10s/60s/15m 3368.9 2759.9 n/a H/s max 3435.9 H/s
[2022-12-25 19:19:19.460]  cpu      accepted (11/1) diff 120001 (248 ms)
[2022-12-25 19:19:22.042]  cpu      accepted (12/1) diff 120001 (245 ms)
[2022-12-25 19:19:45.843]  cpu      accepted (13/1) diff 120001 (252 ms)
[2022-12-25 19:19:50.821]  cpu      accepted (14/1) diff 120001 (245 ms)
[2022-12-25 19:20:17.353]  miner    speed 10s/60s/15m 3048.9 3283.6 n/a H/s max 3435.9 H/s
[2022-12-25 19:20:22.241]  net      xmr.2miners.com:2222 read error: "end of file"
[2022-12-25 19:20:22.241]  net      no active pools, stop mining
[2022-12-25 19:20:28.000]  net      use pool xmr.2miners.com:2222  127.0.0.1
[2022-12-25 19:20:28.001]  net      new job from xmr.2miners.com:2222 diff 120001 algo rx/0 height 2784995 (14 tx)
[2022-12-25 19:21:18.371]  miner    speed 10s/60s/15m 3396.1 3022.4 n/a H/s max 3435.9 H/s
[2022-12-25 19:21:27.642]  net      xmr.2miners.com:2222 read error: "end of file"
[2022-12-25 19:21:27.643]  net      no active pools, stop mining
[2022-12-25 19:21:33.249]  net      use pool xmr.2miners.com:2222  127.0.0.1
[2022-12-25 19:21:33.249]  net      new job from xmr.2miners.com:2222 diff 120001 algo rx/0 height 2784995 (14 tx)

I'm using a socks5 proxy.

# Discussion History
## Spudz76 | 2022-12-25T14:18:30+00:00
Looks like the proxy is set for 120 second maximum connection life and does not allow "pegged" connections forever, which is what you would need.  From the connect message to the EOF message its exactly 120 seconds (plus accounting/reaction/net-lag time)... `19:18:22.603 ... 19:20:22.241`

## WindowsMEMZ | 2022-12-25T17:13:57+00:00
> Looks like the proxy is set for 120 second maximum connection life and does not allow "pegged" connections forever, which is what you would need. From the connect message to the EOF message its exactly 120 seconds (plus accounting/reaction/net-lag time)... `19:18:22.603 ... 19:20:22.241`

OK, I know this problem now. Thanks!

# Action History
- Created by: WindowsMEMZ | 2022-12-25T11:24:33+00:00
- Closed at: 2022-12-25T17:13:57+00:00
