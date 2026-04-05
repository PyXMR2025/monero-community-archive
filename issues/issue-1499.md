---
title: XMRig with Intel Xeon e5-1680 v2 L2 and L3 cache
source_url: https://github.com/xmrig/xmrig/issues/1499
author: ValoWaking
assignees: []
labels:
- question
created_at: '2020-01-13T13:56:09+00:00'
updated_at: '2020-02-01T09:24:29+00:00'
type: issue
status: closed
closed_at: '2020-02-01T09:24:29+00:00'
---

# Original Description
I want to ask. If CPU have L2 2MB cache XMRig will use for mining L2 and L3 cache?
In the issue Intel Xeon e5-1680 v2 has 13 (L2 - 2MB, L3 - 25MB cache) possible threads for mining? 

# Discussion History
## ValoWaking | 2020-01-14T08:06:29+00:00
the question is - can L2 and L3 cache work together and used by XMRig?

## kio3i0j9024vkoenio | 2020-01-14T08:28:05+00:00
For each thread you need 2MB L3 Cache and 256KB L2 Cache. Note that you need BOTH to be satisfied for each thread.

The Xeon e5-1680 v2 has:

http://www.cpu-world.com/CPUs/Xeon/Intel-Xeon%20E5-1680%20v2.html

The number of CPU cores: 8
The number of threads: 16
Level 2 cache size: 8 x 256 KB 8-way set associative caches
Level 3 cache size: 25 MB 20-way set associative shared cache

For mining you can only use the 8 real cores (not the HT cores) because of the L2 limit of Level 2 cache size: 8 x 256 KB


## ValoWaking | 2020-01-14T08:35:36+00:00
ok, thanks! What about ryzen 3700, he can run with 16 threads? 

Level 2 cache size 8 x 512 KB 8-way set associative unified cache
Level 3 cache size | 32 MB 16-way set associative shared cache








## xmrig | 2020-02-01T09:24:29+00:00
Ryzen 3700 hash enough cache for 16 threads.
Thank you.

# Action History
- Created by: ValoWaking | 2020-01-13T13:56:09+00:00
- Closed at: 2020-02-01T09:24:29+00:00
