---
title: CPU Affinity Help
source_url: https://github.com/xmrig/xmrig/issues/88
author: Prefinity
assignees: []
labels:
- question
- NUMA
created_at: '2017-09-04T02:12:18+00:00'
updated_at: '2017-11-27T00:27:00+00:00'
type: issue
status: closed
closed_at: '2017-09-08T13:46:22+00:00'
---

# Original Description
Not very sure how to get the binary codes for entering the proper affinity into config, will appreciate some assistance! E5 2686 V4 64 cores but it seems like only 70% of cpu is used even when i entered 100 in config, and only 45 cores are displayed in the window when i start the program.
![image](https://user-images.githubusercontent.com/7398235/30009143-9abeef20-9158-11e7-8e24-0a18e8d3f023.png)


# Discussion History
## xmrig | 2017-09-06T13:52:41+00:00
Each thread required 2 MB of CPU cache for optimal performance. If you try use more threads it will decrease hashrate. About 22-23 threads per single CPU should be better config.
Sorry for late reply.

## Prefinity | 2017-09-06T14:55:13+00:00
thanks for the response. so how should i calculate the bitmask for this? or just leave null on affinity and let the program automatically set it up?

## xmrig | 2017-09-06T16:18:47+00:00
Set proper affinity maybe not work, because of 2 NUMA nodes see #86
If affinity option not set it means leave OS choice where place threads.

## xmrig | 2017-09-08T13:46:22+00:00
#86

# Action History
- Created by: Prefinity | 2017-09-04T02:12:18+00:00
- Closed at: 2017-09-08T13:46:22+00:00
