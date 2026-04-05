---
title: max-cpu-usage
source_url: https://github.com/xmrig/xmrig/issues/1003
author: guigeddos
assignees: []
labels:
- question
created_at: '2019-03-29T02:47:59+00:00'
updated_at: '2019-04-01T06:08:24+00:00'
type: issue
status: closed
closed_at: '2019-04-01T06:08:24+00:00'
---

# Original Description
This setting is useless at all. No matter how many CPUs are set, they are 100%.

# Discussion History
## tarris034 | 2019-03-30T12:14:02+00:00
Yes, it's useless as stated by the dev. It is deprecated.
if you want to use 50% of your CPU, use 50% of your cores.

 "threads": 1

will use 25% on a 4 core CPU and 12.5% on a 8 core CPU.

In the past max-cpu-usage was just modifying the threads in reality, so each thread/core is always 100%.

# Action History
- Created by: guigeddos | 2019-03-29T02:47:59+00:00
- Closed at: 2019-04-01T06:08:24+00:00
