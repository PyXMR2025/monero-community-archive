---
title: API threads 404 - not found (
source_url: https://github.com/xmrig/xmrig/issues/1286
author: minzak
assignees: []
labels: []
created_at: '2019-11-14T01:49:42+00:00'
updated_at: '2019-11-23T11:21:51+00:00'
type: issue
status: closed
closed_at: '2019-11-23T11:21:51+00:00'
---

# Original Description
Very strange, but for API detail about threads - not answered, and in miner console put this:

```[2019-11-14 03:43:15.736] 127.0.0.1 GET /api/1/threads 404 289 "curl/7.64.0"```

And result is:
```
{
    "status": 404,
    "error": "Not Found"
}

```
But in summary threads is present:
```
...
   "hashrate": {
        "total": [83.71, 82.6, 77.05],
        "highest": 88.67,
        "threads": [
            [41.83, 41.28, 38.51],
            [41.87, 41.32, 38.53]
        ]
    },
    "hugepages": true
}
```

My API curls are:

```
curl -s -X GET -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" http://127.0.0.1:44444/1/summary
curl -s -X GET -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" http://127.0.0.1:44444/1/config
curl -s -X GET -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" http://127.0.0.1:44444/1/threads
```
Only last one not works.

# Discussion History
## xmrig | 2019-11-14T07:24:30+00:00
API docs outdated, this endpoint was replaced by `GET /2/backends` in v3.
Thank you,

## minzak | 2019-11-23T11:21:51+00:00
Thanks.

# Action History
- Created by: minzak | 2019-11-14T01:49:42+00:00
- Closed at: 2019-11-23T11:21:51+00:00
