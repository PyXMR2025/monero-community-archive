---
title: Transaction extra has unsupported format
source_url: https://github.com/monero-project/monero/issues/2875
author: Revinand
assignees: []
labels: []
created_at: '2017-11-28T18:50:36+00:00'
updated_at: '2023-01-12T04:58:46+00:00'
type: issue
status: closed
closed_at: '2017-12-13T21:16:25+00:00'
---

# Original Description
In the latest version (0.11.1) there are a lot of warnings on `rescan_blockchain` call:

```
monero-wallet-rpc[1467]: 2017-11-28 18:21:47.420#011[RPC0]#011WARN #011wallet.wallet2#011src/wallet/wallet2.cpp:660#011Transaction extra has unsupported format: <...>
```

I understand there is nothing criminal, but it seems that this increases request runtime.

# Discussion History
## stoffu | 2017-11-28T23:24:39+00:00
Transaction extra is used for attaching auxiliary data to the transaction such as the transaction public key and the payment ID, see https://github.com/monero-project/monero/blob/master/src/cryptonote_basic/tx_extra.h

The official wallet implements a standard protocol to write/read data to/from the tx extra using predefined prefixes, but anyone can modify the code and implement any sort of custom data format in order to attach other arbitrary data to the transaction.

TLDR; you can just ignore those warnings.

## moneromooo-monero | 2017-11-29T10:16:31+00:00
This was getting triggered for empty additional tx keys.

## stoffu | 2017-11-29T10:44:20+00:00
Aha, makes sense.

## moneromooo-monero | 2017-12-13T21:15:15+00:00
This was fixed for empty additional tx keys, it will be kept otherwise.

+resolved

## Revinand | 2018-01-12T13:38:47+00:00
Still see such messages. Can't understand does it affect `rescan_blockchain` command time execution anyhow? Looks like it does

## ghost | 2023-01-12T04:58:46+00:00
Still seeing these messages also. Unclear if it matters.

# Action History
- Created by: Revinand | 2017-11-28T18:50:36+00:00
- Closed at: 2017-12-13T21:16:25+00:00
