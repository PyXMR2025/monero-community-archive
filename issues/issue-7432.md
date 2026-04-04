---
title: Can't start RPC without daemon
source_url: https://github.com/monero-project/monero/issues/7432
author: mrx23dot
assignees: []
labels: []
created_at: '2021-03-05T15:05:47+00:00'
updated_at: '2021-03-11T09:14:27+00:00'
type: issue
status: closed
closed_at: '2021-03-11T09:14:27+00:00'
---

# Original Description
monero-wallet-rpc --wallet-file wallet --password xxx --rpc-bind-port 28089 --rpc-bind-ip 127.0.0.1 --disable-rpc-login
Monero 'Oxygen Orion' (v0.17.1.9-release) 
Win10 64x

2021-03-05 15:01:58.267 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-05 15:01:58.268 E Wallet initialization failed: no connection to daemon
then exits

I want to assign daemon-address from RPC later, since servers can change.

# Discussion History
## ndorf | 2021-03-05T17:40:30+00:00
Pass the `--offline` flag to `monero-wallet-rpc`.

## mrx23dot | 2021-03-08T15:58:19+00:00
That solves it, without offline param it gives these extra lines:

> 2021-03-08 15:54:50.925 D Reconnecting...
> 2021-03-08 15:54:52.930 D Some problems at connect, message: No connection could be made because the target machine actively refused it
> 2021-03-08 15:54:52.932 D Failed to connect to localhost:18081
> 2021-03-08 15:54:52.932 I Failed to invoke http request to  /getheight
> 2021-03-08 15:54:53.051 D Reconnecting...
> 2021-03-08 15:54:55.058 D Some problems at connect, message: No connection could be made because the target machine actively refused it
> 2021-03-08 15:54:55.059 D Failed to connect to localhost:18081
> 2021-03-08 15:54:55.059 I Failed to invoke http request to  /json_rpc
> 2021-03-08 15:54:55.059 E Failed to connect to daemon
> 2021-03-08 15:54:55.060 D Reconnecting...
> 2021-03-08 15:57:17.614 D Reconnecting...
> 2021-03-08 15:57:19.616 D Some problems at connect, message: No connection could be made because the target machine actively refused it
> 2021-03-08 15:57:19.616 D Failed to connect to localhost:18081
> 2021-03-08 15:57:19.617 I Failed to invoke http request to  /gethashes.bin
> 2021-03-08 15:57:19.618 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
> 2021-03-08 15:57:19.618 W /home/ubuntu/build/monero/src/wallet/wallet2.cpp:13997:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = gethashes.bin
> 2021-03-08 15:57:19.618 E Exception at while refreshing, what=no connection to daemon

Shouldn't --offline  be the default when there is no --daemon-address specified?

## ndorf | 2021-03-11T06:48:33+00:00
> Shouldn't --offline be the default when there is no --daemon-address specified?

I think not. The current default is probably expected behavior in the vast majority of cases, plus it's consistent with `monero-wallet-cli`.

# Action History
- Created by: mrx23dot | 2021-03-05T15:05:47+00:00
- Closed at: 2021-03-11T09:14:27+00:00
