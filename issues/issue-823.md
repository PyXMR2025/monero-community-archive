---
title: AMD Opteron's 62XX series  hashrate dropped bitterly by 30% on v8
source_url: https://github.com/xmrig/xmrig/issues/823
author: nuriyevn
assignees: []
labels: []
created_at: '2018-10-19T11:25:03+00:00'
updated_at: '2018-11-13T08:26:11+00:00'
type: issue
status: closed
closed_at: '2018-11-13T08:26:11+00:00'
---

# Original Description
Opteron's 6234, 6276 dropped not for 10%.
for 6276 the max what I can get now is 702 H/s, before it was 995-1002 . minus 30%
6234 dropped from 800 to 600  minus 25%. The same setting, the same environment.

# Discussion History
## 2010phenix | 2018-10-19T15:41:18+00:00
@nuriyevn and where is problem? where issue?
already write what CPU optimizzzze and what not... use search...

## nuriyevn | 2018-10-19T16:36:14+00:00
Thank you for your answer.
"already write what CPU optimizzzze and what not... use search..."
You speak like a drunk russian man, lol :))
Using the search isn't the worst idea in the  world, however this reference is covering only small number of CPU-s as for reference.
https://github.com/SChernykh/xmr-stak-cpu/blob/master/README.md
So I am asking if someone can confirm  this is the normal hashrate or can provide an instruction  regarding optimization according to the changes that happened  in the recent update? That's a question.

## 2010phenix | 2018-10-20T14:55:37+00:00
as write before @SChernykh work on optimization... and search is very good things man ;-) https://github.com/SChernykh/xmr-stak-cpu/commit/f4dfc2b36d11a7271948c3c7858f93c58f209852

PS and maybe useful be for @xmrig, that not need do already make some work by @Bendr0id for Lite and etc( Additionally i added the asm version for cn-litev1 and XTL. Performance gain is quite nice.):  https://github.com/Bendr0id/xmrigCC/commit/9b0ec951b49d10ae483c0df9f7a7b8c9983eb371

## fantforever | 2018-10-23T08:01:04+00:00
I also confirm 30% hashrate drop with all Opterons 62xx series

## madscientist159 | 2018-10-25T21:49:07+00:00
The Bulldozer core is old and very weak on the integer math that CNv8 relies on.  I shut my Opteron miners down as they are no longer profitable; the only ones left are driving GPUs that are doing the real heavy lifting.

## nuriyevn | 2018-10-26T18:43:26+00:00
> The Bulldozer core is old and very weak on the integer math that CNv8 relies on. I shut my Opteron miners down as they are no longer profitable; the only ones left are driving GPUs that are doing the real heavy lifting.

I think the reason is simpler, no one asked to optimize it for Bulldozer before CNv8? :)

## BlackFury | 2018-11-01T22:33:26+00:00
Hashrate drop too with Buldozer gen since v8.
This gen isn't weak but now need opti !

## xmrig | 2018-11-02T04:58:03+00:00
Current dev branch include ASM for such CPUs https://github.com/xmrig/xmrig/pull/834, but it can bring back only few %. cryptonight/2 designed to iluminate any hardware cheats, Buldozer use hardware cheats it's 1 FPU for 2 cores because of this perfomance drop much more than other CPUs.

## nuriyevn | 2018-11-10T19:44:28+00:00
Hm.  Before update it was 2.43 years to start making it profitable with amazing price of energy (0.03$ per kilo) now those servers  can only start making profit after 5.7 years.
I am not including the cost of energy accumulators because that energy price is available only at the night.
Thanks for eliminating hardware cheats! :dancer: 
I hope monero will be at least 36000$  otherwise...
At least I can heat my two apartment with 13 servers, lol. 
Could you make this fork earlier before I spent 3000$ on shitty AMD servers?  lol.

# Action History
- Created by: nuriyevn | 2018-10-19T11:25:03+00:00
- Closed at: 2018-11-13T08:26:11+00:00
