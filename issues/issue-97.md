---
title: Rpcwallet doesn't wait (enough?) for the daemon RPC's initialization
source_url: https://github.com/monero-project/monero/issues/97
author: Jojatekok
assignees: []
labels: []
created_at: '2014-08-21T08:24:47+00:00'
updated_at: '2014-08-21T14:55:52+00:00'
type: issue
status: closed
closed_at: '2014-08-21T14:55:52+00:00'
---

# Original Description
2014-Aug-21 09:58:20.960909 ERROR C:\Users\user\Desktop\bitmonero-daemonize_wip\contrib\epee\include\net/http_client.h:867 failed to connect localhost:18081

It was definitely NOT 20 seconds of waiting before throwing the error above, and also, the daemon port becomes alive even before 20 seconds


# Discussion History
## Jojatekok | 2014-08-21T14:55:52+00:00
Compiling from the new 'development' branch seems to solve this issue


# Action History
- Created by: Jojatekok | 2014-08-21T08:24:47+00:00
- Closed at: 2014-08-21T14:55:52+00:00
