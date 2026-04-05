---
title: Rejected - Low difficulty share - TRTL on v 2.5.2 and 2.6
source_url: https://github.com/xmrig/xmrig/issues/529
author: 4Reallive
assignees: []
labels: []
created_at: '2018-04-09T11:44:50+00:00'
updated_at: '2018-07-11T06:32:48+00:00'
type: issue
status: closed
closed_at: '2018-04-10T02:16:33+00:00'
---

# Original Description
 * VERSIONS:     XMRig/2.5.2 libuv/1.8.0 gcc/5.4.0
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz (2) x64 AES-NI
 * CPU L2/L3:    8.0 MB/40.0 MB
 * THREADS:      29, cryptonight-lite, av=1, donate=5%
 * POOL #1:      geo.atpool.party:8888
 * COMMANDS:     hashrate, pause, resume
[2018-04-09 11:01:51] use pool geo.atpool.party:8888 198.251.81.71
[2018-04-09 11:01:51] new job from geo.atpool.party:8888 diff 80000
[2018-04-09 11:02:07] rejected (0/1) diff 80000 "Low difficulty share" (177 ms)
[2018-04-09 11:02:20] new job from geo.atpool.party:8888 diff 27586
[2018-04-09 11:02:23] new job from geo.atpool.party:8888 diff 27586
[2018-04-09 11:02:26] new job from geo.atpool.party:8888 diff 27586
[2018-04-09 11:02:28] rejected (0/2) diff 27586 "Low difficulty share" (172 ms)
[2018-04-09 11:02:32] Ctrl+C received, exiting

* VERSIONS:     XMRig/2.6.0-beta1 libuv/1.19.2 gcc/5.4.0
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz (2) x64 AES-NI
 * CPU L2/L3:    8.0 MB/40.0 MB
 * THREADS:      29, cryptonight-lite, av=1, donate=5%
 * POOL #1:      geo.atpool.party:8888
 * COMMANDS:     hashrate, pause, resume
[2018-04-09 11:23:34] use pool geo.atpool.party:8888 198.251.81.71
[2018-04-09 11:23:34] new job from geo.atpool.party:8888 diff 80000
[2018-04-09 11:23:52] rejected (0/1) diff 80000 "Low difficulty share" (173 ms)
[2018-04-09 11:23:54] new job from geo.atpool.party:8888 diff 40000
[2018-04-09 11:23:58] rejected (0/2) diff 40000 "Low difficulty share" (171 ms)
[2018-04-09 11:24:03] Ctrl+C received, exiting

# Discussion History
## 4Reallive | 2018-04-09T11:45:51+00:00
Seems to be lots of people having this issue in the TRTL mining discord channel

On the plus side it mines SUMO great. Thank you.

## xmrig | 2018-04-09T11:51:30+00:00
Please read #482 for TRTL, change `algo` is not enough.
Thank you.

## 4Reallive | 2018-04-09T11:58:16+00:00
Thank you very much for such a quick response

The variant is set to 1
What else needs to change?
I also tried auto which selects av=2.. Also doesn't work

{
    "algo": "cryptonight-lite",  // cryptonight (default) or cryptonight-lite
    "av": 1,                     // algorithm variation, 0 auto select
    "background": false,    // true to run the miner in the background
    "colors": true,         // false to disable colored output    
    "donate-level": 5,      // donate level, mininum 1%
    "log-file": null,       // log all output to a file, example: "c:/some/path/xmrig.log"
    "max-cpu-usage": 100,   // maximum CPU usage for automatic mode, usually limiting factor is CPU cache not this option.  
    "print-time": 60,       // print hashrate report every N seconds
    "retries": 5,           // number of times to retry before switch to backup server
    "retry-pause": 5,       // time to pause between retries
    "syslog": false,        // use system log for output messages
    "threads": null,        // number of miner threads
    "pools": [
        {
            "url": "geo.atpool.party:7777", // URL of mining server
            "user": "TRTLuzj8yzQ6ZZ5skStmeQALGpnUxtgN7dmm1V1egkYycoB7hnidC4RCn2ZxgiqDSZDoV8wmiXgqBQvNcsegnwM2HQkeFtoSycU",
            "keepalive": false,               // send keepalived for prevent timeout (need pool support)
            "nicehash": false,               // enable nicehash/xmrig-proxy support
        }
        ]
}



## 4Reallive | 2018-04-09T12:03:18+00:00
Oh just heads up the recommended solution on the discord is to switch to xmrstak

but i like your product much better for CPU mining.

