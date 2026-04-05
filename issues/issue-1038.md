---
title: '[stratum+tcp://xx.xx.com:3333] read error: "end of file"'
source_url: https://github.com/xmrig/xmrig/issues/1038
author: garywu520
assignees: []
labels: []
created_at: '2019-06-20T04:27:55+00:00'
updated_at: '2019-08-26T01:48:29+00:00'
type: issue
status: closed
closed_at: '2019-08-02T13:15:25+00:00'
---

# Original Description
[stratum+tcp://xx.xx.com:3333] read error: "end of file"

# Discussion History
## ghost | 2019-08-26T01:13:37+00:00
i get [2019-08-25 18:09:41] [stratum+tcp://192.168.0.27:3333] connect error: "connection refused" and i don't know how to fix this my config file, im on mac os, i hope i gave enough info 
 `{
  "retry-pause": 5,
  "log-file": null,
  "colors": true,
  "pools": [
    {
      "variant": -1,
      "keepalive": false,
      "nicehash": false,
      "url": "stratum+tcp://192.168.0.27:3333",
      "pass": "your_password",
      "user": "47asQFxKNfceKDw7Pm27sYGw3wUXNdot9Na1KsEvSFxF8GGjqPvuf7x7vD4dQWa7uC8zSHCeYw1jUGoe8yZexRxPHiBBNve"
    }
  ],
  "threads": [
    {
      "affine_to_cpu": true,
      "worksize": 90,
      "intensity": 180,
      "index": 0
    }
  ],
  "donate-level": 1,
  "cpu-priority": 5,
  "background": false,
  "cpu-affinity": null,
  "print-time": 60,
  "retries": 5,
  "max-cpu-usage": 75
}`
and log 

`MacBook-Pro ~ % /xmrig/xmrig-amd ; exit;
 * ABOUT        XMRig-AMD/2.14.5 clang/10.0.0
 * LIBS         libuv/1.31.0 OpenCL/1.2 OpenSSL/1.0.2s microhttpd/0.9.63 
 * CPU          Intel(R) Core(TM) i5-7360U CPU @ 2.30GHz x64 AES
 * ALGO         cryptonight, donate=1%
 * POOL #1      stratum+tcp://192.168.0.27:3333 variant auto
 * COMMANDS     hashrate, pause, resume
[2019-08-25 18:09:35] compiling code and initializing GPUs. This will take a while...
[2019-08-25 18:09:35] #00, GPU #00 Intel(R) Iris(TM) Plus Graphics 640, i:180 (90/256), si:2/2, u:8, cu:48
[2019-08-25 18:09:35]              0.35/0.38/2 GB
[2019-08-25 18:09:35] [stratum+tcp://192.168.0.27:3333] read error: "end of file"
[2019-08-25 18:09:41] [stratum+tcp://192.168.0.27:3333] connect error: "connection refused"
[2019-08-25 18:09:43] Ctrl+C received, exiting

[Process completed]`
edit on 192.168.0.27 im running node cryptonote pool on Ubuntu 18.04.3 LTS 

log 

pool@pool-VirtualBox:~/pool$ node init.js
2019-08-25 18:44:51 [master] Pool spawned on 1 thread(s)
2019-08-25 18:44:54 [unlocker] Started
2019-08-25 18:44:54 [payments] Started
2019-08-25 18:44:54 [unlocker] No blocks candidates in redis
2019-08-25 18:44:54 [payments] No workers' balances reached the minimum payment threshold
2019-08-25 18:44:54 [api] API started & listening on port 8117
2019-08-25 18:44:54 [api] Stat collection finished: 592 ms redis, 659 ms daemon
2019-08-25 18:44:55 [api] Broadcasting to 0 visitors and 0 address lookups
2019-08-25 18:45:01 [api] Stat collection finished: 5 ms redis, 1229 ms daemon
2019-08-25 18:45:01 [api] Broadcasting to 0 visitors and 0 address lookups
2019-08-25 18:45:01 [pool] (Thread 1) New block to mine at height 1402165 w/ difficulty of 27729277746
2019-08-25 18:45:01 [pool] (Thread 1) Started server listening on port 3333
2019-08-25 18:45:01 [pool] (Thread 1) Started server listening on port 7777

TypeError: buffArray.reverse is not a function
    at Object.getTargetHex (/home/pool/pool/lib/pool.js:288:19)
    at Object.getJob (/home/pool/pool/lib/pool.js:305:27)
    at handleMinerMethod (/home/pool/pool/lib/pool.js:514:28)
    at handleMessage (/home/pool/pool/lib/pool.js:648:13)
    at Socket.<anonymous> (/home/pool/pool/lib/pool.js:702:25)
    at emitOne (events.js:96:13)
    at Socket.emit (events.js:188:7)
    at readableAddChunk (_stream_readable.js:176:18)
    at Socket.Readable.push (_stream_readable.js:134:10)
    at TCP.onread (net.js:548:20)

2019-08-25 18:45:03 [master] Pool fork 1 died, spawning replacement worker...
2019-08-25 18:45:06 [api] Stat collection finished: 3 ms redis, 16 ms daemon
2019-08-25 18:45:06 [api] Broadcasting to 0 visitors and 0 address lookups
2019-08-25 18:45:13 [api] Stat collection finished: 3 ms redis, 2436 ms daemon
2019-08-25 18:45:13 [api] Broadcasting to 0 visitors and 0 address lookups
2019-08-25 18:45:13 [pool] (Thread 1) New block to mine at height 1402185 w/ difficulty of 27565858059
2019-08-25 18:45:13 [pool] (Thread 1) Started server listening on port 3333
2019-08-25 18:45:13 [pool] (Thread 1) Started server listening on port 7777

TypeError: buffArray.reverse is not a function
    at Object.getTargetHex (/home/pool/pool/lib/pool.js:288:19)
    at Object.getJob (/home/pool/pool/lib/pool.js:305:27)
    at handleMinerMethod (/home/pool/pool/lib/pool.js:514:28)
    at handleMessage (/home/pool/pool/lib/pool.js:648:13)
    at Socket.<anonymous> (/home/pool/pool/lib/pool.js:702:25)
    at emitOne (events.js:96:13)
    at Socket.emit (events.js:188:7)
    at readableAddChunk (_stream_readable.js:176:18)
    at Socket.Readable.push (_stream_readable.js:134:10)
    at TCP.onread (net.js:548:20)

2019-08-25 18:45:14 [master] Pool fork 1 died, spawning replacement worker...

config file 

{
    "coin": "monero",
    "symbol": "XMR",

    "logging": {
        "files": {
            "level": "info",
            "directory": "logs",
            "flushInterval": 5
        },
        "console": {
            "level": "info",
            "colors": true
        }
    },

    "poolServer": {
        "enabled": true,
        "clusterForks": "auto",
        "poolAddress": "47asQFxKNfceKDw7Pm27sYGw3wUXNdot9Na1KsEvSFxF8GGjqPvuf7x7vD4dQWa7uC8zSHCeYw1jUGoe8yZexRxPHiBBNve",
        "blockRefreshInterval": 1000,
        "minerTimeout": 900,
        "ports": [
            {
                "port": 3333,
                "difficulty": 100,
                "desc": "Low end hardware"
            },
            {
                "port": 7777,
                "difficulty": 10000,
                "desc": "High end hardware"
            }
        ],
        "varDiff": {
            "minDiff": 2,
            "maxDiff": 100000,
            "targetTime": 100,
            "retargetTime": 30,
            "variancePercent": 30,
            "maxJump": 100
        },
        "shareTrust": {
            "enabled": true,
            "min": 10,
            "stepDown": 3,
            "threshold": 10,
            "penalty": 30
        },
        "banning": {
            "enabled": false,
            "time": 600,
            "invalidPercent": 25,
            "checkThreshold": 30
        },
        "slushMining": {
            "enabled": false,
            "weight": 300,
            "blockTime": 60,
            "lastBlockCheckRate": 1
        }
    },

    "payments": {
        "enabled": true,
        "interval": 600,
        "maxAddresses": 50,
        "mixin": 3,
        "transferFee": 5000000000,
        "minPayment": 100000000000,
        "denomination": 100000000000
    },

    "blockUnlocker": {
        "enabled": true,
        "interval": 30,
        "depth": 60,
        "poolFee": 2,
        "devDonation": 0.1,
        "coreDevDonation": 0.1
    },

    "api": {
        "enabled": true,
        "hashrateWindow": 600,
        "updateInterval": 5,
        "port": 8117,
        "blocks": 30,
        "payments": 30,
        "password": "your_password"
    },

    "daemon": {
        "host": "127.0.0.1",
        "port": 18081
    },

    "wallet": {
        "host": "127.0.0.1",
        "port": 8082
    },

    "redis": {
        "host": "127.0.0.1",
        "port": 6379,
        "auth": null
    }
}

# Action History
- Created by: garywu520 | 2019-06-20T04:27:55+00:00
- Closed at: 2019-08-02T13:15:25+00:00
