---
title: Max temperature option
source_url: https://github.com/xmrig/xmrig/issues/259
author: Mek7
assignees: []
labels:
- enhancement
created_at: '2017-12-12T16:14:42+00:00'
updated_at: '2021-04-18T00:55:02+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello,
first I want to say, xmrig is a great miner, thanks for putting the effort into it!
I have an idea to make it even better - to avoid CPU/GPU overheating, it would be good to have the possibility to specify maximum temperature - e.g. use only such hashrate that temperature does not exceed specified value.
I hope this can be useful also for others :)

# Discussion History
## mxjoe | 2017-12-12T16:24:41+00:00
This is a nice feature request for the future. But I think it might be hard to get temperature control over several OS's.
What you also could do to lower the temperature is reduce the max-cpu-usage value.

## xmrig | 2017-12-16T12:10:09+00:00
This option can be added only to NVIDIA miner, for others need implement reading temperature first.
Thank you.

## tanengtiong0918 | 2021-04-18T00:55:02+00:00
Consider a feature for balancing all temperature related hardwares, or just topical documentation, then most users wouldnt bother setting them up.

# Action History
- Created by: Mek7 | 2017-12-12T16:14:42+00:00
