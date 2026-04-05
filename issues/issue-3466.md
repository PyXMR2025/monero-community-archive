---
title: Zen3 architecture CPU, core computing power is unbalanced
source_url: https://github.com/xmrig/xmrig/issues/3466
author: 3600cpuminer
assignees: []
labels: []
created_at: '2024-04-20T09:15:54+00:00'
updated_at: '2025-06-16T19:43:45+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:43:45+00:00'
---

# Original Description
My zen3 architecture CPU, whether it is a notebook (5800u es) or a desktop (5950x), the hash is unbalanced, and core 1 is always lower than core 0. This has never happened with other architecture CPUs, such as 3950x, 7742, and 7900x. The computing power of core 1 is significantly lower than that of core 0. The exact same system is used. I have tested multiple versions of xmrig and it is the same
![Screenshot_2024-04-20-17-08-49-000_com microsoft rdc android](https://github.com/xmrig/xmrig/assets/95530739/f94187c2-313a-4c1f-912e-fb6b058c108d)


# Discussion History
## 3600cpuminer | 2024-04-20T09:21:33+00:00
![Screenshot_2024-04-20-17-20-13-225_com microsoft rdc android](https://github.com/xmrig/xmrig/assets/95530739/437a6642-df35-4467-8c64-edfa67270687)
I ran the benchmark directly and it was still the same. Core 1 was significantly lower than core 0.


## SChernykh | 2024-04-20T14:46:56+00:00
I had the similar issue on my 7950X. I don't remember exactly what I did to fix it, but it was because of my Windows installation. I think I installed some "gaming optimized" build that turned off Spectre/Meltdown mitigations, and it resulted in this unstable hashrate. I fixed it by re-enabling those mitigations in the registry, but I don't remember how and I can't find the instructions now. Stock Windows 10 doesn't have this problem, but it needs tweaks to be done manually: https://www.reddit.com/r/MoneroMining/comments/f18825/windows_10_tuning_guide_for_randomx_mining/

# Action History
- Created by: 3600cpuminer | 2024-04-20T09:15:54+00:00
- Closed at: 2025-06-16T19:43:45+00:00
