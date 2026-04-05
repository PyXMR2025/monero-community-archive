---
title: Randomly crashes
source_url: https://github.com/xmrig/xmrig/issues/1783
author: needhelp101
assignees: []
labels:
- opencl
created_at: '2020-07-18T20:58:52+00:00'
updated_at: '2021-04-12T14:52:58+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:52:58+00:00'
---

# Original Description
Hi,

So basically the miner works for periods of time, then randomly seems to crash.. just reports watts drop on the cards, and stops hashing... 

Then when i try restart it, it does not want to start hashing, and gets stuck on the first job that it receives and i am forced to reboot the pc in order for it work again..

Here is an example first one card drops out, then the others follow...

[2020-07-18 22:40:07.014]  opencl   #0 01:00.0 114W 74C 1326RPM 0/0MHz
[2020-07-18 22:40:07.015]  opencl   #1 05:00.0  56W 49C  778RPM 0/0MHz
[2020-07-18 22:40:38.815]  net      new job from solo-rvn.2miners.com:7070 diff 4295M algo kawpow height 1324833
[2020-07-18 22:40:39.222]  opencl   KawPow program for period 441612 compiled (404ms)
[2020-07-18 22:40:49.998]  net      new job from solo-rvn.2miners.com:7070 diff 4295M algo kawpow height 1324834
[2020-07-18 22:41:07.094]  opencl   #0 01:00.0  30W 58C 1166RPM 0/0MHz
[2020-07-18 22:41:07.095]  opencl   #1 05:00.0  57W 47C  776RPM 0/0MHz

And just stops hashing... 

Any ideas? 

Thanks


# Discussion History
## needhelp101 | 2020-07-18T21:01:18+00:00
Also after the crash, no other miner can work untill a reboot if that helps out too... 

## zn3x | 2020-07-21T08:53:31+00:00
Are you using a GPU with less than 3gb memory?

## needhelp101 | 2020-07-21T17:47:47+00:00
nope, using 8gb RX cards Thanks

# Action History
- Created by: needhelp101 | 2020-07-18T20:58:52+00:00
- Closed at: 2021-04-12T14:52:58+00:00
