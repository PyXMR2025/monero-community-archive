---
title: JSON-RPC always respond with http 200
source_url: https://github.com/monero-project/monero/issues/181
author: sammy007
assignees: []
labels: []
created_at: '2014-10-22T10:05:30+00:00'
updated_at: '2016-10-11T16:40:01+00:00'
type: issue
status: closed
closed_at: '2016-10-11T16:40:01+00:00'
---

# Original Description
```
< HTTP/1.1 200 Ok
* Server Epee-based is not blacklisted
< Server: Epee-based
< Content-Length: 105
< Content-Type: text/plain
< Last-Modified: Wed, 22 Oct 2014 09:27:39 GMT
< Accept-Ranges: bytes
<
{
  "error": {
    "code": -9,
    "message": "Core is busy."
  },
  "id": 0,
  "jsonrpc": "2.0"
* Connection #0 to host 127.0.0.1 left intact
}
```

Even "method not found"

```
< HTTP/1.1 200 Ok
* Server Epee-based is not blacklisted
< Server: Epee-based
< Content-Length: 113
< Content-Type: text/plain
< Last-Modified: Wed, 22 Oct 2014 09:55:00 GMT
< Accept-Ranges: bytes
<
{
  "error": {
    "code": -32601,
    "message": "Method not found"
  },
  "id": "",
  "jsonrpc": "2.0"
* Connection #0 to host 127.0.0.1 left intact
}⏎
```

I can't find any JSON-RPC over HTTP specs I can trust. Just think it's not good to always respond with 200. At least it's a good start to respond with **503 Service Unavailable** while daemon is flushing or not in sync yet.


# Discussion History
## ghost | 2016-10-06T01:55:18+00:00
Hi @sammy007 is this issue still present for you in 0.10.0 or can it be closed?


## sammy007 | 2016-10-11T16:40:01+00:00
Ah forgot to close, IIRC json-rpc always responds with 200.


# Action History
- Created by: sammy007 | 2014-10-22T10:05:30+00:00
- Closed at: 2016-10-11T16:40:01+00:00
