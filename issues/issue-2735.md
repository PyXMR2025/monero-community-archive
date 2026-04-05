---
title: Not better than cpuminer on rtm
source_url: https://github.com/xmrig/xmrig/issues/2735
author: danjylon
assignees: []
labels: []
created_at: '2021-11-28T02:50:17+00:00'
updated_at: '2021-11-29T06:49:33+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
AMD R5 3600, 1.4KH(average) by using cpuminer at 10 threads, but only 900H by using xmrig at 10 threads and 1.2KH at 12 threads! 

# Discussion History
## SChernykh | 2021-11-28T09:16:25+00:00
Are you comparing 24 hour average at the pool? Windows or Linux? And if Windows, MSVC or GCC build?

## dastardlyman12 | 2021-11-28T15:58:52+00:00
we have a lot of windows 10 mining rigs. (ethereum) we have had over 40 cpus on raptoreum for months (its a little bonus cos eth is the priority) on all of them the new xmrig is drawing slightly less watts than the cpuminer. result! thats measured using hwinfo and with a few killawatt meters.  on all the cache starved lga 1150 xeons (e3-1245-v3) xmrig is more hash than cpu miner but the ones with more cache per thread (e3-1225-v3) xmrig is lower hash than cpu miner. ryzen 1600 with locked cores - 8% more hash on xmrig. ryzen 3950x,3900x ,3600x and 3600 are all slightly more hash on xmrig. if anyone is struggling i suggest ryzen master and lock cores to get a handle on whats going on. but pbo is very good. we are now using cpu priority 1 on xmrig and it seems to be fine - not affecting eth hash. i used to think you needed spare threads for eth mining - not so sure now.  great work xmrig we need mining software in competition. raptoreum great project love it. ps cos of the slightly reduced power consumption im able to do a cheeky durrty core boost on all my ryzens and they dont run into heat problem. everyone loves a durrty core boost

## danjylon | 2021-11-29T06:45:46+00:00
Okay, It turns out that chia synchronization decreases the hashrate. Hashrate returns to normal after closing chia, but the hashrate is almost the same as cpuminer. But I still choose xmrig, for familiar configuration.

# Action History
- Created by: danjylon | 2021-11-28T02:50:17+00:00
