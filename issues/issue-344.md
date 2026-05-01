---
title: restoring from seed fails to sync
source_url: https://github.com/seraphis-migration/monero/issues/344
author: nahuhh
assignees: []
labels: []
created_at: '2026-04-29T13:00:03+00:00'
updated_at: '2026-04-29T13:11:14+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
```
Error: refresh failed: internal error: Unrecognized exception in enote scanning threadpool. Blocks received: 264000
```

`./monero-wallet-cli --testnet --restore-determ`

reported on matrix by thankful_for_never


Edit: this also happens when using an existing key file

it seems to be trying to rewind the wallet, as even starting with a synced master-testnet wallet, the sync progress starts from zero

```
2026-04-29 13:08:33.168     74c2399fe6c0        DEBUG   serialization   src/fcmp_pp/tree_cache.cpp:1114 Popping block 965003 from tree cache
2026-04-29 13:08:33.168     74c2399fe6c0        DEBUG   serialization   src/fcmp_pp/tree_cache.cpp:1114 Popping block 965002 from tree cache
2026-04-29 13:08:33.168     74c2399fe6c0        DEBUG   serialization   src/fcmp_pp/tree_cache.cpp:1114 Popping block 965001 from tree cache
2026-04-29 13:08:33.211     74c2399fe6c0        DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:3741     Finished restoring the tree cache
2026-04-29 13:08:33.212     74c2399fe6c0        ERROR   wallet.wallet2  src/wallet/wallet2.cpp:4474     Error processing parsed blocks: Unrecognized exception in enote scanning threadpool
```

# Discussion History
# Action History
- Created by: nahuhh | 2026-04-29T13:00:03+00:00
