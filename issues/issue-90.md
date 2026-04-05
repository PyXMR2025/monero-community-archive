---
title: config.json
source_url: https://github.com/xmrig/xmrig/issues/90
author: boymafia
assignees: []
labels:
- question
created_at: '2017-09-05T07:53:25+00:00'
updated_at: '2018-03-14T22:41:37+00:00'
type: issue
status: closed
closed_at: '2018-03-14T22:41:37+00:00'
---

# Original Description
Hi,

I'd like to know how to configure more mine URL in config.json file.

Thanks!

# Discussion History
## xmrig | 2017-09-06T13:29:31+00:00
Like that:
```
    "pools": [
        {
            "url": "pool.minemonero.pro:5555",
            "user": "",
            "pass": "x",
            "keepalive": true,
            "nicehash": false
        },
       {
            "url": "failover.pool",
            "user": "",
            "pass": "x",
            "keepalive": true,
            "nicehash": false
        }
    ]
```
Syntax standard JSON array, first element will be primary pool, any others are backup pools.
Thank you.

## Jh0nW1cK | 2017-10-02T16:24:22+00:00
Adding another pool in config.json gives me this error: [pool.xxxxxx.com:5555] "No login / password especified", code -1 
Never connect to the primary pool, connect to the backup pool.

## Jh0nW1cK | 2017-10-03T16:32:10+00:00
It was my fault, I solved it

## davidenoto | 2017-11-20T12:20:45+00:00
hi!
I want change URL pool with MoneroOcean, but "config.json:1260: Invalid escape character in string.
No pool URL supplied. Exiting."
the URL is gulf.moneroocean.stream:80
Help me

## xmrig | 2017-11-27T00:29:21+00:00
Please show your config.

# Action History
- Created by: boymafia | 2017-09-05T07:53:25+00:00
- Closed at: 2018-03-14T22:41:37+00:00
