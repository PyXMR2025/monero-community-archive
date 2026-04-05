---
title: NiceHash rejected
source_url: https://github.com/xmrig/xmrig/issues/458
author: welj
assignees: []
labels: []
created_at: '2018-03-17T06:06:17+00:00'
updated_at: '2018-03-25T03:21:09+00:00'
type: issue
status: closed
closed_at: '2018-03-25T03:21:09+00:00'
---

# Original Description
there were rejected shares after the update to 2.5.0 approximately 20%

# Discussion History
## xmrig | 2018-03-17T06:20:45+00:00
What error message you get?
Thank you.

## welj | 2018-03-17T06:25:35+00:00
for example:
[18-03-16 21:58:05] speed 2.5s/60s/15m 907.4 864.8 895.5 H/s max: 1016.2 H/s
[2018-03-16 21:58:12] new job from 159.122.29.199:3355 diff 200007
[2018-03-16 21:58:39] rejected (53/1) diff 200007 "Share above target." (107 ms)
[2018-03-16 21:59:05] speed 2.5s/60s/15m 754.2 902.6 896.0 H/s max: 1016.2 H/s
[2018-03-16 21:59:23] new job from 159.122.29.199:3355 diff 200007
[2018-03-16 21:59:28] rejected (53/2) diff 200007 "Share above target." (110 ms)
[2018-03-16 21:59:28] rejected (53/3) diff 200007 "Share above target." (86 ms)


## xmrig | 2018-03-17T06:36:29+00:00
Can you rebuild miner from source with enabled protocol debug? If not I can build it for you, only tell what exactly version do you need. Protocol debug need to see what miner received and send.

Also possible, someone use nicehash to mine GRAFT, check this comment https://github.com/xmrig/xmrig/issues/434#issuecomment-373184425 maybe simple disable new PoW helps with this issue.
Thank you.



## welj | 2018-03-17T06:58:25+00:00

i rty it with --variant 0

## Balzhur | 2018-03-18T10:13:25+00:00
It seems that --variant 0 fixed the "Share above target." with Nicehash.
I've got around 30% rejected over last night, then implemented --variant 0 and so far no rejects. Thanks @xmrig.

# Action History
- Created by: welj | 2018-03-17T06:06:17+00:00
- Closed at: 2018-03-25T03:21:09+00:00
