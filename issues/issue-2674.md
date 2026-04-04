---
title: Monerod, method not found
source_url: https://github.com/monero-project/monero/issues/2674
author: lukaisailovic
assignees: []
labels: []
created_at: '2017-10-17T19:23:47+00:00'
updated_at: '2017-10-17T19:39:37+00:00'
type: issue
status: closed
closed_at: '2017-10-17T19:36:29+00:00'
---

# Original Description
I'm trying to call any method from my php script like this: 

```
      $client = new Client('http://127.0.0.1:28081/json_rpc');
      $result = $client->execute('getbalance');
      dd($result);
```
Now whatever method I chose from documentation it always result in error response `Method not found`. Is there any configuration to the node or anything that I'm not aware of ? 

# Discussion History
## glv2 | 2017-10-17T19:27:41+00:00
```getbalance``` is a valid RPC method for *monero-wallet-rpc*, not for *monerod*.

## lukaisailovic | 2017-10-17T19:29:10+00:00
@glv2  Never made anything with monero before, assumed it was same as Btc but looks like there are some major differences. So how can I run `monero-wallet-rpc` in testnet mode ? 

## glv2 | 2017-10-17T19:39:37+00:00
Basically, you run ```monero-wallet-rpc --testnet --rpc-bind-port 28091 --wallet-file path_to_your_testnet_wallet_file```.

You can find some answers about RPC related questions on stackexchange: https://monero.stackexchange.com/questions/tagged/rpc.


# Action History
- Created by: lukaisailovic | 2017-10-17T19:23:47+00:00
- Closed at: 2017-10-17T19:36:29+00:00
