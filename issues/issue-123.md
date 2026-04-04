---
title: Transaction history can dissapear depending on advanced filter
source_url: https://github.com/monero-project/monero-gui/issues/123
author: medusadigital
assignees: []
labels: []
created_at: '2016-11-06T21:48:37+00:00'
updated_at: '2016-11-13T17:40:31+00:00'
type: issue
status: closed
closed_at: '2016-11-13T17:40:31+00:00'
---

# Original Description
Transaction history can dissapear depending on advanced filter.

Reproduce:

- open monero-core freshly
- go to transaction history tab
- swictch advanced filter to "SENT"
- press filter button
- switch advanced gilter to "ALL"
- press filter button




# Discussion History
## mbg033 | 2016-11-08T12:34:19+00:00
@medusadigital, I just checked it with my [develop](https://github.com/mbg033/monero-core/commits/develop), couldn't reproduce the issue. This branch contains merged PRs: https://github.com/monero-project/monero-core/pull/119, https://github.com/monero-project/monero-core/pull/120


## medusadigital | 2016-11-09T09:03:58+00:00
ok, will try again once stuff merged. too many PRs pending right now to get a clear picture. 
when i tried i tested without #119 and #120.


## M5M400 | 2016-11-10T09:05:47+00:00
tried to reproduce this, but advanced filter does not work at all for me. I can set to "sent", "received", enter min/max amounts... it always shows me the complete history, no matter how often I hit the "filter" button. c9bb2f5


## taushet | 2016-11-12T07:26:32+00:00
I could not reproduce this.


## medusadigital | 2016-11-13T17:40:31+00:00
cant reproduce myself either, seems to be an anomaly --> close


# Action History
- Created by: medusadigital | 2016-11-06T21:48:37+00:00
- Closed at: 2016-11-13T17:40:31+00:00
