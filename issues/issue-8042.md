---
title: RPC setup
source_url: https://github.com/monero-project/monero/issues/8042
author: S1700
assignees: []
labels: []
created_at: '2021-11-04T18:44:03+00:00'
updated_at: '2021-11-05T18:31:07+00:00'
type: issue
status: closed
closed_at: '2021-11-05T18:31:07+00:00'
---

# Original Description
So I'm setting up monerod for a pool that I am making but when I am running monerod it says that RPC has already been initialized but when I use the IP and port that it lists it says that there is no RPC server on that IP/port. So I try running `monero-wallet-rpc` and it cant bind to the IP/port because it is already in use?

# Discussion History
## selsta | 2021-11-04T23:50:30+00:00
Please post the exact commands you are using.

## S1700 | 2021-11-05T18:15:26+00:00
 ./monero-wallet-rpc --rpc-bind-port 18080 --wallet-file moneropool --log-level 1 --prompt-for-password

## selsta | 2021-11-05T18:24:20+00:00
18080 is the default p2p port, you can't bind `monero-wallet-rpc` to it. Use for example 18083 instead.

## S1700 | 2021-11-05T18:28:52+00:00
ah alr sorry for making a issue for something so simple

## selsta | 2021-11-05T18:31:07+00:00
There are the default daemon ports:

```
18080: P2P port
18081: RPC port
18082: ZMQ port
```

Closing as the question seems resolved.

# Action History
- Created by: S1700 | 2021-11-04T18:44:03+00:00
- Closed at: 2021-11-05T18:31:07+00:00
