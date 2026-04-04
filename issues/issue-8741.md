---
title: wallet RPC method generate_from_keys with bad address
source_url: https://github.com/monero-project/monero/issues/8741
author: dimalinux
assignees: []
labels:
- bug
- low priority
created_at: '2023-02-15T05:43:24+00:00'
updated_at: '2023-12-09T12:18:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The `generate_from_keys` RPC method takes an `address` field that is required when creating a view-only wallet (i.e. no `spendkey` passed), but should be optional (although it is not documented that way) when creating a spend wallet (`spendkey` field passed).

Problems:
(1) If, when passing a `spendkey` field, but not passing an `address` field, the `address` field returned by `generate_from_keys` should be correctly filled in. (Right now it is empty, but the wallet works and `get_address` on the 0 index returns the correct address.)
(2) If, when passing a `spendkey` field and also passing an `address` field, `generate_from_keys` should error if the passed address does not match the address generated from the passed `spendkey` and `viewkey`. Right now you just get a wallet that looks like it succeeded, but will fail if you try to transfer out of it.

I'm using:
```
monero-wallet-rpc --version
Monero 'Fluorine Fermi' (v0.18.1.2-release)
```

# Discussion History
# Action History
- Created by: dimalinux | 2023-02-15T05:43:24+00:00
