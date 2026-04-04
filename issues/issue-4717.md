---
title: Sweep Unmixable fails with ring size too small
source_url: https://github.com/monero-project/monero/issues/4717
author: Excedrin
assignees: []
labels: []
created_at: '2018-10-24T17:27:16+00:00'
updated_at: '2018-11-07T14:33:14+00:00'
type: issue
status: closed
closed_at: '2018-11-07T14:33:14+00:00'
---

# Original Description
I'm using v0.13.0.3 of the wallet and `Monero 'Beryllium Bullet' (v0.13.0.2-release)` of the daemon, using a local daemon.

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

set_log 2 log from the daemon with a bit more detail.
```
2018-10-24 17:12:41.409 [RPC0]  ERROR   verify  src/cryptonote_core/blockchain.cpp:2526 Tx <40dfc404a084f166cedb0745766c189f8e21d5d34db84d80b5d28c07e28128c9> has invalid ring size (1), it should be 11
2018-10-24 17:12:41.409 [RPC0]  DEBUG   perf    src/common/perf_timer.cpp:140   PERF        1        check_tx_inputs
2018-10-24 17:12:41.409 [RPC0]  INFO    txpool  src/cryptonote_core/tx_pool.cpp:266     tx used wrong inputs, rejected
2018-10-24 17:12:41.410 [RPC0]  DEBUG   perf    src/common/perf_timer.cpp:140   PERF        1      add_tx
2018-10-24 17:12:41.410 [RPC0]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:909     Transaction verification failed: <40dfc404a084f166cedb0745766c189f8e21d5d34db84d80b5d28c07e28128c9>
2018-10-24 17:12:41.410 [RPC0]  WARN    daemon.rpc      src/rpc/core_rpc_server.cpp:728 [on_send_raw_tx]: tx verification failed: ring size too small, invalid input
```

Tried sweep_unmixable from the CLI wallet and got the same result.

```
Error: transaction <9ddb9d2232141b2ae97ebe4e62d3e7d7bd3919d52609b9e2190ce3f68ec912f6> was rejected by daemon with status: Failed
Error: Reason: ring size too small, invalid input
```

# Discussion History
## moneromooo-monero | 2018-10-24T18:29:19+00:00
Run monero-wallet-cli with log level 2, it will print the tx JSON, paste it here.

## Excedrin | 2018-10-25T06:54:48+00:00
Do I need to censor any of this? The transaction is about 500 lines. I could remove all the k_image, key and signatures if that's ok.

## moneromooo-monero | 2018-10-25T08:55:34+00:00
Yes, that would be OK.

## moneromooo-monero | 2018-10-25T08:56:10+00:00
You can also paste an encrypted version of it, my GPG pubkey is in utils/gpg_keys/moneromooo.asc.

## Excedrin | 2018-10-25T17:53:20+00:00
```
2018-10-25 06:47:40.232	5312	WARN 	net.http	src/wallet/wallet_errors.h:814	C:/msys64/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:5366:N5tools5error11tx_rejectedE: transaction was rejected by daemon, status = Failed, tx:
{
  "version": 1, 
  "unlock_time": 0, 
  "vin": [ {
      "key": {
        "amount": 750421621, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 994252428, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 312560042, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 99631166, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 198711870, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 117560000, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 768485557, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 196731738, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 990693485, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 982765223, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 412377876, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 198855312, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 547940561, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 329952736, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 580055279, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 150436506, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 257665264, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 509211928, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 893459269, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 189630156, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 425533879, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 1378868610, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 196919173, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 30726422, 
        "key_offsets": [ 2
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 181950166, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 4909981689, 
        "key_offsets": [ 2
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 2484219707, 
        "key_offsets": [ 1
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 834471483, 
        "key_offsets": [ 1
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 454823697, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 547788535, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 878748577, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 316732208, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 890864204, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 286447517, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 865545578, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 657183450, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 4717930405, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 2716394554, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 60664253, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 487637660, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 879427875, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 79502060, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 659306853, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 522832661, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 122756501, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 843446170, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 599997398, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 469948393, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 474830951, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 201229383, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 522167738, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 864544339, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 882219684, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 777929463, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 180442730, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 420462694, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 547623751, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 76195278, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 3673139354, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 999056238, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 756286001, 
        "key_offsets": [ 1
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 3064862300, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 495709201, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 324591100, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 83411923, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }, {
      "key": {
        "amount": 4713376876, 
        "key_offsets": [ 0
        ], 
        "k_image": "censor"
      }
    }
  ], 
  "vout": [ {
      "amount": 300000, 
      "target": {
        "key": "censor"
      }
    }, {
      "amount": 9, 
      "target": {
        "key": "censor"
      }
    }, {
      "amount": 90, 
      "target": {
        "key": "censor"
      }
    }, {
      "amount": 5000000000, 
      "target": {
        "key": "censor"
      }
    }, {
      "amount": 60000000, 
      "target": {
        "key": "censor"
      }
    }, {
      "amount": 1000000, 
      "target": {
        "key": "censor"
      }
    }, {
      "amount": 600, 
      "target": {
        "key": "censor"
      }
    }, {
      "amount": 6000, 
      "target": {
        "key": "censor"
      }
    }, {
      "amount": 800000000, 
      "target": {
        "key": "censor"
      }
    }, {
      "amount": 50000000000, 
      "target": {
        "key": "censor"
      }
    }
  ], 
  "extra": [ 1, 56, 179, 161, 48, 19, 220, 218, 129, 216, 24, 201, 245, 243, 31, 214, 249, 172, 166, 63, 148, 250, 5, 150, 106, 111, 156, 170, 141, 18, 0, 40, 56
  ], 
  "signatures": [ "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor",
  "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor",
  "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor",
  "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor", "censor"]
} (ring size too small, invalid input)
2018-10-25 06:47:40.232	5312	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: transaction <5477e2ffc72fd7360d7cb6546afff5afa1af49a9361e2da88750d1d9462856a0> was rejected by daemon with status: Failed
2018-10-25 06:47:40.232	5312	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Reason: ring size too small, invalid input
```

## moneromooo-monero | 2018-10-25T18:55:35+00:00
It's a bug. Ring size is now fixed at 11, and those special unmixable cases aren't allowed with the move to fixed ring size. This will be fixed, likely in next fork. In the meantime, you won't be able to spend these dust outputs before the fork, sorry.

## Excedrin | 2018-10-25T19:20:54+00:00
No problem, thanks for looking into it!

## moneromooo-monero | 2018-11-07T14:17:53+00:00
This will be spendable again starting next fork.

+resolved

# Action History
- Created by: Excedrin | 2018-10-24T17:27:16+00:00
- Closed at: 2018-11-07T14:33:14+00:00
