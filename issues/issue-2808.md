---
title: 'RTM: invalid wallet address'
source_url: https://github.com/xmrig/xmrig/issues/2808
author: PSLLSP
assignees: []
labels: []
created_at: '2021-12-12T07:00:44+00:00'
updated_at: '2021-12-12T11:05:26+00:00'
type: issue
status: closed
closed_at: '2021-12-12T11:05:26+00:00'
---

# Original Description
`xmrig-6.16.2-linux-static-x64.tar.gz`

I cannot mine **RTM** (Raptoreum) with `xmrig`. Shares are rejected with error **invalid wallet address**
`cpuminer-gr` can mine with the same wallet address, no issue.... [pool stat](https://flockpool.com/miners/rtm/RSh1vvL1QVhCuuDg44TFknJjjTe4gDCYzL)
Wallet address is from **[ZelCore wallet](https://zelcore.io/)**. 

```
$ cat test-rtm-flock.sh 
#!/bin/sh

HOST="TEST1"

POOL="eu.flockpool.com:4444"
USER="RSh1vvL1QVhCuuDg44TFknJjjTe4gDCYzL"
PASS="x"

OPTS="-t 2"

./xmrig -a gr -o "stratum+tcp://$POOL" -u "$ADDR.$HOST" -p "$PASS" $OPTS "$@"
```

```
$ sh test-rtm-flock.sh
 * ABOUT        XMRig/6.16.2 gcc/9.3.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
...
 * POOL #1      stratum+tcp://eu.flockpool.com:4444 algo ghostrider
...
[2021-12-12 07:31:24.717]  net      new job from eu.flockpool.com:4444 diff 15578 algo ghostrider height 203868
[2021-12-12 07:31:36.303]  cpu      rejected (0/1) diff 15578 "invalid wallet address, invalid wallet address" (19 ms)
[2021-12-12 07:31:53.174]  miner    speed 10s/60s/15m 184.3 183.2 n/a H/s max 188.4 H/s avg 182.9 H/s
[2021-12-12 07:32:09.977]  cpu      rejected (0/2) diff 15578 "invalid wallet address, invalid wallet address" (19 ms)
[2021-12-12 07:32:15.830]  cpu      rejected (0/3) diff 15578 "invalid wallet address, invalid wallet address" (19 ms)
...
[2021-12-12 07:35:53.665]  miner    speed 10s/60s/15m 173.5 150.4 n/a H/s max 176.0 H/s avg 139.5 H/s
[2021-12-12 07:36:26.763]  net      new job from eu.flockpool.com:4444 diff 15578 algo ghostrider height 203870
[2021-12-12 07:36:37.147]  cpu      rejected (0/11) diff 15578 "invalid wallet address, invalid wallet address" (18 ms)
[2021-12-12 07:36:53.941]  miner    speed 10s/60s/15m 174.6 173.3 n/a H/s max 176.0 H/s avg 150.8 H/s
```

# Discussion History
## Spudz76 | 2021-12-12T10:36:59+00:00
`stratum+tcp://` prefix is not needed

Do not use `--threads 2`

But the real issue you may find if you look for `$ADDR` in your script (hint: it's not `$USER`)

## PSLLSP | 2021-12-12T11:05:26+00:00
**USER ERROR!** LOL

# Action History
- Created by: PSLLSP | 2021-12-12T07:00:44+00:00
- Closed at: 2021-12-12T11:05:26+00:00
