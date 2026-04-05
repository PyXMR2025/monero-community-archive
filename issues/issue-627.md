---
title: New version 2.6.2 is to slow! 2.5.0 - much more faster! 630H/s vs 855 H/s!
  HUGE PAGE?
source_url: https://github.com/xmrig/xmrig/issues/627
author: minzak
assignees: []
labels: []
created_at: '2018-05-13T14:45:28+00:00'
updated_at: '2018-05-13T19:41:06+00:00'
type: issue
status: closed
closed_at: '2018-05-13T19:41:06+00:00'
---

# Original Description
I decide on new host use fresh version, and how it can be?
My old version give me **850** H/s vs new just **630**!
And it is not depend from gcc and libuv.
Also i see that in old version i can see **HUGE PAGE**, in new version this string is absent.

same PC with just different xmrig

What is wrong?

**XMRig/2.5.0 libuv/1.9.1 gcc/7.3.0**
```
root@z820:/opt/xmrig# ./xmrig4
Try "xmrig" --help' for more information.
 * VERSIONS:     XMRig/2.5.0 libuv/1.9.1 gcc/7.3.0
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Xeon(R) CPU E5-2660 0 @ 2.20GHz (2) x64 AES-NI
 * CPU L2/L3:    8.0 MB/40.0 MB
 * THREADS:      20, cryptonight, av=1, donate=0%
 * POOL #1:      mining.pool.com:3333
 * API PORT:     8080
 * COMMANDS:     'h' hashrate, 'p' pause, 'r' resume
[2018-05-13 17:34:27] use pool mining.pool.com:3333 18.197.112.104
[2018-05-13 17:34:27] new job from mining.pool.com:3333 diff 2000
[2018-05-13 17:34:32] speed 2.5s/60s/15m 858.3 n/a n/a H/s max: n/a H/s
[2018-05-13 17:34:34] speed 2.5s/60s/15m 858.2 n/a n/a H/s max: n/a H/s
[2018-05-13 17:34:34] accepted (1/0) diff 2000 (79 ms)
[2018-05-13 17:34:35] speed 2.5s/60s/15m 858.3 n/a n/a H/s max: n/a H/s
[2018-05-13 17:34:35] speed 2.5s/60s/15m 858.4 n/a n/a H/s max: n/a H/s
[2018-05-13 17:34:35] speed 2.5s/60s/15m 858.3 n/a n/a H/s max: n/a H/s
[2018-05-13 17:34:36] Ctrl+C received, exiting
[2018-05-13 17:34:36] no active pools, stop mining
```
**XMRig/2.6.2 libuv/1.9.1 gcc/6.3.0**
```
root@z820:/opt/xmrig# ./xmrig
 * VERSIONS:     XMRig/2.6.2 libuv/1.9.1 gcc/6.3.0
 * CPU:          Intel(R) Xeon(R) CPU E5-2660 0 @ 2.20GHz (2) x64 AES-NI
 * CPU L2/L3:    8.0 MB/40.0 MB
 * THREADS:      20, cryptonight, av=0, donate=1%
 * POOL #1:      mining.tpool.com:3333
 * API BIND:     0.0.0.0:8080
 * COMMANDS:     hashrate, pause, resume
[2018-05-13 17:34:41] use pool mining.tpool.com:3333 18.197.112.104
[2018-05-13 17:34:41] new job from mining.pool.com:3333 diff 2000 algo cn/1
[2018-05-13 17:34:41] READY (CPU) threads 20(20) huge pages 20/20 100% memory 40.0 MB
[2018-05-13 17:34:44] accepted (1/0) diff 2000 (80 ms)
[2018-05-13 17:34:46] speed 2.5s/60s/15m 630.6 n/a n/a H/s max: n/a H/s
[2018-05-13 17:34:46] new job from mining.pool.com:3333 diff 4000 algo cn/1
[2018-05-13 17:34:47] accepted (2/0) diff 4000 (77 ms)
[2018-05-13 17:34:51] Ctrl+C received, exiting
[2018-05-13 17:34:51] no active pools, stop mining
```
**XMRig/2.5.0 libuv/1.9.1 gcc/6.3.0**
```
root@z820:/opt/xmrig# ./xmrig0
Try "xmrig" --help' for more information.
 * VERSIONS:     XMRig/2.5.0 libuv/1.9.1 gcc/6.3.0
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Xeon(R) CPU E5-2660 0 @ 2.20GHz (2) x64 AES-NI
 * CPU L2/L3:    8.0 MB/40.0 MB
 * THREADS:      20, cryptonight, av=1, donate=1%
 * POOL #1:      mining.pool.com:3333
 * API PORT:     8080
 * COMMANDS:     'h' hashrate, 'p' pause, 'r' resume
[2018-05-13 17:34:54] use pool mining.pool.com:3333 18.197.112.104
[2018-05-13 17:34:54] new job from mining.grftpool.com:3333 diff 2000
[2018-05-13 17:34:54] accepted (1/0) diff 2000 (83 ms)
[2018-05-13 17:34:55] accepted (2/0) diff 2000 (79 ms)
[2018-05-13 17:34:57] accepted (3/0) diff 2000 (79 ms)
[2018-05-13 17:34:57] speed 2.5s/60s/15m 857.0 n/a n/a H/s max: n/a H/s
[2018-05-13 17:34:58] accepted (4/0) diff 2000 (80 ms)
[2018-05-13 17:34:58] speed 2.5s/60s/15m 855.7 n/a n/a H/s max: n/a H/s
[2018-05-13 17:34:59] Ctrl+C received, exiting
[2018-05-13 17:35:00] no active pools, stop mining
```


