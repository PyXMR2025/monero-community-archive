---
title: Maybe a bug in donation system.!!
source_url: https://github.com/xmrig/xmrig/issues/519
author: Gill1000
assignees: []
labels:
- bug
created_at: '2018-04-08T05:17:57+00:00'
updated_at: '2018-04-13T22:16:12+00:00'
type: issue
status: closed
closed_at: '2018-04-13T22:16:12+00:00'
---

# Original Description
Im using 2.5.2 xmrig and first tell me how to show logs of donation timings.?? like dev donation started...
and regarding bug i put 100% in donate.h but still it is mining in my pool my shares are accepting!!!!!!!
Is this fix in 2.6.0????????

# Discussion History
## xmrig | 2018-04-08T08:17:55+00:00
* Miner on startup show what donation level used.
* To change level don't need edit donate.h in config file has option `donate-level` you can set any value from 1 to 99. donate.h only usable if someone want set 0 donation.
Thank you.

## Gill1000 | 2018-04-08T08:48:29+00:00
How to see the donation logs...???

## xmrig | 2018-04-08T08:53:15+00:00
You will see message `dev donate started` and `new job...` from donation url and after it finished will be message `dev donate finished`.

## Gill1000 | 2018-04-08T10:29:28+00:00
This is my log from original 2.6.0  64bit.

 * VERSIONS:     XMRig/2.6.0-beta1 libuv/1.19.2 gcc/7.3.0
 * HUGE PAGES:   unavailable, disabled
 * CPU:          Intel(R) Core(TM) i3-4130 CPU @ 3.40GHz (1) x64 AES-NI
 * CPU L2/L3:    0.5 MB/3.0 MB
 * THREADS:      1, cryptonight, av=1, donate=99%
 * POOL #1:      pool.supportxmr.com:8080
 * COMMANDS:     hashrate, pause, resume
[2018-04-08 11:15:13] use pool pool.supportxmr.com:8080 103.253.40.189
[2018-04-08 11:15:13] new job from pool.supportxmr.com:8080 diff 5000
[2018-04-08 11:16:04] speed 2.5s/60s/15m 60.7 n/a n/a H/s max: 61.6 H/s
[2018-04-08 11:16:26] accepted (1/0) diff 5000 (2461 ms)
[2018-04-08 11:16:38] new job from pool.supportxmr.com:8080 diff 5000
[2018-04-08 11:16:53] speed 2.5s/60s/15m 60.5 61.0 n/a H/s max: 61.6 H/s
[2018-04-08 11:17:04] speed 2.5s/60s/15m 61.3 61.0 n/a H/s max: 61.6 H/s
[2018-04-08 11:17:38] new job from pool.supportxmr.com:8080 diff 5000
[2018-04-08 11:18:04] speed 2.5s/60s/15m 61.5 61.0 n/a H/s max: 61.6 H/s
[2018-04-08 11:18:24] speed 2.5s/60s/15m 61.1 61.1 n/a H/s max: 61.6 H/s
[2018-04-08 11:18:38] new job from pool.supportxmr.com:8080 diff 5000
[2018-04-08 11:18:55] accepted (2/0) diff 5000 (962 ms)
[2018-04-08 11:19:04] speed 2.5s/60s/15m 61.4 55.8 n/a H/s max: 61.6 H/s
[2018-04-08 11:19:38] new job from pool.supportxmr.com:8080 diff 5000
[2018-04-08 11:19:49] accepted (3/0) diff 5000 (1849 ms)
[2018-04-08 11:20:04] speed 2.5s/60s/15m 60.5 57.8 n/a H/s max: 61.6 H/s

check the timings ,!!!!!!donation is 99% and still doesnt donating after 1 min.there is no DEV DONATE STARTED!!!

here is config.json

    "algo": "cryptonight",  // cryptonight (default) or cryptonight-lite
    "av": 0,                // algorithm variation, 0 auto select
    "background": false,    // true to run the miner in the background
    "colors": true,         // false to disable colored output    
    "cpu-affinity": null,   // set process affinity to CPU core(s), mask "0x3" for cores 0 and 1
    "cpu-priority": null,   // set process priority (0 idle, 2 normal to 5 highest)
    "donate-level": 99,      // donate level, mininum 1%
    "log-file": null,       // log all output to a file, example: "c:/some/path/xmrig.log"
    "max-cpu-usage": 75,    // maximum CPU usage for automatic mode, usually limiting factor is CPU cache not this option.  
    "print-time": 60,       // print hashrate report every N seconds
    "retries": 5,           // number of times to retry before switch to backup server
    "retry-pause": 5,       // time to pause between retries
    "safe": false,          // true to safe adjust threads and av settings for current CPU
    "syslog": false,        // use system log for output messages
    "threads": null,        // number of miner threads
    "pools": [
        {
            "url": "pool.supportxmr.com:8080", // URL of mining server
            "user": "4BrL51JCc9NGQ71kWhnYoDRffsDZy7m1HUU7MRU4nUMXAHNFBEJhkTZV9HdaL4gfuNBxLPc3BeMkLGaPbF5vWtANQtLufzCXbL68Ge7mA5",           // username for mining server
            "pass": "x",                     // password for mining server
            "keepalive": true,               // send keepalived for prevent timeout (need pool support)
            "nicehash": false,               // enable nicehash/xmrig-proxy support
            "variant": -1                    // algorithm PoW variant
        }
    ],
    "api": {
        "port": 0,                             // port for the miner API https://github.com/xmrig/xmrig/wiki/API
        "access-token": null,                  // access token for API
        "worker-id": null                      // custom worker-id for API
    }
}

still thinks there is bug.!!!!
@xmrig 

## xmrig | 2018-04-08T13:21:04+00:00
You right it a bug, not so long time ago I [added](https://github.com/xmrig/xmrig/commit/673a1291e1342d2363dca1679b48dd22e7aa40fc) randomization to prevent waves if someone start a lot of miners simultaneity, it works fine for usual few % levels, but for levels like 99% donation never start.
Thank you.

## Gill1000 | 2018-04-08T13:43:04+00:00
So..you gonna fix this into 2.6 version ..right..????

## xmrig | 2018-04-08T15:23:02+00:00
Fixed, for level 99% donation starts after random time from 30 to 90 seconds, then will mine on donation pool for 99 minutes, after that switch to user pool for 1 minute and again 99 minutes... until miner closed.
Thank you.

## alfhg | 2018-04-09T06:51:44+00:00
I do see a bug in donation level in the newest release 2.6.0 beta CPU miner. But it's the other way. I set the donation level to 1% in both config.bat and start.cmd (I'm using the pre built windows binary). Then I saw a considerable drop in hash rate. It turned out the new binary release is ignoring my donation setting, and donating 2.5% instead. For every 200 minutes it would mine for dev for 5 min.

## alfhg | 2018-04-09T06:53:39+00:00
And is it true that donation level can never be below 1%? Or is there a way to set 0% donation in donate.h and custom build from source code?

## xmrig | 2018-04-13T22:16:12+00:00
Donation can't affect hashrate in any way and possible set level default level to 0.
Thank you.

# Action History
- Created by: Gill1000 | 2018-04-08T05:17:57+00:00
- Closed at: 2018-04-13T22:16:12+00:00
