---
title: v2.99.[234]-beta segfaults on opteron 6372
source_url: https://github.com/xmrig/xmrig/issues/1092
author: neuroscr
assignees: []
labels:
- bug
- NUMA
- need feedback
created_at: '2019-08-01T00:27:29+00:00'
updated_at: '2020-04-05T07:24:23+00:00'
type: issue
status: closed
closed_at: '2019-08-09T09:46:08+00:00'
---

# Original Description
had to go back to .1

was getting `warning: "can't bind memory"` and then a segfault

Running in LXC container on ubuntu 18LTS, what info do you need? I have 4 sockets, plenty of ram available (256gb in the box, 16gb on the container)

# Discussion History
## xmrig | 2019-08-01T02:17:33+00:00
Please run command `./xmrig --export-topology` (for 2.99.3) inside container and if possible outside too then attach resulting `topology.xml` to this issue.

Seems something wrong with hwloc inside container, I will try use LXC container, build miner without hwloc support (`-DWITH_HWLOC=OFF`) should restore 2.99.1 behavior.
Thank you.

## neuroscr | 2019-08-04T10:30:06+00:00
from inside lxc
https://spit.mixtape.moe/view/8e31be8a

also tested .4 and it also segfaults with the similar results:
```
[2019-08-04 10:32:05.017]  rx   init datasets algo rx/loki (16 threads) seed db194afda36bd91a...
[2019-08-04 10:32:05.018]  cpu  use profile  rx/loki  (16 threads) scratchpad 2048 KB
[2019-08-04 10:32:06.095] CPU #32 warning: "can't bind memory"
[2019-08-04 10:32:06.096] CPU #16 warning: "can't bind memory"
```

## xmrig | 2019-08-05T11:12:44+00:00
I forgot to ask, but what pool do you use? Might be same issue https://github.com/xmrig/xmrig/issues/1066#issuecomment-518080529
Thank you.

## xmrig | 2019-08-05T15:22:29+00:00
According hwloc topology you can use only one (first) CPU (16 cores) (from `0` to `15`), 3 other CPUs not available and miner should not generate config for not exists cores.

* I fixed the crash, but cores above `15` not available anyway.
* You use generated config or custom?

## neuroscr | 2019-08-06T23:29:17+00:00
topology outside https://spit.mixtape.moe/view/7d39e65b

pool: loki.hashvault.pro

I did lock down the LXC container to 16 cores (because I could no figure out any way to get it to use less CPUs, tried a couple different CLI options).

I did start with an auto config but I did edit it ofc, tried setting up cpu affinity like xmr-stak auto-detected for me:

```
        "rx/loki": [
            0,
            1,
            8,
            9,
            16,
            17,
            24,
            25,
            32,
            33,
            40,
            41,
            48,
            49,
            56,
            57
        ],
```

## neuroscr | 2019-08-06T23:43:15+00:00
also crashes with and without -t

## xmrig | 2019-08-09T09:46:08+00:00
v2.99.5-beta released https://github.com/xmrig/xmrig/releases/tag/v2.99.5-beta

## neuroscr | 2020-04-05T07:24:23+00:00
fixed as of at least 5.10

# Action History
- Created by: neuroscr | 2019-08-01T00:27:29+00:00
- Closed at: 2019-08-09T09:46:08+00:00
