---
title: Further optimizing AstroBWT hash skipping
source_url: https://github.com/xmrig/xmrig/issues/1597
author: nYrXvcpk2l47ciid
assignees: []
labels: []
created_at: '2020-03-19T17:59:17+00:00'
updated_at: '2020-03-19T18:18:30+00:00'
type: issue
status: closed
closed_at: '2020-03-19T18:18:29+00:00'
---

# Original Description
Regarding commit eeadea53e2ee0841927e23fbf97bd26848b8dc86, how can one benchmark their hardware to find what range of values may be most optimal for the --astrobwt-max-size flag? Seeing as the default of 550 is a middle ground of sorts between cpus, it would be nice if one could fine-tune it. @SChernykh, did you happen to get the values for the different cpus from some benchmarking program?

# Discussion History
## SChernykh | 2020-03-19T18:16:54+00:00
I found little difference between all values in 500-600 range on my CPUs (both AMD and Intel), values outside that range were worse.

## nYrXvcpk2l47ciid | 2020-03-19T18:18:29+00:00
Thanks for the closure.

# Action History
- Created by: nYrXvcpk2l47ciid | 2020-03-19T17:59:17+00:00
- Closed at: 2020-03-19T18:18:29+00:00
