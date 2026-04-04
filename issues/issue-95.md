---
title: Rpcwallet crashes without leaving a clue behind while the daemon is initializing
source_url: https://github.com/monero-project/monero/issues/95
author: Jojatekok
assignees: []
labels: []
created_at: '2014-08-17T16:57:20+00:00'
updated_at: '2015-11-24T14:38:15+00:00'
type: issue
status: closed
closed_at: '2015-11-24T14:38:15+00:00'
---

# Original Description
The new rpcwallet simply exits (without leaving an error message behind) whether opened straight after the daemon: The daemon starts loading the blockchain, and that results in the rpcwallet closing. Please let the wallet check for the daemon's RPC port to be active, thus, indicating that it has already loaded the chain.


# Discussion History
## fluffypony | 2015-11-24T14:38:15+00:00
Fixed


# Action History
- Created by: Jojatekok | 2014-08-17T16:57:20+00:00
- Closed at: 2015-11-24T14:38:15+00:00
