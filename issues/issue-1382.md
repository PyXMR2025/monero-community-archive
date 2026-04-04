---
title: 'Request: Report uptime with monerod status'
source_url: https://github.com/monero-project/monero/issues/1382
author: ghost
assignees: []
labels: []
created_at: '2016-11-26T23:01:20+00:00'
updated_at: '2017-01-13T22:30:46+00:00'
type: issue
status: closed
closed_at: '2017-01-13T22:30:46+00:00'
---

# Original Description
Potentially interesting and useful for people running nodes

# Discussion History
## ghost | 2016-11-27T12:43:05+00:00
I can see it being quite simple to implement, if there's a global timer available somewhere. Does anyone know if that's a thing? 

Just log the daemon startup time and then do a little calculation every time someone calls `monerod status`.

# Action History
- Created by: ghost | 2016-11-26T23:01:20+00:00
- Closed at: 2017-01-13T22:30:46+00:00
