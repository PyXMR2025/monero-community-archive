---
title: Api Json restitution Bug
source_url: https://github.com/xmrig/xmrig/issues/419
author: I28ko
assignees: []
labels:
- bug
created_at: '2018-02-28T18:44:33+00:00'
updated_at: '2018-07-09T21:02:50+00:00'
type: issue
status: closed
closed_at: '2018-07-09T21:02:50+00:00'
---

# Original Description
Hello !

First of all, i want to thank the devs for this great mining application <3

And before i describe my issue, here is my configuration : 
- 1 worker is running xmrig-amd (worker A)
- 2 workers are running xmrig : 1 with running 4 thread (worker B), and 1 other with 20 (worker C).
- all are running under a Ubuntu server edition 16.10 LTS

I'm trying to get json informations with a NodeJS/Express stack. Every json seems to be correct if i use my browser.In node, Worker A & B seems to throw a correct response, but i had an error with my worker C. When i'm trying to JSON.parse() the response, i had a json error and when i throw it directly on my page without parsing i obtain a string like this : 

`41.04, 0.0, 0.0 ], [ 42.98, 0.0, 0.0 ], [ 42.08, 0.0, 0.0 ], [ 41.66, 0.0, 0.0 ], [ 42.1, 0.0, 0.0 ], [ 41.77, 0.0, 0.0 ], [ 41.1, 0.0, 0.0 ], [ 41.29, 0.0, 0.0 ], [ 37.55, 0.0, 0.0 ], [ 38.83, 0.0, 0.0 ], [ 43.03, 0.0, 0.0 ], [ 41.51, 0.0, 0.0 ], [ 41.21, 0.0, 0.0 ] ] }, "results": { "diff_current": 5000, "shares_good": 1, "shares_total": 1, "avg_time": 17, "hashes_total": 5000, "best": [ 6753, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], "error_log": [] }, "connection": { "pool": "XX.XX.XX.XX:YYYY", "uptime": 17, "ping": 125, "failures": 0, "error_log": [] } }`

The begin of the json seem to be troncated (maybe because of the 20 running thread) and to avoid this error, i had to comment the line 207 in https://github.com/xmrig/xmrig/blob/master/src/api/ApiState.cpp

Thank you and i'm sorry for my poor english level 

# Discussion History
## xmrig | 2018-03-01T02:33:22+00:00
API output was truncated like this issue #290?
Thank you.

## xmrig | 2018-03-01T03:06:28+00:00
Unfortunately I can't reproduce this issue, but can you please check replace line https://github.com/xmrig/xmrig/blob/master/src/api/ApiState.cpp#L202 to `threads.PushBack(thread.Move(), allocator);`
Thank you.

## I28ko | 2018-03-01T08:43:55+00:00
> API output was truncated like this issue #290?

It's seems broken at the same place, in threads array

> can you please check replace line https://github.com/xmrig/xmrig/blob/master/src/api/ApiState.cpp#L202 to threads.PushBack(thread.Move(), allocator);

After recompilating, here's is the output : 
`{ "id": "852b4082a6432bb7", "worker_id": "worker_C", "version": "2.4.5", "kind": "cpu", "ua": "XMRig/2.4.5 (Linux x86_64) libuv/1.8.0 gcc/7.1.0", "cpu": { "brand": "Intel(R) Xeon(R) CPU E5-2450 0 @ 2.10GHz", "aes": true, "x64": true, "sockets": 2 }, "algo": "cryptonight", "hugepages": true, "donate_level": 1, "hashrate": { "total": [ 732.92, 734.75, 733.32 ], "highest": 773.89 }, "results": { "diff_current": 10000, "shares_good": 144, "shares_total": 144, "avg_time": 41, "hashes_total": 4202710, "best": [ 1713713, 1151632, 655876, 601382, 572086, 484596, 421869, 399131, 328301, 326110 ], "error_log": [] }, "connection": { "pool": "XX.XX.XX.XX:YYYY", "uptime": 5961, "ping": 18, "failures": 0, "error_log": [] } }`

Thank you :)


## xmrig | 2018-03-01T09:27:05+00:00
But line 207 should reverted back.
Thank you.

## I28ko | 2018-03-01T10:31:27+00:00
> But line 207 should reverted back.

So after uncommented ligne 207, the problem is back. So i made some test with the `-t` option in command line. As i see, the problem occur when the threads quantity is greater than `8`

## xmrig | 2018-03-01T10:36:54+00:00
So okay `.Move` won't help, that weird. I can't reproduce it was test with more than `8` threads too.
Thank you.

## I28ko | 2018-07-09T21:02:50+00:00
Hi !
I close the issue today (btw sorry for the delay). 
The bug was caused by a (stupid) mistake in my JS code 
Thank you again for your help

# Action History
- Created by: I28ko | 2018-02-28T18:44:33+00:00
- Closed at: 2018-07-09T21:02:50+00:00
