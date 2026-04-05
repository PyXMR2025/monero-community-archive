---
title: '"invalid block template received from daemon" when solomining ArQmA'
source_url: https://github.com/xmrig/xmrig/issues/3691
author: WaltVinegar
assignees: []
labels: []
created_at: '2025-08-04T11:19:50+00:00'
updated_at: '2025-08-04T14:38:35+00:00'
type: issue
status: closed
closed_at: '2025-08-04T14:38:35+00:00'
---

# Original Description
Set up [config.json]:
    "pools": [
		{
            "algo": "rx/arq",
            "coin": "arqma",
            "url": "127.0.0.1:19994",
            "user": "WALLET ADDRESS",
            "pass": null,
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "sni": false,
            "tls-fingerprint": null,
            "daemon": true,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        },
]

I'm fully synched up and the address/port settings match the daemon. I've even scrubbed the settings and used the configurator. Still the same response: "Invalid block template received from daemon."

# Discussion History
## SChernykh | 2025-08-04T11:25:10+00:00
Solo mining is fully supported only for Monero and Wownero.

## WaltVinegar | 2025-08-04T14:38:23+00:00
> Solo mining is fully supported only for Monero and Wownero.

Well that explains it; thought I was going mad. Thanks.

# Action History
- Created by: WaltVinegar | 2025-08-04T11:19:50+00:00
- Closed at: 2025-08-04T14:38:35+00:00
