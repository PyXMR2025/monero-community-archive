---
title: 'CLI: slow refresh when pool is large'
source_url: https://github.com/seraphis-migration/monero/issues/152
author: j-berman
assignees: []
labels:
- upstream
created_at: '2025-10-09T00:04:04+00:00'
updated_at: '2025-10-21T23:49:27+00:00'
type: issue
status: closed
closed_at: '2025-10-21T23:49:27+00:00'
---

# Original Description
I'm noticing every refresh attempt is slow because my wallet is requesting every tx in the pool every refresh loop. That shouldn't be happening. The wallet should only be requesting txs it hasn't seen yet.

# Discussion History
## j-berman | 2025-10-09T00:25:58+00:00
It's because `try_incremental` is false [here](https://github.com/monero-project/monero/blob/d32b5bfe18e2f5b979fa8dc3a8966c76159ca722/src/simplewallet/simplewallet.cpp#L5745-L5748).



## j-berman | 2025-10-09T00:39:52+00:00
I think a better approach would be to not fetch pool data at all when background/idle refreshing (i.e. when `check_pool` is false in the current impl), but to always use the incremental approach when foreground refreshing. Otherwise the CLI won't benefit from incremental refresh.

This is an upstream issue as well.

## j-berman | 2025-10-21T23:49:27+00:00
Fixed by #162, included in v1.3 of the alpha stressnet release

# Action History
- Created by: j-berman | 2025-10-09T00:04:04+00:00
- Closed at: 2025-10-21T23:49:27+00:00
