---
title: 'E Exception at while refreshing, what=reorg exceeds maximum allowed depth,
  use ''set max-reorg-depth N'' to allow it, reorg depth: 356'
source_url: https://github.com/monero-project/monero/issues/8147
author: 7jw92nVd1kLaq1
assignees: []
labels: []
created_at: '2022-01-18T13:25:02+00:00'
updated_at: '2022-02-18T22:57:45+00:00'
type: issue
status: closed
closed_at: '2022-02-18T22:57:45+00:00'
---

# Original Description
> wallet-rpc_1         |  2022-01-18 13:10:21.478    E reorg_depth > m_max_reorg_depth. THROW EXCEPTION: error::reorg_depth_error
> 
> wallet-rpc_1         | 2022-01-18 13:10:21.485  E Exception at while refreshing, what=reorg exceeds maximum allowed depth, use 'set max-reorg-depth N' to allow it, reorg depth: 356  


Here is the issue I am currently facing with launching the RPC server in a Docker container of Monero image using Dockerfile.

So, I was able to create a Docker image using Dockerfile successfully, and subsequently tried the RPC server out in a Docker container. And the errors I posted above keep popping up no matter which wallet I use to launch the server. I wonder if some of you guys deal with the same issue I am dealing with.



# Discussion History
## selsta | 2022-01-21T02:31:32+00:00
Is your node fully synced?

## selsta | 2022-02-18T22:57:44+00:00
No reply by the issue creator, closing.

# Action History
- Created by: 7jw92nVd1kLaq1 | 2022-01-18T13:25:02+00:00
- Closed at: 2022-02-18T22:57:45+00:00
