---
title: Got NOTIFY_RESPONSE_CHAIN_ENTRY past expected height, dropping connection
source_url: https://github.com/seraphis-migration/monero/issues/264
author: j-berman
assignees: []
labels: []
created_at: '2025-12-12T04:11:18+00:00'
updated_at: '2025-12-15T17:42:23+00:00'
type: issue
status: closed
closed_at: '2025-12-15T17:42:23+00:00'
---

# Original Description
Seeing lots of these in my logs while syncing:

```
2025-12-12 04:05:47.183	I [<IP addr> OUT] Received NOTIFY_RESPONSE_CHAIN_ENTRY: m_block_ids.size()=743, m_start_height=2893839, m_total_height=2894582
2025-12-12 04:05:47.183	I [<IP addr> OUT] [0] state: received chain in state synchronizing
2025-12-12 04:05:47.183	E [<IP addr> OUT] Got NOTIFY_RESPONSE_CHAIN_ENTRY past expected height, dropping connection
2025-12-12 04:05:47.183	D [<IP addr>] dropping connection id 307c60f2-0f30-4253-8dcd-8fe2904c0a9a (pruning seed 0), score 1, flush_all_spans 0
2025-12-12 04:05:47.183	D Host <IP addr> fail score=11
2025-12-12 04:05:47.184	I Host <IP addr> blocked.
```

Seems to be a prevalent cause of connection drops / blocks.

Also reported [here](https://github.com/seraphis-migration/monero/issues/180#issuecomment-3505567985)


# Discussion History
## j-berman | 2025-12-12T04:48:27+00:00
Looks like a race, simple fix. PR incoming

# Action History
- Created by: j-berman | 2025-12-12T04:11:18+00:00
- Closed at: 2025-12-15T17:42:23+00:00
