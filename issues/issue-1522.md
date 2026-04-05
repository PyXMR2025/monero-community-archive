---
title: How to Increase RAM Usage
source_url: https://github.com/xmrig/xmrig/issues/1522
author: moneroxxl
assignees: []
labels:
- question
created_at: '2020-01-30T00:31:10+00:00'
updated_at: '2020-02-23T23:25:02+00:00'
type: issue
status: closed
closed_at: '2020-02-23T23:25:02+00:00'
---

# Original Description
Hey there Guys,

We got a Google Cloud Instance with 986GB Ram and 20 CPU Cores. (Screenshot)

We tried every different config but wont get managed to use more than 1% of the CPU. So we only achieve around 4Kh/s on nearly 1 TB Ram.... 

Anybody have suggestions how we can increase this ?

![Bildschirmfoto 2020-01-30 um 01 21 26](https://user-images.githubusercontent.com/60453641/73409621-218a6380-4300-11ea-88c0-127cdf8c14b8.png)
 

# Discussion History
## SChernykh | 2020-01-30T12:57:54+00:00
Enable huge pages to increase hashrate. Try running with less than 20 threads because 20 virtual cores doesn't mean CPU has enough cache to use them all.

## xmrig | 2020-02-01T09:10:57+00:00
With huge pages hashrate will be higher, but it virtual machine, hashare may also low because other users heavy use CPU and there no benefit of 1 TB ram, please check memory requirements https://xmrig.com/docs/miner/randomx-optimization-guide#memory-size-requirements
Thank you.

## BlankerL | 2020-02-23T08:51:33+00:00
It is not a memory-intensive algorithm. It has a minimum requirement, but will not take all the free memory to speed up. 

You are sharing a machine with others rather than using this CPU individually, so other people are taking the L2/L3 cache, which will heavily slow you down. 

# Action History
- Created by: moneroxxl | 2020-01-30T00:31:10+00:00
- Closed at: 2020-02-23T23:25:02+00:00
