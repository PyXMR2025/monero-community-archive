---
title: Add an RPC call to preview/calculate transaction fee
source_url: https://github.com/monero-project/monero/issues/2432
author: lessless
assignees: []
labels: []
created_at: '2017-09-11T13:35:51+00:00'
updated_at: '2023-09-24T18:24:51+00:00'
type: issue
status: closed
closed_at: '2017-09-12T01:46:43+00:00'
---

# Original Description
Hello team, 

Calculating transaction fee is relatively concentrated topic - some answers even has plots attached. 
And at the same time it's a very basic piece of functionality for everyone who want to have his service under control.

Example use case: make designated counter-party pay the transaction fee. The most obvious example is that I want to see how much I should pay to **receive** N XMR, not N - tx_fee XMR.

For that to work we need to have ability to obtain exact transaction fee in a no-brainer way. Couple of possible options:

I think the best option will be to introduce two additional Wallet RPC calls:

- `get_transfer_fee` - accepts `destinations`, `mixin`, `unlock_time` and `priority` that are equal to those in `transfer` call and returns `fee`

- `get_split_transfer_fees` - accepts `destinations`, `unlock_time`, `priority` and `new_algorithm` that are equal to those in `transfer_split ` call and returns `fee_list ` and returns `amount_list`


p.s. Why `transfer` doesn't have `new_algorithm` option? 

# Discussion History
## moneromooo-monero | 2017-09-11T18:15:46+00:00
You do that by seting "do_not_relay" and "get_tx_hex" to true. The tx is then only made, not relayed to the network. You get it back, and the fee. You can then relay it if you like the fee. transfer is old, do not use.



## lessless | 2017-09-12T01:46:43+00:00
thanks @moneromooo-monero, I will add `do_not_relay` to the docs

## onemanstartup | 2017-12-08T01:04:37+00:00
@moneromooo-monero basically it is the same in bitcoin, but they have send_raw_transaction in rpc, but in moner-wallet rpc this is absent, so I must to support 2 rpc apis, daemon and wallet. Is it intentional?

## skoniks | 2023-09-24T18:24:50+00:00
> You do that by seting "do_not_relay" and "get_tx_hex" to true. The tx is then only made, not relayed to the network. You get it back, and the fee. You can then relay it if you like the fee. transfer is old, do not use.

If i want to precalculate fee, i face an error "not enough money". So in my case i need the way to calculate fee even if total transaction sum will be higher than account balance.

# Action History
- Created by: lessless | 2017-09-11T13:35:51+00:00
- Closed at: 2017-09-12T01:46:43+00:00
