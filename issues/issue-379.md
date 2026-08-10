---
title: Docs say maximum priority is 3 while the real maximum is 4
source_url: https://github.com/monero-project/monero-docs/issues/379
author: Jacoblightning
assignees: []
labels: []
created_at: '2026-08-08T04:17:26+00:00'
updated_at: '2026-08-08T04:17:26+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
In the wallet-rpc docs, under both [`transfer`](https://docs.getmonero.org/rpc-library/wallet-rpc/#transfer) and [`transfer_split`](https://docs.getmonero.org/rpc-library/wallet-rpc/#transfer_split), it says that accepted values for `priority` are 0-3 and then lists 5 things they correspond to: default, unimportant, normal, elevated, priority.

The actual maximum priority value is 4 as seen [in the `on_transfer` function](https://github.com/monero-project/monero/blob/d56daee/src/wallet/wallet_rpc_server.cpp#L1254-L1259) where it calls[ `fee_priority_utilities::is_valid`](https://github.com/monero-project/monero/blob/d56daee995d176f3ab2f38ef3d1e4d8e1bd4aa44/src/wallet/fee_priority.h#L91-L94) which checks whether the priority is less than or equal to 4.

# Discussion History
# Action History
- Created by: Jacoblightning | 2026-08-08T04:17:26+00:00
