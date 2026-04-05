---
title: Help randomx ?
source_url: https://github.com/xmrig/xmrig/issues/1237
author: ghost
assignees: []
labels:
- question
created_at: '2019-10-12T12:48:40+00:00'
updated_at: '2019-10-13T11:07:43+00:00'
type: issue
status: closed
closed_at: '2019-10-13T11:07:43+00:00'
---

# Original Description
Can you explain and let me understand about this configuration.

`
"randomx": {
        "init": -1,
        "numa": true
    },
`

# Discussion History
## xmrig | 2019-10-12T13:30:14+00:00
`init` number of threads for initialize RandomX dataset, -1 means auto (all threads).
`numa` Allow miner use use dataset on each NUMA node, usable for complex hardware, eg multi socket servers.

# Action History
- Created by: ghost | 2019-10-12T12:48:40+00:00
- Closed at: 2019-10-13T11:07:43+00:00
