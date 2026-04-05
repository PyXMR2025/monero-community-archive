---
title: '[BUG] error: m_blockchain <> m_tree_cache top block idx mismatch'
source_url: https://github.com/seraphis-migration/monero/issues/45
author: j-berman
assignees: []
labels: []
created_at: '2025-05-16T01:12:54+00:00'
updated_at: '2025-10-03T16:29:10+00:00'
type: issue
status: closed
closed_at: '2025-10-03T16:29:10+00:00'
---

# Original Description
Reported by @ComputeryPony ([link](https://github.com/seraphis-migration/monero/pull/32#issuecomment-2878453797)):

> Got another bug. I was testing with a copy of stagenet. I had one node mining with 2 threads for ~90 blocks, during which I got a message about a block being added as an alternative. Then I switched to 1 thread and mined for another ~228 blocks. I went to the wallet this node was mining to and attempted a refresh to get this:

```
[wallet 5Ag1C5 (out of sync)]: refresh
Starting refresh...
Error: refresh failed: internal error: m_blockchain <> m_tree_cache top block idx mismatch (m_blockchain_top_block_idx: 1851805 vs tree top idx: 1851819). Blocks received: 0
```

> Was testing on the fcmp++ branch after the torsion ban patch was merged and with this PR applied.

_______

I haven't been able to repro this on the latest. I requested @ComputeryPony share log level 2 logs from the wallet if possible.

This issue can serve as a tracker for this bug.

# Discussion History
## plowsof | 2025-06-10T16:20:41+00:00
first off, apologies as i don't know what i've done to achieve this but i have this now:
```
Error: refresh failed: internal error: m_blockchain <> m_tree_cache top block idx mismatch (m_blockchain_top_block_idx: 2024 vs tree top idx: 0). Blocks received: 0
```
IIRC i changed the data dir of one of the running nodes which the wallet then connected to.

## j-berman | 2025-06-19T00:17:03+00:00
I still haven't been able to repro this issue and can't see how to trigger it. I will probably need more complete logs to be able to solve it or a definitive way to reproduce.

## ComputeryPony | 2025-10-02T01:56:45+00:00
I haven't had any luck in replicating this or #46 again and at this point the code has changed quite a bit from what I was testing before. I think you can just close these issues and reopen them only if we get some indication that this is still happening.

## nahuhh | 2025-10-02T10:22:47+00:00
Iirc this was due to having a no-zero restore height.

In any case, it was fixed

# Action History
- Created by: j-berman | 2025-05-16T01:12:54+00:00
- Closed at: 2025-10-03T16:29:10+00:00
