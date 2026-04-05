---
title: v2.13.1 Exit automatically after running
source_url: https://github.com/xmrig/xmrig/issues/949
author: ttsite
assignees: []
labels:
- duplicate
created_at: '2019-02-26T03:36:12+00:00'
updated_at: '2019-03-06T10:31:58+00:00'
type: issue
status: closed
closed_at: '2019-03-06T10:31:58+00:00'
---

# Original Description
As with the previous version, try compiling all of these problems with vs2015 vs2017 and gcc. The same is true for downloading compiled software directly from the website. The software before replacing the new algorithm will work properly.

Testing system windows Server 2008
CPU E5-2620 V3
 CPU E5-2620 v4
CPU E5-2690 v2 


# Discussion History
## ttsite | 2019-02-26T12:20:02+00:00
Looking forward to your solution, today you get a new version of the test or run after the automatic exit. Replace the old algorithm software can work normally. Attempted to download the website compiled in a variety of ways is still the same. I also tried to compile the next vs2015 vs2017 GCC mode. Has been running after the automatic exit. Thank you!!!

## ttsite | 2019-02-27T02:20:38+00:00
V2.13.x The original CPU default war 75% of the machine as long as it is replaced by V2.13x version, if it can work, it will immediately increase the CPU occupancy to 100%.

## ttsite | 2019-02-28T12:33:38+00:00
> hi
> did you fix your issue ?
> my miner which I compiled it exit as soon as runnng it
> how to fix this ?

Hello, there has been no solution, so far has not found a solution, now V2.13x is not available on my machine, as long as the point to open just to connect to the mine automatically quit. Attempted to compile a variety of ways and websites to download the author compiled, all this is the case. Very anxious can not update the new version. Before March 9, there is no new version to solve my machine. In this case, all my machines can only stop working. It's very impatient.

## xmrig | 2019-02-28T12:55:29+00:00
Again, please provide all information (including configs) how to reproduce this issue, preferably with original binaries, if you modify source I need this too. If I can't reproduce the issue I can't help.

## ttsite | 2019-03-01T02:35:56+00:00
> Again, please provide all information (including configs) how to reproduce this issue, preferably with original binaries, if you modify source I need this too. If I can't reproduce the issue I can't help.

Every time I just want to connect to the mine address, when I see that the CPU is occupied, I automatically quit. This situation did not appear in the previous version of the new algorithm. Just now, I tested the version of v2.12.0, which is also automatic exit. Because the original version of 2.83 is stable and has not been replaced, I saw that the version of v2.13X appeared automatic exit and tested the version of v2.12x under this situation. It should start from this version, I hope the author can see from here. Look for the reasons above the version. Think about where the major changes were made at that time. Thank you!!
Test System and Processor
Windows Server 2008
CPU E5-2620 V3
CPU E5-2620 V4
CPU E5-2690 V2

## ttsite | 2019-03-02T09:27:10+00:00
> after compiled the xmrig I created cmd file and wrote this code in it
> @echo off
> xmrig.exe
> pause
> 
> and I got this
> 
> unable to open "C:\xmrig\build\config.json".
> No valid configuration found. Exiting.
> Press any key to continue . . .

Hello, have you solved the problem of automatic exit? Thank you!! I've been doing this all the time.

## xmrig | 2019-03-02T09:44:02+00:00
https://github.com/xmrig/xmrig/issues/957#issuecomment-468890667 bug with `m_data.push_back` also fixed.

## ttsite | 2019-03-04T04:46:54+00:00
> [#957 (comment)](https://github.com/xmrig/xmrig/issues/957#issuecomment-468890667) bug with `m_data.push_back` also fixed.

I found that auto-exit only happened on E5 26xx CPU. I downloaded the xmrig-dev version issued by the author yesterday. It still happened on E5 26xx level CPU, and only on 64-bit version. If I use 32-bit version on 64-bit system, I can run normally. If I use 64-bit version, it will not work. When I connect to the pool after running, it will happen. Shipping has withdrawn.

## xmrig | 2019-03-06T10:31:58+00:00
Merge with #951 

# Action History
- Created by: ttsite | 2019-02-26T03:36:12+00:00
- Closed at: 2019-03-06T10:31:58+00:00
