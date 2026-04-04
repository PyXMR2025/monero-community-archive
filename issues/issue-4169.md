---
title: '[Feature request]: wallet RPC: get_address_index to retrieve the index of
  an address '
source_url: https://github.com/monero-project/monero/issues/4169
author: artyomsol
assignees: []
labels: []
created_at: '2018-07-23T13:47:36+00:00'
updated_at: '2018-08-16T19:00:57+00:00'
type: issue
status: closed
closed_at: '2018-08-16T19:00:57+00:00'
---

# Original Description
As soon as main part of RPC methods accepts accont/subaddress index as a parameter It would be convenient to have a method to retrieve the subaddress index (major and minor) having the address provided. Only if the address belongs to the one of wallet's accounts obviously.
It should be a method reversal to the `get_address`.
#### Inputs
* `address` - string; The 95-character hex address string.
#### Outputs
* `subaddr_index` - (Optional) subaddress index if found:
* * `major` - unsigned int; Account index for the subaddress.
* * `minor` - unsigned int; Index of the subaddress in the account.

# Discussion History
## stoffu | 2018-07-23T14:58:56+00:00
#4170 

## moneromooo-monero | 2018-08-16T18:54:54+00:00
+resolved

# Action History
- Created by: artyomsol | 2018-07-23T13:47:36+00:00
- Closed at: 2018-08-16T19:00:57+00:00
