---
title: CPU config generation issue
source_url: https://github.com/xmrig/xmrig/issues/3247
author: chapst1ck
assignees: []
labels: []
created_at: '2023-04-08T06:49:59+00:00'
updated_at: '2025-06-18T22:44:16+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:44:16+00:00'
---

# Original Description
I noticed that when I'm setting `"max-threads-hint": 100` it makes `rx` profile use only 1 of 2 cores. I need to remove that limit and always generate `rx` profile that is matching my `max-threads-hint` setting.
I was searching what's causing my issue and found that:
https://github.com/xmrig/xmrig/blob/834ea445072e50ffc385d7b88ee395c1e8ce957f/src/backend/cpu/platform/BasicCpuInfo.cpp#L355
The question is, will it be enough to change that to `return std::max<size_t>(count, 1);` or should I also be looking at changing something in `HwlocCpuInfo::threads()`?

# Discussion History
## Spudz76 | 2023-04-08T15:24:47+00:00
Oversubscribing your caches will only make it slower.

## chapst1ck | 2023-04-08T23:27:21+00:00
It's much better when miner utilizes both cores on that CPU. I should try it on other machines as well.
![image](https://user-images.githubusercontent.com/126701337/230746508-aee695f5-7043-4ef7-80c8-21141ca931e5.png)

![image](https://user-images.githubusercontent.com/126701337/230746400-16aa662b-8b1b-4799-a411-366e8e314fde.png)

![image](https://user-images.githubusercontent.com/126701337/230746461-f8a4ecde-a555-4e0a-9535-e69956ed9d4e.png)


## DeeDeeRanged | 2023-04-24T09:59:17+00:00
FYI I am using a AMD 200GE iGPU 2 core 4 threads just to give you some idea.
profile		huge pages		memory		priority
rx rx/0		1170/1170 100%	4096 KB		default
\# 2	intensity	affinity	10s		1m		15m
0	1			0			558.59	565.47	597.20
1	1			1			537.87	546.65	584.02

To be honest I haven't tried running 4 threads but I can see both cores are running more or less 99/100%

# Action History
- Created by: chapst1ck | 2023-04-08T06:49:59+00:00
- Closed at: 2025-06-18T22:44:16+00:00
