---
title: monero-wallet-rpc won't connect to remote node
source_url: https://github.com/monero-project/monero/issues/8236
author: MajesticBank
assignees: []
labels: []
created_at: '2022-04-02T16:17:12+00:00'
updated_at: '2022-05-29T15:33:20+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello,


The issue appears when trying to use monero-wallet-rpc with remote node inside virtual machine behind tor network when using Linux but also when using directly on Windows without virtual machine but behind tor network 

I initially tried 

--daemon-address node.majesticbank.is --daemon-port 18089

--daemon-address majesticrepik35vnngouksfl7jiwf6sj7s2doj3bvdffq27tgqoeayd.onion --daemon-port 18089

--daemon-address node.majesticbank.is --daemon-port 18089 --proxy 127.0.0.1:9050 --daemon-ssl-allow-any-cert


Error before workaround:

E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
E Wallet initialization failed: no connection to daemon

I figured workaround using ssh / socat to connect to remote node and bind local port which works

Error after workaround:

E Failed to query mining status: No connection to daemon
I Binding on 127.0.0.1 (IPv4):28090
W Starting wallet RPC server

Seems like timeout issue







# Discussion History
# Action History
- Created by: MajesticBank | 2022-04-02T16:17:12+00:00
