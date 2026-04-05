---
title: '[Expected Behaviour?] Accidentally ran 2 instances on M1 Ultra. Hash rate
  increased 30%'
source_url: https://github.com/xmrig/xmrig/issues/3200
author: AntlerDM
assignees: []
labels:
- question
created_at: '2023-01-24T23:05:34+00:00'
updated_at: '2026-01-14T18:30:53+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:25:09+00:00'
---

# Original Description
Not really an issue. Just curious if this is expected.

Apple Mac Studio (M1 Ultra, 20-core, 128GB) with one instance of XMRig 6.18.1 results in approx. 4.2kh/s.

Running 2 instances (same configuration) gets 2.8kh/s each.

# Discussion History
## SChernykh | 2023-01-25T06:39:11+00:00
M1 Ultra should be doing 6.4 kh/s with a single instance: https://xmrig.com/benchmark?cpu=Apple+M1+Ultra
Your config probably doesn't use all threads.

## AntlerDM | 2023-01-25T21:31:20+00:00
That was it. I deleted the CPU section in the config and it rebuilt with the correct number of threads.

Thanks you.

## UnixCro | 2026-01-14T18:30:53+00:00
I would be in favor of the benchmark also measuring wattage, wouldn't you dear developers?

# Action History
- Created by: AntlerDM | 2023-01-24T23:05:34+00:00
- Closed at: 2025-06-16T19:25:09+00:00
