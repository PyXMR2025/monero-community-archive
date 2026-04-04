---
title: 'Kovri: extend benchmarks timeout length?'
source_url: https://github.com/monero-project/meta/issues/34
author: anonimal
assignees: []
labels: []
created_at: '2017-01-01T14:39:31+00:00'
updated_at: '2017-01-03T14:09:27+00:00'
type: issue
status: closed
closed_at: '2017-01-03T14:09:27+00:00'
---

# Original Description
https://build.getmonero.org/builders/kovri-all-ubuntu-arm7/builds/103/steps/benchmark/logs/stdio
https://build.getmonero.org/builders/kovri-all-debian-arm8/builds/99/steps/benchmark/logs/stdio

The build "fails" because of benchmarks timing out on ARM boxes. IMHO, 28 minutes is more than enough time to run benchmarks so I'm wondering if the problem is kovri-side. @danrmiller says that the machines may be to blame though, so info needed.

I had said I would do a cryptopp benchmark test and see if there are compiler flags that can resolve the situation. Ticketing for housekeeping while I look into that.

# Discussion History
## anonimal | 2017-01-01T15:46:15+00:00
@danrmiller JFTR, cubieboard takes about 42m16s to finish. I haven't tested the ARMv8 box though. Could we temporarily extend the timeout length to 45 min or maybe 60 for some wiggle room? Will this leave other builds in the queue during that duration? If so then I think we should just not run benchmarks on ARM until this issue is fully resolved.

## anonimal | 2017-01-01T16:42:09+00:00
Note: ARMv8 took 48m2s but buildbot was building at the time (kovri was also running).

## danrmiller | 2017-01-01T17:49:12+00:00
I've disabled the timeout for the test step and queued up armv7 and armv8 builds, which should run in a few hours. 

Also I'll look into appropriate scheduling/locking/queuing/parallel settings

## danrmiller | 2017-01-02T23:16:39+00:00
@anonimal see 
https://build.getmonero.org/builders/kovri-all-ubuntu-arm7/builds/104
https://build.getmonero.org/builders/kovri-all-debian-arm8/builds/100


## anonimal | 2017-01-03T14:09:27+00:00
Thanks @danrmiller.

Note: when https://github.com/monero-project/kovri/issues/498 is resolved, the timeout length shouldn't be an issue (for the time being). As for any compile-time optimizations, I'll deal with that in the kovri repo.

# Action History
- Created by: anonimal | 2017-01-01T14:39:31+00:00
- Closed at: 2017-01-03T14:09:27+00:00
