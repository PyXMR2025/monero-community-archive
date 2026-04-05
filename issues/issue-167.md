---
title: xmrig & nohup doubt...
source_url: https://github.com/xmrig/xmrig/issues/167
author: sfichera
assignees: []
labels:
- bug
- libuv
created_at: '2017-10-23T22:50:54+00:00'
updated_at: '2023-08-21T08:02:46+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:21:03+00:00'
---

# Original Description
Is nohup properly supported on *nix environments?

I'm getting the following error while trying to use xmrig with nohup

xmrig: src/unix/stream.c:1485: uv_read_start: Assertion `stream->type == UV_TCP || stream->type == UV_NAMED_PIPE || stream->type == UV_TTY' failed.

Thanks & Regards!
Sebastián

# Discussion History
## xmrig | 2017-10-24T07:43:02+00:00
Please provide more details:

* How you exactly run the miner.
* What environment, OS, terminal, etc.

Because I can't reproduce this assertion.
You also can try to remove/comment this line https://github.com/xmrig/xmrig/blob/master/src/Console.cpp#L40
Thank you.

## sfichera | 2017-10-24T17:03:57+00:00
I'm sorry, didn't see the background option... I've changed the background property to **true** in the **config.json** file and everything works as expected without using **nohup**...

Anyways and for the benefit of future readers:
1) The command I was trying to execute in my bash term was:  _**nohup xmrig &**_
2) CentOS 6.5 with libuv 1.8.0 compiled from source.

Thanks!

## NmxMilk | 2017-10-29T19:23:24+00:00
Yes, indeed, if you try using nohup with xmrig configured to open tty you get:
$ nohup ./xmrig
nohup: ignoring input and appending output to ‘nohup.out’
Aborted
$more nohup.out
xmrig: src/unix/stream.c:1559: uv_read_start: Assertion `stream->type == UV_TCP || stream->type == UV_NAMED_P
IPE || stream->type == UV_TTY' failed.

I get this on centos 7.4, using latest :
 * VERSIONS:     XMRig/2.4.2 libuv/1.15.1-dev gcc/4.8.5
 * HUGE PAGES:   available, disabled
 * CPU:          Intel(R) Celeron(R) CPU G1610 @ 2.60GHz (1) x64 -AES-NI
 * CPU L2/L3:    0.5 MB/2.0 MB

Workaround is to use the -B option.


## zhuxindong | 2023-08-21T08:02:45+00:00
when i run in background mod，how can i find the log？

# Action History
- Created by: sfichera | 2017-10-23T22:50:54+00:00
- Closed at: 2018-03-14T23:21:03+00:00
