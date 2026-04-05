---
title: Low hashrate , dont understand at all XMRig configs
source_url: https://github.com/xmrig/xmrig/issues/298
author: Estebantr
assignees: []
labels:
- question
created_at: '2017-12-26T20:48:01+00:00'
updated_at: '2018-03-14T22:50:19+00:00'
type: issue
status: closed
closed_at: '2018-03-14T22:50:19+00:00'
---

# Original Description
{
    "algo": "cryptonight",  // cryptonight (default) or cryptonight-lite
    "av": 0,                // algorithm variation, 0 auto select
    "background": false,    // true to run the miner in the background
    "colors": true,         // false to disable colored output    
    "cpu-affinity": null,   // set process affinity to CPU core(s), mask "0x3" for cores 0 and 1
    "cpu-priority": null,   // set process priority (0 idle, 2 normal to 5 highest)
    "donate-level": 1,      // donate level, mininum 1%
    "log-file": null,       // log all output to a file, example: "c:/some/path/xmrig.log"
    "max-cpu-usage": 80,    // maximum CPU usage for automatic mode, usually limiting factor is CPU cache not this option.  
    "print-time": 60,       // print hashrate report every N seconds
    "retries": 5,           // number of times to retry before switch to backup server
    "retry-pause": 5,       // time to pause between retries
    "safe": false,          // true to safe adjust threads and av settings for current CPU
    "threads": null,        // number of miner threads
    "pools": [
        {
            "url": "pool.monerominepool.com:3333",   // URL of mining server
            "user": "4A24k6GZgSw5fBsQkTgt6aSNzkDn9AekLAVrtfu52ba5UtyNjcmCTSR5YSP7bLTD9sYmoxuJ5NEggT339U88T3yU7mZ8R8V",                        // username for mining server
            "pass": "x",                       // password for mining server
            "keepalive": true,                 // send keepalived for prevent timeout (need pool support)
            "nicehash": false                  // enable nicehash/xmrig-proxy support
        }
    ],
    "api": {
        "port": 0,                             // port for the miner API https://github.com/xmrig/xmrig/wiki/API
        "access-token": null,                  // access token for API
        "worker-id": null                      // custom worker-id for API
    }
}


with that config i only do like 80-99H/s . (i7 4700MQ 3.4ghz)

how can i improve that , with XMR stak i used to do like 600 or less .



# Discussion History
## TheUnity | 2017-12-27T07:02:37+00:00
xmr-stak using gpu too

## xmrig | 2017-12-28T07:55:16+00:00
This CPU should do about 150 or so with 3 threads, please make sure huge pages enabled and other heavy applications is closed.
600 only possible with GPU.
Thank you.

## davwheat | 2018-01-03T12:42:52+00:00
For me, my GPU gets about 80 H/s and my CPU 110 H/s... I have a 970 and an i3 8100 so I don't think that should be right. Can you enlighten me?

## ZachE84 | 2018-01-10T18:18:13+00:00
Same performance problem. Config file overly complicated and not very flexible.

# Action History
- Created by: Estebantr | 2017-12-26T20:48:01+00:00
- Closed at: 2018-03-14T22:50:19+00:00
