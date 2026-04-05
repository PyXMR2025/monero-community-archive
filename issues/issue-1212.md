---
title: Low RandomX performance on fast algo switch
source_url: https://github.com/xmrig/xmrig/issues/1212
author: MoneroOcean
assignees: []
labels:
- bug
created_at: '2019-09-30T22:35:53+00:00'
updated_at: '2019-10-01T23:50:53+00:00'
type: issue
status: closed
closed_at: '2019-10-01T23:50:53+00:00'
---

# Original Description
After fast algo switch (reproduced with rx/wow and rx/loki) sometimes 4.2.0-beta miner (saw it on all older v4 versions as well) starts to mine rx/loki with very low speed (6100 is expected, but it mines with 700 here). After next algo switch this is usually is fixed automatically:

```
[2019-09-30 21:36:59.873] new job from gulf.moneroocean.stream:10064 diff 200858 algo rx/loki height 370454
[2019-09-30 21:37:03.952] new job from gulf.moneroocean.stream:10064 diff 200858 algo rx/loki height 370455
[2019-09-30 21:37:05.625] speed 10s/60s/15m 6014.2 6015.9 n/a H/s max 6022.6 H/s
[2019-09-30 21:38:05.683] speed 10s/60s/15m 6017.6 6016.1 n/a H/s max 6022.6 H/s
[2019-09-30 21:38:10.229] accepted (862/1) diff 200858 (126 ms)
[2019-09-30 21:38:42.999] new job from gulf.moneroocean.stream:10064 diff 210620 algo rx/wow height 146279
[2019-09-30 21:38:43.002]  cpu  stopped (2 ms)
[2019-09-30 21:38:43.002]  rx   init dataset algo rx/wow (12 threads) seed 64087c1d057c067a...
[2019-09-30 21:38:45.012] new job from gulf.moneroocean.stream:10064 diff 196090 algo rx/loki height 370455
[2019-09-30 21:38:46.275]  rx   #0 init done 1/1 (3274 ms)
[2019-09-30 21:38:46.275]  rx   init dataset algo rx/loki (12 threads) seed 07bf109146892d2d...
[2019-09-30 21:38:49.719]  rx   #0 init done 1/1 (3444 ms)
[2019-09-30 21:38:49.719]  cpu  use profile  rx  (12 threads) scratchpad 2048 KB
[2019-09-30 21:38:49.722]  cpu  READY threads 12/12 (12) huge pages 12/12 100% memory 24576 KB (3 ms)
[2019-09-30 21:39:09.743] speed 10s/60s/15m 699.8 n/a n/a H/s max 6022.6 H/s
[2019-09-30 21:39:13.141] new job from gulf.moneroocean.stream:10064 diff 195048 algo rx/loki height 370458
[2019-09-30 21:39:30.538] new job from gulf.moneroocean.stream:10064 diff 195048 algo rx/loki height 370459
[2019-09-30 21:40:09.779] speed 10s/60s/15m 702.1 701.7 n/a H/s max 6022.6 H/s
[2019-09-30 21:40:54.693] accepted (863/1) diff 195048 (161 ms)
[2019-09-30 21:41:09.813] speed 10s/60s/15m 702.3 702.1 n/a H/s max 6022.6 H/s
[2019-09-30 21:42:09.852] speed 10s/60s/15m 702.4 702.1 n/a H/s max 6022.6 H/s
[2019-09-30 21:43:09.888] speed 10s/60s/15m 702.5 702.3 n/a H/s max 6022.6 H/s
[2019-09-30 21:44:05.545] accepted (864/1) diff 195048 (360 ms)
```

# Discussion History
## xmrig | 2019-09-30T22:48:45+00:00
Please show result of full hashrate report, `h` key, I will try simulate this issue later.
Thank you.

## MoneroOcean | 2019-09-30T22:51:08+00:00
Will try to catch that during interactive session next time. Output above is from systemd based miner, so I can not press ```h``` there unfortunately.

## xmrig | 2019-09-30T22:57:40+00:00
In this case hashrate report from API is fine too.

## xmrig | 2019-10-01T01:16:30+00:00
I successfully reproduced the bug, not all threads mine after fast dataset change, no extra information required.
Thank you.

## MoneroOcean | 2019-10-01T01:31:47+00:00
Thank you! Just in case just got this h output with bug:

```
[2019-10-01 01:30:13.577] speed 10s/60s/15m 1540.7 1540.5 1540.3 H/s max 6096.3 H/s
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |     n/a |     n/a |     n/a |
|        1 |        1 |     n/a |     n/a |     n/a |
|        2 |        2 |     n/a |     n/a |     n/a |
|        3 |        3 |     n/a |     n/a |     n/a |
|        4 |        4 |     n/a |     n/a |     n/a |
|        5 |        5 |     n/a |     n/a |     n/a |
|        6 |        6 |     n/a |     n/a |     n/a |
|        7 |        7 |     n/a |     n/a |     n/a |
|        8 |        8 |     n/a |     n/a |     n/a |
|        9 |        9 |     n/a |     n/a |     n/a |
|       10 |       10 |   770.3 |   770.2 |   770.0 |
|       11 |       11 |   769.9 |   770.6 |   770.3 |
|        - |        - |  1540.2 |  1540.8 |  1540.4 |
[2019-10-01 01:31:02.977] speed 10s/60s/15m 1540.2 1540.8 1540.4 H/s max 6096.3 H/s
```

## xmrig | 2019-10-01T23:40:03+00:00
Fixed, but I think pool should not do fast randomx switching, dataset re-initialization take some time.
Thank you.

## MoneroOcean | 2019-10-01T23:42:11+00:00
Thank you very much! Unfortunately sometimes it is inevitable in case of coin daemon having issues.

## mk7R | 2019-10-01T23:47:09+00:00
Thanks! 

# Action History
- Created by: MoneroOcean | 2019-09-30T22:35:53+00:00
- Closed at: 2019-10-01T23:50:53+00:00
