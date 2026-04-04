---
title: RPC API Auth issue
source_url: https://github.com/monero-project/monero/issues/3022
author: jinglics
assignees: []
labels:
- invalid
created_at: '2017-12-28T16:08:32+00:00'
updated_at: '2017-12-28T19:24:24+00:00'
type: issue
status: closed
closed_at: '2017-12-28T19:24:24+00:00'
---

# Original Description
I tried monerod and monero-wallet-rpc with rpc-login. But it only can be accessed using curl or python.
Is there any way to use digest auth in C++ or Nodejs? Thanks

# Discussion History
## moneromooo-monero | 2017-12-28T19:21:43+00:00
It can be accessed with a client in whatever language you want, you just need to send the right data. It's also possible in C++, since monero-wallet-cli optionally does it to connect to monerod.

+invalid


# Action History
- Created by: jinglics | 2017-12-28T16:08:32+00:00
- Closed at: 2017-12-28T19:24:24+00:00
