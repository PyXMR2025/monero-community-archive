---
title: Support subaddress lookahead in monero-wallet-rpc
source_url: https://github.com/monero-project/monero/issues/8954
author: woodser
assignees: []
labels:
- feature
- proposal
created_at: '2023-07-18T14:16:15+00:00'
updated_at: '2025-07-10T12:20:55+00:00'
type: issue
status: closed
closed_at: '2025-07-10T12:20:55+00:00'
---

# Original Description
This issue requests setting the wallet's subaddress lookahead with monero-wallet-rpc.

Preferably a new RPC call is added, e.g. `set_subaddress_lookahead`, but it needs to be confirmed if that works after the initial wallet is created, since most or all times `wallet2::set_subaddress_lookahead()` is used, it's before `wallet2::generate()` is called. For example: https://github.com/monero-project/monero/blob/00fd416a99686f0956361d1cd0337fe56e58d4a7/src/simplewallet/simplewallet.cpp#L4658

If it turns out the subaddress lookahead must be set when the wallet is created, a new `subaddress_lookahead` parameter can be added to these methods in wallet_rpc_server.cpp:

- `create_wallet`
- `restore_deterministic_wallet`
- `generate_from_keys`

# Discussion History
## jeffro256 | 2023-07-19T04:06:18+00:00
IMO, it would be more preferable to create a new RPC endpoint whose sole purpose is to set the lookahead values to minimize code replication in the wallet rpc server.

## woodser | 2023-07-19T11:50:50+00:00
> IMO, it would be more preferable to create a new RPC endpoint whose sole purpose is to set the lookahead values to minimize code replication in the wallet rpc server.

That sounds good to me, to create a new RPC call, e.g. `set_subaddress_lookahead`, as long as it works after wallet creation. I recall there may have been some issue related to that, but might be fixed now. I updated the issue description.

## SamsungGalaxyPlayer | 2024-10-04T16:43:20+00:00
It would be very useful to additionally support setting a subaddress lookahead as a parameter when restoring or creating a wallet with monero-wallet-rpc. This applies to the following commands:


* restore_deterministic_wallet
* create_wallet
* generate_from_keys

## nahuhh | 2024-10-04T18:27:43+00:00
> IMO, it would be more preferable to create a new RPC endpoint whose sole purpose is to set the lookahead values to minimize code replication in the wallet rpc server.

Via cli, subaddress-lookahead only work on wallet generation or restore.

using `set` to interactively manage it after wallet creation/restored doesnt have any effect. It also errors if you try to use --wallet-file along with the runtime flag.

all this is to say that i believe a new rpc endpoint would have to add the ability to modify the lookahead post-creation/restore.

option a) adding the rpc param to existing create and restore rpc endpoints would bring feature parity to cli. 

option b) adding a new rpc endpoint that can modify an existing wallet and enabling interactive modification for existing wallets via cli

i'm not sure if b) is non-existent due to technical limitation, but as stated earlier, it intentionally throws errors if trying to use subaddress-lookahead flag when specifying am existing wallet.

# Action History
- Created by: woodser | 2023-07-18T14:16:15+00:00
- Closed at: 2025-07-10T12:20:55+00:00
