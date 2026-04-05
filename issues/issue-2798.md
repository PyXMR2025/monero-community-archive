---
title: '[RandomX] Foreground applications slowdown'
source_url: https://github.com/xmrig/xmrig/issues/2798
author: electroape
assignees: []
labels:
- question
created_at: '2021-12-06T17:42:17+00:00'
updated_at: '2022-04-03T14:37:46+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:37:46+00:00'
---

# Original Description
I apologize if this was discussed before.

I think it's no secret that RandomX algo is very heavy and demanding so i don't expect anyone being able to do something about this but nevertheless i just report my findings just in case.

My case :
Priority 0 - idle
Yield enabled (as by default)
Microsoft Word and Excel (for Windows) : extreme lags when typing, scrolling and general workflow.

I think some general slight slowdown, especially on low-end machines like (i3 6100/7100) is noticeable overall but it's extremely noticeable in Microsoft Word and Excel for some reason, even with aforementioned settings it feels like the miner has normal priority or higher. There's nothing even close to that with other algos, hence me thinking that maybe that's started with some recent version but nope, still the same with the XMRig 2.16.


# Discussion History
## Lonnegan | 2021-12-06T21:26:09+00:00
Hm, the Core i3-6100 has only 3 MB last level cache. So it's really not ideal for RandomX mining, since rx/0 needs 2 MB scratchpad size for each thread. Thus, even starting two threads causes the cache to overflow and accesses to the slow RAM become necessary. But: When you start just 1 or 2 threads (out of 4 the i3-6100 the supports), the system should not be laggy.

The other option is to set pause_on_active in the config.json from false to 5. Then, every time you tough the mouse or the keyboard to work mining stops. 5 s after you moved anything, mining restarts again. Very cool for machines which are not mining only rigs.

## electroape | 2021-12-07T03:30:55+00:00
It's not only about low-end machines, exactly the same level of slowdown is observed on Ryzen 5 5600X and Intel Core i9 11900F.

## Spudz76 | 2021-12-07T04:04:20+00:00
On my daily driver i7-4700MQ I just cut one thread so it runs 7 of them and the resulting lag is tolerable.

Obviously there would never be a way to have zero-lag with the CPU all busy and the memory bus all saturated and all the cache in use.

## electroape | 2021-12-07T04:30:18+00:00
Yeah, setting core utilization to ~75% on my home Ryzen 5 helps to reduce lag significantly and i guess i could use max-threads-hint to do that on all machines without having to tweak CPU config manually on each machine. It's just that i don't think i've seen this amount of lags on any of other algos i've used, and despite RandomX is a very demanding algo indeed, i've posted this just to provide an easy way to reproduce it, since in general usage aside of some minute slowdowns it's not really that noticeable as in Microsoft Office apps, so someone could perhaps look at it and do something, like maybe some more aggressive resource yielding option.

## Spudz76 | 2021-12-07T04:43:17+00:00
Yes I only really notice it in Chrome but that is as "bloaty" as Office apps.  They just go nuts with multi-threading and do too many things in the background constantly, have scripting engines, plugins, spellcheck, and just too much stuff going on for a "tool".  It's like a whole little OS within itself for word processing or adding up numbers or browsing web sites.

If anything the "bug" is that these tools are so over-complicated and heavy.

# Action History
- Created by: electroape | 2021-12-06T17:42:17+00:00
- Closed at: 2022-04-03T14:37:46+00:00
