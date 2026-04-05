---
title: Autoconfig not working / Slow performance / 'h' not working
source_url: https://github.com/xmrig/xmrig/issues/192
author: stna1981
assignees: []
labels: []
created_at: '2017-11-08T15:54:13+00:00'
updated_at: '2017-11-10T02:41:12+00:00'
type: issue
status: closed
closed_at: '2017-11-10T02:41:12+00:00'
---

# Original Description
Hello,

today I gave XMRig-NVIDIA a try as I was using XMR-STAK-NVIDIA in the past and wanted to have its good performance for NiceHash. However, after 5 minutes of testing, I discovered several issues with the tool:

1. The autoconfig is not working properly for my system. I have 8x GTX 1060 3GB and the tool proposes settings of 44x27 for all cards which crashes immediately. The highest I can go is 38x27. May the 44x27 are working for a single cards, but not for a rig with 8 cards. XMR-STAK proposes 32/27 which also seems to be the fastest option.

2. The performance is really bad. I get a max. of 3240 H/s. XMR-STAK gives 4230 H/s which is a whopping 30% more. I had expected XMRig to perform at least similar. Tested with the latest CUDA9 x64 release.

3. When I press 'h', the miner just quits hard. No error, no dialog, cmd just closed. The other three shortcuts work fine. Really strange.

Best regards

Stefan

# Discussion History
## xmrig | 2017-11-10T02:41:12+00:00
Try CUDA8 release too. Autoconfig is really tricky, not linear dependency of memory usage (threads * blocks) and performance, sometimes, more than 32 threads good. Previous release suggest 32 threads.

Looks like miner crash when try get per card hashrate, very strange, now have no idea, why it can be happen.

Also it wrong place for this issue, should be here https://github.com/xmrig/xmrig-nvidia/issues
Thank you.

# Action History
- Created by: stna1981 | 2017-11-08T15:54:13+00:00
- Closed at: 2017-11-10T02:41:12+00:00
