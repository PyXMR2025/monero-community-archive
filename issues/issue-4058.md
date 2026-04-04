---
title: 'RPC create wallet from seed '
source_url: https://github.com/monero-project/monero/issues/4058
author: julesGoullee
assignees: []
labels: []
created_at: '2018-06-27T06:36:46+00:00'
updated_at: '2018-11-16T23:33:01+00:00'
type: issue
status: closed
closed_at: '2018-11-16T23:33:01+00:00'
---

# Original Description
What is the right way to restore wallet from seed with the rpc api ?

# Discussion History
## moneromooo-monero | 2018-06-27T08:37:08+00:00
Such questions are a good for for monero.stackexchange.com. More generally, help can be asked in #monero on Freenode, or reddit.


## stoffu | 2018-06-28T03:14:59+00:00
Currently there's no such functionality implemented for the RPC. The CLI has the full set of functionalities, while the RPC only supports some subset of them.

The RPC has the command `create_wallet` which lets you create a new wallet, but other commands for wallet restoration (from seed, from device, etc) are not implemented. IIRC there was some debate about the design of the wallet RPC client regarding the management of multiple wallets, and the discussion didn't end with a decisive conclusion. CC: @hyc 

See #4007

## hyc | 2018-06-28T12:31:52+00:00
I guess there's no reason not to add this to the RPC, I just didn't think of it when adding `create_wallet`.

## artyomsol | 2018-07-20T15:58:09+00:00
+1 for RPC API wallet restoration from seed

## moneromooo-monero | 2018-07-20T16:54:19+00:00
in fact, this could be merged with the generate-from-json code, so we get everything.

## moneromooo-monero | 2018-10-02T18:44:14+00:00
+hacktoberfest


## omani | 2018-10-28T02:58:07+00:00
hi all,
please see #4746.

if it makes more sense to merge this with `create_wallet` I can do this. I would probably look for a flag like `from_seed: ...` in the json and take the appropriate path in `create_wallet`. I thought it would probably be too much in the json and thus gave it a separate function.

## moneromooo-monero | 2018-11-16T23:17:28+00:00
+resolved

# Action History
- Created by: julesGoullee | 2018-06-27T06:36:46+00:00
- Closed at: 2018-11-16T23:33:01+00:00
