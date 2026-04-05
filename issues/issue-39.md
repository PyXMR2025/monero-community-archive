---
title: Some cache double counted on intel too.
source_url: https://github.com/xmrig/xmrig/issues/39
author: phillipsjk
assignees: []
labels:
- NUMA
created_at: '2017-07-17T12:55:57+00:00'
updated_at: '2017-11-27T00:25:15+00:00'
type: issue
status: closed
closed_at: '2017-09-03T03:32:06+00:00'
---

# Original Description
I was able to reproduce this:
https://github.com/anrieff/libcpuid/issues/97

 under WinXP-64, on an Intel Core 2 Duo E8400

Note:
Only the gcc compiled binary works, msvc one says: "permission denied" and  Windows complains it is not a valid win32 app.

# Discussion History
## xmrig | 2017-09-03T03:32:06+00:00
I will switch to hwloc instead of libcpuid, it fixes cache size issues and helps with NUMA nodes support #86 

# Action History
- Created by: phillipsjk | 2017-07-17T12:55:57+00:00
- Closed at: 2017-09-03T03:32:06+00:00
