---
title: Donation ERROR mining RTM on Flockpoll XMRig 6.16.3
source_url: https://github.com/xmrig/xmrig/issues/2910
author: ivanbalseirogarcia
assignees: []
labels:
- bug
created_at: '2022-01-30T22:02:07+00:00'
updated_at: '2025-06-16T20:00:10+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:00:10+00:00'
---

# Original Description
Dev Donate always rejects with "Invalid Params" error.

# Discussion History
## ivanbalseirogarcia | 2022-01-30T22:02:57+00:00
![Captura](https://user-images.githubusercontent.com/10364451/151719708-f673c9bb-94df-4464-8741-3a74c4a57dd1.PNG)


## ivanbalseirogarcia | 2022-01-30T22:18:32+00:00
config.json file:

"donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "donate.v2.xmrig.com:3333",
            "user": "YOUR_WALLET_ADDRESS",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        }
    ],

## xmrig | 2022-01-31T07:32:22+00:00
Fixed in the dev branch, but the miner update will be required to fix this issue.
Thank you.


## xmrig | 2022-02-04T10:37:36+00:00
https://github.com/xmrig/xmrig/releases/tag/v6.16.4

# Action History
- Created by: ivanbalseirogarcia | 2022-01-30T22:02:07+00:00
- Closed at: 2025-06-16T20:00:10+00:00
