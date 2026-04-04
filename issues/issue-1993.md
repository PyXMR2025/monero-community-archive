---
title: Missing wallet rpc methods in wallet-rpc.md
source_url: https://github.com/monero-project/monero-site/issues/1993
author: MexicanTakeout
assignees: []
labels:
- '📚 docs: dev guides'
created_at: '2022-07-01T23:36:25+00:00'
updated_at: '2022-12-21T10:17:37+00:00'
type: issue
status: closed
closed_at: '2022-12-21T10:17:37+00:00'
---

# Original Description
A few methods I found missing in wallet-rpc.md while checking wallet_rpc_server.h
from [here](https://github.com/monero-project/monero/blob/9750e1fa103539b3e533455500610aae76e253a5/src/wallet/wallet_rpc_server.h#L70)
... to [here](https://github.com/monero-project/monero/blob/9750e1fa103539b3e533455500610aae76e253a5/src/wallet/wallet_rpc_server.h#L163)

- freeze
- thaw
- frozen
- sweep_unmixable
- scan_tx 
- exchange_multisig_keys
- set_log_level
- set_log_categories
- estimate_tx_size_and_weight

Let me know if you need a script showing these diffs.

# Discussion History
## eversinc33 | 2022-07-20T19:27:13+00:00
sweep_unmixable is available in the documentation as sweep_dust (where the former is an alias for the latter).

Came here to open an issue about the same thing though.

## plowsof | 2022-12-10T04:45:58+00:00
closed by #2083 

# Action History
- Created by: MexicanTakeout | 2022-07-01T23:36:25+00:00
- Closed at: 2022-12-21T10:17:37+00:00
