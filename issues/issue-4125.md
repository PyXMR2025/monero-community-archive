---
title: Monero wallet not syncing (stuck)
source_url: https://github.com/monero-project/monero/issues/4125
author: mcb345
assignees: []
labels: []
created_at: '2018-07-10T10:58:54+00:00'
updated_at: '2018-07-10T11:24:10+00:00'
type: issue
status: closed
closed_at: '2018-07-10T11:24:10+00:00'
---

# Original Description
I tried running monero using  
`./monerod --detach`  
and ran monero-wallet-rpc with following command :  
`/monero-wallet-rpc --rpc-bind-port <port_here>--rpc-bind-ip 0.0.0.0 --wallet-dir "/home/ubuntu/.bitmonero/" --disable-rpc-login --confirm-external-bind`  

and I tried checking whether the wallet has been fully synced or not using jsonrpc method `getheight`

It keeps returning me same height which is 207186

I already wait for some times, no luck

Any idea whats happening here ?

# Discussion History
# Action History
- Created by: mcb345 | 2018-07-10T10:58:54+00:00
- Closed at: 2018-07-10T11:24:10+00:00
