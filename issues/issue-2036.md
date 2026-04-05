---
title: Use memory instead of three-level cache
source_url: https://github.com/xmrig/xmrig/issues/2036
author: ahTy
assignees: []
labels:
- question
created_at: '2021-01-12T03:57:52+00:00'
updated_at: '2021-01-14T01:36:40+00:00'
type: issue
status: closed
closed_at: '2021-01-14T01:36:40+00:00'
---

# Original Description
**Describe the bug**
Compared with the number of threads, the intel server cpu three-level cache cannot allocate 2M three-level cache per thread, so there is a great waste of resources

**To Reproduce**
E5 2680 V3 only hava 30M three-level cache, 24 threads.

**Expected behavior**
Add an optional parameter to let the remaining core CPU directly read the memory instead of not using it


# Discussion History
## SChernykh | 2021-01-12T08:42:10+00:00
This will not increase the hashrate.

## ahTy | 2021-01-12T09:14:11+00:00
> This will not increase the hashrate.

Why?

The third-level cache is the data cache, which is just a copy of the data in the memory. The read speed of the third-level cache is only several times faster than the memory speed, and will not have a significant impact, and the data of the third-level still needs to be transferred to the second-level cache. Yes, this is not much different from the speed of directly transferring from the memory to the second-level cache

## ahTy | 2021-01-12T09:42:27+00:00
> This will not increase the hashrate.

A new idea:
https://github.com/xmrig/xmrig/issues/2037

## Spudz76 | 2021-01-13T20:23:24+00:00
Not that much faster than system ram, huh?  Weird I find at least twice the speed on L3 and 25 times the speed or more for L2/L1.  Expanding your work units into system ram would only make the overall hashrate slower than just using cache and a matching number of cores.  Unless you like burning more watts for less hashrate for some reason (self-harm?).

![image](https://user-images.githubusercontent.com/2391234/104505950-ee3cf500-55a1-11eb-8019-47c8cfb21f2b.png)

The entire point of CPU-algos are to leverage the speed of caches and avoid slow remote system ram.  Get a CPU with more cache or live with less threads than cores, it's how it works.

## Spudz76 | 2021-01-13T20:28:00+00:00
Also there are several metrics about memory access, not just bandwidth but also latency.  System ram latency sucks way worse than the bandwidth difference.  Only looking at the bandwidth is ignoring the RTT to get there, similar to predicting a school bus would win NASCAR because it carries more passengers, even if it does it way slower latency.  BUT IT HOLDS SO MUCH MORE PEOPLE!  no.

## SChernykh | 2021-01-13T20:45:40+00:00
Both L3 bandwidth and latency is 5-6 times better on Ryzen:

![aida2](https://user-images.githubusercontent.com/15806605/104508444-85c53680-55e8-11eb-9c76-da2727bd9cc2.png)


## ahTy | 2021-01-14T01:32:16+00:00
> Not that much faster than system ram, huh? Weird I find at least twice the speed on L3 and 25 times the speed or more for L2/L1. Expanding your work units into system ram would only make the overall hashrate slower than just using cache and a matching number of cores. Unless you like burning more watts for less hashrate for some reason (self-harm?).
> 
> ![image](https://user-images.githubusercontent.com/2391234/104505950-ee3cf500-55a1-11eb-8019-47c8cfb21f2b.png)
> 
> The entire point of CPU-algos are to leverage the speed of caches and avoid slow remote system ram. Get a CPU with more cache or live with less threads than cores, it's how it works.


I mean to use L3 cache first and use memory when L3 is not enough

## ahTy | 2021-01-14T01:36:40+00:00
> 此外，还有一些有关内存访问的指标，不仅包括带宽，还包括延迟。系统ram延迟比带宽差糟得多。只看带宽就忽略了到达那里的RTT，这与预测校车会赢得NASCAR一样，因为它载有更多的乘客，即使这样做会降低延迟，也是如此。但它拥有更多的人！没有。



# Action History
- Created by: ahTy | 2021-01-12T03:57:52+00:00
- Closed at: 2021-01-14T01:36:40+00:00
