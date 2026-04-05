---
title: Optimized JSON config for 8th Gen i7
source_url: https://github.com/xmrig/xmrig/issues/1187
author: Xavien01
assignees: []
labels: []
created_at: '2019-09-21T20:12:34+00:00'
updated_at: '2019-09-28T17:51:50+00:00'
type: issue
status: closed
closed_at: '2019-09-28T17:51:50+00:00'
---

# Original Description
So a few things. Trying to optimize a json config for the CPU ver of XMRIG. I have it down ok currently running 4 threads each assigned to the core I specified to make sure and load balance this as much as possible. Now the issue, previously I was able to use the option of the "max-cpu-usage" which I had set at 50% which would mine and not pin the CPU and make it unusable. I dont see that option in ver 4.0.1 and I have succesfully used it in the 2.15.1 with no issue. Is this no longer valid on the new ver. How can I cap the workload on. 4.0+. Lastly how many threads would u say would be the cap on an 8th gen i7 without getting too wild. Any help is appreciated, Thanks!

# Discussion History
## xmrig | 2019-09-28T17:51:50+00:00
`max-cpu-usage` option reverted back in v4.2 with new name, please read docs carefully https://github.com/xmrig/xmrig/blob/beta/doc/CPU_MAX_USAGE.md

# Action History
- Created by: Xavien01 | 2019-09-21T20:12:34+00:00
- Closed at: 2019-09-28T17:51:50+00:00
