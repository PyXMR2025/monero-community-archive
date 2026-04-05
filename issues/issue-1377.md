---
title: When switching between RandomX and Loki XMRig runs out of Huge Pages on Window
  7
source_url: https://github.com/xmrig/xmrig/issues/1377
author: kio3i0j9024vkoenio
assignees: []
labels: []
created_at: '2019-12-04T02:53:20+00:00'
updated_at: '2019-12-04T03:28:04+00:00'
type: issue
status: closed
closed_at: '2019-12-04T03:28:04+00:00'
---

# Original Description
Pool is Moneroocean, Miner is XMRig v5.1.0 on Windows 7

XMRig on Moneroocean will auto switch between mining RandomX and/or Loki which is fine with me.

The problem is today I noticed the hash rate had dropped about 20% and looking at the miner screen I saw that only 60% of the Huge Pages were allocated and further up that 70% were allocated. Even though the system was only running XMRig (I way away from the computer) the less than 100% Huge Page issue occurred.

Is there some way that the miner could grab the necessary number of Huge Pages and not release them when switching between RandomX and Loki so that this issue does not happen again?



# Discussion History
## xmrig | 2019-12-04T03:09:23+00:00
You can use `"memory-pool": true,` option https://github.com/xmrig/xmrig/blob/master/src/config.json#L27 
This option create huge pages in one sequential block and preserve it between threads restarts.
Thank you.

## kio3i0j9024vkoenio | 2019-12-04T03:28:00+00:00
Thanks, will do.

# Action History
- Created by: kio3i0j9024vkoenio | 2019-12-04T02:53:20+00:00
- Closed at: 2019-12-04T03:28:04+00:00
