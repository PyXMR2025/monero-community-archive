---
title: Was more access to APIs than previous versions.
source_url: https://github.com/xmrig/xmrig/issues/526
author: sergneo
assignees: []
labels: []
created_at: '2018-04-09T06:12:39+00:00'
updated_at: '2018-11-05T14:50:17+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:22:39+00:00'
---

# Original Description
Now when you access via the api.json is too large access time (0.34 sec ), when hundreds of workers, this greatly slows the statistics, is it possible to do something quickly?
        "ipv6": false

XMRig 2.6.0-beta1
 built on Apr  3 2018 with MSVC 2017
 features: x86_64 AES-NI

libuv/1.19.0
libmicrohttpd/0.9.58

Windows 7 x64

# Discussion History
## xmrig | 2018-04-09T14:54:42+00:00
Since v2.6 http server run in main loop, it great for make API easy extensible, because don't need worry about thread synchronization. Same changes was made in proxy v2.5. But to reduce any possible negative impact to main loop I made some optimizations, so first request to API can take up to 200 ms, after that up to 25 ms, this values adjustable in source https://github.com/xmrig/xmrig/blob/dev/src/api/Httpd.h#L52

What do you use for monitoring? Proper software should fetch data in parallel.
Thank you.

## cupertank | 2018-04-10T14:01:14+00:00
I wrote a bot for these purposes.
https://t.me/Miner_checker_bot

# Action History
- Created by: sergneo | 2018-04-09T06:12:39+00:00
- Closed at: 2018-11-05T13:22:39+00:00
