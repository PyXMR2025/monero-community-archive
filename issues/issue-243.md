---
title: config server failover
source_url: https://github.com/xmrig/xmrig/issues/243
author: warcries
assignees: []
labels: []
created_at: '2017-12-07T02:51:12+00:00'
updated_at: '2017-12-07T04:27:02+00:00'
type: issue
status: closed
closed_at: '2017-12-07T04:27:02+00:00'
---

# Original Description
hi guys,

how can I setup a server failover on config.json?

Sample config:

"pools": [
        {
            "url": "crypto01.server.com:443",   // URL of mining server
            "user": "asdf",                        // username for mining server
            "pass": "x",                       // password for mining server
            "keepalive": true,                 // send keepalived for prevent timeout (need pool support)
            "nicehash": false                  // enable nicehash/xmrig-proxy support
        }
    ],
// How do I add another sever failover here? Thanks in advance guys.

# Discussion History
## xmrig | 2017-12-07T04:27:01+00:00
Please check this comment https://github.com/xmrig/xmrig/issues/90#issuecomment-327483294
Thank you.

# Action History
- Created by: warcries | 2017-12-07T02:51:12+00:00
- Closed at: 2017-12-07T04:27:02+00:00
