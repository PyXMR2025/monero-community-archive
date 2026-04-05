---
title: Cannot read MSR 0xc0011020
source_url: https://github.com/xmrig/xmrig/issues/2857
author: iLaurian
assignees: []
labels: []
created_at: '2022-01-08T15:31:24+00:00'
updated_at: '2022-01-08T15:41:34+00:00'
type: issue
status: closed
closed_at: '2022-01-08T15:41:34+00:00'
---

# Original Description
[2022-01-08 15:25:00.825]  net      use pool gulf.moneroocean.stream:10128  195.201.124.214
[2022-01-08 15:25:00.825]  net      new job from gulf.moneroocean.stream:10128 diff 128001 algo rx/0 height 2532797 (31 tx)
[2022-01-08 15:25:00.825]  cpu      use argon2 implementation AVX2
[2022-01-08 15:25:00.825]  msr      cannot read MSR 0xc0011020
[2022-01-08 15:25:00.825]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2022-01-08 15:25:00.826]  randomx  init dataset algo rx/0 (4 threads) seed 48caf06bbddd4c44...
[2022-01-08 15:25:01.187]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (362 ms)

I mine monero in the cloud.

# Discussion History
## SChernykh | 2022-01-08T15:39:04+00:00
Cloud VMs don't have access to MSR registers.

## iLaurian | 2022-01-08T15:41:24+00:00
Ok thank you

# Action History
- Created by: iLaurian | 2022-01-08T15:31:24+00:00
- Closed at: 2022-01-08T15:41:34+00:00
