---
title: "ERROR\tcn.block_queue\tsrc/cryptonote_protocol/cryptonote_protocol_handler.h:95\t\
  Error in handle_invoke_map: Attempt to get cumulative difficulty from height 2241261\
  \ failed -- difficulty not in db"
source_url: https://github.com/monero-project/monero/issues/7047
author: Gingeropolous
assignees: []
labels: []
created_at: '2020-11-30T04:10:55+00:00'
updated_at: '2021-01-09T01:39:37+00:00'
type: issue
status: closed
closed_at: '2021-01-09T01:39:37+00:00'
---

# Original Description
I have 24 instances of this over 3 days. 

this is on a node with its RPC ports publicly listed and its also mining (via other machines pointing xmrig to this daemon) 

# Discussion History
## moneromooo-monero | 2020-12-06T16:39:11+00:00
That usually means your db is toast.

# Action History
- Created by: Gingeropolous | 2020-11-30T04:10:55+00:00
- Closed at: 2021-01-09T01:39:37+00:00
