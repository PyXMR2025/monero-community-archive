---
title: Minergate issue Procedure not found
source_url: https://github.com/xmrig/xmrig/issues/83
author: Afapa
assignees: []
labels: []
created_at: '2017-09-01T22:11:19+00:00'
updated_at: '2017-09-02T00:41:48+00:00'
type: issue
status: closed
closed_at: '2017-09-02T00:41:48+00:00'
---

# Original Description
Hello, im getting this issue "code": -32601, "message": "Procedure not found." then timeout error, when i mining via xmr.pool.minergate.com:45560, this issue happens sometimes, so i'm losing my h/s while xmrig trying to decide this problem... It doesn't happens on same pc when i'm mining via minemonero.

# Discussion History
## xmrig | 2017-09-02T00:40:22+00:00
minergate doesn't support keepalived method (ping pool if miner long time not submit shares), remove `-k` command line option or set `"keepalive": false,` in config file.
Thank you.

## Afapa | 2017-09-02T00:41:48+00:00
Thank you :)

# Action History
- Created by: Afapa | 2017-09-01T22:11:19+00:00
- Closed at: 2017-09-02T00:41:48+00:00
