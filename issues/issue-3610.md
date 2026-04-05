---
title: Ghostrider mining
source_url: https://github.com/xmrig/xmrig/issues/3610
author: mrwhitti
assignees: []
labels: []
created_at: '2024-12-29T12:29:29+00:00'
updated_at: '2025-06-18T22:02:57+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:02:57+00:00'
---

# Original Description
Before running xmrig for the first time i set max threads hint to 50% & the config.json gets written correctly only using half the cores for the various algos.

However when i  set the miner to mine ghostrider it starts correctly using only 8 cores from the ghostrider profile however it then switches to using all 16 threads with 100% cpu useage when mining.

I have to manually edit the ghostrider threads in the config.json down  to 4 threads to get 50% cpu useage.

![ghostrider](https://github.com/user-attachments/assets/0606d5d1-34cf-4458-9918-2cd8fff1fff4)



# Discussion History
## SChernykh | 2024-12-29T12:59:11+00:00
Ghostrider implementation in XMRig can use up to 2 threads to calculate 1 hash, so this is why you get doubling from 8 to 16.

# Action History
- Created by: mrwhitti | 2024-12-29T12:29:29+00:00
- Closed at: 2025-06-18T22:02:57+00:00
