---
title: RandomX - Free dataset memory on Pause
source_url: https://github.com/xmrig/xmrig/issues/944
author: tarris034
assignees: []
labels:
- enhancement
- review later
created_at: '2019-02-23T17:27:05+00:00'
updated_at: '2019-12-21T20:09:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
If we use RandomX for the second fork, please make it so when you push "**P**ause" in the miner, it will also release the dataset memory.

It will be much more pleasant to coexist with it.

Thank you.

# Discussion History
## tarris034 | 2019-02-24T17:01:16+00:00
also would be nice if the miner did auto-detect of available memory and run with 4 gig or 256 mb mode according to available memory so we don't have to manually set on different machines.

again thank you for your great work my friend.

## tarris034otheracc | 2019-09-26T14:52:33+00:00
I lost access to my old account so writing from this new, after considering couple things I think it's a bad idea to release the memory at every pause as it may cause problems in future allocations and require miner to restart the whole system or use some third party defragmentation tools.
From Microsoft docs:

> Large-page memory regions may be difficult to obtain after the system has been running for a long time because the physical space for each large page must be contiguous, but the memory may have become fragmented. Allocating large pages under these conditions can significantly affect system performance. Therefore, applications should avoid making repeated large-page allocations and instead allocate all large pages one time, at startup.

I'm sure you're aware of this, I was not.

Thank you for your consideration.

## xmrig | 2019-09-26T15:31:36+00:00
Exactly right, also this is issue for mining threads too not only RandomX dataset, following changes come in near future (v4.2 or v4.3):
1. Option `huge-pages-pool` `true/false/number` for preallocate huge pages for mining threads.
2. Stop command (it already paritialy implemented for OpenCL backend) to release resources, but miner will not release huge pages by default.

# Action History
- Created by: tarris034 | 2019-02-23T17:27:05+00:00
