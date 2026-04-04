---
title: Include block height/hash when possible for "/gettransactions" method
source_url: https://github.com/monero-project/monero/issues/707
author: bigreddmachine
assignees: []
labels: []
created_at: '2016-03-07T23:02:59+00:00'
updated_at: '2016-04-05T17:35:16+00:00'
type: issue
status: closed
closed_at: '2016-04-05T17:35:16+00:00'
---

# Original Description
This issue came up [on the forums](https://forum.getmonero.org/5/support/2494/rpc-get-transaction-by-hash).

When using the "/gettransactions" method, for example:

`curl http://localhost:18081/gettransactions -d '{"txs_hashes" : ["45f21d......"], "decode_as_json": True }'`

the following information is returned:

`{"extra": ..., "hash": ..., "signatures": [...], "unlock_time": ..., "version": ..., "vin": [...], "vout": [...]}`

It would be very helpful if block information was also included, such as
- height
- hash
- depth


# Discussion History
## moneromooo-monero | 2016-04-03T11:55:28+00:00
https://github.com/monero-project/bitmonero/pull/791 adds height.
The rest is easily obtainable, and would require more DB calls to include it even if the client doesn't need it, so I'm not sure it's worth adding here. Feel free to comment if you think it is.


## bigreddmachine | 2016-04-05T17:35:16+00:00
Yes, this looks perfect. Thanks @moneromooo-monero.


# Action History
- Created by: bigreddmachine | 2016-03-07T23:02:59+00:00
- Closed at: 2016-04-05T17:35:16+00:00
