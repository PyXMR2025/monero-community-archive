---
title: not enough memory for RandomX dataset
source_url: https://github.com/xmrig/xmrig/issues/1354
author: oiuacc
assignees: []
labels:
- question
- randomx
created_at: '2019-12-01T12:37:41+00:00'
updated_at: '2022-02-20T13:07:41+00:00'
type: issue
status: closed
closed_at: '2019-12-02T01:07:54+00:00'
---

# Original Description
[2019-12-01 20:33:03.453]  rx   init dataset algo rx/0 (2 threads) seed 993ba25f
61d47e1e...
[2019-12-01 20:33:03.453]  rx   not enough memory for RandomX dataset
[2019-12-01 20:33:03.484]  rx   failed to allocate RandomX dataset, switching to
 slow mode (40 ms)
[2019-12-01 20:33:04.468]  rx   dataset ready (972 ms)
[2019-12-01 20:33:04.468]  cpu  use profile  rx  (2 threads) scratchpad 2048 KB
[2019-12-01 20:33:04.500]  cpu  READY threads 2/2 (2) huge pages 100% 2/2 memory
 4096 KB (26 ms)


 * CPU:Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz (1) x64 AES L2:0.5 MB L3:35.0 MB 2C/2T NUMA:1
 * MEMORY:0.6/2.0 GB (31%)

I run it on VMs.
It always on  slow mode

# Discussion History
## xmrig | 2019-12-01T12:43:03+00:00
But it true 2.0 GB not enough, RandomX required 2080+256 MB for dataset and cache to run in fast mode.
Thank you.

## SweetRiot | 2022-02-18T04:02:58+00:00
2GB of RAM or hard disk ? 

## schniklab | 2022-02-20T13:07:41+00:00
how to Fix it? Could Anybody help a beginner?

# Action History
- Created by: oiuacc | 2019-12-01T12:37:41+00:00
- Closed at: 2019-12-02T01:07:54+00:00
