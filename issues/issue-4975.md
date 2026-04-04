---
title: ' Two request make this error'
source_url: https://github.com/monero-project/monero/issues/4975
author: steffanjensen
assignees: []
labels:
- invalid
created_at: '2018-12-12T14:44:52+00:00'
updated_at: '2019-01-01T14:16:59+00:00'
type: issue
status: closed
closed_at: '2019-01-01T14:16:59+00:00'
---

# Original Description
After two request i start to get this error, did this not happen a few weeks ago?

018-11-29 00:41:46.706 [RPC0] ERROR wallet.wallet2 src/wallet/wallet2.cpp:4582 !is_keys_file_locked(). THROW EXCEPTION: error::wallet_internal_error

I talked with other devs, they say it's a problem with monero rpc.

https://github.com/monero-integrations/monerophp/issues/80


# Discussion History
## moneromooo-monero | 2018-12-12T14:46:46+00:00
What monero version ? What requests ? What other pertinent information ?

## steffanjensen | 2018-12-12T14:51:31+00:00
When i run two instance of the same key with rpc i get this error. No issue from version 12 and before, started after release of 12.

## moneromooo-monero | 2018-12-12T14:55:58+00:00
By "key" you mean "wallet file" ?

## steffanjensen | 2018-12-12T15:38:40+00:00
yes the wallet file, I just woke up.. I will get better logs files soon, sorry for that. 

## moneromooo-monero | 2018-12-12T15:53:39+00:00
Then it's normal. Do not run two wallet programs on the same wallet file at the same time.


## moneromooo-monero | 2019-01-01T14:10:17+00:00
+invalid

# Action History
- Created by: steffanjensen | 2018-12-12T14:44:52+00:00
- Closed at: 2019-01-01T14:16:59+00:00
