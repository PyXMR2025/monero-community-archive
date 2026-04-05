---
title: Backup pool using the same user and pass of the primary one
source_url: https://github.com/xmrig/xmrig/issues/398
author: ghost
assignees: []
labels: []
created_at: '2018-02-12T10:08:25+00:00'
updated_at: '2018-02-12T11:12:53+00:00'
type: issue
status: closed
closed_at: '2018-02-12T11:12:53+00:00'
---

# Original Description
How i can make xmrig connect to the same pool but on another port in case the first port is not availible

# Discussion History
## ghost | 2018-02-12T11:12:35+00:00
Successfully made it
`xmrig -o <pool:port1> -o <pool:port2> -o <pool:port3> -u <user> -p <pass> [other options]`

# Action History
- Created by: ghost | 2018-02-12T10:08:25+00:00
- Closed at: 2018-02-12T11:12:53+00:00
