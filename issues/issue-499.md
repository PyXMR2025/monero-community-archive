---
title: HTTP Daemon failed to start
source_url: https://github.com/xmrig/xmrig/issues/499
author: babyrig
assignees: []
labels:
- bug
created_at: '2018-04-04T13:11:06+00:00'
updated_at: '2018-04-06T18:20:17+00:00'
type: issue
status: closed
closed_at: '2018-04-06T18:20:17+00:00'
---

# Original Description
I have this error on start in version 2.5.2 and in this beta anyone more have this issue ?


* VERSIONS:     XMRig/2.6.0-beta1 libuv/1.8.0 gcc/7.1.0
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Xeon(R) CPU           E5620  @ 2.40GHz (2) x64 -AES-NI
 * CPU L2/L3:    4.0 MB/24.0 MB
 * THREADS:      12, cryptonight, av=3, donate=5%
 * POOL #1:      failover.xmrig.com:443
 * API BIND:     [::]:6000
 * COMMANDS:     hashrate, pause, resume
[2018-04-04 10:08:29] HTTP Daemon failed to start.
[2018-04-04 10:08:30] use pool failover.xmrig.com:443 108.61.164.63


# Discussion History
## Pasha49 | 2018-04-04T13:49:36+00:00
+1
same problem
on version 2.4.4 works without errors

## xmrig | 2018-04-04T14:55:36+00:00
What OS do you use? maybe IPv6 not available on your system, try disable it via option `"ipv6": false,` in `api` section. This option only available for 2.6.0-beta1. Thank you.

```json
    "api": {
        "port": 600,
        "access-token": "TOKEN",
        "worker-id": null,
        "ipv6": false,
        "restricted": true
    },
```

## babyrig | 2018-04-04T15:21:47+00:00
I am running with Hive OS (Ubuntu 16.04) like you said ipv6 are disabled by default in the OS but default version are now 2.5.2.

Worked fine in the beta, any tip to make 2.5.2 to work ?

## xmrig | 2018-04-04T15:41:42+00:00
In 2.5.2 only possible if edit source and recompile https://github.com/xmrig/xmrig/blob/master/src/api/Httpd.cpp#L55 3 lines (55-57) should removed.
Thank you.

## sergneo | 2018-04-04T19:52:17+00:00
WindowsXP 32bit
 * API BIND:     [::]:8888
 * COMMANDS:     hashrate, pause, resume
[2018-04-04 22:51:03] HTTP Daemon failed to start.


## xmrig | 2018-04-04T19:55:33+00:00
I will disable IPv6 for API by default in next versions.
Thank you.

## Pasha49 | 2018-04-05T06:59:27+00:00
> In 2.5.2 only possible if edit source and recompile https://github.com/xmrig/xmrig/blob/master/src/api/Httpd.cpp#L55 3 lines (55-57) should removed.

It works, thanks!

## xmrig | 2018-04-06T18:20:17+00:00
Start from v2.6.0-beta2 IPv6 will be disabled by default.

# Action History
- Created by: babyrig | 2018-04-04T13:11:06+00:00
- Closed at: 2018-04-06T18:20:17+00:00
