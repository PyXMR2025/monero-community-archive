---
title: ARMv7 buildbot warning - looks like another 32 vs 64 bit issue
source_url: https://github.com/monero-project/monero/issues/1238
author: ghost
assignees: []
labels: []
created_at: '2016-10-20T08:44:36+00:00'
updated_at: '2016-10-21T01:13:22+00:00'
type: issue
status: closed
closed_at: '2016-10-21T01:13:22+00:00'
---

# Original Description
```
In file included from /home/buildbot/slave/monero-static-ubuntu-arm7/build/src/common/perf_timer.cpp:29:0:
/home/buildbot/slave/monero-static-ubuntu-arm7/build/src/common/perf_timer.h: In destructor ‘tools::PerformanceTimer::~PerformanceTimer()’:
/home/buildbot/slave/monero-static-ubuntu-arm7/build/src/common/perf_timer.h:71:43: warning: format ‘%lu’ expects argument of type ‘long unsigned int’, but argument 4 has type ‘uint64_t {aka long long unsigned int}’ [-Wformat=]
     snprintf(s, sizeof(s), "%8lu  ", ticks);
```

Hmm...does the tick holder need to be 64 bits long or if changed to 32 would we be maintaining backwards compatibility for no good reason?


# Discussion History
## moneromooo-monero | 2016-10-20T17:44:50+00:00
https://github.com/monero-project/monero/pull/1239


## ghost | 2016-10-21T01:13:22+00:00
Cool. Closing.


# Action History
- Created by: ghost | 2016-10-20T08:44:36+00:00
- Closed at: 2016-10-21T01:13:22+00:00
