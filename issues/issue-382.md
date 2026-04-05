---
title: 'Improvements: Remote configure options through API'
source_url: https://github.com/xmrig/xmrig/issues/382
author: hgs81
assignees: []
labels:
- enhancement
created_at: '2018-02-02T14:19:11+00:00'
updated_at: '2019-08-02T12:14:21+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:14:21+00:00'
---

# Original Description
I would like to add some REST API to set options on-the-fly remotely.
Something like this:
curl -X POST -F "pools.url=xxx" -F "pools.user=xxx" -F "pools.pass=xxx" http://localhost:8080/set_config
Or:
curl -X POST -F "donate-level=5%" -F "max-cpu-usage=80" -F "threads=4" http://localhost:8080/set_config

# Discussion History
## RansomFuck | 2018-02-12T22:30:16+00:00
Read xmrigCC thread

## hgs81 | 2018-02-12T22:37:34+00:00
Can you send me link please?

## xmrig | 2019-08-02T12:14:20+00:00
Recent versions can change config via API in JSON format.
Thank you.

# Action History
- Created by: hgs81 | 2018-02-02T14:19:11+00:00
- Closed at: 2019-08-02T12:14:21+00:00
