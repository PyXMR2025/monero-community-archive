---
title: monerod RPC server should not be listening on all interlaces by default
source_url: https://github.com/monero-project/monero/issues/7983
author: adrelanos
assignees: []
labels: []
created_at: '2021-09-30T17:14:21+00:00'
updated_at: '2021-09-30T17:26:19+00:00'
type: issue
status: closed
closed_at: '2021-09-30T17:26:19+00:00'
---

# Original Description
    monerod --version

> Monero 'Oxygen Orion' (v0.17.2.3-release)

    monerod

> 2021-09-30 17:00:49.882 I Binding on 127.0.0.1 (IPv4):18081
> 2021-09-30 17:00:50.075 I core RPC server initialized OK on port: 18081

Quote monerod man page:

> --public-node | Advertise to other users they can use this node as a remote one for connecting their wallets. Requires --restricted-rpc, --rpc-bind-ip and --confirm-external-bind. Without --public-node the node can still be public (assuming other relevant options are set) but won't be advertised as such on the P2P network. This option will allow wallets to auto-discover public nodes (instead of requiring user to manually find one).

Not using `--public-node`.

> --rpc-bind-port | TCP port to listen on. By default 18081 (mainnet)

18081 = default RPC port.

> --rpc-bind-ip | IP to listen on. By default 127.0.0.1 because API gives full administrative capabilities over the node. Set it to 0.0.0.0 to listen on all interfaces - but only in connection with one of *-restricted-* options and --confirm-external-bind.

Man page saying RPC binding by default on localhost 127.0.0.1 only. And with good reason, "because API gives full administrative capabilities over the node". 

Exactly doesn't seem to be happening. monerod is listening on all interfaces 0.0.0.0.

    netstat -tulpen | grep monero

> tcp        0      **0 0.0.0.0**:18080           0.0.0.0:*               LISTEN      1000       47239      4789/monerod
> tcp        0      0 127.0.0.1:18081         0.0.0.0:*               LISTEN      1000       47240      4789/monerod
> tcp        0      0 127.0.0.1:18082         0.0.0.0:*               LISTEN      1000       47242      4789/monerod

Running `monerod --rpc-bind-ip 127.0.0.1` does not fix the issue either. monerod still listening on all interfaces 0.0.0.0.

Functional workaround is `monerod --rpc-bind-ip 127.0.0.1 --p2p-bind-ip 127.0.0.1`.

    netstat -tulpen | grep monero

> tcp        0      0 127.0.0.1:18080         0.0.0.0:*               LISTEN      1000       49119      4873/monerod
> tcp        0      0 127.0.0.1:18081         0.0.0.0:*               LISTEN      1000       49120      4873/monerod
> tcp        0      0 127.0.0.1:18082         0.0.0.0:*               LISTEN      1000       49122      4873/monerod


# Discussion History
## selsta | 2021-09-30T17:24:41+00:00
Seems like you are confusing P2P (18080) and RPC (18081) port. You want P2P to bind on 0.0.0.0 so that other nodes can connect to your node.

>tcp 0 0 0.0.0.0:18080 0.0.0.0:* LISTEN 1000 47239 4789/monerod
>tcp 0 0 127.0.0.1:18081 0.0.0.0:* LISTEN 1000 47240 4789/monerod
>tcp 0 0 127.0.0.1:18082 0.0.0.0:* LISTEN 1000 47242 4789/monerod

The RPC port binds on 127.0.0.1 here so there is no risk regarding "administrative capabilities".


## adrelanos | 2021-09-30T17:26:19+00:00
My mistake.
Thank you!

# Action History
- Created by: adrelanos | 2021-09-30T17:14:21+00:00
- Closed at: 2021-09-30T17:26:19+00:00
