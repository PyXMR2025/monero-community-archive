---
title: Release v2.6.3 does not work with latest haven fork
source_url: https://github.com/xmrig/xmrig/issues/693
author: acca
assignees: []
labels: []
created_at: '2018-06-14T09:12:57+00:00'
updated_at: '2018-06-14T11:19:51+00:00'
type: issue
status: closed
closed_at: '2018-06-14T11:19:51+00:00'
---

# Original Description
Just installed release v2.6.3 but I got bad shares from the pool mining haven protocol. I'm using https://cryptoknight.cc/haven/#. Cannot understand if it is a pool issue or a miner one?

# Discussion History
## postalman | 2018-06-14T09:22:27+00:00
Same Thing. Its not autoswitching and cn-heavy/xhv doesnt work. non of heavy algo works for XHV

## xmrig | 2018-06-14T09:57:09+00:00
Haven forked and changed PoW, so you need change `variant` option to `"variant": "xhv"`
Key options:
```json
{
    "algo": "cryptonight-heavy",
    "pools": [
        {
            "url": "haven.ingest.cryptoknight.cc:5831",
            "variant": "xhv"
        }
    ]
}
```

@postalman Autoswitching between `cn-heavy` and `cn-heavy/xhv` not possible if pool not support this feature. With config above and v2.6.3 anything should work fine.
Thank you.

## postalman | 2018-06-14T10:09:11+00:00
Thanks. Now its works.

## acca | 2018-06-14T11:19:51+00:00
Many Thanks, it is working also for me now.

# Action History
- Created by: acca | 2018-06-14T09:12:57+00:00
- Closed at: 2018-06-14T11:19:51+00:00
