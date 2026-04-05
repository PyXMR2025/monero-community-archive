---
title: how to get the best configuration for cpu
source_url: https://github.com/xmrig/xmrig/issues/461
author: developernew123
assignees: []
labels: []
created_at: '2018-03-18T12:57:16+00:00'
updated_at: '2019-08-02T13:07:47+00:00'
type: issue
status: closed
closed_at: '2019-08-02T13:07:47+00:00'
---

# Original Description
I want to get the best configuration for cpu 
I thought the more threads I use , the more hashrate I get 

but I found that this is wrong due to the cpu cache

is there any formula to get the best configuration (number of threads)


# Discussion History
## BusaSpectre | 2018-03-18T15:55:47+00:00
There are two approaches.

1) Cache size divided by 2 MB - this holds true for most processors.
2) Set threads to match actual core count (so don't count hyperthreading or total "logical" cores).

Examples:
i7-2600K - 4 threads - (4 cores, 8 threads) - ~290 H/s
i7-3770K - 4 threads - (4 cores, 8 threads) - ~300 H/s
R7-1700 - 8 threads - (8 cores, 16 threads) - ~555 H/s
i7-7820X - 8 threads - (8 cores, 16 threads) - ~595 H/s

I was surprised by the i7-7820X, as following the cache size divided by 2 MB would have been less than 8 threads.

In all of these instances, I don't use any additional settings or parameters.

I've found that manually setting core affinity causes the computer to bog or even temporarily freeze while performing other tasks. Even when not on other tasks, I've noticed higher and more consistent hash rate without affinity.

The only extra parameter I would recommend is priority. IF you are multitasking on the computer, setting the priority higher/lower could help the computer behave as you want.

TL;DR - Set threads to equal PHYSICAL cores.

## developernew123 | 2018-03-19T10:00:02+00:00
what about using --safe parameter , I think it's better

## Gill1000 | 2018-03-20T05:33:11+00:00
--safe parameter uses only 1 thread. (Default)....i know because i m using this.

## developernew123 | 2018-03-20T16:45:22+00:00
won't it increase threads even if the cache is 10 mb ?!!!!

@Gill1000 

# Action History
- Created by: developernew123 | 2018-03-18T12:57:16+00:00
- Closed at: 2019-08-02T13:07:47+00:00
