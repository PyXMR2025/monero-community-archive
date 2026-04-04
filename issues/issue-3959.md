---
title: Multiple RPC calls raises error message
source_url: https://github.com/monero-project/monero/issues/3959
author: ghost
assignees: []
labels: []
created_at: '2018-06-08T10:15:39+00:00'
updated_at: '2018-06-08T21:03:46+00:00'
type: issue
status: closed
closed_at: '2018-06-08T21:03:46+00:00'
---

# Original Description
I run a perl script that makes multiple RPC calls to extract difficulty and timestamp data. When script is ran on Monero v0.12.2.0, the script stalls, the deamon pushes CPU usage over 100%, and I get the following error:

`ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:1117	Exception at [boosted_tcp_server<t_protocol_handler>::connect], what=open: Too many open files`

Issue might be related to commit https://github.com/monero-project/monero/commit/4d158647289088ef316da44cc06146f049179137

https://github.com/wownero/wownero/issues/50

# Discussion History
## moneromooo-monero | 2018-06-08T11:55:13+00:00
What is that script ?

## moneromooo-monero | 2018-06-08T19:15:12+00:00
https://github.com/monero-project/monero/pull/3962

## ghost | 2018-06-08T21:03:46+00:00
Issue resolved. Thank you @moneromooo-monero.

# Action History
- Created by: ghost | 2018-06-08T10:15:39+00:00
- Closed at: 2018-06-08T21:03:46+00:00
