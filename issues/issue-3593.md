---
title: opencl disable
source_url: https://github.com/xmrig/xmrig/issues/3593
author: luckytalk
assignees: []
labels: []
created_at: '2024-12-05T06:18:44+00:00'
updated_at: '2025-06-18T22:03:19+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:03:19+00:00'
---

# Original Description
My server is already running OPENCL, but I still prompt opencl disable when running XMRIG

# Discussion History
## BonhomieBG | 2024-12-05T09:45:45+00:00
Had you turn in config json file? There a section to opencl.By default, opencl is off. If you mine on both cpu and gpu, you need another instead of xmrig. 

Hooking up configure file is the easiest, all you have to do is change config.json and open terminal and type in xmrig -c config.json. You can also use commandline --opencl.

## luckytalk | 2024-12-09T05:33:54+00:00
If I open OPENCL, will it not improve the efficiency of mining

## BonhomieBG | 2024-12-11T01:28:08+00:00
To be able to mine using opencl, you need to enable it. It doesn't improve hashrate, it just enable your gpu to mine using opencl

# Action History
- Created by: luckytalk | 2024-12-05T06:18:44+00:00
- Closed at: 2025-06-18T22:03:19+00:00
