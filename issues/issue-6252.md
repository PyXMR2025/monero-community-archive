---
title: 'error when running monero-wallet-rpc, E status == CORE_RPC_STATUS_PAYMENT_REQUIRED.
  THROW EXCEPTION: tools::error::payment_required'
source_url: https://github.com/monero-project/monero/issues/6252
author: thestick613
assignees: []
labels: []
created_at: '2019-12-18T17:54:37+00:00'
updated_at: '2020-05-16T16:03:50+00:00'
type: issue
status: closed
closed_at: '2020-05-16T16:03:50+00:00'
---

# Original Description
```
2019-12-18 17:52:53.993 E status == CORE_RPC_STATUS_PAYMENT_REQUIRED. THROW EXCEPTION: tools::error::payment_required
2019-12-18 17:52:53.993 W /home/ubuntu/build/monero/src/wallet/wallet2.cpp:13431:N5tools5error16payment_requiredE: payment required, request = get_transaction_pool_hashes.bin
2019-12-18 17:52:53.993 E Exception at while refreshing, what=payment required


```

# Discussion History
## moneromooo-monero | 2019-12-18T19:07:24+00:00
This is a bug tracker. Are you reporting a bug ? If so, explain what the bug is. What you did. What happened. What you think should have happened. Bits of logs without context do not make a bug report unless the bug is obvious.

## moneromooo-monero | 2019-12-20T14:44:41+00:00
Ping. Is there a bug, and if so what is it ? I'll close in a couple days if no info is forthcoming.

## thestick613 | 2019-12-20T14:52:31+00:00
I am using https://github.com/monero-integrations/monerowhmcs. 
The error appears after i pay.

## moneromooo-monero | 2019-12-20T14:57:55+00:00
So, I understand you:
- connected to a node which requires payment
- mined a bit and submitted at least one share, for which the daemon presumably credit you some
- got the error you pasted when you tried to use that credit

1: is the above correct ?
2: is the daemon one you're running, or a one from a stranger on the internet ?
3: paste the output of "rpc_payment_info" (in monero-wallet-cli)

## thestick613 | 2019-12-20T18:56:42+00:00
Hello,

I'm running an instance of monero-wallet-rpc, and i'm connecting to a public monero node (node.moneroworld.com). I've configured the monero whmcs integration to use this monero wallet rcp. I've had a few failed payments the last days. This is the log from the last one:

```
2019-12-17 12:54:18.590 [RPC0]  INFO    perf.wallet.wallet2     src/common/perf_timer.cpp:156   PERF      455    process_new_transaction
2019-12-17 12:54:18.590 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:3422     Refresh done, blocks received: 1, balance (all accounts): XXX, unlocked: XXX
2019-12-17 12:55:39.538 [RPC0]  INFO    net.http        contrib/epee/include/storages/http_abstract_invoke.h:53 Failed to invoke http request to  /get_transaction_pool_hashes.bin
2019-12-17 12:55:39.538 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:13426    !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2019-12-17 12:55:39.538 [RPC0]  WARNING net.http        src/wallet/wallet_errors.h:896  /home/ubuntu/build/monero/src/wallet/wallet2.cpp:13426:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = get_transaction_pool_hashes.bin
2019-12-17 12:55:39.560 [RPC0]  ERROR   wallet.rpc      src/wallet/wallet_rpc_server.cpp:131    Exception at while refreshing, what=no connection to daemon
2019-12-17 12:55:59.562 [RPC0]  INFO    net.http        contrib/epee/include/storages/http_abstract_invoke.h:53 Failed to invoke http request to  /get_transaction_pool_hashes.bin
2019-12-17 12:55:59.563 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:13426    !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2019-12-17 12:55:59.563 [RPC0]  WARNING net.http        src/wallet/wallet_errors.h:896  /home/ubuntu/build/monero/src/wallet/wallet2.cpp:13426:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = get_transaction_pool_hashes.bin
2019-12-17 12:55:59.563 [RPC0]  ERROR   wallet.rpc      src/wallet/wallet_rpc_server.cpp:131    Exception at while refreshing, what=no connection to daemon
2019-12-17 12:56:19.565 [RPC0]  ERROR   net.http        contrib/epee/include/net/http_client.h:411      HTTP_CLIENT: Failed to SEND
2019-12-17 12:56:19.565 [RPC0]  INFO    net.http        contrib/epee/include/storages/http_abstract_invoke.h:53 Failed to invoke http request to  /get_transaction_pool_hashes.bin
2019-12-17 12:56:19.565 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:13426    !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2019-12-17 12:56:19.565 [RPC0]  WARNING net.http        src/wallet/wallet_errors.h:896  /home/ubuntu/build/monero/src/wallet/wallet2.cpp:13426:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = get_transaction_pool_hashes.bin
2019-12-17 12:56:19.565 [RPC0]  ERROR   wallet.rpc      src/wallet/wallet_rpc_server.cpp:131    Exception at while refreshing, what=no connection to daemon
2019-12-17 12:56:39.982 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:13431    status == CORE_RPC_STATUS_PAYMENT_REQUIRED. THROW EXCEPTION: tools::error::payment_required
2019-12-17 12:56:39.982 [RPC0]  WARNING net.http        src/wallet/wallet_errors.h:896  /home/ubuntu/build/monero/src/wallet/wallet2.cpp:13431:N5tools5error16payment_requiredE: payment required, request = get_transaction_pool_hashes.bin
2019-12-17 12:56:39.982 [RPC0]  ERROR   wallet.rpc      src/wallet/wallet_rpc_server.cpp:131    Exception at while refreshing, what=payment required
2
```

Now that i'm looking more into it, it seems that my connection to a public node is the culprit here, right?
The monero whmcs integration could be the other issue, because it didn't work out correctly without [some patches](https://github.com/monero-integrations/monerowhmcs/pull/36).
I've opened this ticket because i don't understand what this error means.

## moneromooo-monero | 2019-12-20T22:55:00+00:00
Are you *sure* that you have enough credits on that node ? I asked for the output of "rpc_payment_info" which should tell us.

## thestick613 | 2019-12-20T23:43:24+00:00
This node is only used for receiving, so it doesn't matter how many credits i have. However, if i run monero-wallet-cli, i get this error:

```
Error: failed to load wallet: internal error: "my_wallet.txt.keys" is opened by another wallet program
Error: You may want to remove the file my_wallet.txt" and try again
```

I am able to load the same wallet on another machine, and it displays the correct balance.

## moneromooo-monero | 2019-12-21T02:17:48+00:00
I have to ask:
You do realize that you are asking for service from a daemon which expects payment in the form of mining, right ? That the payment it's asking for is not sending it any monero, but your wallet hashing for some time in return for the node to perform RPC services for you ?


## moneromooo-monero | 2020-05-16T16:03:50+00:00
There seems to be no bug here. If you think there is one, describe it precisely.

# Action History
- Created by: thestick613 | 2019-12-18T17:54:37+00:00
- Closed at: 2020-05-16T16:03:50+00:00
