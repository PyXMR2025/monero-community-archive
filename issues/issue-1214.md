---
title: 'Auto threads config doesn’t work correctly on Ryzen 7 3700x/RandomX '
source_url: https://github.com/xmrig/xmrig/issues/1214
author: vegaman64
assignees: []
labels: []
created_at: '2019-10-02T13:38:23+00:00'
updated_at: '2020-04-18T11:48:32+00:00'
type: issue
status: closed
closed_at: '2019-10-08T11:49:26+00:00'
---

# Original Description
On 3700x it’s seems 15 threads do the best job even if it seems there is enough L2 and L3 cache to  feed all 16 threads. I think for CPUs having L3 = cpu threads x 2 and L2 = cpu threads x 256 miner thread count should be cpu threads-1. It seems there must be some free headroom in L3 to effectively work. Someone with similar cache/threads setup could confirm this though 

# Discussion History
## SChernykh | 2019-10-03T14:56:29+00:00
I have 3700X and 16 threads is the best setting. I just don't have anything running in the background and I've gone to great lengths tweaking Windows and disabling unnecessary services.

## vegaman64 | 2019-10-03T15:15:16+00:00
Even on Linux I’m getting 7100hs as a max using 16 threads and 7800hs using 15. Thanks for your reply. Can you share how much did you get with 16 threads?

## SChernykh | 2019-10-03T15:37:24+00:00
I've just tested at fixed 4.1 GHz clock speed to get more stable hashrate. 16 threads are a bit faster: https://imgur.com/a/CXpN4LF

## vegaman64 | 2019-10-03T15:53:17+00:00
Thanks again.. Except memory settings and cpu OC, isn’t  there some trick on bios ? I’m playing on 4 different boards, windows, Linux.. all the same. 8.5+kh sounds more  reasonable for 3700x

## SChernykh | 2019-10-03T15:56:16+00:00
Memory tweaked with timings from Ryzen DRAM calculator (fast preset), CPU overclocked in Ryzen Master, that's it. And Windows just cleaned of garbage as I mentioned before.

## vegaman64 | 2019-10-08T11:49:26+00:00
Thanks! Playing on windows I managed to get all threads working and even on Linux there’s small, but benefit running 16 threads if memory is pushed to its max. 

## vegaman64 | 2019-10-08T11:56:25+00:00
One last question about Linux - is there still something wrong with kernel (4.15 and 5.4 rc1 tested) or xmrig/rx-benchmark isn’t jet fully optimized for ryzen+Linux? Getting less Hashrate on Ubuntu no matter what I do. (At 4.1ghz/1.085v 9050hs Win, 8750hs Linux and at 4.4ghz/1.35v 9500hs Win, 9150hs Linux) 

## k0ngl0ng | 2020-04-17T02:25:17+00:00
How do you solve this problem? I have the same problem.
thank you.

## k0ngl0ng | 2020-04-18T11:48:32+00:00
how to push the memory to its max？

# Action History
- Created by: vegaman64 | 2019-10-02T13:38:23+00:00
- Closed at: 2019-10-08T11:49:26+00:00
