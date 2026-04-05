---
title: Wallet tracking/storing 0 value outputs
source_url: https://github.com/seraphis-migration/monero/issues/247
author: nahuhh
assignees: []
labels: []
created_at: '2025-11-29T19:50:15+00:00'
updated_at: '2025-12-15T18:21:14+00:00'
type: issue
status: closed
closed_at: '2025-12-15T18:21:14+00:00'
---

# Original Description
Seemingly caused by sweep, the wallet stores the 0 value change output, visible in unspent _outputs of wallet-cli, and in the log level 2 when wallet-rpc evaluates which inputs to use when building a tx

i imagine this might slow down other functions of the wallet as well

# Discussion History
## jeffro256 | 2025-12-01T03:56:47+00:00
Was this wallet restored from seed at some point?

## nahuhh | 2025-12-01T15:13:08+00:00
> Was this wallet restored from seed at some point?


not restored from seed, but similar. It's had the restore height moved up and rescan_bc or deleted the cache file.

i assume that these appear after sending txs, not immediately on restore. I'll double check


## jeffro256 | 2025-12-01T15:22:04+00:00
Okay that matches expectations then, thank you, #248 should fix. 

# Action History
- Created by: nahuhh | 2025-11-29T19:50:15+00:00
- Closed at: 2025-12-15T18:21:14+00:00
