---
title: GPU Mining isn't calculated
source_url: https://github.com/xmrig/xmrig/issues/3398
author: recabasic
assignees: []
labels: []
created_at: '2024-01-13T06:46:18+00:00'
updated_at: '2025-06-18T22:25:15+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:25:15+00:00'
---

# Original Description
**Describe the bug**
When attempting to mine with my AMD GPU (Integrated), it displays a hash rate of around 300k Hashes/s. However, upon checking Nanopool's account stats section, the reported hash rate is consistently lower, ranging between 800-1000 Hashes/s.

**Expected behavior**
I anticipated Nanopool to reflect the same hash rate as displayed by Xmrig.

**Required data**
OS: Windows 11 23H2 64-bit
CPU & GPU: AMD Ryzen 5 7520U with Radeon Graphics
Config: [config.json](https://github.com/xmrig/xmrig/files/13927194/config.json)
Logs: [xmrig.txt](https://github.com/xmrig/xmrig/files/13927196/xmrig.txt)

# Discussion History
## SChernykh | 2024-01-13T17:00:06+00:00
This is a driver issue. OpenCL optimized RandomX code was only tested with drivers from 2019-2020. You can try to install older drivers, but they will probably not work with a new GPU. Anyway, the real hashrate will be around 100-200 h/s, so it doesn't make sense to mine RandomX on integrated GPU.

# Action History
- Created by: recabasic | 2024-01-13T06:46:18+00:00
- Closed at: 2025-06-18T22:25:15+00:00
