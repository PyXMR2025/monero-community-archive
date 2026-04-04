---
title: Error when trying to submit_transfer. Says "fee too low".
source_url: https://github.com/monero-project/monero/issues/2935
author: ghost
assignees: []
labels:
- bug
created_at: '2017-12-15T18:36:31+00:00'
updated_at: '2018-09-19T10:16:54+00:00'
type: issue
status: closed
closed_at: '2018-09-19T10:16:54+00:00'
---

# Original Description
I made sure to `set priority 0` on both ends just to be safe. Perhaps the issue is on my end, but on the new v7 testnet I'm unable submit signed transfers in a view wallet.

https://paste.fedoraproject.org/paste/e5J4WRBVEc2ZO8~xh5aucQ

# Discussion History
## ghost | 2017-12-15T18:41:38+00:00
Here's the daemon output: `2017-12-15 18:25:43.537 [RPC1]  WARN    daemon.rpc      src/rpc/core_rpc_server.cpp:690 [on_send_raw_tx]: tx verification failed: fee too low`

## moneromooo-monero | 2017-12-16T09:01:28+00:00
Run again with --log-level 2 in the wallet. In particular, check the tx sizes.

## ghost | 2017-12-16T19:55:47+00:00
Here you go (I think): https://paste.fedoraproject.org/paste/gwnpF8~~LvP7tu~Tt1qURQ

Above line 86 is me inside the CLI. Below line 86 is the monero-wallet-cli.log file

Note: these are with freshly mined funds. The previous example was old inputs so I made sure to see if it would error with newer inputs as well.

## moneromooo-monero | 2017-12-16T20:34:09+00:00
That doesn't look like a level 2 log.
Add --log-level 2 to the command line.

## ghost | 2017-12-17T16:17:17+00:00
Inside CLI: https://paste.fedoraproject.org/paste/4H1RYnL5GLrsrHZRJR5b0g
CLI log file: https://paste.fedoraproject.org/paste/OkbVYuIXOmBzLMsJEnrUOA
Daemon log file: https://paste.fedoraproject.org/paste/w4Apt6yuogN9FlAfUsMrBQ

## ghost | 2018-01-07T21:14:06+00:00
Ping @moneromooo-monero - Response from OP.

## dEBRUYNE-1 | 2018-01-08T12:32:10+00:00
+bug

## dEBRUYNE-1 | 2018-01-15T13:17:38+00:00
Fwiw, I incurred the same error when testing Bulletproofs. 

## ghost | 2018-03-16T15:49:17+00:00
Just checking in. Retested with recent master and it still errors out with "fee too low"

## arnuschky | 2018-04-02T08:45:13+00:00
Same problem on stagenet:

```
[wallet 58cisX]: sweep_all 5AiV6wffn42AN3RTkKzE3sKzZHMbNWsCjFCJkdTwb1AZL1pcyK4gjfqZMXXeoumLtmSfELyu9t93d7LXGxMEzPqzVhUwZLn
Wallet password: 
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y

Transaction 1/6:
Spending from address index 0

Transaction 2/6:
Spending from address index 0

Transaction 3/6:
Spending from address index 0

Transaction 4/6:
Spending from address index 0

Transaction 5/6:
Spending from address index 0

Transaction 6/6:
Spending from address index 0
Sweeping 57961.974120396672 in 6 transactions for a total fee of 0.470207580000.  Is this okay?  (Y/Yes/N/No): y

Transaction successfully submitted, transaction <84cb4f6f73226cc22b3a224356357cfbd2d96e364439d9e23ec80305ba71a68e>
You can check its status by using the `show_transfers` command.
Error: transaction <dbf44ce6ea6d6c2ea5dabc73bc5169402ebcdf2fb540abe84c4f037a3c88b758> was rejected by daemon with status: Failed
Error: Reason: fee too low
Height 46332, txid <26263ff1032aace1de58358f46c84df8cde9143d15ebcd23af139d012253c59f>, 33.206587519886, idx 0/0
[wallet 58cisX]: set_log 2
New log categories: *:DEBUG
[wallet 58cisX]: sweep_all 5AiV6wffn42AN3RTkKzE3sKzZHMbNWsCjFCJkdTwb1AZL1pcyK4gjfqZMXXeoumLtmSfELyu9t93d7LXGxMEzPqzVhUwZLn
Wallet password: 
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y

Transaction 1/6:
Spending from address index 0

Transaction 2/6:
Spending from address index 0

Transaction 3/6:
Spending from address index 0

Transaction 4/6:
Spending from address index 0

Transaction 5/6:
Spending from address index 0

Transaction 6/6:
Spending from address index 0
Sweeping 55165.455358629378 in 6 transactions for a total fee of 0.103605060000.  Is this okay?  (Y/Yes/N/No): y
Transaction successfully submitted, transaction <4052893669f8deace0c4e7061b3ee5f549ff50b7c0aff8e5b42b2312cace7f15>
You can check its status by using the `show_transfers` command.
Error: transaction <865d73f4969c6a6ecd2f1823761f29ce46cf4c3dccc35a85e2ef10feacb2ab3a> was rejected by daemon with status: Failed
Error: Reason: fee too low
[wallet 58cisX]: 
```

Version:
```
From the log:monerod --version
Monero 'Lithium Luna' (v0.12.0.0-master-release)
```

I got the full debug log, but it's 30MB.


## somebodyLi | 2018-06-05T05:58:40+00:00
I have the same issue ??? please tell me why ???

## moneromooo-monero | 2018-06-07T11:30:55+00:00
Fixed in https://github.com/monero-project/monero/pull/3955

## stoffu | 2018-06-07T13:26:16+00:00
#3955 is a solution to the issue described by @dEBRUYNE-1 above, but I don't think it applies to the one reported by @arnuschky because Bulletproofs isn't activated on stagenet.

@liyanhrxy Please provide a bit more details about your issue. Is it fixed by #3955?

## moneromooo-monero | 2018-07-19T21:59:58+00:00
Anybody still getting this with #3955 ? If so, send level 2 wallet logs.

## arnuschky | 2018-07-20T05:08:40+00:00
I tried replicating this with 0.12.3.0 and couldn't. Either my unspents were structured in a way that didn't cause the problem, or it's indeed fixed. I'll try again later.

## moneromooo-monero | 2018-09-01T23:04:17+00:00
Did you repro it ?

## moneromooo-monero | 2018-09-18T11:43:09+00:00
ping :)

## arnuschky | 2018-09-18T11:48:42+00:00
Ah, thanks for the ping @moneromooo-monero. Apologies, totally forgot about it.

No I didn't manage to reproduce it using 0.12.3.0. So from my side this can be closed.

## moneromooo-monero | 2018-09-19T10:10:58+00:00
OK, thanks.

+resolved

# Action History
- Created by: ghost | 2017-12-15T18:36:31+00:00
- Closed at: 2018-09-19T10:16:54+00:00
