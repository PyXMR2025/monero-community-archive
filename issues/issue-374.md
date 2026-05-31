---
title: Failed to switch to alternative blockchain
source_url: https://github.com/seraphis-migration/monero/issues/374
author: j-berman
assignees: []
labels: []
created_at: '2026-05-12T20:31:00+00:00'
updated_at: '2026-05-30T22:56:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Multiple users reporting this error message in their logs. @nahuhh notes:

> I get that but then it successfully reorgs after a second attempt

Log level 2 with this would be good to narrow it down.

# Discussion History
## SNeedlewoods | 2026-05-13T16:40:26+00:00
[bitmonero.log-2026-05-13-02-52-58.tar.gz](https://github.com/user-attachments/files/27719622/bitmonero.log-2026-05-13-02-52-58.tar.gz)
[bitmonero.log-2026-05-13-02-55_09.tar.gz](https://github.com/user-attachments/files/27719623/bitmonero.log-2026-05-13-02-55_09.tar.gz)

## j-berman | 2026-05-13T17:07:34+00:00
What's happening:

1. Tx A gets kicked from the pool because the pool is at capacity.
2. Node receives alt block that has Tx A in it.
3. Node fails to switch to that alt fluffy block on first try because it's missing Tx A.
4. [Not in the above logs but assumed] The node successfully queries for the missing tx via the normal sync flow.

I'll update this comment with more clarity on step 4, but for now this doesn't look like a major issue. The node recovers smoothly from it, though it could handle the case where it's missing Tx A in step 3 smoother.

## selsta | 2026-05-14T14:55:10+00:00
[failed_switch.log.zip](https://github.com/user-attachments/files/27764697/failed_switch.log.zip)

## j-berman | 2026-05-30T22:56:01+00:00
Tbc, @selsta 's fail to switch error was caused by the v1 consensus issue (#393). @SNeedlewoods `Failed to switch` looks like [this is the cause](https://github.com/seraphis-migration/monero/issues/374#issuecomment-4443482031).

# Action History
- Created by: j-berman | 2026-05-12T20:31:00+00:00
