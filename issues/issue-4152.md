---
title: '[Feature request]  make_integrated_address from an arbitrary one'
source_url: https://github.com/monero-project/monero/issues/4152
author: artyomsol
assignees: []
labels: []
created_at: '2018-07-19T13:35:46+00:00'
updated_at: '2018-08-16T19:16:54+00:00'
type: issue
status: closed
closed_at: '2018-08-16T19:16:54+00:00'
---

# Original Description
### Problem
The `make_integrated_address` method of **wallet_rpc** produces integrated address from the wallet primary one. 
1. It is not possible to make integrated address based on one of wallet's subaddresses with RPC API.
2. It is not possible to reconstruct integrated address based on transfer `destination` `address` with RPC API. (For example to reconstruct the integrated one used during a new transfer creation. Destination address and payment_id could be retrieved with `get_transfers` method, but not the integrated address)

### Solution suggested 
1. Extend the `make_integrated_address` method with optional `subaddr_index` parameter, to specify the account and subaddress indices for the standard address used.
```
"subaddr_index": {
                    "major": 0,
                    "minor": 0
                }
```
`major` - unsigned int; Default: 0. Account index for the subaddress.
`minor` - unsigned int; Default: 0. Index of the subaddress in the account.

2. Extend the `make_integrated_address` method with optional `address` parameter, to specify arbitrary standard **or** integrated address to be used as base to make the new integrated one. The value of this parameter should be converted to standard address if necessary. `subaddr_index` ignored for such a method call.

# Discussion History
## moneromooo-monero | 2018-07-19T15:09:07+00:00
This would defeat part of the purpose of subaddesses, which is to allow a way to map a tx to a sender without having to use an extraneous piece of data.

## artyomsol | 2018-07-20T11:54:25+00:00
Ok! Integrated subaddresses are meaningless, but what about `make_integrated_address` with base address specified? Just to reconstruct integrated address from standard address + payment ID retrieved with `get_transfer_by_txid` !? (p.2 of suggested solution) 

## moneromooo-monero | 2018-07-20T12:03:54+00:00
That can be added, though not very useful I think since the party generating those is the recipient.

## stoffu | 2018-07-20T12:36:05+00:00
#4158

## moneromooo-monero | 2018-08-16T18:54:08+00:00
+resolved

# Action History
- Created by: artyomsol | 2018-07-19T13:35:46+00:00
- Closed at: 2018-08-16T19:16:54+00:00
