---
title: config for silent active time and idle time
source_url: https://github.com/xmrig/xmrig/issues/3383
author: DARK-DEVIL-66
assignees: []
labels: []
created_at: '2023-12-16T14:21:08+00:00'
updated_at: '2025-06-18T22:26:58+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:26:58+00:00'
---

# Original Description
{
    "autosave": true,
    "cpu": true,
    "opencl": false,
    "background": true,
    "cuda": false,
    "pools": [
        {
            "coin": "monero",
            "algo": "rx/0",
            "url": "http://212.213.9.0:8888",
            "user": "your_user",
            "pass": "x",
            "tls": true,
            "keepalive": true,
            "nicehash": false
        }
    ],
    "donate": 0,                // Set the donation level to 0
    "max-cpu-usage": 20,        // Set the maximum CPU usage during active time
    "cpu-usage-percent": 80     // Set the CPU usage during idle time
}


it's correct for active time 20% max cpu and idle time 80% cpu ? or wrong ?

# Discussion History
## SlavisaBakic | 2023-12-17T22:57:03+00:00
"priority": 1
in CPU section might be better choice. It shouldn't slow down active work because xmrig will run at lower priority and when you are idle/AFK xmrig will run at full speed.

# Action History
- Created by: DARK-DEVIL-66 | 2023-12-16T14:21:08+00:00
- Closed at: 2025-06-18T22:26:58+00:00
