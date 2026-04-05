---
title: please add SSL support
source_url: https://github.com/xmrig/xmrig/issues/573
author: aleqx
assignees: []
labels:
- enhancement
created_at: '2018-04-22T01:34:00+00:00'
updated_at: '2018-09-22T06:01:12+00:00'
type: issue
status: closed
closed_at: '2018-09-22T06:01:12+00:00'
---

# Original Description
It would be really nice to add SSL support. A lot of pools support it and a lot of miners use it and are using xmr-stak instead (which supports SSL).

I haven't looked at your code, but depending on how you're using sockets then grafting in libssl could be pretty easy (gives you a file descriptor to pass around).

# Discussion History
## enwillyado | 2018-04-23T23:26:20+00:00
You can use SSL in my pre-release: https://github.com/enwillyado/xmrig/releases/tag/VW-3.4.0-6

## xmrig | 2018-09-22T06:01:12+00:00
SSL/TLS will be available in next v2.8 release #758.
Thank you.

# Action History
- Created by: aleqx | 2018-04-22T01:34:00+00:00
- Closed at: 2018-09-22T06:01:12+00:00
