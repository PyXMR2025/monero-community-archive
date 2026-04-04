---
title: Redefinition of WALLET_RPC_VERSION_MINOR
source_url: https://github.com/monero-project/monero/issues/8376
author: woodser
assignees: []
labels: []
created_at: '2022-06-04T14:13:54+00:00'
updated_at: '2022-06-05T12:56:57+00:00'
type: issue
status: closed
closed_at: '2022-06-05T12:56:57+00:00'
---

# Original Description
The release-v0.17 branch defines `WALLET_RPC_VERSION_MINOR` twice, causing a warning.

https://github.com/monero-project/monero/blob/424e4de16b98506170db7b0d7d87a79ccf541744/src/wallet/wallet_rpc_server_commands_defs.h#L51

# Discussion History
## selsta | 2022-06-04T23:02:06+00:00
Sorry, my mistake, overlooked it during review: https://github.com/monero-project/monero/pull/8166

Shouldn't have any bad consequences apart from the warning.

# Action History
- Created by: woodser | 2022-06-04T14:13:54+00:00
- Closed at: 2022-06-05T12:56:57+00:00
