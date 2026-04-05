---
title: logs are not working
source_url: https://github.com/xmrig/xmrig/issues/410
author: fireheadman
assignees: []
labels: []
created_at: '2018-02-22T08:45:21+00:00'
updated_at: '2018-11-05T12:53:41+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:53:41+00:00'
---

# Original Description
OSX version, 
miner is running on macmini.   The log gets 1 line of input and stops logging.

Trying to use `tail -f <logfile>`

```
[fireheadman@hostname logs]$ tail -f monero.log
[2018-02-22 01:44:22] speed 2.5s/60s/15m 43.5 43.7 n/a H/s max: 45.6 H/s
00

ity=0x5
64 AES-NI
```

# Discussion History
## enwillyado | 2018-02-26T22:07:48+00:00
A standard implementation using std iostream are implemented in:
https://github.com/enwillyado/xmrig/commit/86f0d9d944b99eb1fd20a4e4be32a92388450e90#diff-fe21862032a22a919410f85011c2fe73

# Action History
- Created by: fireheadman | 2018-02-22T08:45:21+00:00
- Closed at: 2018-11-05T12:53:41+00:00
