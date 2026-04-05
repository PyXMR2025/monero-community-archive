---
title: Ability to pause/resume using the API?
source_url: https://github.com/xmrig/xmrig/issues/479
author: Duckbuster
assignees:
- xmrig
labels:
- enhancement
created_at: '2018-03-26T09:58:43+00:00'
updated_at: '2025-06-14T12:05:32+00:00'
type: issue
status: closed
closed_at: '2019-12-21T20:08:07+00:00'
---

# Original Description
Hi, I was wondering if there was a way to pause resume the miner using the Web API?
If not, could I ask for this enchancement?
Or is there some other way to pause/resume from an external script or program?
(using Linux)

Thanks

# Discussion History
## dunklesToast | 2018-03-26T13:14:36+00:00
No. Right now there is no direct way to control the miner over the API. I am also looking forward to this feature, so I can extend my XMRIG Frontend.

A little bit tricky (and I don't know if it would would) could be something like a nodeJS Script, which starts the miner via childprocress and then there is an API which just passes the Keypresses to the stdin from the childprocess. If I have time, I'll try that later this day :)

Or on Linux: Just kill the miner and restart it. Something like this:

stop.sh:
`killall xmrig`
start.sh
`screen -dmS xmrig /path/to/xmrig`


You could also wrap these commands into a PHP Script so you can control it via HTTP Requests. It's a very dirty way I believe but it should work

## FranzDE | 2018-03-28T17:02:15+00:00
you can use xmrigCC for manage all your clients
[https://github.com/Bendr0id/xmrigCC](https://github.com/Bendr0id/xmrigCC)

## xmrig | 2018-03-29T07:33:24+00:00
Scheduled to v2.6.
Thank you.

## xmrig | 2019-12-21T20:08:07+00:00
Implemented via JSON-RPC API `POST /json_rpc` with body `{"method":"pause","id":1}` or `{"method":"resume","id":1}`

## divinity76 | 2025-06-14T12:05:32+00:00
cmd/windows example:
```
xmrig --http-port=7681 --http-no-restricted --http-access-token=token
```
+
```
curl.exe -X POST http://localhost:7681/json_rpc -H "Content-Type: application/json" -H "Authorization: Bearer token" --data-raw "{\"method\":\"pause\",\"id\":1}"


curl.exe -X POST http://localhost:7681/json_rpc -H "Content-Type: application/json" -H "Authorization: Bearer token" --data-raw "{\"method\":\"resume\",\"id\":1}"
```

# Action History
- Created by: Duckbuster | 2018-03-26T09:58:43+00:00
- Closed at: 2019-12-21T20:08:07+00:00