# Discussion History
## minzak | 2018-05-13T14:52:37+00:00
P.S. I also build 2.5.3 version - the same 850 H/s.
NEW 2.6.X - Too slow.

## Gill1000 | 2018-05-13T18:09:59+00:00
Can you plz tell me the pool you are mining..??

## minzak | 2018-05-13T18:29:55+00:00
It does not matter because conf.json is one with several binaries.
In this experiment was this - mining.grftpool.com



## 2010phenix | 2018-05-13T19:06:49+00:00
@bizlevel av=1 \ av=0 
you have L3 40 MB and used double mode....

## minzak | 2018-05-13T19:31:05+00:00
I always use **av=0**.
But if i change it:

```
[2018-05-13 22:22:23]  * THREADS:      20, cryptonight, av=0, donate=1%
[2018-05-13 22:22:23]  * POOL #1:      mining.grftpool.com:3333
[2018-05-13 22:22:23]  * API BIND:     0.0.0.0:8080
[2018-05-13 22:22:23]  * COMMANDS:     'h' hashrate, 'p' pause, 'r' resume
[2018-05-13 22:22:23] use pool mining.grftpool.com:3333 18.197.112.104
[2018-05-13 22:22:23] new job from mining.grftpool.com:3333 diff 2000 algo cn/1
[2018-05-13 22:22:23] READY (CPU) threads 20(20) huge pages 0/20 0% memory 40.0 MB
[2018-05-13 22:22:28] accepted (1/0) diff 2000 (83 ms)
[2018-05-13 22:22:31] speed 2.5s/60s/15m 579.7 n/a n/a H/s max: n/a H/s
[2018-05-13 22:22:36] speed 2.5s/60s/15m 571.8 n/a n/a H/s max: 575.5 H/s
[2018-05-13 22:22:39] speed 2.5s/60s/15m 572.2 n/a n/a H/s max: 575.5 H/s
```


```
[2018-05-13 22:26:55]  * THREADS:      20, cryptonight, av=1, donate=1%
[2018-05-13 22:26:55]  * CPU L2/L3:    8.0 MB/40.0 MB
[2018-05-13 22:26:55]  * POOL #1:      mining.grftpool.com:3333
[2018-05-13 22:26:55]  * COMMANDS:     'h' hashrate, 'p' pause, 'r' resume
[2018-05-13 22:26:55]  * API BIND:     0.0.0.0:8080
[2018-05-13 22:26:55] use pool mining.grftpool.com:3333 18.197.112.104
[2018-05-13 22:26:55] new job from mining.grftpool.com:3333 diff 2000 algo cn/1
[2018-05-13 22:26:55] READY (CPU) threads 20(20) huge pages 0/20 0% memory 40.0 MB
[2018-05-13 22:27:01] accepted (1/0) diff 2000 (83 ms)
[2018-05-13 22:27:02] speed 2.5s/60s/15m 597.3 n/a n/a H/s max: n/a H/s
[2018-05-13 22:27:02] accepted (2/0) diff 2000 (81 ms)
[2018-05-13 22:27:03] speed 2.5s/60s/15m 597.4 n/a n/a H/s max: n/a H/s
[2018-05-13 22:27:04] accepted (3/0) diff 2000 (82 ms)
[2018-05-13 22:27:04] speed 2.5s/60s/15m 597.3 n/a n/a H/s max: 597.2 H/s
```

```
[2018-05-13 22:22:55]  * THREADS:      10, cryptonight, av=2, donate=1%
[2018-05-13 22:22:55]  * POOL #1:      mining.grftpool.com:3333
[2018-05-13 22:22:55]  * API BIND:     0.0.0.0:8080
[2018-05-13 22:22:55]  * COMMANDS:     'h' hashrate, 'p' pause, 'r' resume
[2018-05-13 22:22:55] use pool mining.grftpool.com:3333 18.197.112.104
[2018-05-13 22:22:55] new job from mining.grftpool.com:3333 diff 2000 algo cn/1
[2018-05-13 22:22:55] READY (CPU) threads 10(20) huge pages 0/20 0% memory 40.0 MB
[2018-05-13 22:23:02] accepted (1/0) diff 2000 (79 ms)
[2018-05-13 22:23:03] speed 2.5s/60s/15m 368.7 n/a n/a H/s max: 368.7 H/s
[2018-05-13 22:23:05] accepted (2/0) diff 2000 (80 ms)
[2018-05-13 22:23:06] speed 2.5s/60s/15m 368.8 n/a n/a H/s max: 368.7 H/s
[2018-05-13 22:23:07] speed 2.5s/60s/15m 386.1 n/a n/a H/s max: 368.7 H/s
```

