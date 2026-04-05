---
title: how do i increase the amount of cores and the cpu usage
source_url: https://github.com/xmrig/xmrig/issues/2806
author: LearnersUD
assignees: []
labels:
- question
created_at: '2021-12-11T15:47:26+00:00'
updated_at: '2021-12-19T14:32:02+00:00'
type: issue
status: closed
closed_at: '2021-12-19T14:32:02+00:00'
---

# Original Description
how do i increase the amount of cores and the cpu usage

# Discussion History
## Spudz76 | 2021-12-11T19:06:00+00:00
You don't, since the autoconfigurator selects the maximum useful amount in the first place.

If you insist on making it run worse but show "more percent usage" then edit config.json and add threads.

## fairclothj | 2021-12-15T15:33:06+00:00
Does the autoconfig assume the improvement is due to higher boost clocks for lower number of cores being used?  Mostly curious if the improvement would still hold true for fixed all core overclocks.

## Spudz76 | 2021-12-15T16:04:02+00:00
It uses entirely math not actual benchmarking.

For RandomX (rx/0), it's 2MB of cache per thread mainly, but also Intel hyperthreads generally get ignored they don't get their own path to cache (shared with parent real-core).  So it will be actual cores * 2MB if you have that much cache.  Running out of cache stops more threads, hitting hyperthreads does not help and will leave cache unused if you happen to have more than cores*2.  Ryzen can use all threads, assuming enough cache.

CPU clock speed has less to do with RandomX speed than RAM and Cache.

## fairclothj | 2021-12-15T16:28:42+00:00
Thanks for the info and your time.

That definitely makes since for intel given how hyperthreading works.

My curiosity was based on observing ghostrider using 2/12 threads on a Ryzen 3600 for some cycles which seemed weird. 
 For Ryzen Zen2/3 wouldn't cache speed be directly tied to clock speed since they are both on the die together?  Or is cache speed tied to CClk and ignores boosting clock speeds?  I was basing this on the link below, but I am not sure how accurate that info is.

https://en.wikichip.org/wiki/amd/microarchitectures/zen#Clock_domains

If it does work that way and cache speed gets increased with single core workloads I could see how that would be beneficial in particular for some cycles of ghostrider since it seems to be primarily dependent on cache speed.  But in this case would that benefit be lost with an all core overclock?

## Spudz76 | 2021-12-15T16:48:43+00:00
Ghostrider does do a bit of actual benchmarking when it fires up the algo but only to select an implementation.  It should show that info if `verbose` is 1 or more.  (not sure it shows if verbose:0)

Yes CClk should boost cache also but may not be noticeable.  I know more about RandomX tuning where tuning for max FClk is more important.

If anything crosses CCX's then it has to move the cache content via the fabric so then FClk comes back in to play.  It should not be doing that unless some threads are `-1` and the process scheduler decides to move processes around cores (across CCX).  Each CCX gets its own division of the total L3 cache.  Most Ryzen have two CCX's.

# Action History
- Created by: LearnersUD | 2021-12-11T15:47:26+00:00
- Closed at: 2021-12-19T14:32:02+00:00
