---
title: Sweep Unmixable fails with ring size too small
source_url: https://github.com/monero-project/monero-gui/issues/1702
author: Excedrin
assignees: []
labels:
- invalid
created_at: '2018-10-24T17:05:25+00:00'
updated_at: '2018-10-24T17:29:50+00:00'
type: issue
status: closed
closed_at: '2018-10-24T17:27:26+00:00'
---

# Original Description
I have a wallet with about 0.10 XMR in it that's been active for a very long time, since the early days of Monero. I'm not able to transfer the remaining balance out, it fails with: 
```
Can't create transaction: not enough outputs for specified ring size = 11:
output amount = 0.000999056238, found outputs to use = 1
output amount = 0.000879427875, found outputs to use = 1
output amount = 0.000768485557, found outputs to use = 1
output amount = 0.000469948393, found outputs to use = 1
output amount = 0.000756286001, found outputs to use = 2
output amount = 0.000865545578, found outputs to use = 1
output amount = 0.000189630156, found outputs to use = 1
output amount = 0.000060664253, found outputs to use = 1
output amount = 0.000522167738, found outputs to use = 1
output amount = 0.000454823697, found outputs to use = 1
output amount = 0.002484219707, found outputs to use = 2
output amount = 0.000890864204, found outputs to use = 1
output amount = 0.000878748577, found outputs to use = 1
output amount = 0.000196919173, found outputs to use = 1
output amount = 0.000198855312, found outputs to use = 1
output amount = 0.000580055279, found outputs to use = 1
output amount = 0.000117560000, found outputs to use = 4
output amount = 0.000083411923, found outputs to use = 1
output amount = 0.000198711870, found outputs to use = 1
output amount = 0.000547788535, found outputs to use = 1
output amount = 0.000412377876, found outputs to use = 1
output amount = 0.000982765223, found outputs to use = 2
output amount = 0.000599997398, found outputs to use = 1
output amount = 0.000994252428, found outputs to use = 2
output amount = 0.000882219684, found outputs to use = 1
output amount = 0.003064862300, found outputs to use = 4
output amount = 0.000893459269, found outputs to use = 1
output amount = 0.000099631166, found outputs to use = 1
output amount = 0.004713376876, found outputs to use = 1
output amount = 0.000509211928, found outputs to use = 1
output amount = 0.000487637660, found outputs to use = 1
output amount = 0.000420462694, found outputs to use = 1
output amount = 0.000750421621, found outputs to use = 1
output amount = 0.003673139354, found outputs to use = 1
output amount = 0.000990693485, found outputs to use = 1
output amount = 0.000522832661, found outputs to use = 1
output amount = 0.000181950166, found outputs to use = 1
output amount = 0.000257665264, found outputs to use = 1
output amount = 0.000547623751, found outputs to use = 1
output amount = 0.000864544339, found outputs to use = 1
output amount = 0.000312560042, found outputs to use = 1
output amount = 0.000547940561, found outputs to use = 1
output amount = 0.000030726422, found outputs to use = 3
output amount = 0.000180442730, found outputs to use = 1
output amount = 0.000079502060, found outputs to use = 1
output amount = 0.002716394554, found outputs to use = 1
output amount = 0.000076195278, found outputs to use = 2
output amount = 0.000150436506, found outputs to use = 1
output amount = 0.000201229383, found outputs to use = 1
output amount = 0.000495709201, found outputs to use = 1
output amount = 0.000843446170, found outputs to use = 1
output amount = 0.000425533879, found outputs to use = 1
output amount = 0.000316732208, found outputs to use = 1
output amount = 0.004717930405, found outputs to use = 2
output amount = 0.001378868610, found outputs to use = 1
output amount = 0.000474830951, found outputs to use = 1
output amount = 0.000659306853, found outputs to use = 1
output amount = 0.000834471483, found outputs to use = 2
output amount = 0.000196731738, found outputs to use = 1
Please sweep unmixable outputs.
```

and Sweep Unmixable results in this error:
```
Couldn't send the money: transaction <f9893286ef4137d72dad7e1e986e024fd6326250cca9a01d893c60266bca151b> was rejected by daemon with status: Failed. Reason: ring size too small, invalid input
```

# Discussion History
## Excedrin | 2018-10-24T17:08:19+00:00
Daemon log:
```
2018-10-24 17:06:44.604 [RPC0]  WARN    daemon.rpc      src/rpc/core_rpc_server.cpp:728 [on_send_raw_tx]: tx verification failed: ring size too small, invalid input
```

## Excedrin | 2018-10-24T17:09:35+00:00
Also, should have mentioned, I'm using v0.13.0.3 of the wallet and `Monero 'Beryllium Bullet' (v0.13.0.2-release)` of the daemon, using a local daemon.

## Excedrin | 2018-10-24T17:13:52+00:00
set_log 2 log from the daemon with a bit more detail.
```
2018-10-24 17:12:41.409 [RPC0]  ERROR   verify  src/cryptonote_core/blockchain.cpp:2526 Tx <40dfc404a084f166cedb0745766c189f8e21d5d34db84d80b5d28c07e28128c9> has invalid ring size (1), it should be 11
2018-10-24 17:12:41.409 [RPC0]  DEBUG   perf    src/common/perf_timer.cpp:140   PERF        1        check_tx_inputs
2018-10-24 17:12:41.409 [RPC0]  INFO    txpool  src/cryptonote_core/tx_pool.cpp:266     tx used wrong inputs, rejected
2018-10-24 17:12:41.410 [RPC0]  DEBUG   perf    src/common/perf_timer.cpp:140   PERF        1      add_tx
2018-10-24 17:12:41.410 [RPC0]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:909     Transaction verification failed: <40dfc404a084f166cedb0745766c189f8e21d5d34db84d80b5d28c07e28128c9>
2018-10-24 17:12:41.410 [RPC0]  WARN    daemon.rpc      src/rpc/core_rpc_server.cpp:728 [on_send_raw_tx]: tx verification failed: ring size too small, invalid input
```

## Excedrin | 2018-10-24T17:25:12+00:00
Tried sweep_unmixable from the CLI wallet and got the same result.

```
Error: transaction <9ddb9d2232141b2ae97ebe4e62d3e7d7bd3919d52609b9e2190ce3f68ec912f6> was rejected by daemon with status: Failed
Error: Reason: ring size too small, invalid input
```

## sanderfoobar | 2018-10-24T17:26:28+00:00
The GUI has no influence in specifying ring size / mixin when making unmixable sweeps. Problem is somewhere in https://github.com/monero-project/monero. 

Edit: https://github.com/monero-project/monero/issues/4717

+invalid

# Action History
- Created by: Excedrin | 2018-10-24T17:05:25+00:00
- Closed at: 2018-10-24T17:27:26+00:00
