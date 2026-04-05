---
title: max-threads-hint not working anymore?
source_url: https://github.com/xmrig/xmrig/issues/1905
author: heavyarms2112
assignees: []
labels: []
created_at: '2020-10-19T03:15:11+00:00'
updated_at: '2021-04-12T14:45:04+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:45:04+00:00'
---

# Original Description
**Describe the bug**
max-threads-hint cpu option not working anymore?

[2020-10-18 23:10:34.057]  randomx  init datasets algo rx/wow (20 threads) seed 453297e5c742cb52...
[2020-10-18 23:10:34.073]  randomx  #0 allocated 2080 MB huge pages 100% (15 ms)
[2020-10-18 23:10:34.100]  randomx  #1 allocated 2080 MB huge pages 100% (42 ms)
[2020-10-18 23:10:34.102]  randomx  #0 allocated  256 MB huge pages 100% +JIT (2 ms)
[2020-10-18 23:10:34.102]  randomx  -- allocated 4416 MB huge pages 100% 2208/2208 (44 ms)
[2020-10-18 23:10:36.367]  randomx  #0 dataset ready (2265 ms)
[2020-10-18 23:10:36.545]  randomx  #1 dataset ready (177 ms)
[2020-10-18 23:10:36.545]  cpu      use profile  rx/wow  (24 threads) scratchpad 1024 KB
[2020-10-18 23:10:37.277]  cpu      READY threads 24/24 (24) huge pages 100% 24/24 memory 24576 KB (731 ms)
[2020-10-18 23:10:37.847]  cpu      accepted (1/0) diff 994 (576 ms)

It does take the hint but regardless starts mining with all threads?

# Discussion History
## heavyarms2112 | 2020-10-19T03:20:34+00:00
After removing existing cpu core settings and having the parameter in config file it worked.  But shouldn't this override the config again for core affinities?
` "rx/wow": [0, 2, 4, 1, 3, 6, 8, 10, 7, 9, 12, 14, 16, 13, 15, 18, 20, 22, 19, 21],`

# Action History
- Created by: heavyarms2112 | 2020-10-19T03:15:11+00:00
- Closed at: 2021-04-12T14:45:04+00:00
