---
title: a lot of rejected shares for GR - is it normal?
source_url: https://github.com/xmrig/xmrig/issues/2780
author: musiu
assignees: []
labels: []
created_at: '2021-12-03T08:14:52+00:00'
updated_at: '2021-12-03T11:21:14+00:00'
type: issue
status: closed
closed_at: '2021-12-03T11:21:14+00:00'
---

# Original Description
**Describe the bug**
as above, running from HiveOs for 22h and have 19 rejected shares, I didn't notice that when using cpuminer on the same pool

**To Reproduce**
run miner on hiveOs 

**Expected behavior**
reduced number of rejected shares.

**Required data**
![image](https://user-images.githubusercontent.com/8035665/144568486-87ed5e67-97dc-460d-b184-85430e29e728.png)
![image](https://user-images.githubusercontent.com/8035665/144568501-62726dcc-ce87-4e1d-8a59-a8961037431b.png)


 - OS: [HiveOs

if you need anything else, please shout :)
thank you and regards,
Pawel


# Discussion History
## SChernykh | 2021-12-03T08:19:43+00:00
"Job not found" is a stale share. XMRig just displays it as rejected because technically it was rejected by the pool.

## SChernykh | 2021-12-03T08:21:04+00:00
From what I can see it's only one of ~650 shares that is stale which is not bad at all. cpuminer probably displays them differently or doesn't display them as rejected at all.

## Lonnegan | 2021-12-03T11:14:18+00:00
As soon as the rejected shares are just due to stale or not found jobs, everything is ok. When you look at your log, it's just a timing problem. The miner tried to send back a result at 08:41:35,219 o'clock. 0.05 s (!) earlier, the pool sent a new job. So sending back and getting a new job just overlapped. No reason to worry.

What would be worrying is when the pool rejects results without a timing problem is not so obvious. In this case instable hardware could be the trigger or a buggy miner.

## musiu | 2021-12-03T11:20:22+00:00
> From what I can see it's only one of ~650 shares that is stale which is not bad at all. cpuminer probably displays them differently or doesn't display them as rejected at all.

ok, thank you very much for quick reply and explanation - wasn't aware of that.
Fingers crossed for future improvements of GR on XMRig!!

## musiu | 2021-12-03T11:21:10+00:00
> As soon as the rejected shares are just due to stale or not found jobs, everything is ok. When you look at your log, it's just a timing problem. The miner tried to send back a result at 08:41:35,219 o'clock. 0.05 s (!) earlier, the pool sent a new job. So sending back and getting a new job just overlapped. No reason to worry.
> 
> What would be worrying is when the pool rejects results without a timing problem is not so obvious. In this case instable hardware could be the trigger or a buggy miner.

"buggy miner" part thats what I was affraid about ;) 

# Action History
- Created by: musiu | 2021-12-03T08:14:52+00:00
- Closed at: 2021-12-03T11:21:14+00:00
