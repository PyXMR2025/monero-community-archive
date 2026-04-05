---
title: Using only one core on 64+ threads dual xeon systems
source_url: https://github.com/xmrig/xmrig/issues/150
author: c-corazza
assignees: []
labels:
- NUMA
created_at: '2017-10-12T13:06:15+00:00'
updated_at: '2019-08-02T12:37:35+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:37:35+00:00'
---

# Original Description
It is using only one cpu on dual Xeon with more than 64 threads. I have a dual 2683v3 56threads and everything works fine. On my dual 2699v4, it is using only one core. I guess it's because windows make processor groups above 64threads, and it's not handled by the program.  

# Discussion History
## xmrig | 2017-10-12T19:29:51+00:00
You meant used only one physical CPU? Probably it 2 NUMA nodes, please check #86 and related issues.
Thank you.

## c-corazza | 2017-10-13T10:20:04+00:00
Yes, it uses one physical CPU only. There are 2 NUMA nodes for sure as I have 88 threads on this computer. What's strange is that it seems to detect only one CPU : 

CPU:          Intel(R) Xeon(R) CPU E5-2696 v4 @ 2.20GHz (1) x64 AES-NI 

I looked #86 but did not help much. Is there a way to fix it on my own?

## xmrig | 2019-07-29T02:19:51+00:00
If this issue still actual, please check v2.99.2-beta release #1077.
Thank you.

# Action History
- Created by: c-corazza | 2017-10-12T13:06:15+00:00
- Closed at: 2019-08-02T12:37:35+00:00
