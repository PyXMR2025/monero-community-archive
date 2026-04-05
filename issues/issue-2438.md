---
title: Donation Issue Miner Stops At First Donation Round
source_url: https://github.com/xmrig/xmrig/issues/2438
author: DarrylWhitworth
assignees: []
labels: []
created_at: '2021-06-11T21:02:56+00:00'
updated_at: '2021-06-11T21:33:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi, please see attached image file. XMRig for nVidia stops and crashes. The issue can be repeated and occurs at the first donation round. It's a big issue as it's a show stopper. Restarting the miner has everything work perfectly right up until the first occurence of the donation round.
![Screenshot 2021-06-11 135748](https://user-images.githubusercontent.com/15150454/121748375-afae5680-cabd-11eb-958d-ee45a99585cd.png)


# Discussion History
## xmrig | 2021-06-11T21:14:20+00:00
What algorithm do you mine before donation?
Thank you.

## DarrylWhitworth | 2021-06-11T21:23:36+00:00
Hi,

cn/gpu

Let me know if you need anything else.

## xmrig | 2021-06-11T21:33:51+00:00
Since `cn/gpu` removed from recent versions and from donation servers as well I can only suggest disable donation (required recompile) or switch to another miner.
Thank you.


# Action History
- Created by: DarrylWhitworth | 2021-06-11T21:02:56+00:00
