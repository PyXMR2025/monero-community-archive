---
title: Why are two identical CPU's reporting different hashrates?
source_url: https://github.com/xmrig/xmrig/issues/2638
author: mastaxx
assignees: []
labels: []
created_at: '2021-10-19T08:49:57+00:00'
updated_at: '2021-10-19T20:31:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi All,

I'm sorry if posting this here turns out to be irrelevant to any issues pertaining to xmrig. It feels situational on my end but I don't know where else to turn. I've got xmrig running on both macs which have identical processors and they both have signifanctly different hashrates

Details:

Mac mini (Late 2012)
Processor: 2.3GHz Quad-Core Intel Core i7
Memory: 4GB 1600 MH DDR3
**xmrig hashrate: 600-700 H/s**

Mac mini (Late 2012)
Processor: 2.3GHz Quad-Core Intel Core i7
Memory: 16GB 1600 MH DDR3
**xmrig hashrate: 1000-1100 H/s**

Anyone know why this could be? Is the difference in RAM the reason why? Activity monitor is showing 199% CPU utilization on both machines.


# Discussion History
## Spudz76 | 2021-10-19T09:33:55+00:00
Yes, especially if the 4GB one has a single stick (1x4GB) and the other is 16GB (2x8GB)... But also 4GB is very very tight (3GB needed for RandomX) and it may not be allocating fully.

So add another 4GB stick to the first one and it probably will go the right speed.

## mastaxx | 2021-10-19T09:38:01+00:00
Hi Spudz,

I also noticed that the (4GB) one with low hashrate has a very high fault count when looking at the statistics of the xmrig process within Activity Monitor:
![low hashrate](https://user-images.githubusercontent.com/92784401/137884096-baa4c5c8-fab9-4b81-aa9f-52c7cfa7e812.jpg)

When comparing that to the mac (16GB) with the better hashrate which has a low fault count in comparison:
![high hashrate](https://user-images.githubusercontent.com/92784401/137884200-49803675-5c64-4521-ae80-2326de3f74f5.jpg)

Are there any logs i can look at to confirm what you're saying is indeed the case? Also, there is a 256GB SSD inside the macs with loads of space on them both. Is there not a way around it by allocating virtual memory to XMRIG instead?


## Spudz76 | 2021-10-19T09:48:40+00:00
There should be tons of Swap Used in the Memory tab on the 4GB one, because it's already thrashing the virtual memory.

But wasting time moving things around like a slide puzzle is terrible for hashrate which needs all the 3GB in real actual fast memory with no (or, low) page-faults.

It may be churning things from the OS to swap while trying to keep 3GB pinned (unswappable) for xmrig, 1GB is very tight for "the entire rest of MacOS".  And then the page faulting is eating CPU for moving data from SSD to RAM.

And you'll toast the SSD sooner, swapping is bad for flash erase-count.

Therefore more memory.  And if it does not have 2 sticks the memory bus is half as wide (i7 have dual-channel but only with dual sticks).

## mastaxx | 2021-10-19T12:02:41+00:00
Hi Spudz,

It had 2 x 2GB sticks so i just replaced one with a spare 4GB stick (so now 6GB total) and the hashrate has now gone up to 1000-1100 H/s. Thanks so much for the advise on that one! Appreciated.

## Spudz76 | 2021-10-19T20:31:00+00:00
Yes that will work as well, some boards don't like mixed sizes but for once Apple didn't make it difficult. :)

# Action History
- Created by: mastaxx | 2021-10-19T08:49:57+00:00
