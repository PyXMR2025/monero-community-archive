---
title: donate level 0 is ignored
source_url: https://github.com/xmrig/xmrig/issues/71
author: trashhalo
assignees: []
labels: []
created_at: '2017-08-27T20:35:41+00:00'
updated_at: '2017-09-03T03:06:00+00:00'
type: issue
status: closed
closed_at: '2017-09-03T03:06:00+00:00'
---

# Original Description
when I change the config to set the donate level to 0 it boots ` cryptonight, av=1, donate=5%` I thought it was just a cosmetic issue until I hit a dns error on my box today and low and behold fee.xmrig.com was being hit
![2017-08-27 16_28_17-](https://user-images.githubusercontent.com/177491/29753731-b63c1fb6-8b45-11e7-8693-a2ab29aa2699.png)


# Discussion History
## xmrig | 2017-08-27T20:44:19+00:00
Donate can set to 0 only if you compile miner by yourself from source, need change single line in `donate.h` file.
Thank you.

# Action History
- Created by: trashhalo | 2017-08-27T20:35:41+00:00
- Closed at: 2017-09-03T03:06:00+00:00
