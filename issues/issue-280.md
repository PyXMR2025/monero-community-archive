---
title: Hashrate randomly good, randomly bad (forever)
source_url: https://github.com/xmrig/xmrig/issues/280
author: Nexworks
assignees: []
labels:
- bug
created_at: '2017-12-21T03:16:50+00:00'
updated_at: '2018-03-14T23:49:40+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:49:40+00:00'
---

# Original Description
When I run the program my hashrate will either be around 150 H/s, 220 H/s or 275 H/s. It will be like that forever until I close the program, upon which reopening it again gives me one or the other. Its an i5 8600k (six core, no hyperthreading). Program is configured to use 5 out of 6 cores. On a i5 4670k with just 3 cores gives me around 200 H/s. So the 275 on five cores is closer to being correct. The 220 obviously isnt (nor is the 150). So why is it that half the time the program starts at the wrong hash rate and never deviates from it?

# Discussion History
## 2010phenix | 2017-12-21T15:22:33+00:00
CPU loaded by other service \ program

## Nexworks | 2017-12-21T21:06:00+00:00
2% CPU usage when I run it by background programs. And even if something were using the CPU, im still instructing the program to use 5 cores, so why wouldnt it start using the 4th or 5th core when it becomes available?

## NmxMilk | 2017-12-29T19:34:51+00:00
Bottleneck is in cache size. 
Optimal number of threads in your case is 9/2 = 4.
Recheck your config, mainly:
"cpu-affinity": 0x3A,
"threads": 4,
and give it a try. You should be getting a steady value of 275h/s

## Nexworks | 2017-12-29T20:50:56+00:00
I get 240 at 4 threads. The issue is every time I run the program the hash rate is different (at 5 threads). Sometimes its 150 forever, usually its around 220, but sometimes when I run it I get a nice 275-280 and it will stay that way until I close the program, at which time I still have to play the open/close game to try to get that figure again. Point is it CAN do 275-280, but its very rare it locks in on that. A 4670k at 3 threads gets me 200 even. With 50% more cache and cores I should be destroying that CPU with my 8600k but I am not. 

## Nexworks | 2017-12-31T00:55:31+00:00
For example, after two reboots and reopening the program 8 times, it finally locked in at 275+ hash rate on 5 threads (cpu affinity set for 3E so cores 1 to 5 with core 0 left available for windows). It even peaked at 301.6 H/s. Been like this for 12+ hours now. So the program is certainly capable of running 5 threads very well on a 8600k, it just takes a whole lot of luck sometimes to get it to lock-in at the correct hash rate.

## HansHagberg | 2018-01-05T13:46:36+00:00
This has been highlighted in other places before. There is something strange going on with some coffee lake CPUs.  I have a similar issue with a i5-8600K performing really bad. I can't make it do better than 150 and no amount of rebooting changes anything. Running with large memory pages makes things worse and this one maxes out at 3 threads. Not much difference up to 6 threads either.
Performance is worse than an i3-8350K in an otherwise identical system. I get 245 with that one.
Never found an explanation for this behavior with i5-8600K. 

## Nexworks | 2018-01-17T21:59:40+00:00
This issue is mostly resolved in the latest version. At 4 out of 6 cores on the 8600k I can now get 300+, maxing out at 340.6!

## MaKla89 | 2018-02-22T07:47:50+00:00
Sorry to dig through these older posts again, but I just got a 8600k yesterday and I'm still having exactly what you described: random speeds that the miner will lock to after start. With huge pages enabled I get to 270 H/s (in best cases, but if it locks to this speed, it'll run with that speed until infinity^^). What are your settings if I may ask? (also: did you OC?) Thank you! :)

## Nexworks | 2018-02-22T15:49:25+00:00
I run my 8600k at 4.7 / 4.6 Ghz, stock voltage. Yes once it locks in at the correct speed it will run like that forever. Highest ive had it go to is 345.2 H/s. The problem is the whole lockin mechanic is horribly broken and sometimes you have to reopen the program a dozen times before it gets going correctly.

## MaKla89 | 2018-02-22T22:11:31+00:00
ah thank you :) so OC really does matter (especially if it doesnt consume more energ). It  would be interesting to know whether this locking-issue has any hopes to be resolved

## xmrig | 2018-03-14T23:49:40+00:00
Duplicate #207

# Action History
- Created by: Nexworks | 2017-12-21T03:16:50+00:00
- Closed at: 2018-03-14T23:49:40+00:00
