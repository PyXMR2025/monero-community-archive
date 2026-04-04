---
title: Add more zmq features
source_url: https://github.com/monero-project/monero/issues/9192
author: Codi33
assignees: []
labels:
- question
- low priority
created_at: '2024-02-21T18:49:50+00:00'
updated_at: '2024-02-24T15:12:32+00:00'
type: issue
status: closed
closed_at: '2024-02-24T15:12:32+00:00'
---

# Original Description
Need more features in ZMQ to accept real-time payments.
Could be implemented using RPC but long polling is needed.
The information provided by txpool_add and chain_main events
is insufficient for verification.

# Discussion History
## vtnerd | 2024-02-21T21:26:26+00:00
Perhaps [LWS](https://github.com/vtnerd/monero-lws) will meet your needs? It has _receive_ notifications via Webhooks/ZMQ per monero address, and optionally per integrated address. There is also ZMQ notification on new address creation.

There is some [rough documentation](https://github.com/vtnerd/monero-lws/blob/master/docs/zmq.md) on LWS ZMQ usage.

## vtnerd | 2024-02-21T21:28:47+00:00
If you have further questions about LWS, I recommend opening an issue on LWS project page to track the discussion. Otherwise, it is unlikely that `monerod` will use ZMQ for real-time payments (because it is not designed to track user funds, which is different than `bitcoind` for instance).

## Codi33 | 2024-02-24T15:12:32+00:00
Thank you for answering my question! Your project is good solution for what I need.

# Action History
- Created by: Codi33 | 2024-02-21T18:49:50+00:00
- Closed at: 2024-02-24T15:12:32+00:00
