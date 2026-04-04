---
title: Limits don't match
source_url: https://github.com/monero-project/monero/issues/327
author: Gingeropolous
assignees: []
labels: []
created_at: '2015-06-21T16:19:21+00:00'
updated_at: '2016-01-25T18:18:21+00:00'
type: issue
status: closed
closed_at: '2016-01-25T18:18:21+00:00'
---

# Original Description
Modified the limit with the general limit flag, and the up/down don't change. 

  --seed-node arg                       Connect to a node to retrieve peer
                                        addresses, and disconnect
  --hide-my-port                        Do not announce yourself as peerlist
                                        candidate
  --no-igd                              Disable UPnP port mapping
  --out-peers arg (=-1)                 set max limit of out peers
  --tos-flag arg (=-1)                  set TOS flag
  --limit-rate-up arg (=-1)             set limit-rate-up [kB/s]
  --limit-rate-down arg (=-1)           set limit-rate-down [kB/s]
  --limit-rate arg (=128)               set limit-rate [kB/s]
  --save-graph                          Save data for dr monero
  --rpc-bind-ip arg (=127.0.0.1)        IP for RPC server
  --rpc-bind-port arg (=18081)          Port for RPC server
  --testnet-rpc-bind-port arg (=28081)  Port for testnet RPC server

**_e5405@e5405-G31M-ES2L:~/new_bitmonero/bitmonero/build/release/bin$ ./2bitmonerod --testnet --limit-rate 999**_
Creating the logger system
2015-Jun-21 12:16:14.449237 Initializing cryptonote protocol...
2015-Jun-21 12:16:14.501151 Cryptonote protocol initialized OK
2015-Jun-21 12:16:14.501536 Initializing p2p server...
**_2015-Jun-21 12:16:14.541771 Set limit-up to 128 kB/s
2015-Jun-21 12:16:14.542094 Set limit-down to 128 kB/s
2015-Jun-21 12:16:14.542472 Set limit to 999 kB/s**_
2015-Jun-21 12:16:14.570333 Binding on 0.0.0.0:28080
2015-Jun-21 12:16:14.570623 Net service bound to 0.0.0.0:28080
2015-Jun-21 12:16:14.570731 Attempting to add IGD port mapping.
2015-Jun-21 12:16:18.575192 No IGD was found.
2015-Jun-21 12:16:18.575326 P2p server initialized OK
2015-Jun-21 12:16:18.575584 Initializing core rpc server...
2015-Jun-21 12:16:18.575754 Binding on 127.0.0.1:28081


# Discussion History
## fluffypony | 2016-01-25T18:18:21+00:00
Overall limits take precedence over up/down if specified, so this is correct and to spec. It'll be done...better...when we change the wire protocol.


# Action History
- Created by: Gingeropolous | 2015-06-21T16:19:21+00:00
- Closed at: 2016-01-25T18:18:21+00:00
