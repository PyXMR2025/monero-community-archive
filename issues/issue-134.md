---
title: Add more pools
source_url: https://github.com/xmrig/xmrig/issues/134
author: Jh0nW1cK
assignees: []
labels:
- question
created_at: '2017-10-02T07:57:43+00:00'
updated_at: '2018-07-01T03:06:33+00:00'
type: issue
status: closed
closed_at: '2017-10-02T11:59:38+00:00'
---

# Original Description
Good morning, 
how can I add another pool in the config.json file in case the first one fails? 
Thank you.

# Discussion History
## xmrig | 2017-10-02T11:50:08+00:00
Something like that:
```json
    "pools": [
        {
            "url": "primary:5555",
            "user": "",
            "pass": "x",
            "keepalive": true,
            "nicehash": false
        },
        {
            "url": "backup:5555",
            "user": "",
            "pass": "x",
            "keepalive": true,
            "nicehash": false
        }
    ]
```

## xmrig | 2017-10-02T11:59:38+00:00
Duplicate #90

## Jh0nW1cK | 2017-10-02T16:19:23+00:00
Adding another pool in config.json gives me this error: [pool.xxxxxx.com:5555] "No login / password especified", code -1 
Never connect to the primary pool, connect to the backup pool.

## Jh0nW1cK | 2017-10-03T16:31:54+00:00
It was my fault, I solved it

## sailei00 | 2018-07-01T03:06:33+00:00
xmrig always connect to the broken primary pool ,never try to connect the backup pool. why

# Action History
- Created by: Jh0nW1cK | 2017-10-02T07:57:43+00:00
- Closed at: 2017-10-02T11:59:38+00:00
