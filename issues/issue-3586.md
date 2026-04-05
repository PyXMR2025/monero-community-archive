---
title: Zephyr (v2) solo mine to daemon "Invalid block template received from daemon"
source_url: https://github.com/xmrig/xmrig/issues/3586
author: toy1111
assignees: []
labels: []
created_at: '2024-11-17T20:17:11+00:00'
updated_at: '2025-06-30T05:05:20+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:29:27+00:00'
---

# Original Description
I think the issue with solo mining Zephyr has returned and seeing a few others on their Discord experiencing it also. I'm using the Windows MSVC compiled xmrig 6.22.2 and connecting to a local Zephyr 2.0.1 daemon,
![20241117 xmrig-6 22 2 template error](https://github.com/user-attachments/assets/ac023f93-8c89-412d-9e9a-468114a3b88a)

My json.config pools section below. Xmrig did automatically add/save the last 3 daemon settings and shortened the coin to "ZEPH". And based on the original issue solo mining to daemon I left algo null and populated coin: "zephyr" to overcome xmrig using the monero (rx/0) template.
"pools": [
        {
            "algo": null,
            "coin": "ZEPH",
            "url": "192.168.0.52:17767",
            "user": "ZEPHYR_wallet_address_xxxxxxxxxxxxxxxxxxxxxxx",
            "enabled": true,
            "tls": false,
            "sni": false,
            "tls-fingerprint": null,
            "daemon": true,
            "socks5": null,
            "daemon-poll-interval": 1000,
            "daemon-job-timeout": 15000,
            "daemon-zmq-port": -1
        }
    ],

I tried several older version of xmrig, as well as tried xmrig-proxy 6.22.0 - same template error. Zephyr had major update on the Sept 29th, possible cause solo mining to daemon to break?


# Discussion History
## toy1111 | 2025-06-30T05:05:20+00:00
This doesn't appear to be completed/fixed. Tested newest XMRig (6.24.0) and get same Invalid block template error when trying to solo mine to a local daemon. The Zephyr project has had more updates but not sure if those affect the block template like the one September last year.

# Action History
- Created by: toy1111 | 2024-11-17T20:17:11+00:00
- Closed at: 2025-06-28T10:29:27+00:00
