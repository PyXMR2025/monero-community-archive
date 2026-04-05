---
title: 2.5.0 BUG-hash value is inaccurate
source_url: https://github.com/xmrig/xmrig/issues/457
author: guigeddos
assignees: []
labels: []
created_at: '2018-03-17T05:00:24+00:00'
updated_at: '2018-11-05T12:59:23+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:59:23+00:00'
---

# Original Description
The CPU of the 12 thread shows the maximum hash value 900h/s

In fact, only 300h/s
@xmrig 

# Discussion History
## guigeddos | 2018-03-17T05:01:30+00:00
The 2.4 version shows the maximum 300h/s

The 2.5 version shows the maximum 900h/s

## xmrig | 2018-03-17T05:56:00+00:00
What exactly CPU? Where you see 900 H/s in miner or on pool.
Thank you.

## guigeddos | 2018-03-17T08:35:36+00:00
this  AMD Opteron 6344
The miners show the maximum 900h/s

But in fact, the 2.4 version only shows the maximum 350-400h/s
@xmrig

## guigeddos | 2018-03-17T09:01:28+00:00
![tim 20180317165931](https://user-images.githubusercontent.com/35347058/37553523-bec5bf80-2a04-11e8-8eac-d9a4d56e4298.png)
@xmrig  What's the matter. Is it a donation
I can't visit the donated mine pool here.
If so, iterate through thanks.xmrig.com. Does it affect the consumption of hash value?

## xmrig | 2018-03-17T09:48:33+00:00
If you use Dual Opteron 6344, so about 900 H/s is ok, of course depends of load, but in v2.5 no changes can affect hashrate, big changes planned to v2.6.

In current master I already fix such errors, they will not disturb, it not affect hashrate, just to noise.
Just for test can miner connect to 108.61.188.145:80 or 108.61.188.145:443 I'd like know it just DNS issue or something bigger.
Thank you.

## guigeddos | 2018-03-17T10:42:41+00:00
Updating to 2.6. does not affect 2.5. Because I'm a botnet hash. It is more troublesome to replace the miners. I want to use 2.5 all the time. Is there a problem after March 28th
@xmrig 

## xmrig | 2018-03-17T10:48:50+00:00
PoW may changed again on September, so miner will be required to update if it happens.

## guigeddos | 2018-03-17T14:44:34+00:00
2.5 before September, there was no problem.？The replacement of miners after September has no problem
@xmrig 

# Action History
- Created by: guigeddos | 2018-03-17T05:00:24+00:00
- Closed at: 2018-11-05T12:59:23+00:00
