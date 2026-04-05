---
title: Affinity max value ?
source_url: https://github.com/xmrig/xmrig/issues/1293
author: srwx666
assignees: []
labels:
- bug
created_at: '2019-11-16T19:27:05+00:00'
updated_at: '2025-06-16T17:19:13+00:00'
type: issue
status: closed
closed_at: '2025-06-16T17:19:13+00:00'
---

# Original Description
Running latest version (4.5 also) on dual epyc 32c (not es)

without setting affinity (based on hwloc) all threads are not bind to core (-1 in stats)
setting -t64 with --cpu-affinity=0xFFFFFFFFFFFFFFFF gives exactly the same result (threads are not bind to cores)
setting -t64 --cpu-affinity=0xFFFFFFFFFFFFFFFE binds 0-62 threads to proper cores, and one not (-1)

didn't tested with config.json but proabably effect will be the same ?

thats quite strange, on dual ROME (128 threads) it's working OK...

any ideas ?

S


# Discussion History
## xmrig | 2019-11-16T19:58:16+00:00
Size of affinity is 64bit, so theoretically it can define up to 64 threads, but -1 used as no affinity, so only 63 values remaining, `0xFFFFFFFFFFFFFFFF == -1` it reason why miner didn't set affinity, I mark this issue as bug because if that value received from user, miner should bind 63 cores.

Config file has no such restriction and it really strange how 128 threads was work with this option.
Thank you.

## srwx666 | 2019-11-16T20:28:57+00:00
256 threads will be todays max probably.

## xmrig | 2025-06-16T17:19:13+00:00
@srwx666 6 years later: 512 threads https://xmrig.com/benchmark/5mJeLH

# Action History
- Created by: srwx666 | 2019-11-16T19:27:05+00:00
- Closed at: 2025-06-16T17:19:13+00:00
