---
title: Recommended zmq port conflict with recommended onion P2P port
source_url: https://github.com/monero-project/monero-site/issues/2589
author: li5lo
assignees: []
labels: []
created_at: '2026-01-16T05:10:16+00:00'
updated_at: '2026-01-16T20:10:33+00:00'
type: issue
status: closed
closed_at: '2026-01-16T20:10:33+00:00'
---

# Original Description
[This](https://www.reddit.com/r/Monero/comments/vga773/psa_to_public_node_operators_that_have_enabled/) old reddit post asks us to change the zmq port to 18084 to **not** conflict with monerod Tor port and [here](https://xmrvsbeast.com/p2pool/monero_nodes.html) it's 18084 too.

But the [Monero docs](https://docs.getmonero.org/running-node/monerod-tori2p/#node-configuration) and the [docs for anonymity networks](https://github.com/monero-project/monero/blob/master/docs/ANONYMITY_NETWORKS.md#configuration) mention port 18084 as the recommended port for onion P2P service.

Now i am confused.

What is the recommended port for zmq and what is the recommended port for onion P2P when i run a public node?

# Discussion History
## nahuhh | 2026-01-16T12:45:41+00:00
18080 p2p
18081 unrestricted rpc
18082 zmq rpc
18083 zmq pub
18084 tor inbound
18085 i2p inbound
18089 restricted rpc

See "Mainnet TCP ports" [here](https://docs.getmonero.org/infrastructure/networks/#mainnet) 


# Action History
- Created by: li5lo | 2026-01-16T05:10:16+00:00
- Closed at: 2026-01-16T20:10:33+00:00
