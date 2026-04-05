---
title: Duplicate shares after algo switch
source_url: https://github.com/xmrig/xmrig/issues/1180
author: MoneroOcean
assignees: []
labels:
- bug
created_at: '2019-09-19T14:27:52+00:00'
updated_at: '2019-09-19T19:56:28+00:00'
type: issue
status: closed
closed_at: '2019-09-19T19:56:28+00:00'
---

# Original Description
Sometimes after algo switches (noticed that only for rx/wow and rx/loki switches) xmrig starts to emit duplicate shares (this is visible because I added submitted nonce extra log):

```
[2019-09-19 13:53:06.875] new job from gulf.moneroocean.stream:10064 diff 48231 algo rx/loki height 362295
[2019-09-19 13:53:06.877]  cpu  stopped (2 ms)
[2019-09-19 13:53:06.877]  rx   init dataset algo rx/loki (12 threads) seed 4ea280d70f6567ff...
[2019-09-19 13:53:09.878]  rx   #0 init done 1/1 (3001 ms)
[2019-09-19 13:53:09.878]  cpu  use profile  rx  (12 threads) scratchpad 2048 KB
[2019-09-19 13:53:09.881]  cpu  READY threads 12(12) huge pages 12/12 100% memory 24576 KB (3 ms)
[2019-09-19 13:53:11.492] new job from gulf.moneroocean.stream:10064 diff 51589 algo rx/wow height 143012
[2019-09-19 13:53:11.494]  cpu  stopped (2 ms)
[2019-09-19 13:53:11.494]  rx   init dataset algo rx/wow (12 threads) seed 790435e5ba4c9542...
[2019-09-19 13:53:14.352]  rx   #0 init done 1/1 (2858 ms)
[2019-09-19 13:53:14.352]  cpu  use profile  rx/wow  (12 threads) scratchpad 1024 KB
[2019-09-19 13:53:14.356]  cpu  READY threads 12(12) huge pages 12/12 100% memory 12288 KB (4 ms)
[2019-09-19 13:53:14.943] nonce: 44810200
[2019-09-19 13:53:14.945] nonce: 44810200
[2019-09-19 13:53:15.086] accepted (1584/7) diff 51589 (143 ms)
[2019-09-19 13:53:15.159] rejected (1584/8) diff 51589 "Duplicate share" (213 ms)
[2019-09-19 13:53:16.532] new job from gulf.moneroocean.stream:10064 diff 48474 algo rx/loki height 362295
[2019-09-19 13:53:16.533]  cpu  stopped (1 ms)
[2019-09-19 13:53:16.533]  rx   init dataset algo rx/loki (12 threads) seed 4ea280d70f6567ff...
[2019-09-19 13:53:19.543]  rx   #0 init done 1/1 (3010 ms)
[2019-09-19 13:53:19.543]  cpu  use profile  rx  (12 threads) scratchpad 2048 KB
[2019-09-19 13:53:19.546]  cpu  READY threads 12(12) huge pages 12/12 100% memory 24576 KB (3 ms)
[2019-09-19 13:53:30.899] nonce: d3160000
[2019-09-19 13:53:31.017] accepted (1585/8) diff 48474 (118 ms)
[2019-09-19 13:53:37.844] speed 10s/60s/15m 6151.3 n/a n/a H/s max 6187.7 H/s
[2019-09-19 13:53:44.355] nonce: dfb00700
[2019-09-19 13:53:44.428] accepted (1586/8) diff 48474 (73 ms)
[2019-09-19 13:53:45.968] nonce: 13350400
[2019-09-19 13:53:46.041] accepted (1587/8) diff 48474 (73 ms)
[2019-09-19 13:53:54.831] nonce: 78c50300
[2019-09-19 13:53:54.904] accepted (1588/8) diff 48474 (73 ms)
[2019-09-19 13:54:24.476] nonce: a4020100
[2019-09-19 13:54:24.550] accepted (1589/8) diff 48474 (74 ms)
[2019-09-19 13:54:37.888] speed 10s/60s/15m 6142.0 6144.8 n/a H/s max 6187.7 H/s
[2019-09-19 13:54:49.726] nonce: 13350400
[2019-09-19 13:54:49.801] rejected (1589/9) diff 48474 "Duplicate share" (75 ms)
[2019-09-19 13:54:57.884] nonce: 78c50300
[2019-09-19 13:54:57.957] rejected (1589/10) diff 48474 "Duplicate share" (73 ms)
[2019-09-19 13:54:58.104] nonce: 2fc60200
[2019-09-19 13:54:58.178] accepted (1590/10) diff 48474 (74 ms)
[2019-09-19 13:55:04.169] nonce: 74d20100
[2019-09-19 13:55:04.242] accepted (1591/10) diff 48474 (73 ms)
[2019-09-19 13:55:34.840] nonce: 450e0b00
[2019-09-19 13:55:34.915] rejected (1591/11) diff 48474 "Unauthenticated" (75 ms)
```

This can be indication of serious issue (reduce miner rewards) if miner repeats already performed hashing.

P.S. This happens on 3.x and 4.x versions on Ryzen 3600 type of system.

# Discussion History
## xmrig | 2019-09-19T17:33:00+00:00
Please check commit https://github.com/xmrig/xmrig/commit/365667ee0af2e122adac56a36ac6b4ce8cb3be2f it probably solve the issue.
Thank you.

## MoneroOcean | 2019-09-19T17:48:02+00:00
Started testing this. Will report tomorrow. Thank you!

## MoneroOcean | 2019-09-19T19:56:28+00:00
Seems to be working fine now! Thank you again for such a quick fix.

# Action History
- Created by: MoneroOcean | 2019-09-19T14:27:52+00:00
- Closed at: 2019-09-19T19:56:28+00:00
