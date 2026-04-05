---
title: how do I change difficulty in xmrig 3.0
source_url: https://github.com/xmrig/xmrig/issues/1123
author: radioice104
assignees: []
labels:
- question
created_at: '2019-08-17T19:18:41+00:00'
updated_at: '2019-09-28T17:50:04+00:00'
type: issue
status: closed
closed_at: '2019-09-28T17:50:03+00:00'
---

# Original Description
Is there any way to change the difficulty ?
I know for previous version it worked with wallet+diff
but it is not longer working.
Thanks!

# Discussion History
## xmrig | 2019-08-17T19:30:57+00:00
It depends of pool (how it parse user string) miner just sent it as is, so it version independent.
Thank you.

## radioice104 | 2019-08-17T19:35:57+00:00
I am using nanopool mining monero.
I have sent them a question as well.
I want to change it because of low shares.
Thanks for quick reply!

## xmrig | 2019-08-17T19:45:12+00:00
https://help.nanopool.org/article/59-pool-information `Share difficulty is static and equal to 120000` you can't change it, but you probably not set option `"algo":"cn/r",` for this pool, global option `algo` removed.

## radioice104 | 2019-08-17T19:48:50+00:00
I have set it to "cn/r" indeed.
If I have to leave it as default(null) I get this error: 
[xmr-eu1.nanopool.org:14444] Unknown/unsupported algorithm "(null)" detected, reconnect
[2019-08-17 22:47:09.002] [xmr-eu1.nanopool.org:14444] login error code: 6

which one should I set it or just remove that algo line?

## xmrig | 2019-08-17T20:02:59+00:00
Please show config file, wallet address can be omitted and miner output from start as text or screenshot.
Thank you.

## radioice104 | 2019-08-17T20:10:07+00:00
```json
{
    "api": {
        "id": null,
        "worker-id": "mize"
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
        "asm": true,
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 12],
            [1, 14],
            [1, 16],
            [1, 18],
            [1, 20],
            [1, 22],
            [1, 24],
            [1, 26],
            [1, 28],
            [1, 30]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 8],
            [1, 10],
            [1, 16],
            [1, 18],
            [1, 24],
            [1, 26]
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
            [1, 23],
            [1, 24],
            [1, 25],
            [1, 26],
            [1, 27],
            [1, 28],
            [1, 29],
            [1, 30],
            [1, 31]
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
            [2, 23],
            [2, 24],
            [2, 25],
            [2, 26],
            [2, 27],
            [2, 28],
            [2, 29],
            [2, 30],
            [2, 31]
        ],
        "cn/gpu": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        "rx": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": "cn/r",
            "url": "xmr-eu1.nanopool.org:14444",
            "user": "wallet address",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": null,
    "watch": true
}
```
![xmrig 3](https://user-images.githubusercontent.com/47594544/63216848-1d98c980-c144-11e9-942e-48a3549805d0.jpg)


## xmrig | 2019-08-17T20:41:58+00:00
Config and output looks good, anything should work fine.

## radioice104 | 2019-08-17T20:43:38+00:00
Thank you!
Have a great weekend!

## expressups | 2019-08-19T04:12:42+00:00
    "max-cpu-usage": 50,
How should arrays be set？

## xmrig | 2019-09-28T17:50:03+00:00
`max-cpu-usage` option reverted back in v4.2 with new name, please read docs carefully https://github.com/xmrig/xmrig/blob/beta/doc/CPU_MAX_USAGE.md

# Action History
- Created by: radioice104 | 2019-08-17T19:18:41+00:00
- Closed at: 2019-09-28T17:50:03+00:00
