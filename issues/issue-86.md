---
title: Proper NUMA nodes support
source_url: https://github.com/xmrig/xmrig/issues/86
author: xmrig
assignees:
- xmrig
labels:
- enhancement
- NUMA
created_at: '2017-09-03T03:12:54+00:00'
updated_at: '2019-07-29T02:21:34+00:00'
type: issue
status: closed
closed_at: '2019-07-29T02:21:33+00:00'
---

# Original Description
Need proper NUMA nodes support, for example add ability to pin threads to specific node.

- [x] Use **hwloc** instead of **libcpuid**.
- [x] Add optional per thread configuration in config file. #563 

# Discussion History
## 2010phenix | 2017-09-08T12:10:23+00:00
-- cut --
Need proper NUMA nodes support, for example add ability to pin threads to specific node.
 Use hwloc instead of libcpuid.
-- cut --

am too have this problem.....
can i build hwloc myself with xmrig or need redone much things for this ?

## xmrig | 2017-09-08T12:41:18+00:00
Yep it need redone much things.

## github12101 | 2018-02-09T23:52:22+00:00
Any progress on this? I am mining with Dual CPU Xeon E5-2620, 320H/s, how to improve that?

## kimats | 2018-03-02T05:42:28+00:00
hope we can deliver this soon...

## xmrig | 2019-07-29T02:21:33+00:00
Implemented, future details #1077.

# Action History
- Created by: xmrig | 2017-09-03T03:12:54+00:00
- Closed at: 2019-07-29T02:21:33+00:00
