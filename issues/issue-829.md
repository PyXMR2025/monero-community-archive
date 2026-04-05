---
title: 'Low hashrate on i7-4790 CPU '
source_url: https://github.com/xmrig/xmrig/issues/829
author: irevanescence
assignees: []
labels: []
created_at: '2018-10-20T13:58:23+00:00'
updated_at: '2018-11-05T15:07:12+00:00'
type: issue
status: closed
closed_at: '2018-11-05T15:07:12+00:00'
---

# Original Description
i have 3 pc with same config .(i7-4790 CPU ) and xmrig 2.8.3
two of them are windows 7 and last one is windows 10.

Windows 7 hashrates : speed 10s/60s/15m 93.4 93.8 n/a H/s max 94.8 H/s

on windows 10 : speed 10s/60s/15m 295.6 293.9 290.4 H/s max 296.1 H/s

would you please help me or give me an idea.

all PC are fresh installed . 
Regards

# Discussion History
## AndreySerg | 2018-10-20T18:40:45+00:00
A hashrate drop is expected with the new CN2 algo.

## irevanescence | 2018-10-20T19:02:32+00:00
The problem is same config same HW and big diff on hashrate.
Just different OS.


## 2010phenix | 2018-10-20T19:16:30+00:00
same https://github.com/xmrig/xmrig/issues/823

## pr0vieh | 2018-10-20T20:13:13+00:00
hugepages active ? at both Windows Versions ? Run As Admin and restart Your PC

## irevanescence | 2018-10-20T20:16:40+00:00
Yes.memory hugepage is active. Different pool checked. I did all of them .i hope fix in next versions.

## NmxMilk | 2018-10-22T12:51:07+00:00
Post your config file,  mainly number of threads and cpu-affinity which may be the issue.

## irevanescence | 2018-10-22T15:33:45+00:00
> Post your config file, mainly number of threads and cpu-affinity which may be the issue.

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
    "cpu-priority": 1,
    "donate-level": 1,
    "huge-pages": true,
    "hw-aes": "intel",
    "log-file": "log.txt",
    "max-cpu-usage": 75,
    "pools": [
        {
            "url": "51.15.65.182:14433",
            "user": "",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "variant": -1,
            "tls": true,
            "tls-fingerprint": null
        },
        {
            "url": "xmr-eu2.nanopool.org:14433",
            "user": "",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "variant": -1,
            "tls": true,
            "tls-fingerprint": null
        },
        {
            "url": "xmr-asia1.nanopool.org:14433",
            "user": "",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "variant": -1,
            "tls": true,
            "tls-fingerprint": null
        },
        {
            "url": "xmr-us-east1.nanopool.org:14433",
            "user": "",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "variant": -1,
            "tls": true,
            "tls-fingerprint": null
        },
        {
            "url": "xmr-us-west1.nanopool.org:14433",
            "user": "",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "variant": -1,
            "tls": true,
            "tls-fingerprint": null
        }
    ],
    "print-time": 10,
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
        
    ],
    "user-agent": null,
    "watch": false
}

## irevanescence | 2018-10-22T15:35:41+00:00
i still have problem. in windows 10 i have 280H/S and in windows 7 is around 100H/S.
dear developers would you please check it.
The config file is same .
the HW is exactly same.
the net connection is same .

in previous version of xmrig i had 300H/S even in windows 7.

## NmxMilk | 2018-10-22T20:12:34+00:00
try this in your config:
delete the thread array in your config and try something as simple as:
"cpu-affinity" : "0xAA",
"threads" : 4,

This assumes you have 8 threads (CUs) enabled in your bios.
You should check your cpu usage to verify what is going on. With the config i give you should have 4 CUs at 100% out of the eight and always the same.

And yes, you should be squeezing at least 280 Hs out of it.



# Action History
- Created by: irevanescence | 2018-10-20T13:58:23+00:00
- Closed at: 2018-11-05T15:07:12+00:00
