---
title: 'Minor feature request: keep certain algo datasets in memory always'
source_url: https://github.com/xmrig/xmrig/issues/1457
author: ndorf
assignees: []
labels:
- enhancement
created_at: '2019-12-23T01:05:24+00:00'
updated_at: '2021-04-12T15:07:08+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:07:08+00:00'
---

# Original Description
When mining on the MoneroOcean pool, the algo changes regularly between rx/0 and others (e.g. rx/loki, rx/v). When the algo changes, this apparently causes XMRig to discard the initial dataset for the old algorithm, and initialize one for the new one. This seems to take about 3.5 seconds on my 3600.

That seems suboptimal when the machine is dedicated to mining, since almost all machines will have 8GB of RAM, and I'm guessing most will have 16GB (like mine). Would it make sense to just keep certain ones around always, to avoid this initialization delay every time the algo changes?

Of course, there's no telling in advance how many different algos the pool will use. I think that could be cleanly handled by explicitly configuring the ones you want to never discard, though. E.g. `"keep_data":["rx/0","rx/loki"]`. Any ones not in the list would be created/discarded on demand, as before.

Feel free to close if this is a stupid idea or simply too much work.

# Discussion History
## SChernykh | 2019-12-23T15:03:26+00:00
It's possible to do, but each dataset requires 2080 MB of free RAM, and only one dataset is guaranteed to have huge pages enabled, so some additional time will be spent to copy data when switching.

# Action History
- Created by: ndorf | 2019-12-23T01:05:24+00:00
- Closed at: 2021-04-12T15:07:08+00:00
