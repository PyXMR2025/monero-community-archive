---
title: Miner not Re-connecting after connection loss
source_url: https://github.com/xmrig/xmrig/issues/1323
author: BKdilse
assignees: []
labels: []
created_at: '2019-11-27T18:51:45+00:00'
updated_at: '2021-04-12T15:27:23+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:27:23+00:00'
---

# Original Description
Hi,

Using XMRig v5, and when a network/internet connection to pool is lost, the miner doesn't get any shares accepted. I can see it hashing away, but nothing is accepted.

Connection loss is normally when I have to update the OS on the pool, and reboot it.

This occurs both internally (where pools are hosted), and externally over the internet.  I have a split DNS setup so internally the pool address resolves to a valid local IP.

A restart of the miner fixes the issue.

I am also using XLARig, which is a fork of v3.2, and that has no problems re-connecting.

Here is a copy of my config from a CPU machine:
```
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "randomx": {
        "init": -1,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "cn/gpu": [0, 1, 2, 3],
        "rx": [0, 1, 2, 3],
        "rx/wow": [0, 1, 2, 3],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": "arqma",
            "url": "arq.pool.gntl.co.uk:7777",
            "user": "MY_WALLET_REMOVED",
            "pass": "MY_WORKER_ID_REMOVED",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "self-select": null
        }
    ],
    "print-time": 60,
    "health-print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": null,
    "watch": true
}
```

# Discussion History
## xmrig | 2019-11-28T02:09:08+00:00
I unable to reproduce this issue, software or OS restart should cause network errors immediately, like `read error: "end of file"` and then `connect error: "connection refused"`.

Try enable `keepalive` it can be done on pool side https://xmrig.com/docs/extensions/keepalive
Thank you.

## BKdilse | 2019-11-28T09:06:40+00:00
Ok, I'll try and test this again and post more info.

Is there anything required on the pool side to enable keepalive?

## BKdilse | 2019-11-28T10:05:46+00:00
Re-tested this by restarting a pool, and the miner connects back fine.
Maybe it's a timing issue, if pool is down for longer than a certain amount of time?

I'll report back when I have more information.

Could you please expain the keepalive option, and what is required on the pool side, and then I will close this issue?

thanks @xmrig 

## xmrig | 2019-11-29T03:00:09+00:00
Sometimes connection is dead badly, for example when unplug ethernet cable, in this case applications didn't get any notification about it, without keepalive miner will know about it only after submit share + timeout for reply. With keepalive miner will check connection periodically, it can be faster that wait for next share.

You mention you have pool, so you can enable it on pool side (xmrig extension) but basic part should be supported by almost any pool software, but it require configure the miner.

Better leave this issue open, it can be part of bigger issue, for example #1306 another strange thing.
Thank you.





## BKdilse | 2019-11-29T06:03:25+00:00
Thanks, I'll leave this open.

I'm using nodejs-pool, by Snipa22.  I'll try the keep alive on the miner.

## BKdilse | 2019-11-30T13:23:39+00:00
Now testing the keepalive option, and I'll send feedback soon.

## BKdilse | 2019-11-30T17:22:47+00:00
Keepalive seems to have resolved the issue.  Will monitor further and feedback.

Thanks !

# Action History
- Created by: BKdilse | 2019-11-27T18:51:45+00:00
- Closed at: 2021-04-12T15:27:23+00:00
