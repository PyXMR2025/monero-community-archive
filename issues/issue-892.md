---
title: 'simplewallet rpc: Payment IDs are not included when sending to integrated
  addresses using rpc transfer method.'
source_url: https://github.com/monero-project/monero/issues/892
author: osensei
assignees: []
labels: []
created_at: '2016-07-08T21:11:44+00:00'
updated_at: '2016-08-10T14:22:04+00:00'
type: issue
status: closed
closed_at: '2016-08-10T14:22:04+00:00'
---

# Original Description
What the title says.

When sending coins to an integrated address using the rpc transfer method, the coins will be sent to the standard address without the payment ID.

There seems to be some logic in simplewallet.cpp, that parses the integrated address and extracts the payment ID, that is not implemented on wallet_rpc_server.cpp


# Discussion History
## moneromooo-monero | 2016-07-10T12:49:39+00:00
Fixed in https://github.com/monero-project/bitmonero/pull/899


## osensei | 2016-07-11T05:05:24+00:00
You da man!

I can confirm it works.


## luigi1111 | 2016-08-10T14:22:04+00:00
Fixed by #899 


# Action History
- Created by: osensei | 2016-07-08T21:11:44+00:00
- Closed at: 2016-08-10T14:22:04+00:00
