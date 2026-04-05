---
title: Intel MSR optimizations - 6 is maybe not the best?
source_url: https://github.com/xmrig/xmrig/issues/1433
author: jfikar
assignees: []
labels:
- META
created_at: '2019-12-16T15:35:48+00:00'
updated_at: '2021-04-12T15:08:43+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:08:43+00:00'
---

# Original Description
Hi,

I've tried all the possible values X=0-15 in `wrmsr -a 0x1a4 X` . Then I let the xmrig working for at least 15 minutes, pressed H and recorded the max cumulative hash rate (the very last number when you press H).

I have found that **6** is not the best value. It is **13** and sometimes **12**. I've tried 5 different Intel CPUs from these families: SandyBridge, IvyBridge, and Haswell.

Did anyone else try all the values? The guy in the original reddit thread shows a picture, where **14** is actually the fastest, but he uses for some reason **6**, the second fastest. He also looked at the speed of the single fastest thread, not at the cumulative hash rate.  I also observed a smaller gain of the total hash rate of only 0.5-5%, not 30%.
  

# Discussion History
## xmrig | 2019-12-16T16:09:14+00:00
`6` is maybe not the best and it main reason why option `wrmsr` is not just accept `true` or `false`, it also accept the number too.

For old CPUs like yours hashrate improvements is lower and it expected.
Thank you.

## jdmpro | 2019-12-16T17:38:59+00:00
Can you add randomV rx/v algorithm 

## ValoWaking | 2019-12-17T21:56:31+00:00
for me the best is 15 and 7 (z97 4690k, windows 10)

## kio3i0j9024vkoenio | 2019-12-20T03:44:10+00:00
Quote: 

I've tried all the possible values X=0-15 in wrmsr -a 0x1a4 X . Then I let the xmrig working for at least 15 minutes, pressed H and recorded the max cumulative hash rate (the very last number when you press H).

I have found that 6 is not the best value. It is 13 and sometimes 12. I've tried 5 different Intel CPUs from these families: SandyBridge, IvyBridge, and Haswell.

End Quote

---------------------------------------------------------------------------------------------------------------

Could you post the results of your tests or a link to the results.

I have various Intel machines and would like to use the most optimal value for wrmsr.

Thanks

## jfikar | 2019-12-20T10:01:18+00:00
The best is to try it by yourself, as the result may depend on your CPU and other things. Just try all the settings, let xmrig run for 15 mins, press "h" and record the max. Here are results for Haswell-E i7-5930K:

```
0    3198.8
1    3208.1
2    3206.7
3    3205.8
4    3271.7
5    3257.3
6    3254.1
7    3251.2
8    3210.7
9    3181.1
10   3195.5
11   3206.3
12   3260.7
13   3256.9
14   3254.2
15   3238.8
```

## kio3i0j9024vkoenio | 2019-12-20T15:58:49+00:00
Quote: The best is to try it by yourself, as the result may depend on your CPU and other things. Just try all the settings, let xmrig run for 15 mins, press "h" and record the max.

Well I was hoping to not have to replicate results if it was already done for the different Intel families: SandyBridge, IvyBridge, and Haswell.

Quote: Here are results for Haswell-E i7-5930K:

Using "6" as the base setting for the msr registers I have added the percent differences for the other settings:

0    3198.8 -1.7%
1    3208.1 -1.4%
2    3206.7 -1.46%
3    3205.8 -1.48%
4    3271.7 +0.54%
5    3257.3 +0.1%
6    3254.1 0.0% - base
7    3251.2 -0.1%
8    3210.7 -1.3%
9    3181.1 -2.2%
10   3195.5 -1.8%
11   3206.3 -1.5%
12   3260.7 +0.2%
13   3256.9 +0.09%
14   3254.2 0.0%
15   3238.8 -0.47%

This article discloses the MSR setting that can be used to control the various hardware prefetchers that are available on Intel processors based on the following microarchitectures: Nehalem, Westmere, Sandy Bridge, Ivy Bridge, Haswell, and Broadwell.