```
[2018-05-13 22:23:17]  * THREADS:      20, cryptonight, av=3, donate=1%
[2018-05-13 22:23:17]  * POOL #1:      mining.grftpool.com:3333
[2018-05-13 22:23:17]  * API BIND:     0.0.0.0:8080
[2018-05-13 22:23:17]  * COMMANDS:     'h' hashrate, 'p' pause, 'r' resume
[2018-05-13 22:23:17] use pool mining.grftpool.com:3333 18.197.112.104
[2018-05-13 22:23:17] new job from mining.grftpool.com:3333 diff 2000 algo cn/1
[2018-05-13 22:23:17] READY (CPU) threads 20(20) huge pages 0/20 0% memory 40.0 MB
[2018-05-13 22:23:20] accepted (1/0) diff 2000 (82 ms)
[2018-05-13 22:23:20] accepted (2/0) diff 2000 (82 ms)
[2018-05-13 22:23:21] speed 2.5s/60s/15m 320.8 n/a n/a H/s max: n/a H/s
[2018-05-13 22:23:22] speed 2.5s/60s/15m 322.9 n/a n/a H/s max: n/a H/s
```

```
[2018-05-13 22:23:29]  * THREADS:      10, cryptonight, av=4, donate=1%
[2018-05-13 22:23:29]  * POOL #1:      mining.grftpool.com:3333
[2018-05-13 22:23:29]  * API BIND:     0.0.0.0:8080
[2018-05-13 22:23:29]  * COMMANDS:     'h' hashrate, 'p' pause, 'r' resume
[2018-05-13 22:23:29] use pool mining.grftpool.com:3333 18.197.112.104
[2018-05-13 22:23:29] new job from mining.grftpool.com:3333 diff 2000 algo cn/1
[2018-05-13 22:23:29] READY (CPU) threads 10(20) huge pages 0/20 0% memory 40.0 MB
[2018-05-13 22:23:31] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2018-05-13 22:23:33] accepted (1/0) diff 2000 (84 ms)
[2018-05-13 22:23:33] speed 2.5s/60s/15m 188.5 n/a n/a H/s max: n/a H/s
[2018-05-13 22:23:35] speed 2.5s/60s/15m 200.6 n/a n/a H/s max: n/a H/s
```

My **config.json** //no user, no pass

```
{
    "algo": "monero7",      // cryptonight (default) or cryptonight-lite
    "av": 1,                // algorithm variation, 0 auto select
    "background": false,    // true to run the miner in the background
    "colors": false,        // false to disable colored output....
    "cpu-affinity": null,   // set process affinity to CPU core(s), mask "0x3" for cores 0 and 1
    "cpu-priority": 4,      // set process priority (0 idle, 2 normal to 5 highest)
    "donate-level": 0,      // donate level, mininum 1%
    "max-cpu-usage": 95,    // maximum CPU usage for automatic mode, usually limiting factor is CPU cache not this option...
    "print-time": 60,       // print hashrate report every N seconds
    "retries": 5,           // number of times to retry before switch to backup server
    "retry-pause": 5,       // time to pause between retries
    "safe": false,          // true to safe adjust threads and av settings for current CPU
    "threads": null,        // number of miner threads
    "log-file": "/opt/xmrig/xmrig.log", // log all output to a file, example: "c:/some/path/xmrig.log"
    "pools": [
        {
            "url": "mining.grftpool.com:3333", // URL of mining server
            "keepalive": true,               // send keepalived for prevent timeout (need pool support)
            "nicehash": false,               // enable nicehash/xmrig-proxy support
            "variant": -1                    // algorithm PoW variant
        }
    ],
    "api": {
        "port": 8080,                          // port for the miner API https://github.com/xmrig/xmrig/wiki/API
        "access-token": null,                  // access token for API
        "worker-id": null                      // custom worker-id for API
    }
}

```


## minzak | 2018-05-13T19:41:06+00:00
P.S. I reinstall fresh OS, and now i can't reproduce it (( 
Very, very  strange....
But Now is all fine.
Of course after it:
```
echo 128 > /proc/sys/vm/nr_hugepages
sysctl -w vm.nr_hugepages=128

```

# Action History
- Created by: minzak | 2018-05-13T14:45:28+00:00
- Closed at: 2018-05-13T19:41:06+00:00
