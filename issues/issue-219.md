---
title: max hash rate always show n/a
source_url: https://github.com/xmrig/xmrig/issues/219
author: feeeei
assignees: []
labels:
- NUMA
created_at: '2017-11-25T15:51:29+00:00'
updated_at: '2019-08-02T12:38:38+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:38:38+00:00'
---

# Original Description
Hi.
I just started using 'xmrig', but I ran into several questions.
My environment is:
>**OS:** Ubuntu 16.04
>**CPU:** Intel (R) Xeon (R) CPU E5-2690 v2 @ 3.00GHz × 2

Compile method:
```command
git clone https://github.com/xmrig/xmrig.git
cmake .. -DCMAKE_C_COMPILER = gcc-7 -DCMAKE_CXX_COMPILER = g ++ - 7
make
```

config.json
```nohighlight
{
    "algo": "cryptonight",
    "av": 0,
    "background": false,
    "colors": true,
    "cpu-affinity": null,
    "cpu-priority": 5,
    "donate-level": 5,
    "log-file": null,
    "max-cpu-usage": 100,
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "safe": false,
    "syslog": false,
    "threads": 25,
    "pools": [
        {
            "url": "pool.supportxmr.com:5555",
            "user": "xxx",
            "pass": "xxx",
            "keepalive": true,
            "nicehash": false
        }
    ],
    "api": {
        "port": 0,
        "access-token": null,
        "worker-id": null
    }
}
```

run `./xmrig`
```
 * VERSIONS:     XMRig/2.4.2 libuv/1.8.0 gcc/7.1.0
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Xeon(R) CPU E5-2690 v2 @ 3.00GHz (1) x64 AES-NI
 * CPU L2/L3:    8.0 MB/25.0 MB
 * THREADS:      25, cryptonight, av=1, donate=5%
 * POOL #1:      pool.supportxmr.com:5555
 * COMMANDS:     hashrate, pause, resume
[2017-11-25 16:07:12] use pool pool.supportxmr.com:5555 94.23.23.52
[2017-11-25 16:07:12] new job from pool.supportxmr.com:5555 diff 5000
[2017-11-25 16:07:17] new job from pool.supportxmr.com:5555 diff 8824
[2017-11-25 16:07:22] new job from pool.supportxmr.com:5555 diff 8824
[2017-11-25 16:08:15] speed 2.5s/60s/15m n/a 64.0 n/a H/s max: n/a H/s
[2017-11-25 16:08:17] new job from pool.supportxmr.com:5555 diff 5883
[2017-11-25 16:08:43] accepted (1/0) diff 5883 (152 ms)
[2017-11-25 16:09:15] speed 2.5s/60s/15m n/a 64.0 n/a H/s max: n/a H/s
[2017-11-25 16:09:17] new job from pool.supportxmr.com:5555 diff 2000
[2017-11-25 16:09:22] new job from pool.supportxmr.com:5555 diff 2000
[2017-11-25 16:10:15] speed 2.5s/60s/15m n/a 62.0 n/a H/s max: n/a H/s
[2017-11-25 16:10:17] new job from pool.supportxmr.com:5555 diff 2000
[2017-11-25 16:10:21] accepted (2/0) diff 2000 (31 ms)
[2017-11-25 16:10:28] accepted (3/0) diff 2000 (30 ms)
[2017-11-25 16:10:48] accepted (4/0) diff 2000 (165 ms)
[2017-11-25 16:10:59] accepted (5/0) diff 2000 (31 ms)
[2017-11-25 16:11:10] accepted (6/0) diff 2000 (38 ms)
[2017-11-25 16:11:15] speed 2.5s/60s/15m n/a 62.1 n/a H/s max: n/a H/s
[2017-11-25 16:11:17] new job from pool.supportxmr.com:5555 diff 2000
[2017-11-25 16:11:24] accepted (7/0) diff 2000 (27 ms)
[2017-11-25 16:11:39] accepted (8/0) diff 2000 (29 ms)
[2017-11-25 16:11:53] new job from pool.supportxmr.com:5555 diff 2000
```

Wait a few minutes, I can see 50h/s in pool dashboard, but still n/a on the command line.

Why show only one CPU?
Why hash rate has always show n/a?


# Discussion History
## gennadicho | 2017-11-25T17:54:59+00:00
You using NUMA?

## feeeei | 2017-11-25T18:55:13+00:00
Yes

## gennadicho | 2017-11-25T19:10:35+00:00
So, xmrig probably not working with NUMA :( And "n/a" hasrate showing if hardware is really slow(in you situation - slow beacuse NUMA)

## jdevsan | 2017-11-27T20:11:52+00:00
what is NUMA?

## 2010phenix | 2018-01-26T14:35:57+00:00
if @Bendr0id share his solution(Fixed CPU affinity on Windows for NUMA and CPUs with lot of cores), all already done
https://github.com/Bendr0id/xmrigCC/pull/30

## Bendr0id | 2018-01-26T14:57:54+00:00
@2010phenix my fix is just for the cpu affinity, which was broken on windows. It's not full numa support. 
But he is using Linux.

@feeeei Just for testing please try XMRigCC (you don't need to setup the server part) and please run with 10 threads, cpu-affinity 0x55555, hashfactor 2 and multihash-thread-mask 0x3. That should affine 10 threads to 10 real cores, use double hash on 2 threads. In sun it should use 24mb of your l3 cache. Sample config file is in the src folder. Hope this helps.

## xmrig | 2019-07-29T02:19:02+00:00
If this issue still actual, please check v2.99.2-beta release #1077.
Thank you.

# Action History
- Created by: feeeei | 2017-11-25T15:51:29+00:00
- Closed at: 2019-08-02T12:38:38+00:00
