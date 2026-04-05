---
title: max-threads-hint issue [VERY IMPORTANT]
source_url: https://github.com/xmrig/xmrig/issues/1342
author: XeroProg
assignees: []
labels:
- question
created_at: '2019-11-30T21:02:00+00:00'
updated_at: '2019-12-22T19:41:35+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:41:35+00:00'
---

# Original Description
Hi.When i enter 100 in max-threads-hint it doesn't work and it use just 75% of my system.
my system has 4 cores
for 25% , 50% , 75% it doesn't have any problem but for this one (100%) it doesn't work and it just uses 75% of my computer cpu
what is the problem ? how i can fix it?

# Discussion History
## xmrig | 2019-12-02T01:16:22+00:00
Did you read docs carefully? https://github.com/xmrig/xmrig/blob/master/doc/CPU_MAX_USAGE.md likely your CPU limited by L2/L3 cache.
Thank you.

# Action History
- Created by: XeroProg | 2019-11-30T21:02:00+00:00
- Closed at: 2019-12-22T19:41:35+00:00
