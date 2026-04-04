---
title: simplewallet infity loop on Ctrl-D
source_url: https://github.com/monero-project/monero/issues/771
author: fanatid
assignees: []
labels: []
created_at: '2016-03-29T08:36:56+00:00'
updated_at: '2016-04-02T03:04:45+00:00'
type: issue
status: closed
closed_at: '2016-04-02T03:04:45+00:00'
---

# Original Description
```
./simplewallet
..
^D
Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
Wallet file name: Error: wallet file path not valid: 
Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
Wallet file name: Error: wallet file path not valid: 
```

it generate infinity loop, because [ask_wallet_create_if_needed uses do-while without exit condition](https://github.com/monero-project/bitmonero/blob/0ee87e63050c31405182042868a89d4f3f3ac7c2/src/simplewallet/simplewallet.cpp#L696)


# Discussion History
## moneromooo-monero | 2016-03-29T16:53:54+00:00
https://github.com/monero-project/bitmonero/pull/772


## fluffypony | 2016-04-02T03:04:45+00:00
Fixed via #772


# Action History
- Created by: fanatid | 2016-03-29T08:36:56+00:00
- Closed at: 2016-04-02T03:04:45+00:00