## xmrig | 2018-04-09T12:04:05+00:00
`"variant": 1` should set on each pool, it not same as old option `av`.
```json
"pools": [
{
    "url": "geo.atpool.party:7777", // URL of mining server
    "user":         "TRTLuzj8yzQ6ZZ5skStmeQALGpnUxtgN7dmm1V1egkYycoB7hnidC4RCn2ZxgiqDSZDoV8wmiXgqBQvNcsegnwM2HQkeFtoSycU",
    "keepalive": false, // send keepalived for prevent timeout (need pool support)
    "nicehash": false, // enable nicehash/xmrig-proxy support,
    "variant": 1
}
]
```

## 4Reallive | 2018-04-09T12:05:15+00:00
Excellent, i will share the information. Thank you.

(after testing of course)

## 4Reallive | 2018-04-10T02:16:33+00:00
Works great, although i am seeing a problem with a high percentage of nodes dropping half their potential hashing power over time.
Reboot fixes it, will torubleshoot on BETA 2.6 and report if it continues.

This one is SOLVED

## crackwei | 2018-07-09T18:00:45+00:00
hello,i running xmr-stak 2.4.5 b3f79de3.
and xmrig-proxy 2.6.3
xmr-stak's pools txt set "turtlecoin"
and xmrig-proxy config set:

"algo": "cryptonight-lite",
...
"pools": [
        {
            "url": "trtl.pool.mine2gether.com:3335",
            "user": "TRTLuyJDumYJ6MuMQXosUaVRUYNkGxyhsUj7JxPA723545UiuQqZMhWwTt1GM4S2TJd6Bng7Jf5PgV6LYDevCuVd31vjFaAf8r.20000",
            "pass": "proxy:trtl@xxx.com",
            "rig-id": null,
            "keepalive": true,
            "variant": 1
        }
    ],

but it always shonwn "Result rejected by the pool." on xmr-stak console.
what happen and how to solove?



## xmrig | 2018-07-09T18:51:13+00:00
Probably you not enable nicehash in pools.txt `"use_nicehash" : true,` if it not help, press `r` in xmr-stak console and show output.
Thank you.

## crackwei | 2018-07-09T19:44:39+00:00
i set nicehash,it's no problem. this is the report:

RESULT REPORT
Difficulty       : 20000
Good results     : 0 / 8 (0.0 %)
Avg result time  : 7.4 sec
Pool-side hashes : 0

Top 10 best results found:
|  0 |                0 |  1 |                0 |
|  2 |                0 |  3 |                0 |
|  4 |                0 |  5 |                0 |
|  6 |                0 |  7 |                0 |
|  8 |                0 |  9 |                0 |

Error details:
| Count | Error text                       | Last seen           |
|     8 | Incorrect algorithm              | 2018-07-10 03:43:35 |

## crackwei | 2018-07-09T19:48:15+00:00
this is the pools.txt setting:

"pool_list" :
[
	{"pool_address" : "f.edog.online:7788", "wallet_address" : "test", "rig_id" : "", "pool_password" : "x", "use_nicehash" : true, "use_tls" : false, "tls_fingerprint" : "", "pool_weight" : 1 },
],

"currency" : "turtlecoin",




this is the xmrig-proxy setting:

 "access-log-file": null,
    "algo": "cryptonight-lite",
    "api": {
        "port": 0,
        "access-token": null,
        "worker-id": null,
        "ipv6": true,
        "restricted": true
    },
    "background": false,
    "bind": [
        "0.0.0.0:7788",
        "[::]:7788"
    ],
    "colors": true,
    "custom-diff": 0,
    "donate-level": 0,
    "log-file": null,
    "mode": "nicehash",
    "pools": [
        {
            "url": "trtl.pool.mine2gether.com:3335",
            "user": "TRTLuyJDumYJ6MuMQXosUaVRUYNkGxyhsUj7JxPA7hjTYCrUiuQqZMhWwTt1GM4S2TJd6Bng7Jf5PgV6LYDevCuVd31vjFaAf8r.20000",
            "pass": "proxy:trtl@edog.online",
            "rig-id": null,
            "keepalive": true,
            "variant": 1
        }
    ],
    "retries": 2,
    "retry-pause": 1,
    "reuse-timeout": 0,
    "user-agent": null,
......

## crackwei | 2018-07-09T19:56:28+00:00
xmr-stak can be direct mine from pool,it's no problem.but when i through xmrig-proxy to mine,it  it always shown "Result rejected by the pool." 

## xmrig | 2018-07-10T07:44:50+00:00
@crackwei If you use only xmr-stak as miner as temporary solution you can set `"variant": 0` in proxy config, because xmr-stak send wrong algorithm name, also I open issue in xmr-stak repository.
Thank you.

## crackwei | 2018-07-11T06:32:48+00:00
it can be work now,thank you.

# Action History
- Created by: 4Reallive | 2018-04-09T11:44:50+00:00
- Closed at: 2018-04-10T02:16:33+00:00
