---
title: '[Question] How to use Monero over i2p'
source_url: https://github.com/monero-project/monero/issues/5628
author: ghbjklhv
assignees: []
labels: []
created_at: '2019-06-11T22:51:38+00:00'
updated_at: '2021-08-16T03:45:47+00:00'
type: issue
status: closed
closed_at: '2021-08-16T03:45:47+00:00'
---

# Original Description
**Question**: I read online that Monero can be used over i2p (source might be false).
This would provide obvious advantages. Are there any tutorials or projects pursuing this?

Source: https://en.wikipedia.org/wiki/I2P#Crypto-Currency

# Discussion History
## moneromooo-monero | 2019-06-11T23:09:58+00:00
Did you read https://github.com/monero-project/monero/blob/master/ANONYMITY_NETWORKS.md ? If so, please feel free to update it for clarity, etc.

Note that you need the current code from master for this to work, 0.14.0.2 is too old. There will (hopefully) be a release with the necessary code very soon.


## MaxXor | 2019-06-14T15:30:59+00:00
@moneromooo-monero Will v0.14.1.0 work with I2P?

## moneromooo-monero | 2019-06-14T18:02:27+00:00
Probably.

## jtgrassie | 2019-06-21T22:02:53+00:00
> Will v0.14.1.0 work with I2P?

Yes it does. Use i2p-zero, create a socks tunnel (bound to a port like 4444) and a server tunnel (bound to port 18081). When starting your daemon, specify `--proxy i2p,127.0.0.1:4444`, `--anonymous-inbound your-server-tunnel.b32.i2p:18081,127.0.0.1:18081`. If you know any other peers running via i2p, you can also add them with `--add-peer some-other.b32.i2p:18081`. And read the docs.

## xanoni | 2021-08-16T03:44:43+00:00
can be closed

# Action History
- Created by: ghbjklhv | 2019-06-11T22:51:38+00:00
- Closed at: 2021-08-16T03:45:47+00:00
