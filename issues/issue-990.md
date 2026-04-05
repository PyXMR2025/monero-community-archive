---
title: 'nicehash: read error: "end of file"'
source_url: https://github.com/xmrig/xmrig/issues/990
author: ShaddyR
assignees: []
labels:
- question
created_at: '2019-03-14T12:27:32+00:00'
updated_at: '2019-08-02T11:57:45+00:00'
type: issue
status: closed
closed_at: '2019-08-02T11:57:45+00:00'
---

# Original Description
Periodically miner gets this error
> read error: "end of file"

Version no matter - it was with 2.8.x and earlier, server both old cryptonightv8 and new cryptonightr @ any location. So there is no work, it's iddle like that:
__________________________________
[2019-03-14 14:17:24] [cryptonightr.eu.nicehash.com:3375] read error: "end of fi
le"
[2019-03-14 14:17:25] [cryptonightr.usa.nicehash.com:3375] read error: "end of f
ile"
[2019-03-14 14:17:39] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2019-03-14 14:18:39] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2019-03-14 14:19:39] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2019-03-14 14:20:39] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2019-03-14 14:21:39] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2019-03-14 14:22:39] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2019-03-14 14:23:39] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
How to fix it? Thank you.


# Discussion History
## xmrig | 2019-03-14T14:20:32+00:00
Network issue, this error mean remote party closed connection.
Thank you.

## ShaddyR | 2019-03-14T21:39:51+00:00
Hm... what kind of issue is it? I got the error @ different PC with different inet providers. Any network soft works fine, no problem seen, just miner. What decision can you advice?

# Action History
- Created by: ShaddyR | 2019-03-14T12:27:32+00:00
- Closed at: 2019-08-02T11:57:45+00:00
