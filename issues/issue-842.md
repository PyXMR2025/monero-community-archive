---
title: ' "Incorrect hashing protocol in use.  Please upgrade/fix your miner"'
source_url: https://github.com/xmrig/xmrig/issues/842
author: omidnavy
assignees: []
labels:
- question
created_at: '2018-10-24T06:43:01+00:00'
updated_at: '2021-04-14T08:42:08+00:00'
type: issue
status: closed
closed_at: '2018-10-28T08:42:03+00:00'
---

# Original Description
Hi
I can't use xmrig anymore since the new update.
Already downloaded the latest release and also compiled the code but the result is this:
 "Incorrect hashing protocol in use.  Please upgrade/fix your miner"
or
"error: "Low difficulty share"

So whats going on here ?

# Discussion History
## 2010phenix | 2018-10-24T13:27:21+00:00
nothing special @omidnavy - just use search button and you question will gone.

## xmrig | 2018-10-25T07:11:19+00:00
At least config or log/screenshot required.
Thank you.

## krumblez | 2018-10-25T14:46:58+00:00
I am getting the same with 2.8.3 on pool.supportxrm.com - whatever difficulty I set 

![image](https://user-images.githubusercontent.com/11175971/47508911-e2ec3a80-d86c-11e8-8ac1-7470129df993.png)

--

my config is:

{
    "algo": "cryptonight",
    "api": {
        "port": 0,
        "access-token": null,
        "id": null,
        "worker-id": null,
        "ipv6": false,
        "restricted": true
    },
    "asm": true,
    "autosave": true,
    "av": 0,
    "background": false,
    "colors": true,
    "cpu-affinity": null,
    "cpu-priority": null,
    "donate-level": 1,
    "huge-pages": true,
    "hw-aes": null,
    "log-file": null,
    "max-cpu-usage": 65,
    "pools": [
        {
            "url": "pool.supportxmr.com:5555",
            "user": "463tWEBn5XZJSxLU6uLQnQ2iY9xuNcDbjLSjkn3XAXHCbLrTTErJrBWYgHJQyrCwkNgYvyV3z8zctJLPCZy24jvb3NiTcTJ.d079df2b9d6f4873b873dbd624b5d7614eee4faf473a45bc902e2bb283600cb1",
            "pass": "LittleBlu",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "variant": 1,
            "tls": false,
            "tls-fingerprint": null
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "safe": false,
    "threads": [
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        }
    ],
    "user-agent": null,
    "watch": false
}

-

I hope this info helps :) 

I will watch for updates so can start mining again. Thank you!

## krumblez | 2018-10-25T14:55:36+00:00
Ok, quick update... I used the cold config.json file, I just copied across to new miner..

So I then used the config in 2.8.3 and added details.. It works now..

Maybe this is the same instance for the other user with protocol mining errors :)

Thank you for the miner, keep up the good work!

## xmrig | 2018-10-25T14:57:10+00:00
supportxmr doesn't support algorithm protocol negotiation, so you should set `"variant": -1,"`, current value `1` is cryptonight variant 1 also known as cryptonight v7.
Thank you.

## NaikDK | 2021-04-13T05:59:48+00:00
Hi,
I am facing similar issue and variant value is -1 itself.
please find below my config.

{
    "algo": "cryptonight",
    "api": {
        "port": 0,
        "access-token": null,
        "id": null,
        "worker-id": null,
        "ipv6": false,
        "restricted": true
    },
    "background": false,
    "colors": true,
    "cuda-bfactor": 6,
    "cuda-bsleep": 25,
    "cuda-max-threads": 64,
    "donate-level": 1,
    "log-file": null,
    "pools": [
        {
            "url": "monerohash.com:7777",
            "user": "49E1tmUFVg4BUPSZCBpEqJgkUb59M6utrPETpSU9nhjYFjFepEqZgPNd8rPByR9PAzFUYbG5ArkjoW5iUDx9tWZ5H4snQir",
            "pass": "Darhk:deepknaik642@gmail.com",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "variant": -1,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "threads": [
        {
            "index": 0,
            "threads": 4,
            "blocks": 40,
            "bfactor": 8,
            "bsleep": 25,
            "sync_mode": 3,
            "affine_to_cpu": false
        }
    ],
    "user-agent": null,
    "syslog": false,
    "watch": true
}

## SChernykh | 2021-04-13T06:38:01+00:00
@NaikDK use https://xmrig.com/wizard to create new config, this one looks like from an ancient version.

## NaikDK | 2021-04-13T07:02:00+00:00
I tried creating the config but it seems there are some issues in the pool's config.
Your config link will set the config for XMRig while I am using XMRig-Nvidia.
@SChernykh can you please help me out here?

## NaikDK | 2021-04-14T08:22:31+00:00
@xmrig Please help

## xmrig | 2021-04-14T08:40:31+00:00
Current Monero algorithm is RandomX, this is not a cryptonight variant, you can't use XMRig-Nvidia for it. Seems you missed a lot and need to do research again.
Thank you.

## NaikDK | 2021-04-14T08:42:08+00:00
@xmrig Can you please suggest any website fr the same?

# Action History
- Created by: omidnavy | 2018-10-24T06:43:01+00:00
- Closed at: 2018-10-28T08:42:03+00:00
