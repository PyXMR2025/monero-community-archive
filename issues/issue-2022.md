---
title: blocks_to_unlock not listed as output to wallet RPC method get_balance
source_url: https://github.com/monero-project/monero-site/issues/2022
author: dimalinux
assignees: []
labels:
- '📚 docs: dev guides'
created_at: '2022-08-15T03:30:34+00:00'
updated_at: '2022-12-01T07:14:22+00:00'
type: issue
status: closed
closed_at: '2022-12-01T07:14:22+00:00'
---

# Original Description
The `get_balance` wallet RPC method has a `blocks_to_unlock` field (and possibly others) that are not documented here:
https://github.com/monero-project/monero-site/blame/28cfcdb38e735f5c35b83c067d8410ff4dc81ad4/resources/developer-guides/wallet-rpc.md#L173-L178

Implementation reference:
https://github.com/monero-project/monero/blob/v0.18.1.0/src/wallet/wallet_rpc_server_commands_defs.h#L108-L109

# Discussion History
## plowsof | 2022-10-10T15:04:09+00:00
Thanks. There is also a "strict" boolean that is missing. I have traced it back to here:
https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L5989

i will make a PR to update 

# Action History
- Created by: dimalinux | 2022-08-15T03:30:34+00:00
- Closed at: 2022-12-01T07:14:22+00:00
