---
title: 'wallet_rpc: generate_from_keys not setting seed language'
source_url: https://github.com/monero-project/monero/issues/7414
author: camthegeek
assignees: []
labels: []
created_at: '2021-03-01T21:21:43+00:00'
updated_at: '2021-06-25T18:48:40+00:00'
type: issue
status: closed
closed_at: '2021-06-25T18:48:40+00:00'
---

# Original Description
When restoring with keys via wallet-rpc method `generate_from_keys`, the **wallet seed language is not set**.

The wallet is created on the wallet-rpc server and does operate normally, however, when trying to request the mnemonic via query_keys, result is 'Failed to get seed'.

Upon entering wallet using CLI and typing `seed`, the wallet returns with `seed_language not set`.

Could we default to English on this function but have the ability to define which language to restore in?



# Discussion History
## moneromooo-monero | 2021-03-05T12:59:46+00:00
https://github.com/monero-project/monero/pull/7430

## camthegeek | 2021-03-05T13:48:40+00:00
7430 does fix this issue. 

Thanks

# Action History
- Created by: camthegeek | 2021-03-01T21:21:43+00:00
- Closed at: 2021-06-25T18:48:40+00:00
