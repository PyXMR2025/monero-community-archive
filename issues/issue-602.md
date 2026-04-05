---
title: rejected (0/1) diff 4096 "Incorrect share" (123 ms)
source_url: https://github.com/xmrig/xmrig/issues/602
author: ghost
assignees: []
labels:
- question
created_at: '2018-05-04T09:07:49+00:00'
updated_at: '2018-06-17T18:14:51+00:00'
type: issue
status: closed
closed_at: '2018-06-17T18:14:51+00:00'
---

# Original Description
Hi,

I try to pass from xmr-stak to xmrig (cpu for now/ Nvidia after) but I have a error message:

* VERSIONS:     XMRig/2.5.3 libuv/1.8.0 gcc/7.1.0
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Xeon(R) Platinum 8175M CPU @ 2.50GHz (1) x64 AES-NI
 * CPU L2/L3:    2.0 MB/33.0 MB
 * THREADS:      4, cryptonight, av=1, donate=1%
 * POOL #1:      loki.miner.rocks:5555
 * COMMANDS:     hashrate, pause, resume
[2018-05-04 09:02:34] use pool loki.miner.rocks:5555 51.38.205.26
[2018-05-04 09:02:34] new job from loki.miner.rocks:5555 diff 16384
[2018-05-04 09:02:37] new job from loki.miner.rocks:5555 diff 16384
[2018-05-04 09:03:20] new job from loki.miner.rocks:5555 diff 16384
[2018-05-04 09:03:21] new job from loki.miner.rocks:5555 diff 16384
[2018-05-04 09:03:37] speed 2.5s/60s/15m 70.7 71.4 n/a H/s max: 72.7 H/s
[2018-05-04 09:03:41] new job from loki.miner.rocks:5555 diff 8192
[2018-05-04 09:03:55] new job from loki.miner.rocks:5555 diff 8192
[2018-05-04 09:04:01] speed 2.5s/60s/15m 70.0 70.7 n/a H/s max: 72.7 H/s
[2018-05-04 09:04:37] speed 2.5s/60s/15m 65.5 69.6 n/a H/s max: 72.7 H/s
[2018-05-04 09:04:41] new job from loki.miner.rocks:5555 diff 4096
[2018-05-04 09:04:58] speed 2.5s/60s/15m 70.3 70.3 n/a H/s max: 72.8 H/s
[2018-05-04 09:05:21] rejected (0/1) diff 4096 "Incorrect share" (123 ms)


Here is my config 
{
   "algo": "cryptonight-heavy",
   "background": false,
   "colors": true,
   "retries": 5,
   "threads":4,
   "retry-pause": 5,
   "donate-level": 1,
   "syslog": false,
   "log-file": null,
   "access-log-file": null,
   "verbose": true,
   "pools": [
       {   
           "url": "loki.miner.rocks:5555",
           "user": "address",
        "pass": "w=worker",
           "variant": -1
       }
   ],

   "api": {
       "port": 0,
       "access-token": null,
       "worker-id": "worker"
   }
}

the same conf works fine with xmr-stak.

# Discussion History
## xmrig | 2018-05-04T10:31:28+00:00
Please use v2.6+. Currently it https://github.com/xmrig/xmrig/releases/tag/v2.6.0-beta3
Thank you.

# Action History
- Created by: ghost | 2018-05-04T09:07:49+00:00
- Closed at: 2018-06-17T18:14:51+00:00
