---
title: RPC createwallet method does not remove filelock on completion
source_url: https://github.com/monero-project/monero/issues/4990
author: TylerTheFox
assignees: []
labels: []
created_at: '2018-12-17T17:55:15+00:00'
updated_at: '2018-12-17T22:06:11+00:00'
type: issue
status: closed
closed_at: '2018-12-17T22:06:11+00:00'
---

# Original Description
Version: https://github.com/monero-project/monero/releases/tag/v0.13.0.4

Monero RPC (monero-wallet-rpc WIN32/LINUX) method `create_wallet` does not release the file lock after it returns from creating the wallet. Thus the newly created wallet cannot be opened by both Monero RPC or deleted by the system administrator. 

RPC `create_wallet` POST DATA
`{ "id" : "0", "jsonrpc" : "2.0", "method" : "create_wallet", "params" : { "filename" : "Discord-User-431682365832691722", "language" : "English", "password" : "" } }`

RPC `create_wallet` JSON return 
```
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
  }
}
```

When you try to open newly created wallet from the same RPC that created it.
`2018-12-17 17:54:15.416 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:4582     !is_keys_file_locked(). THROW EXCEPTION: error::wallet_internal_error`

Requires RPC that created the wallet to be terminated/restarted before the wallet can be opened.

# Discussion History
## moneromooo-monero | 2018-12-17T20:59:10+00:00
That's because it is open. If you want to open it again, close it first.

## TylerTheFox | 2018-12-17T21:08:46+00:00
Oh has the behavior of the rpc changed to auto open the wallets on create wallet? It didnt always do that. 

Shouldnt it relesse the file lock of the old wallet first when open wallet is called before it attempts to load? 

## moneromooo-monero | 2018-12-17T21:12:14+00:00
I don't know. Reading the code, it currently does not close it.
It closes the old wallet if the new one's creation succeds. If it fails, the old wallet is kept open.

## TylerTheFox | 2018-12-17T22:06:11+00:00
Thanks ill close this unless you think it needs to stay open. 

# Action History
- Created by: TylerTheFox | 2018-12-17T17:55:15+00:00
- Closed at: 2018-12-17T22:06:11+00:00
