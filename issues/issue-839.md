---
title: restricted rpc modifications
source_url: https://github.com/monero-project/monero/issues/839
author: Gingeropolous
assignees: []
labels: []
created_at: '2016-05-14T12:22:24+00:00'
updated_at: '2016-05-17T17:09:21+00:00'
type: issue
status: closed
closed_at: '2016-05-17T17:09:21+00:00'
---

# Original Description
`MAP_URI_AUTO_JON2_IF("/mining_status", on_mining_status,)`

Does this need to be restricted?

`MAP_JON_RPC_WE("flush_txpool",           on_flush_txpool,               COMMAND_RPC_FLUSH_TRANSACTION_POOL)`

should probably be restricted. 


# Discussion History
## iamsmooth | 2016-05-16T02:14:47+00:00
I think mining_status should stay restricted, just in general because it isn't a service that is useful for most public nodes to provide to the public but also specifically because it gives out your address. If you have some special requirement in mind you can modify the code or find another way to do it, or you could add the ability to override the rpc restrictions (--rpc-restriction "mining_status=false")

Agree flush_txpool should definitely be restricted.


## iamsmooth | 2016-05-16T03:09:22+00:00
#843 


# Action History
- Created by: Gingeropolous | 2016-05-14T12:22:24+00:00
- Closed at: 2016-05-17T17:09:21+00:00
