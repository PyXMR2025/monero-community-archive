---
title: XMrig keeps crashing (ARM processor) (XMrig 6.15.2)
source_url: https://github.com/xmrig/xmrig/issues/2629
author: utauyo
assignees: []
labels: []
created_at: '2021-10-14T17:26:03+00:00'
updated_at: '2021-10-14T19:27:26+00:00'
type: issue
status: closed
closed_at: '2021-10-14T19:27:26+00:00'
---

# Original Description
for some reason after the log "allocated 2336 MB (1080+256) huge pages 0% 0/1168 +JIT (1 ms)" the miner just gets killed, i cant figure out why 

Algo: RandomX
CPU: Octa-core 2.36 GHz ARM Cortex-A53
RAM: 2780 MB

# Discussion History
## SChernykh | 2021-10-14T18:38:44+00:00
You don't have enough free memory on Linux OOM killer kills xmrig. Try mining in light mode.
`--randomx-mode=light`

## utauyo | 2021-10-14T19:23:59+00:00
That seems to have fixed it. Though it is still weird that i have run the same miner configuration on even worse arm processors and less ram and they would mine just fine.

# Action History
- Created by: utauyo | 2021-10-14T17:26:03+00:00
- Closed at: 2021-10-14T19:27:26+00:00
