---
title: config.json issue on 'algo' and 'threads'
source_url: https://github.com/xmrig/xmrig/issues/811
author: syrius01
assignees: []
labels:
- question
created_at: '2018-10-18T05:13:14+00:00'
updated_at: '2018-10-18T09:01:58+00:00'
type: issue
status: closed
closed_at: '2018-10-18T09:01:58+00:00'
---

# Original Description
Hi,

Since I would like to be ready for the fork, I updated the version of xmrig, here's what I've put for the algo:

"algo": "cryptonight"

and for threads:

 "threads": null

So the issue I'm having right now is that when I launch xmrig I see the following input:

[2018-10-18 01:07:12] new job from 164.132.109.110:14444 diff 120001 algo cn/1

Shouldn't it be mining on the new variant which is I believe cn/2 ?

Also about threads; 

* THREADS      2, cryptonight, av=0, donate=5%

I have an i5 intel processor and when I type 'nproc' I get '4' so threads should be detected as '4' and not '2' ?

Any help would be very appreciated,
Thanks

# Discussion History
## xmrig | 2018-10-18T05:33:51+00:00
If you set/not change `"variant": -1,` for each Monero pool, miner miner will switch automatically to `cn/2` estimated time 7+ hours from now http://xmr.noctism.com/ 
Threads count depends of CPU cache size, each thread required 2 MB for optimal performance, of course you can change threads count `"threads": 4,` and see what happen.
Thank you.

## syrius01 | 2018-10-18T06:05:00+00:00
Thanks for your quick reply @xmrig ! Very nice option "variant": -1, which is already set to my config.json. So if I leave "threads": null, it will auto-detect what would be best. I've tried "threads": 4 and not much difference on hashrate.

I believe you answered all my questions already, this issue can then be closed :)

# Action History
- Created by: syrius01 | 2018-10-18T05:13:14+00:00
- Closed at: 2018-10-18T09:01:58+00:00
