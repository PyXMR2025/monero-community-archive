---
title: Rename the new "global" output indexes to "unified" indexes
source_url: https://github.com/seraphis-migration/monero/issues/280
author: j-berman
assignees: []
labels: []
created_at: '2026-01-05T18:56:22+00:00'
updated_at: '2026-02-16T21:00:16+00:00'
type: issue
status: closed
closed_at: '2026-02-16T21:00:16+00:00'
---

# Original Description
There has been some confusion over usage of "global" to refer to the unique ID assigned to every single output in the chain (untethered to the output's amount i.e. pre-RingCT can be output n, and no other output in the chain pre-RCT or post-RCT can be output n also). That is because the term "global" has already been used to refer to the "global **amount** output index" that **is** tethered to amount (i.e. there can be pre-RCT amount n output m, and RCT amount 0 output m, and that index is *also* called "global" in the RPC and in code across the repo).

@jeffro256 proposed using the term "unified" output ID's to refer to these output ID's we're using for FCMP++. Unified is a good term because we're "unifying" pre-RCT and post-RCT into one anon set for FCMP++, and FCMP++ is proving membership for outputs among that unified set.

# Discussion History
# Action History
- Created by: j-berman | 2026-01-05T18:56:22+00:00
- Closed at: 2026-02-16T21:00:16+00:00
