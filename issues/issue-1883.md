---
title: Add ZMQ documentation to developer guides
source_url: https://github.com/monero-project/monero-site/issues/1883
author: CryptoGrampy
assignees: []
labels:
- '📚 docs: dev guides'
- enhancement
created_at: '2021-11-03T15:01:13+00:00'
updated_at: '2024-07-18T08:28:47+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
There is currently zero :wink:  documentation on using ZMQ with Monerod.    Would like to see this added to https://www.getmonero.org/resources/developer-guides/ that describes how to use it, and what topics can be subscribed/published(?) to.  Perhaps a 'why would I use this' would be helpful as well.  

# Discussion History
## CryptoGrampy | 2021-11-04T15:36:09+00:00
Was referred to this doc from someone in Monero-Dev.  Would be helpful in creating a dev guide: https://github.com/monero-project/monero/blob/master/docs/ZMQ.md 

I also asked VTNerd about potential upcoming additions to ZMQ in Monero Dev: 
_maybe_ msgpack in addition to json - the notifications are "slow" enough it probably only matters during syncing
there's also the possibility of CurveZMQ for TLS like security
"slow" -> once sync'ed the number of notifications per sec is somewhat low

## plowsof | 2024-07-18T08:28:46+00:00
A CCS proposal in the Idea stage is planning on completing this issue https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/479

# Action History
- Created by: CryptoGrampy | 2021-11-03T15:01:13+00:00
