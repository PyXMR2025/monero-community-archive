---
title: unknown algorithm make sure you set algo or coin while trying to mine  safex
  cash. Please help
source_url: https://github.com/xmrig/xmrig/issues/2607
author: sachinvupparige
assignees: []
labels: []
created_at: '2021-09-26T13:15:26+00:00'
updated_at: '2025-06-20T11:11:01+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:11:01+00:00'
---

# Original Description
Hi guys, I am trying to connect few miners to my proxy and mine SFX.. code as follows.. CODE IN MY XMRIG-PROXY----

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
            "port": 3333,
            "tls": false
        },
        {
            "host": "0.0.0.0",
            "port": 2222,
            "tls": false
        },
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
            "url": "pool.safex.org:4411",
            "user": "Safex5zB6iZN8dAcDGPHCQCmiKvjoA5sdDUeKpRecSSNKNW1k7G4dUV7epDiav6RLjNNtQhYFUHH1fhgWavzXR9fBb9AbBoZUsU4F",
            "pass": "sachinvs",
            "rig-id": null,
            "keepalive": false,
            "variant": 4,
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

and code in Miner is  ----   CODE IN XMRIG MINER----

cd %~dp0
xmrig.exe -o 192.16.0.36:3333 -u Safex5zB6iZN8dAcDGPHCQCmiKvjoA5sdDUeKpRecSSNKNW1k7G4dUV7epDiav6RLjNNtQhYFUHH1fhgWavzXR9fBb9AbBoZUsU4F -p x    pause

getting error 
Unknown algorithm, make sure you set "algo" or "coin option" Login error code 6....

Can any one tell me whats wrong here.. tired of trying the possibalities.

# Discussion History
## Spudz76 | 2021-09-26T14:32:17+00:00
Safex is not mapped as a coin option.  Use only the direct selection of `algo: "rx/sfx"`

Should also work with both coin/algo just left as `null` since pool only sends `rx/sfx` jobs and miner will automatically follow.

# Action History
- Created by: sachinvupparige | 2021-09-26T13:15:26+00:00
- Closed at: 2025-06-20T11:11:01+00:00
