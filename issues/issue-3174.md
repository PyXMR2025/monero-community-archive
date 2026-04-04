---
title: RPC get_transaction_pool not json serializable
source_url: https://github.com/monero-project/monero/issues/3174
author: bianchimro
assignees: []
labels: []
created_at: '2018-01-23T12:09:43+00:00'
updated_at: '2018-07-19T22:09:02+00:00'
type: issue
status: closed
closed_at: '2018-07-19T22:09:02+00:00'
---

# Original Description
RPC method `get_transaction_pool` in master branch (I'm looking at commit 5f09d6c) returns an object with the `tx_blob`, not present in the latest released version (0.11.1.0).

IMHO this creates two problems:

- the content of this key is not JSON serializable
- the serialization takes quite a long time, resulting in very slow response of this API call 

I see two possible options:

- adding an optional parameter to `get_transaction_pool` for omitting `tx_blob`
- create a separate endpoint for this purpose



# Discussion History
## moneromooo-monero | 2018-01-23T14:02:02+00:00
I'd be fine with a flag. There's a get_transaction_pool_hashes call too, wihch is meant to be faster (you then ask for tx data for those txes you haven't seen before). I think the blob should be the hex representation of that tx, not the raw binary anyway, and that'd be JSON friendly.

## bianchimro | 2018-01-23T15:13:09+00:00
@moneromooo-monero thanks for your quick response.

Didn't know about the get_transaction_pool_hashes, thanks for pointing out.

And yes, the hex representation of the tx would be JSON serializable, as it happens in other RPC calls.

## PochenriederAlex | 2018-04-23T14:04:44+00:00
I support the idea of returning tx_blob in hex representation just like gettransactions call. I used to call this method but since the tx_blob was added  i can't parse the response.

@moneromooo-monero  get_transaction_pool_hashes have also a mixed format response.
It's not a full binary response. It's a json with a Binary stream in the tx_hashes field so it's not JSON serializable either.

So, there's another way i can get mempool transactions or at least the hashes to call gettransactions later? 


## moneromooo-monero | 2018-06-20T11:52:21+00:00
https://github.com/monero-project/monero/pull/4033

The new RPC is called without the .bin suffix.

## moneromooo-monero | 2018-07-19T21:57:04+00:00
+resolved

# Action History
- Created by: bianchimro | 2018-01-23T12:09:43+00:00
- Closed at: 2018-07-19T22:09:02+00:00
