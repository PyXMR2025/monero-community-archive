---
title: incorrect description of suggested_confirmations_threshold in wallet RPC documentation
source_url: https://github.com/monero-project/monero-site/issues/2075
author: dimalinux
assignees: []
labels:
- '📚 docs: dev guides'
created_at: '2022-10-16T06:19:37+00:00'
updated_at: '2022-12-01T07:14:23+00:00'
type: issue
status: closed
closed_at: '2022-12-01T07:14:23+00:00'
---

# Original Description
`suggested_confirmations_threshold` has a description in 2 places [on this page](https://github.com/monero-project/monero-site/blame/7535c4c/resources/developer-guides/wallet-rpc.md#L1906) that says:  

> Estimation of the confirmations needed for the transaction to be included in a block.

At minimum, that description is horribly confusing given that a transaction must be included in a block to have a confirmation. I'm not sure what it should say.  Maybe something like this?

>  A suggested number of confirmations to wait for before considering the transaction to be irreversible. 

Here's how the value is getting set:
https://github.com/monero-project/monero/blob/v0.18.1.2/src/wallet/wallet_rpc_server.cpp#L102-L117

# Discussion History
## plowsof | 2022-10-16T11:36:25+00:00
Thanks, it is confusing and seems wrong, i'll have to ask around for a more informed opinion than my own because im thinking  ' 10 conf's are when funds are confirmed ' but looking at that function, it's taking into account the block reward `(entry.amount + block_reward - 1) / block_reward;` and then it provides a different threshold for outputs that are locked, and takes into account the networks hashrate* so there may be some kind of attack this is attempting to account for / broader explanation needed

UPDATE: moneromooo has kindly provided an explanation https://libera.monerologs.net/monero-dev/20221016 

# Action History
- Created by: dimalinux | 2022-10-16T06:19:37+00:00
- Closed at: 2022-12-01T07:14:23+00:00
