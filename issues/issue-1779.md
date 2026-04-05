---
title: '"Connection reset by peer" - No Active Pools Mining'
source_url: https://github.com/xmrig/xmrig/issues/1779
author: parsemehard
assignees: []
labels:
- question
created_at: '2020-07-14T15:11:31+00:00'
updated_at: '2022-02-04T04:06:58+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:39:31+00:00'
---

# Original Description
**Describe the bug**
"Connection reset by peer" - No Active Pools Mining

**To Reproduce**
Relaunch the program - contained errors. Have tried multiple pools, rebooted, reinstalled windows.

**Expected behavior**
To connect to the pool to start mining.

**Required data**
 - Log of the Program:
[2020-07-14 10:08:26.721]  miner    speed 10s/60s/15m 4726.2 3159.9 n/a H/s max 4763.1 H/s
[2020-07-14 10:08:33.434]  net      xmr.2miners.com:2222 read error: "connection reset by peer"
[2020-07-14 10:08:33.434]  net      no active pools, stop mining
[2020-07-14 10:08:38.917]  net      use pool xmr.2miners.com:2222  51.89.96.41
[2020-07-14 10:08:38.917]  net      new job from xmr.2miners.com:2222 diff 120001 algo rx/0 height 2142165
[2020-07-14 10:09:00.975]  net      xmr.2miners.com:2222 read error: "connection reset by peer"
[2020-07-14 10:09:00.976]  net      no active pools, stop mining
[2020-07-14 10:09:07.073]  net      use pool xmr.2miners.com:2222  51.89.96.41
[2020-07-14 10:09:07.073]  net      new job from xmr.2miners.com:2222 diff 120001 algo rx/0 height 2142165
[2020-07-14 10:09:09.617]  net      xmr.2miners.com:2222 read error: "connection reset by peer"
[2020-07-14 10:09:09.618]  net      no active pools, stop mining
[2020-07-14 10:09:15.121]  net      use pool xmr.2miners.com:2222  51.89.96.41
[2020-07-14 10:09:15.121]  net      new job from xmr.2miners.com:2222 diff 120001 algo rx/0 height 2142165
[2020-07-14 10:09:15.166]  net      xmr.2miners.com:2222 read error: "connection reset by peer"
[2020-07-14 10:09:15.166]  net      no active pools, stop mining
[2020-07-14 10:09:21.158]  net      use pool xmr.2miners.com:2222  51.89.96.41
[2020-07-14 10:09:21.158]  net      new job from xmr.2miners.com:2222 diff 120001 algo rx/0 height 2142165
[2020-07-14 10:09:27.993]  miner    speed 10s/60s/15m 4629.7 2853.5 n/a H/s max 4763.1 H/s
[2020-07-14 10:09:52.704]  net      xmr.2miners.com:2222 read error: "connection reset by peer"
[2020-07-14 10:09:52.705]  net      no active pools, stop mining
[2020-07-14 10:09:58.406]  net      use pool xmr.2miners.com:2222  51.89.96.41
[2020-07-14 10:09:58.407]  net      new job from xmr.2miners.com:2222 diff 120001 algo rx/0 height 2142165
[2020-07-14 10:10:06.817]  net      xmr.2miners.com:2222 read error: "connection reset by peer"
[2020-07-14 10:10:06.818]  net      no active pools, stop mining

 - Config file or command line (without wallets)
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
    "title": true,
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 1],
            [1, 3],
            [1, 12],
            [1, 14],
            [1, 16],
            [1, 18],
            [1, 20],
            [1, 22],
            [1, 13],
            [1, 15]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 12],
            [1, 14],
            [1, 16],
            [1, 18]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 15],
            [1, 16],
            [1, 17],
            [1, 18],
            [1, 19],
            [1, 20],
            [1, 21],
            [1, 22],
            [1, 23]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15],
            [2, 16],
            [2, 17],
            [2, 18],
            [2, 19],
            [2, 20],
            [2, 21],
            [2, 22],
            [2, 23]
        ],
        "rx": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        "cn/0": false,
        "cn-lite/0": false,
        "kawpow": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
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
            "coin": null,
            "url": "xmr.2miners.com:2222",
            "user": "REDACTEDs",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null
        }
    ],
    "print-time": 60,
    "health-print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true
}
 - For GPU related issues: information about GPUs and driver version.
Only using CPU



# Discussion History
## xmrig | 2020-07-14T15:22:45+00:00
It network issue, connection to the pool blocked somehow, try other pools preferable with TLS support.
Thank you.

## Omkar2340 | 2022-02-04T04:06:58+00:00
Help me with it 
![16439475666272639234895989875755](https://user-images.githubusercontent.com/98999573/152470123-3b66eb0b-da3f-455f-8205-bb14a5614e9d.jpg)


# Action History
- Created by: parsemehard | 2020-07-14T15:11:31+00:00
- Closed at: 2020-08-28T16:39:31+00:00
