---
title: Numa Xeon CPUs low hash
source_url: https://github.com/xmrig/xmrig/issues/1996
author: mrwhitti
assignees: []
labels: []
created_at: '2020-12-22T20:10:37+00:00'
updated_at: '2021-01-10T01:01:42+00:00'
type: issue
status: closed
closed_at: '2021-01-10T01:01:42+00:00'
---

# Original Description
 My 4 x E7 4830 (8/16 24mb L3) numa servers will give maximum hash as soon as the miner is started however my 4 x E7 4870 (10/20 30mb L3) servers always require many miner restarts to get the max hash.
This has always been the same with all versions of xmrig  .. running windows server. Sometimes the difference in the lowest to the highest on the E7 4870'S can be as much as 2k. The max hash can be pot luck , somtimes straight away or sometimes up to 20 miner restarts

# Discussion History
## agentpatience | 2020-12-22T20:15:33+00:00
I noticed on my 2 and 4 processor servers that if I start xmrig then stop and restart the amount of memory utilized % changes not sure 🤔 if it impacts performance but it seems like some kind of bug 🐛 

Sent from my iPhone

> On Dec 22, 2020, at 3:11 PM, mrwhitti <notifications@github.com> wrote:
> 
> ﻿
> My 4 x E7 4830 (8/16 24mb L3) numa servers will give maximum hash as soon as the miner is started however my 4 x E7 4870 (10/20 30mb L3) servers always require many miner restarts to get the max hash.
> This has always been the same with all versions of xmrig .. running windows server. Sometimes the difference in the lowest to the highest on the E7 4870'S can be as much as 2k. The max hash can be pot lusk , somtimes straight away or sometimes up to 20 miner restarts
> 
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub, or unsubscribe.


## mrwhitti | 2020-12-22T20:25:26+00:00
memory utilization is not really a problem here , i suspect it may be something to do with the 64 max thread in windows as the problem only occurs with the 40/80 core servers although the max hash is still achieved all be it after a few restarts.

## xmrig | 2020-12-23T10:04:34+00:00
Make sure huge pages are always 100% in all places, for RandomX miner allocate dataset (2080 MB) on each NUMA node, 1 node equals 1 CPU package in your case. More than 64 threads are not issue, for example 256 threads on Windows https://xmrig.com/benchmark/4nmg1G with 8 NUMA nodes.
Thank you.

# Action History
- Created by: mrwhitti | 2020-12-22T20:10:37+00:00
- Closed at: 2021-01-10T01:01:42+00:00
