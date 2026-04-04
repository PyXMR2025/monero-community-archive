---
title: 'blocks sync : last 2%  is slow'
source_url: https://github.com/monero-project/monero/issues/7421
author: unamefailed
assignees: []
labels: []
created_at: '2021-03-03T18:09:05+00:00'
updated_at: '2021-08-13T04:53:19+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:53:19+00:00'
---

# Original Description
it's a VPS , SSD hard disk  

From 0 to 98% took 9 hours,  The last 40000+  blocks(2%) has been working several hours  and it says "I Synced 2280357/2309052 (98%, 28695 left, 24% of total synced, estimated 5.9 hours left)" , I have tried restarting  monerod  and rise out_peers to 60 But still slow . 
 is it normal?

# Discussion History
## selsta | 2021-03-03T19:51:21+00:00
There has been no new release in ~2 months, meaning the last fast sync checkpoint is also 2 months old. This is normal.

# Action History
- Created by: unamefailed | 2021-03-03T18:09:05+00:00
- Closed at: 2021-08-13T04:53:19+00:00
