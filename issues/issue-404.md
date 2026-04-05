---
title: Wrong L2/L3 cache
source_url: https://github.com/xmrig/xmrig/issues/404
author: mohammad4u
assignees:
- xmrig
labels:
- bug
- NUMA
created_at: '2018-02-15T15:51:23+00:00'
updated_at: '2019-08-02T12:39:35+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:39:35+00:00'
---

# Original Description
Hi,
 I am a newbie in this mining buisness. I have a dual opteron 6376 processors, when i try to use the xmrig the optimal way to get stable hashes was to use 4 terminals, 1 each for 8 cpu. However the l3/l4 cache shows 64/24. While the actual should be apx 32/32.

# Discussion History
## mohammad4u | 2018-02-15T15:58:41+00:00
![1518710073865100421305](https://user-images.githubusercontent.com/36510957/36266219-fdbaa884-1296-11e8-8023-c255a6cc9fe2.jpg)
Here is the photo from my miner

## 0x3h | 2018-02-16T00:44:36+00:00
You should run in default settings xmrig will automatically choose the best settings, each thread need 2MB L3 cache so the optimal threads count is 12 in your case, and don't set the cpu affinity manually unless you have a good reason; let the OS choose where to run those threads, then tweak the affinity to see if any improvements are made, if not leave it to default. remember 0xF mean 4 cores 0xFF is 8, 0x3 is 2, and running multi instances is a REALLY BAD idea.

## mohammad4u | 2018-02-16T14:44:31+00:00
The default setting is giving me just ~800, while this tweak was able to get me aroung 1k h/s. While the reason for this issue is the L3 cache. The L3 cache is actually 32 mb(16*2), so optimally 16 threads should be for optimal result. But here the miner shows only 24 mb. Can i rectify this on my own ???

## mohammad4u | 2018-02-18T17:38:22+00:00
@xmrig, any help is appreciated

## g5-freemen | 2018-03-03T12:44:24+00:00
try latest version (2.4.5) for the first, maybe it can help

## Mzr-Hussain | 2018-03-06T05:20:44+00:00
Nope, it doesn't help

## erotavlasme | 2018-03-30T12:59:36+00:00
Opteron 6376 should have 2*8 MB of both L2 and L3 cache. So the optimal number of thread should be 8 per CPU for cryptonight [link](https://github.com/xmrig/xmrig/wiki/Threads).
Try again with latest version.

## xmrig | 2018-03-30T13:15:46+00:00
Opteron 6376 is tricky CPU, there is 8 x 2 MB L2 cache and 2 x 8 MB L3 cache, due specific architecture all 32 MB of cache can be used, so optimal is about 16 threads.
Other thing, it's internally dual CPU, so used NUMA, currently xmrig not work well with NUMA, it known issue, likely it will be solved in next release (v2.6).
Thank you.

## xmrig | 2019-07-29T02:17:26+00:00
If this issue still actual, please check v2.99.2-beta release #1077.
Thank you.

# Action History
- Created by: mohammad4u | 2018-02-15T15:51:23+00:00
- Closed at: 2019-08-02T12:39:35+00:00
