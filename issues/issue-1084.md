---
title: rejected (0/1) diff 10345 "Low difficulty share" (222 ms)
source_url: https://github.com/xmrig/xmrig/issues/1084
author: seanwhe
assignees: []
labels:
- duplicate
created_at: '2019-07-29T13:42:59+00:00'
updated_at: '2019-07-29T13:56:31+00:00'
type: issue
status: closed
closed_at: '2019-07-29T13:56:24+00:00'
---

# Original Description
$ uname -a
Linux sean-work-wks 4.15.0-55-generic #60-Ubuntu SMP Tue Jul 2 18:22:20 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux

````````````
$ xmrig -V
XMRig 2.99.2-beta
 built on Jul 29 2019 with GCC 7.4.0
 features: 64-bit AES

libuv/1.18.0
OpenSSL/1.1.1
hwloc/1

````````````

Starting from config file
$ xmrig --config=config.json

when the following is NOT present:
	    "variant": -1,

Produces error:
[2019-07-29 15:16:48.723] rejected (0/1) diff 10345 "Low difficulty share" (222 ms)

when the following IS present:
	    "variant": -1,

Produces error:
[2019-07-29 15:25:06.460] rejected (0/7) diff 10000 "Incorrect hashing protocol in use.  Please upgrade/fix your miner" (180 ms)
[2019-07-29 15:25:06.639] [pool.supportxmr.com:5555] error: "Low difficulty share", code: -1

when the following IS present:
	    "variant": 1,

Produces error:
[2019-07-29 15:31:22.365] "config.json" was changed, reloading configuration
[2019-07-29 15:31:30.854] rejected (0/16) diff 10000 "Incorrect hashing protocol in use.  Please upgrade/fix your miner" (180 ms)
[2019-07-29 15:31:31.034] [pool.supportxmr.com:5555] error: "Low difficulty share", code: -1

Testing to see if the problem is because nicehash is set true
when the following IS present:
            "nicehash": false,
	    "variant": 1,

Produced error:
[2019-07-29 15:38:27.832] rejected (0/21) diff 10000 "Low difficulty share" (237 ms)
[2019-07-29 15:38:52.128] rejected (0/22) diff 10000 "Incorrect hashing protocol in use.  Please upgrade/fix your miner" (181 ms)
[2019-07-29 15:38:52.307] [pool.supportxmr.com:5555] error: "Low difficulty share", code: -1

when the following IS present:
            "nicehash": false,
	    "variant": -1,

Produced error:
[2019-07-29 15:40:50.192] "config.json" was changed, reloading configuration
[2019-07-29 15:42:10.972] rejected (0/23) diff 10000 "Incorrect hashing protocol in use.  Please upgrade/fix your miner" (181 ms)
[2019-07-29 15:42:11.154] [pool.supportxmr.com:5555] error: "Low difficulty share", code: -1

`````````````````
$ cat config.json 
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": true,
        "host": "192.168.1.11",
        "port": 8080,
        "access-token": null,
        "restricted": false
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
            0,
            1,
	    2
        ]
    },
    "donate-level": 5,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": "cryptonight",
            "url": "pool.supportxmr.com:5555",
            "user": "854sqm2Cm4TB2XgPHWqSPSbnFAe3SMzdEDzZHpukQ8NHBPFropbnkFmEKiZPgwjMFC9PTjaFscR2UU6ZwFCqJzGMUiZVbTM",
            "pass": "wks-jhb-lin-11:user@example.com",
            "rig-id": "wks-jhb-lin-11",
            "nicehash": true,
	    "variant": -1,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false
        }
    ],
    "print-time": 30,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": "null",
    "watch": true
}


# Discussion History
## xmrig | 2019-07-29T13:56:24+00:00
Duplicate #1083 

# Action History
- Created by: seanwhe | 2019-07-29T13:42:59+00:00
- Closed at: 2019-07-29T13:56:24+00:00
