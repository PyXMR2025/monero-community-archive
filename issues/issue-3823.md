---
title: 'Feature request: xmrig.com benchmarks qol improvements?'
source_url: https://github.com/xmrig/xmrig/issues/3823
author: adapt-L
assignees: []
labels: []
created_at: '2026-06-12T13:42:16+00:00'
updated_at: '2026-07-06T06:50:14+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It would be nice if on the xmrig benchmarks site you could filter by per-package performance. So for multi-socket submissions it would divide performance by the # of CPUs used.

Also perhaps the engineering sample CPUs could be renamed more clearly, for example "AMD Eng Sample: 100-000000475-15" is really "AMD EPYC 9654 ES (100-000000475-15)".

I was also thinking if users could submit notes alongside their benchmarks, that could also be useful. For example BIOS or overclock settings, or usage of 1GB pages. It would make it easier for new miners to assess price:performance, and thus could help improve the network hashrate.

# Discussion History
## alby6969 | 2026-06-15T22:05:28+00:00
That would be pretty nice if you could add extra information like that.  Especially for bios tweaks and ram settings


## coffnix | 2026-07-06T06:50:13+00:00
We could improve XMRig by trying IPv4 or IPv6 based on a simple connectivity test, for example using netcat before starting the benchmark. This would avoid cases where IPv6 is selected by default even though it’s unreachable, causing the benchmark to never finish, as reported in bug https://github.com/xmrig/xmrig/issues/3692 

# Action History
- Created by: adapt-L | 2026-06-12T13:42:16+00:00
