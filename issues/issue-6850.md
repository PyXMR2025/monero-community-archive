---
title: monero-wallet-rpc error creating multisig tx if wallet is refreshed after import_multisig_hex
  instead of before
source_url: https://github.com/monero-project/monero/issues/6850
author: woodser
assignees: []
labels: []
created_at: '2020-09-28T13:16:23+00:00'
updated_at: '2020-09-28T13:16:23+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm seeing a difference in behavior from monero-wallet-rpc v0.16.0.3 to v0.17.0.1 wherein opening the wallet, importing peer multisig hex, then explicitly refreshing yields an error "No transaction created" on `transfer_split`.  The error is resolved by calling `refresh` before calling `import_multisig_hex`.

# Discussion History
# Action History
- Created by: woodser | 2020-09-28T13:16:23+00:00
