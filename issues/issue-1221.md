---
title: RandomX dataset memory usage and initialization speed improvements for NUMA
  machines
source_url: https://github.com/xmrig/xmrig/issues/1221
author: xmrig
assignees: []
labels:
- enhancement
- META
- algo
created_at: '2019-10-06T05:00:05+00:00'
updated_at: '2019-11-14T08:20:00+00:00'
type: issue
status: closed
closed_at: '2019-11-14T08:20:00+00:00'
---

# Original Description
In upcoming version 4.3 NUMA support for RandomX dataset improved, second and subsequent nodes now require 2080 MB (instead of 2336 MB) and greatly improved initialization speed for that nodes.

Initial implementation, used fully independent RandomX datasets on each NUMA node, it require 2080 MB for dataset and 256 MB for cache, new implementation use cache and initialize dataset only on first node and after initialization done, just copy full dataset memory to another nodes, it much faster and not require extra cache allocation.

In addition `"numa"` option in config extended now possible specify numa nodes to use (instead of all available, it might useful for some corner cases and debug), example `"numa": [0, 1]`

# Discussion History
## 2010phenix | 2019-10-06T10:49:08+00:00
@xmrig, maybe in this case (now require 2080 MB - just copy full dataset memory to another nodes ) do some part solution(split)... like 2080 \2 - 2080\4 or similar....

## xmrig | 2019-10-06T11:29:00+00:00
1. Not possible split dataset to pieces.
2. If target is memory usage, simple `"numa": false` or choice fastest node should be enough.

Thank you.

## a905770 | 2019-10-24T08:51:19+00:00
@xmrig, Why does the new version connect to the test pool and the memory directly goes up to 2G? Is there any way to reduce the memory?

## xmrig | 2019-10-25T08:22:04+00:00
@a905770 because RandomX algorithm require it, there is no direct option to reduce it, miner will use  256 MB only if fails to allocate 2 GB, but it will be 10x slower.
Thank you.

# Action History
- Created by: xmrig | 2019-10-06T05:00:05+00:00
- Closed at: 2019-11-14T08:20:00+00:00
