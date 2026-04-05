---
title: lots of rejected shares with 2.4.0 on dwarfpool [no issue. it's the pool]
source_url: https://github.com/xmrig/xmrig/issues/153
author: McChickn
assignees: []
labels:
- bug
- enhancement
created_at: '2017-10-13T14:53:14+00:00'
updated_at: '2017-10-24T07:52:00+00:00'
type: issue
status: closed
closed_at: '2017-10-24T07:52:00+00:00'
---

# Original Description
It starts with the duplicate job error message, and after that the next shares get rejected ("low difficulty"), until a new job is recieved. Caused ~3% rejected shares. 
Switched back to 2.3.1 - duplicate jobs msg (~2 per hour) is never followed by rejected shares.

# Discussion History
## McChickn | 2017-10-13T16:32:13+00:00
nvm, happens with 2.3.1 too, just too longer and seems less frequent. So maybe a problem with the pool?

## mnik247 | 2017-10-13T16:37:48+00:00
It's not problem xmrig.
Its's pool problem.
I have same problem with ver.2.3.0 yet, and finally left this pool.

## McChickn | 2017-10-13T16:38:55+00:00
Ah damnit. Thanks, good to know.

## xmrig | 2017-10-13T21:15:42+00:00
That weird I was think I fix this dwarf issue in 2.4.0, sometimes pool send job with duplicate ids but different blob. What address did you use (usa/eu) and port?
Thank you.

## McChickn | 2017-10-13T21:42:34+00:00
I'm on the eu server port 8005

Not a single rejected share during the last 2 hours, only 6 times that duplicate job thing, but in total I stand at 595/15.

## xmrig | 2017-10-14T23:29:06+00:00
Definitely something wrong with pool, sometimes received fully duplicated jobs.
Also I get about same rejection ratio in xmr-stak-cpu, but errors is not verbose, need press `r` to see it.
Thank you.

## McChickn | 2017-10-15T09:03:41+00:00
Could this rejecting be worked around by making the miner reconnect or switch to fallback url whenever a duplicate job is recieved? When establishing a new connection the recieved new job should be valid at least.


## xmrig | 2017-10-15T09:21:54+00:00
Good idea, disconnect from pool if duplicated job received probably best solution.
Thank you.

## xmrig | 2017-10-15T22:30:31+00:00
Your idea works well, about 12 hours of run, 0 rejected shares.

## McChickn | 2017-10-17T06:57:21+00:00
I selflessly offer to test it for an even longer time, with a win64 binary.

## klobymoby | 2017-10-23T06:13:09+00:00
have same problems on pool.supportxmr.com getting lots of "[pool.supportxmr.com:7777] duplicate job received, ignore" using xmrrigproxy 2.4.1 and workers use xmrig 2.4.1


## xmrig | 2017-10-23T08:39:27+00:00
It well known issue for nodejs-pool based pools, has no negative impact, no rejected shares, etc.
But connection will be force closed as well in next release.
Thank you.

## xmrig | 2017-10-24T07:52:00+00:00
Fixed in 2.4.2 release.

# Action History
- Created by: McChickn | 2017-10-13T14:53:14+00:00
- Closed at: 2017-10-24T07:52:00+00:00
