---
title: xmrig stops working at suprnova pool
source_url: https://github.com/xmrig/xmrig/issues/221
author: calvintam236
assignees: []
labels: []
created_at: '2017-11-26T18:46:21+00:00'
updated_at: '2017-11-26T20:54:11+00:00'
type: issue
status: closed
closed_at: '2017-11-26T20:54:11+00:00'
---

# Original Description
I pointed my miners to suprnova pool, and today I notice errors: `connect error: "connection timed out` on `xmr-us.suprnova.cc:5222`, no hash rate reported at the miner ("n/a") or pool.

Original settings are: `nicehash=true`, and `keepalive=true`. This settings worked for months. Tried with either and both set to `false`. Tried port 5223 as well. I can ping the target domain, so I don't think it is a network issue.

Looks like some changes made on the pool side broke the `xmrig` connect ability.

# Discussion History
## xmrig | 2017-11-26T19:58:01+00:00
Looks like it pool issue, for me both us and eu servers no work, I also tried other miner. Same timeout issue.
Thank you.

## calvintam236 | 2017-11-26T20:52:04+00:00
Because the XMR pool still have ~850 kH/s, I don't think it is a pool issue.

## calvintam236 | 2017-11-26T20:54:11+00:00
Just tried `xmr.suprnova.cc:5222`, and it works.. I guess something wrong on their config.

# Action History
- Created by: calvintam236 | 2017-11-26T18:46:21+00:00
- Closed at: 2017-11-26T20:54:11+00:00
