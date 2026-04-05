---
title: Low hash rate on linux but high on windows 10
source_url: https://github.com/xmrig/xmrig/issues/3683
author: linnuxx
assignees: []
labels: []
created_at: '2025-07-01T08:03:43+00:00'
updated_at: '2025-07-01T15:41:18+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The hash rate in Linux is 55-57 thousand, and in Windows 10 it is 64-66 thousand.
Parameters: 2 AMD epyc 7k62 processors, supermicro h11dsi rev 2.0, RAM:8 channels active.

# Discussion History
## SChernykh | 2025-07-01T09:22:52+00:00
Check if all the important things work on Linux (MSR mod, huge pages, NUMA mapping). If you get any yellow or red text on XMRig startup, you need to fix these errors.

## SChernykh | 2025-07-01T10:16:01+00:00
You just start XMRig and check what it prints before it starts mining

## SChernykh | 2025-07-01T13:25:54+00:00
It can be a different power limits that Linux and Windows set, so CPU is running at different speeds.

## SChernykh | 2025-07-01T13:36:30+00:00
> > It can be a different power limits that Linux and Windows set, so CPU is running at different speeds.
> 
> How can I run it at full speed on Linux?

`cpupower frequency-set --governor performance`

# Action History
- Created by: linnuxx | 2025-07-01T08:03:43+00:00
