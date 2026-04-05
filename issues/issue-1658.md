---
title: Do we use half of the CPU in mining? Why doesn't he see it all
source_url: https://github.com/xmrig/xmrig/issues/1658
author: restartload
assignees: []
labels:
- question
created_at: '2020-04-23T17:30:05+00:00'
updated_at: '2020-08-19T01:25:07+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:25:07+00:00'
---

# Original Description
![screenshot_v5_2_0](https://user-images.githubusercontent.com/56207175/80130407-309c4d00-85a1-11ea-9068-a26417f77ae1.png)


# Discussion History
## xmrig | 2020-04-24T00:33:04+00:00
This is best configuration for this pair of CPUs, dataset initialization require all threads, mining limited by CPU cache, 256 KB of L2 and 2 MB of L3 per mining thread, since this kind of CPU use non standard cache configuration (large L2) best option is use only physical cores (20), technically this CPU has enough L3 cache for one extra thread per socket, but it useless for this kind of CPU.
Thank you.


# Action History
- Created by: restartload | 2020-04-23T17:30:05+00:00
- Closed at: 2020-08-19T01:25:07+00:00
