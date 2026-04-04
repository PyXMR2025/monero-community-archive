---
title: monero-wallet-rpc --version doesn't output version
source_url: https://github.com/monero-project/monero/issues/2998
author: rwdim
assignees: []
labels:
- invalid
created_at: '2017-12-23T22:24:52+00:00'
updated_at: '2017-12-24T09:48:23+00:00'
type: issue
status: closed
closed_at: '2017-12-24T09:48:23+00:00'
---

# Original Description
> monero.monero-wallet-rpc --version
> Failed to parse arguments: the option '--rpc-bind-port' is required but missing


wallet-cli works, but rpc does not.

> monero.monero-wallet-cli --version
> Monero Helium Hydra (v0.11.1.0-release)

# Discussion History
## moneromooo-monero | 2017-12-24T00:46:10+00:00
It works on master, got fixed a few months ago. Did you test master ?

## rwdim | 2017-12-24T03:05:09+00:00
i built and installed v0.11.1.0 and hour before I posted and it occurs there.



## moneromooo-monero | 2017-12-24T09:47:19+00:00
OK, so most likely fixed.

+invalid


# Action History
- Created by: rwdim | 2017-12-23T22:24:52+00:00
- Closed at: 2017-12-24T09:48:23+00:00
