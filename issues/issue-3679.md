---
title: 'monero-wallet-rpc: Add sub-address parameters to make_integrated_address API'
source_url: https://github.com/monero-project/monero/issues/3679
author: mmorrell
assignees: []
labels: []
created_at: '2018-04-21T21:02:18+00:00'
updated_at: '2018-04-22T12:39:33+00:00'
type: issue
status: closed
closed_at: '2018-04-22T12:06:24+00:00'
---

# Original Description
Currently, the "make_integrated_address" API in monero-wallet-rpc only generates an integrated address for the main account (at address_index 0). 

There should be a version of "make_integrated_address" which can work on sub-addresses. Such as make_integrated_address(address_index) and/or make_integrated_address(address).

This could be done adding by optional parameters to the existing make_integrated_address API.

e.g.

```
{
	"jsonrpc":"2.0","id":"0",
	"method":"make_integrated_address",
	"params": {
		"address_index": 3
	}
}
```

**Use case:** User wants to track individual payments to each subaddress.

# Discussion History
## moneroexamples | 2018-04-22T06:31:29+00:00
You mean making integrated sub-addresses? If so, this has been discussed already and the idea of integrated sub-addresses has been dropped. 

https://github.com/monero-project/monero/pull/2056#issuecomment-318844037

## krtschmr | 2018-04-22T08:27:10+00:00
subadresses don't have payment IDs, or am i wrong?

## moneromooo-monero | 2018-04-22T10:30:25+00:00
Subaddresses are supposed to obsolete payment ids.

## mmorrell | 2018-04-22T12:06:24+00:00
Fair enough. Thanks for looking into this.

# Action History
- Created by: mmorrell | 2018-04-21T21:02:18+00:00
- Closed at: 2018-04-22T12:06:24+00:00
