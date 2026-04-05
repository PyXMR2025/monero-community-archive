---
title: Algo switch on Dev donation.
source_url: https://github.com/xmrig/xmrig/issues/1307
author: trasherdk
assignees: []
labels:
- bug
created_at: '2019-11-21T03:13:49+00:00'
updated_at: '2019-12-22T19:38:39+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:38:39+00:00'
---

# Original Description
Running v5.0.1 mining XMR RandomX on testnet.
When `dev donation` job start, algo switches to `cn/r` as expected...
When the job ends, I would expect to return to the previous algo. This doesn't happen
until a new (second) job is send from the pool.

I'm using [ponero-pool](https://github.com/jtgrassie/monero-pool) with `self-select` enabled.

```
[2019-11-21 02:36:19.189]  net  new job from localhost:8000 diff 157330 algo rx/0 height 1347279
[2019-11-21 02:36:33.583] speed 10s/60s/15m 1092.8 1116.9 1116.0 H/s max 1136.6 H/s
[2019-11-21 02:36:53.345]  cpu  accepted (37/0) diff 157330 (86 ms)
[2019-11-21 02:37:03.618] speed 10s/60s/15m 1109.7 1115.2 1116.2 H/s max 1136.6 H/s
[2019-11-21 02:38:33.735] speed 10s/60s/15m 1115.6 1115.5 1115.4 H/s max 1136.6 H/s
[2019-11-21 02:38:56.356]  cpu  accepted (38/0) diff 157330 (62 ms)
[2019-11-21 02:39:03.772] speed 10s/60s/15m 1111.6 1113.4 1114.8 H/s max 1136.6 H/s
[2019-11-21 02:40:03.851] speed 10s/60s/15m 1105.3 1120.5 1114.8 H/s max 1136.6 H/s
[2019-11-21 02:40:04.656]  net  new job from localhost:8000 diff 158042 algo rx/0 height 1347280

[2019-11-21 02:40:05.487]  net  dev donate started
[2019-11-21 02:40:05.487]  net  new job from donate.ssl.xmrig.com:443 diff 1000225 algo cn/r height 1971450
[2019-11-21 02:40:33.898] speed 10s/60s/15m 91.5 622.2 1082.3 H/s max 1055.4 H/s
[2019-11-21 02:41:03.979] speed 10s/60s/15m 92.6 108.0 1048.0 H/s max 1055.4 H/s
[2019-11-21 02:41:05.488]  net  dev donate finished

[2019-11-21 02:41:05.488]  net  new job from localhost:8000 diff 158042 algo cn/r

[2019-11-21 02:41:34.050] speed 10s/60s/15m 156.8 107.9 1014.9 H/s max 1055.4 H/s
[2019-11-21 02:42:04.104] speed 10s/60s/15m 155.8 139.6 982.6 H/s max 1055.4 H/s
[2019-11-21 02:44:34.418] speed 10s/60s/15m 156.3 156.6 823.4 H/s max 1055.4 H/s
[2019-11-21 02:45:04.471] speed 10s/60s/15m 155.8 155.8 791.8 H/s max 1055.4 H/s

[2019-11-21 02:45:07.205]  net  new job from localhost:8000 diff 144796 algo rx/0 height 1347281
```

# Discussion History
## xmrig | 2019-11-21T08:25:32+00:00
Confirmed, this issue happen only for pools with self-select, regular pools switch back correctly.
Thank you.

## xmrig | 2019-11-21T08:47:05+00:00
Fixed.

# Action History
- Created by: trasherdk | 2019-11-21T03:13:49+00:00
- Closed at: 2019-12-22T19:38:39+00:00
