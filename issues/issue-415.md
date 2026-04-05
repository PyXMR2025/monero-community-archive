---
title: 2.4.5 didn't run multiple threads even though 2.4.4 was running multiple threads
  on the same device and does failover.xmrig.com work like a real pool?
source_url: https://github.com/xmrig/xmrig/issues/415
author: tcanbot
assignees: []
labels: []
created_at: '2018-02-27T21:42:17+00:00'
updated_at: '2018-02-28T05:33:45+00:00'
type: issue
status: closed
closed_at: '2018-02-28T05:33:45+00:00'
---

# Original Description
I had been using 2.4.4 on a device and it would run multiple threads but then I tried running 2.4.5 on the same device and it won't run multiple threads and so I have to run multiple instances to run multiple threads. Should I go back to running 2.4.4? It seems to be more suitable for this device.
Another unrelated question: I had left a device running multiple instances of 2.4.5 overnight and I had not changed the default URL (failover.xmrig.com) so now I'm just curious if that is like a real pool or did I just make a mistake? I would have entered the URL of a pool but I didn't because I just wanted to know what would happen and it kept using it as a pool.

# Discussion History
## xmrig | 2018-02-28T02:25:30+00:00
v2.4.5 is minor release, should be fully compatible with previous version, failover.xmrig.com is not real pool (thanks for donation). Anyway what CPU you talking about, how many threads run v2.4.4 and new version or you talking about GPU.
Thank you.

## tcanbot | 2018-02-28T03:43:11+00:00
WoW! I can't believe you responded so quickly. I was using an old core 2 duo it was running on two threads with 2.4.4 and on a single thread in 2.4.5 per instance. I had enabled huge pages by typing in sudo sysctl -w vm.nr_hugepages=5 in the terminal and that would enable huge pages for one instance in 2.4.4 but not for the second instance. In 2.4.5 it would be enabled for two instances but not the third. I probably had to increase the value from the minimum 5 to 10 or something to enable them for second and third instances.
I just wanted to let you know that this was happening. I had assumed that failover.xmrig.com wasn't a pool but I thought the donation would still be worth it since you've contributed so much by creating the most efficient CPU cryptonote miner out there.

## xmrig | 2018-02-28T04:03:26+00:00
Please check https://github.com/xmrig/xmrig/pull/385 it related to core 2 duo and similar CPUs.

* Fixed L2 cache size detection, also it change autoconfig.
* Increased performance.

Anyway you don't need run multiple instances, you can just change threads count, `threads: 2,` in config file or `-t 2` in command line. Miner required 1 huge page per thread (or 2 for `--av 2` and `--av 4`) and 1 extra per each instance.
Thank you.

## tcanbot | 2018-02-28T05:27:38+00:00
alright thanks a lot for your help man!

# Action History
- Created by: tcanbot | 2018-02-27T21:42:17+00:00
- Closed at: 2018-02-28T05:33:45+00:00
