---
title: how to limit gpu usage with only one cpu ?
source_url: https://github.com/xmrig/xmrig/issues/2610
author: luckBegin
assignees: []
labels: []
created_at: '2021-09-30T04:14:26+00:00'
updated_at: '2021-09-30T12:30:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
set max-threads-hint look like not working 

# Discussion History
## Spudz76 | 2021-09-30T12:29:56+00:00
It's a... hint.  It will not force anything.  You also must not have any existing thread profiles in config.json or it won't rerun autoconfig thus won't even look at max-threads-hint since it already has thread profiles.

Also if you ask for 0 cores it will still give you 1.  And it's in percent of cores and always rounds upward.  So if you say 30% but have 8 cores that's 2.4 threads requested but you will get 3.

Much easier to just edit the thread profiles by hand in config.json.

## Spudz76 | 2021-09-30T12:30:46+00:00
Also how would this help GPU?  Maybe I don't quite follow your setup or question or problem.

# Action History
- Created by: luckBegin | 2021-09-30T04:14:26+00:00
