---
title: Extremely high bandwidth usage
source_url: https://github.com/monero-project/monero/issues/1556
author: Snipa22
assignees: []
labels: []
created_at: '2017-01-10T20:14:42+00:00'
updated_at: '2021-08-13T05:01:12+00:00'
type: issue
status: closed
closed_at: '2021-08-13T05:01:12+00:00'
---

# Original Description
Hello,

I was doing an audit of my server/pool nodes, which run just Monerod, and noticed that several of them were performing extremely high levels of network transit, in excess of 200Mbit/second.  Based on this, I pulled a full stats logs for my servers, and noted almost 37Tb of traffic being transferred in the last week:
http://i.imgur.com/9joIAbL.png

This would equate out to over 12k blockchain syncs at this point, which seems quite excessive offhand, as this is only a week's worth of traffic.  I've gone ahead and reduced the speed of syncs on my boxes, but hope this can be resolved.

# Discussion History
## Snipa22 | 2017-01-11T21:38:13+00:00
Looks like a good chunk of this may be bad nodes trying to sync as well:
http://i.imgur.com/rU03eaU.png

## moneromooo-monero | 2017-08-01T10:01:11+00:00
https://github.com/monero-project/monero/pull/2149 will help a fair amount (once your peers have updated).

## moneromooo-monero | 2017-09-20T21:08:41+00:00
What does it look like now ? :)

## moneromooo-monero | 2020-05-17T14:59:44+00:00
monerod should now use about a third less bandwidth, and another third less once most other nodes have updated.

## selsta | 2021-08-13T05:01:12+00:00
06:07 <Snipa> Haven't checked in forever.  My ISP's stoped complaining, so I'll assume they're fine.

# Action History
- Created by: Snipa22 | 2017-01-10T20:14:42+00:00
- Closed at: 2021-08-13T05:01:12+00:00
