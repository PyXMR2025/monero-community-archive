---
title: stray char in migration logs still
source_url: https://github.com/seraphis-migration/monero/issues/149
author: j-berman
assignees: []
labels: []
created_at: '2025-10-08T21:40:19+00:00'
updated_at: '2026-04-20T17:28:13+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Reported by @nahuhh even after applying #128:

```
2025-10-06 17:25:06.239 I Setting up a locked outputs table (step 1/2 of the full-chain membership proof migration) 
2025-10-06 17:25:59.909 I Setting up a merkle tree using existing cryptonote outputs (step 2/2 of the full-chain membership proof migration)
80050 / 2847320 blocks (2% of step 2/2)2)
```

# Discussion History
## j-berman | 2026-04-20T17:28:13+00:00
Want to re-test before closing this issue

# Action History
- Created by: j-berman | 2025-10-08T21:40:19+00:00
