---
title: 'transfer error not_enough_money '
source_url: https://github.com/monero-project/monero/issues/7457
author: mrx23dot
assignees: []
labels: []
created_at: '2021-03-06T23:39:25+00:00'
updated_at: '2021-03-16T06:03:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm trying to transfer 0.000000000001 (smallest amount) from 0.000000470000 **unlocked** balance via RPC, but I get **not_enough_money** error.

I have waited more than 20mins after received the 047 to spend, and transaction has 65 confirms. 
Using lower prio fees. I only have one account in wallet and I'm fully synced.

So why can't I send money?

monero-wallet-rpc --wallet-file wallet --password xxx --daemon-address xmr.fail:18081 --rpc-bind-port 28089 --rpc-bind-ip 127.0.0.1 --disable-rpc-login --log-level 2
Latest release.

2021-03-06 23:23:10.536 I Refresh done, blocks received: 0, balance (all accounts): 0.000000470000, **unlocked: 0.000000470000**

2021-03-06 23:23:31.865 D Using v8 rules
2021-03-06 23:23:31.867 W Requested ring size 1 too low, using 11
2021-03-06 23:23:31.868 D Using v8 rules
2021-03-06 23:23:31.868 D on_transfer_split calling create_transactions_2
2021-03-06 23:23:32.020 D Using v5 rules
2021-03-06 23:23:32.022 D Using v8 rules
2021-03-06 23:23:32.023 D Using v8 rules
2021-03-06 23:23:32.167 D Using v4 rules
2021-03-06 23:23:32.169 D Using v8 rules
2021-03-06 23:23:32.319 D Using v13 rules
2021-03-06 23:23:32.321 D Using v13 rules
2021-03-06 23:23:32.321 D Using v4 rules
2021-03-06 23:23:32.467 D Using v8 rules
2021-03-06 23:23:32.469 D Using v8 rules
2021-03-06 23:23:32.469 D transfer: adding 0.000000000001, for a total of 0.000000000001
2021-03-06 23:23:32.469 D estimated bulletproof rct tx size for 1 inputs with ring size 11 and 2 outputs: 1416 (800 saved)
2021-03-06 23:23:32.470 E needed_money + min_fee > balance_subtotal. THROW EXCEPTION: error::not_enough_money
2021-03-06 23:23:32.470 W /home/ubuntu/build/monero/src/wallet/wallet2.cpp:9843:N5tools5error16 **not_enough_moneyE: not enough money, available = 0.000000470000, tx_amount = 0.000000000001**

# Discussion History
## selsta | 2021-03-06T23:54:05+00:00
I don't think 0.000000470000 is enough to cover the fee.

## ndorf | 2021-03-07T09:58:28+00:00
@selsta We can assume as much based on the penultimate log message (`2021-03-06 23:23:32.470 E needed_money + min_fee > balance_subtotal`), but I think it would be better if the final message included the actual computed fee. [This](https://github.com/ndorf/monero/commit/c58f441904f16236fa4c0e1b2bf9fc821646df25) change would make that happen. What do you think?

## mrx23dot | 2021-03-07T13:33:36+00:00
That's correct I didn't have enough to cover transfer fee. (~0.00001095 XMR)

Since we know the transfer fee it would be nice to include it in the error message. 
Especially if we just forward error msg to the user.

## mrx23dot | 2021-03-15T09:19:35+00:00
Looks like the US government tries to spam us, since they can't do more against Monero :D

# Action History
- Created by: mrx23dot | 2021-03-06T23:39:25+00:00
