---
title: ERROR   net.http        src/rpc/core_rpc_server.h:84    Failed to on_get_blocks()
source_url: https://github.com/monero-project/monero/issues/4462
author: jdscott0
assignees: []
labels: []
created_at: '2018-09-28T11:33:30+00:00'
updated_at: '2022-03-16T15:42:26+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:42:26+00:00'
---

# Original Description
2018-09-28 11:11:46.751 [P2P7]  WARN    global  src/cryptonote_core/cryptonote_core.cpp:1380    [1;31m**********************************************************************[0m
2018-09-28 11:11:46.761 [P2P7]  WARN    global  src/cryptonote_core/cryptonote_core.cpp:1381    [1;31mLast scheduled hard fork time shows a daemon update is needed soon.[0m
2018-09-28 11:11:46.764 [P2P7]  WARN    global  src/cryptonote_core/cryptonote_core.cpp:1382    [1;31m**********************************************************************[0m
2018-09-28 11:12:10.592 [RPC0]  ERROR   net.http        contrib/epee/include/net/http_client.h:456   Unexpected recv fail
2018-09-28 11:12:10.596 [RPC0]  ERROR   net.http        src/rpc/core_rpc_server.h:84    Failed to on_get_blocks()
2018-09-28 11:13:21.988 [RPC1]  ERROR   net.http        contrib/epee/include/net/http_client.h:456   Unexpected recv fail
2018-09-28 11:13:21.992 [RPC1]  ERROR   net.http        src/rpc/core_rpc_server.h:84    Failed to on_get_blocks()


# Discussion History
## moneromooo-monero | 2018-09-28T11:44:27+00:00
Testnet or mainnet ?
Which (precise) version ?
Please run with --log-level 1 and paste new logs.

## jdscott0 | 2018-09-28T11:52:20+00:00
mainnet and monero gui version 0.12.3.0. How to log 1 and paste new logs

> Testnet or mainnet ?
> Which (precise) version ?
> Please run with --log-level 1 and paste new logs.

mainnet and monero gui version 0.12.3.0. How to paste new logs

## moneromooo-monero | 2018-09-28T12:03:57+00:00
Use 0.13.0.1, it should fix most of the timeouts (which " Unexpected recv fail" is).
To set log level to 1, you add "--log-level 1" to the command line. If you're using the GUI, there should be a widget to add command line parameters in the settings window somewhere.

## jdscott0 | 2018-09-28T12:05:48+00:00
> Use 0.13.0.1, it should fix most of the timeouts (which " Unexpected recv fail" is).
> To set log level to 1, you add "--log-level 1" to the command line. If you're using the GUI, there should be a widget to add command line parameters in the settings window somewhere.

Thank you  where do I get the update from 

## moneromooo-monero | 2018-09-28T12:07:24+00:00
If you mean 0.13.0.1, from github. If you need a prebuilt binary, there's none yet though.

## moneromooo-monero | 2018-10-12T21:13:03+00:00
There are prebuilt binaries now (except for the ARM ones which aren't yet ready).


# Action History
- Created by: jdscott0 | 2018-09-28T11:33:30+00:00
- Closed at: 2022-03-16T15:42:26+00:00
