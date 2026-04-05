---
title: Dual Intel Xeon 5639 only using 1 CPU?
source_url: https://github.com/xmrig/xmrig/issues/329
author: sirbig
assignees: []
labels:
- NUMA
created_at: '2018-01-09T02:34:57+00:00'
updated_at: '2018-01-09T09:01:18+00:00'
type: issue
status: closed
closed_at: '2018-01-09T09:01:18+00:00'
---

# Original Description
Hello,

First of all I'm new in the mining world so don't judge me if this is a dummy post, please.
I currently have one dedicated server running Dual Intel Xeon 5639 with CentOS 7.

Clockspeed: 2.1 GHz
Turbo Speed: 2.7 GHz
No of Cores: 6 (2 logical cores per physical) x 2 = 12 cores with 24 threads
L2/L3: 6MB/24MB

While running xmrig it only uses 50% of the CPU with 12 threads, why isn't it running 100% with 24 threads?



# Discussion History
## xmrig | 2018-01-09T05:42:25+00:00
6 threads per CPU is optimal, because for optimal performance each thread required 2 MB of CPU cache. 12 MB L3 / 2 = 6.
Thank you.

## sirbig | 2018-01-09T09:01:07+00:00
I see, I'm almost hiting 400 H/s with that so it's not that bad for a free machine I guess.
Thanks for the fast response and keep on improving this amazing project! 👍 

# Action History
- Created by: sirbig | 2018-01-09T02:34:57+00:00
- Closed at: 2018-01-09T09:01:18+00:00
