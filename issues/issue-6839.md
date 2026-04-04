---
title: Deploy monero testnet myself ,can't sync
source_url: https://github.com/monero-project/monero/issues/6839
author: GongSuiLi
assignees: []
labels: []
created_at: '2020-09-24T07:15:38+00:00'
updated_at: '2021-08-13T04:58:31+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:58:31+00:00'
---

# Original Description
Recently I used monero v0.15.0.5 to deploy, and started the monerod service on testnet. It can only synchronize to 1544280 height, and then no synchronization is performed. The log is as follows. I tried to use a different server and tried to use the new version v0.16.0.3. It's all the same problem, how can I solve it？

=======
Is it because of the testnet fork? If so, when will the release version be available?


2020-09-23 11:18:20.307	[P2P1]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
2020-09-23 11:18:52.420	[P2P1]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1733	Version 0.16.0.3 of monero for linux-x64 is available: https://downloads.getmonero.org/cli/monero-linux-x64-v0.16.0.3.tar.bz2, SHA256 hash cb67ad0bec9a342b0f0be3f1fdb4a2c8d57a914be25fc62ad432494779448cc3
2020-09-23 13:18:20.988	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
2020-09-23 13:19:11.754	[P2P2]	WARNING	global	src/p2p/net_node.inl:1821	No incoming connections - check firewalls/routers allow port 28080
2020-09-23 14:19:59.095	[P2P0]	WARNING	global	src/p2p/net_node.inl:1821	No incoming connections - check firewalls/routers allow port 28080

# Discussion History
## selsta | 2020-09-24T09:04:48+00:00
Please try v0.17.0.0

## GongSuiLi | 2020-09-24T10:19:10+00:00
> Please try v0.17.0.0

Thank you, I think I should wait for the v0.17.0.0 release package, not source code. 

## ghost | 2020-09-24T12:07:33+00:00
v0.17 CLI  can download at Getmonero.org , dont know why  the website and github  not synchronous update.

## moneromooo-monero | 2020-09-24T12:43:53+00:00
That height looks like it might be the first CLSAG transaction, which you need 0.17 to understand.


# Action History
- Created by: GongSuiLi | 2020-09-24T07:15:38+00:00
- Closed at: 2021-08-13T04:58:31+00:00
