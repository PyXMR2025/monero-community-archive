---
title: Bump default mempool max weight
source_url: https://github.com/seraphis-migration/monero/issues/274
author: j-berman
assignees: []
labels: []
created_at: '2025-12-18T18:49:38+00:00'
updated_at: '2025-12-18T18:49:38+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Raised by @nahuhh and @Rucknium on various occasions in discussions in MRL / stressnet channel.

Since FCMP++ txs are larger, it seems to make some sense to bump the default max weight from 600mb. A limit of 1GB seems sane to me.

It's worth keeping in mind that wallets are not currently optimally structured to handle ingesting a large pool:

1) Wallets will reload / rescan the entire pool on open every time (#165).
2) Scanning the pool is currently single threaded.
3) It doesn't currently work on unrestricted RPC's (https://github.com/monero-project/monero/pull/9473).
4) Downloading over the restricted RPC is pretty slow since it chunks 100 txs at a time.

# Discussion History
# Action History
- Created by: j-berman | 2025-12-18T18:49:38+00:00