https://software.intel.com/en-us/articles/disclosure-of-hw-prefetcher-control-on-some-intel-processors

So the base setting of 6 equates to 0110b which disables the "L2 adjacent cache line prefetcher" and the "DCU prefetcher".

Focusing on the only positive gain of any significance the "4" 0100b +0.54% it looks like re-enabling the "DCU prefetcher" is the reason for the gain at least for the Haswell.

In the 4 0100b vs the 5 0101b the disabling of the "L2 hardware prefetcher" caused the loss.

In the 6 0110b vs the 12 1110b the disabling of the "DCU IP prefetcher" caused the loss.

At least for Haswell it is best not to disable the "L2 hardware prefetcher" or the "DCU IP prefetcher" and that only re-enabling the "DCU prefetcher" gives slightly better results.

Using the base "6" 0110b for Intel may be good overall for Intel but I will be testing The "4", "6" and "12" on other Intel processors and post the results here.

## jfikar | 2019-12-20T16:17:39+00:00
It seems I missed **4** was the fastest for this one. Also, it seems the max hash rate can easily vary by as much as +/- 3h/s, so it difficult to obtain stable results.

I suspect it depends not only on the CPU family, but also on the L2 cache size (more cache, more threads, which somehow compete for the resources) and also on RAM speed, etc. The IvyBridge and SandyBridge Xeons (large L2, ECC memory) have max hash rate for **13**, you may also want to include that.

## jfikar | 2020-01-08T15:40:06+00:00
I've done more testing and it seems it is better to look at the 15 min average. It is more reliable than the max hash rate. You can also change the MSR setting while xmrig runs, just wait 15 minutes and record the new average. And before I had not optimal thread count for the i7-5930K, now the hashrate is better.

Results for more CPUs:

|  | i5-2520M | E3-1230 | E3-1265L v2 | E5-1607 | i7-5930K| 
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 0 | 705.3  | 1817.4 | 1926.3 | 1651.8 | 3404.8 |
| 1 | 705.3  | 1828.4 | 1932.2 | 1655.5 | 3415.1 |
| 2 | 680.1  | 1816.4 | 1926.3 | 1650.2 | 3404.2 |
| 3 | 678.3 | 1829.4 | 1932.4 | 1652.9 | 3413.1 |
| 4 | 705.1 | 1888.3 | 1955.5 | 1650.8 | 3485.9 |
| 5 | 692.9  | 1898.9 | 1963.1 | 1653.5 | **3496.5** |
| 6 | 710.8  | 1887.8 | 1955.6 | 1649.0 | 3483.9 |
| 7 | 708.8  | 1897.8 | 1962.9 | 1652.5 | 3495.4 |
| 8 | 704.3  | 1820.2 | 1926.6 | 1651.0 | 3405.0 |
| 9 | 705.4  | 1829.8 | 1932.5 | **1654.5** | 3415.6 |
| 10 | 705.3 | 1818.4 | 1926.6 | 1650.5 | 3403.9 |
| 11 | 704.8 | 1831.0 | 1932.7 | 1653.3 | 3412.0 |
| 12 | **716.5**  | 1889.1 | 1956.5 | 1653.0 | 3487.4 |
| 13 | 713.9  | 1899.0 | **1964.2** | 1651.8 | 3495.4 | 
| 14 | 716.4  | 1894.6 | 1956.3 | 1651.5 | 3484.1 |
| 15 | 713.4  | **1900.4** | 1963.9 |1653.2 | 3494.9 |

## SChernykh | 2020-01-09T07:07:25+00:00
It seems that 15 is the best setting overall for Intel CPUs - it disables all 4 prefetchers.

## jfikar | 2020-01-10T11:51:47+00:00
Yes, indeed **15** is fastest overall for the 5 CPUs measured, followed by **13**, **14**, **12**, and **7**.

# Action History
- Created by: jfikar | 2019-12-16T15:35:48+00:00
- Closed at: 2021-04-12T15:08:43+00:00
