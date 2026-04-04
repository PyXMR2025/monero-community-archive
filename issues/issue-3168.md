---
title: File descriptor leaks
source_url: https://github.com/monero-project/monero/issues/3168
author: Gingeropolous
assignees: []
labels:
- duplicate
created_at: '2018-01-21T13:54:26+00:00'
updated_at: '2018-01-21T14:00:28+00:00'
type: issue
status: closed
closed_at: '2018-01-21T14:00:28+00:00'
---

# Original Description
When providing service as a remote node (opening the daemon to multiple and concurrent RPC connections), the amount of connections detectable via ```netstat -anp ``` for the RPC port seems to always increase over time. 

# Discussion History
## moneromooo-monero | 2018-01-21T13:58:38+00:00
See... somewhere in the issues, fairly close to the oldest ones.

+duplicate


# Action History
- Created by: Gingeropolous | 2018-01-21T13:54:26+00:00
- Closed at: 2018-01-21T14:00:28+00:00
