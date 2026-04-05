---
title: Issue while mining SUGAR.. I am getting " stratum_recv_line failed. Please
  try again after 10 seconds
source_url: https://github.com/xmrig/xmrig/issues/2608
author: sachinvupparige
assignees: []
labels: []
created_at: '2021-09-28T00:29:20+00:00'
updated_at: '2025-06-20T11:10:50+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:10:50+00:00'
---

# Original Description
Issue while mining SUGAR.. I am getting " stratum_recv_line failed. Please try again after 10 seconds. I am trying to run XMrig proxy. Code used in CPUminer - "%~dp0"cpuminer-sse2.exe -a yespowerSUGAR -o 192.16.0.14:1111 -u sugar1q9k2y2kjhtwtzj0eu2zccw8357ewt36960m3rn3.sachinvs1.

And Code in XMRIG proxy - 
{
    "access-log-file": null,
    "api": {
         "port": 0,
         "access-token": null,
        "id": null,
        "worker-id": null,
        "ipv6": false,
        "restricted": true,
    },
    "background": false,
    "bind": [
            {
            "host": "0.0.0.0",
            "port": 1111,
            "tls": false
         },
    ],
    "colors": true,
    "custom-diff": 0,
    "donate-level": 0,
    "log-file": null,
    "mode": "simple",
    "pools": [
        {
            "url": "eu.rplant.Singapore:17042",
            "user": "sugar1q9k2y2kjhtwtzj0eu2zccw8357ewt36960m3rn3",
            "pass": "Sachinvupparige",
            "coin": "sugar", 
            "rig-id": null,
            "keepalive": false,
            "enabled": true,
            "tls": false,
        }
    ],
    "retries": 2,
    "retry-pause": 1,
    "reuse-timeout": 0,
    "tls": {
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "user-agent": null,
    "syslog": false,
    "verbose": false,
    "watch": true,
    "workers": true
}

Error keeps on going.. Any suggestion or FIX for this??

# Discussion History
## SChernykh | 2021-09-28T06:22:55+00:00
xmrig doesn't support this coin.

# Action History
- Created by: sachinvupparige | 2021-09-28T00:29:20+00:00
- Closed at: 2025-06-20T11:10:50+00:00
