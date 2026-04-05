---
title: SOS,how to config 5.0?
source_url: https://github.com/xmrig/xmrig/issues/1330
author: smzwsz
assignees: []
labels: []
created_at: '2019-11-29T13:26:59+00:00'
updated_at: '2019-12-22T19:40:08+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:40:08+00:00'
---

# Original Description
I used xmrig-proxy.

Here is my xmrig config.json:

"cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "max-threads-hint": 50,
        "asm": true,
        "argon2-impl": null,
        "cn/0": false,
        "cn-lite/0": false
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
    
"donate-level": 5,
    
"donate-over-proxy": 1,
    
"log-file": null,
    
"pools": [
        {
            "algo": null,
            "coin": "monero",
            "url": "hk01.supportxmr.com:3333",
            "user": "YOUR_WALLET_ADDRESS",
            "pass": "x",
            "rig-id": null,
            "nicehash": true,
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

That's something wrong.how to config it?

# Discussion History
## SChernykh | 2019-11-29T14:12:43+00:00
It's probably a typo somewhere. Try to use https://xmrig.com/wizard

# Action History
- Created by: smzwsz | 2019-11-29T13:26:59+00:00
- Closed at: 2019-12-22T19:40:08+00:00
