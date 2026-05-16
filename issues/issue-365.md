---
title: Sporadic double spends & broken rescan_spent
source_url: https://github.com/seraphis-migration/monero/issues/365
author: j-berman
assignees: []
labels: []
created_at: '2026-05-08T22:13:13+00:00'
updated_at: '2026-05-13T18:31:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Reported by u/kico in the stressnet channel:

> rescan_spent on cli seems to really do nothing

# Discussion History
## j-berman | 2026-05-09T03:13:48+00:00
Helpful logs from u/kico that indicate `rescan_spent` isn't identifying the spends as expected:

[8terjt.log](https://github.com/user-attachments/files/27544950/8terjt.log)

Can see double spend errors for a tx with the same key images before *and* after `rescan_spent`.

Plus, `rescan_spent` *is* identifying some spends previously marked as unspent, which is also unexpected. The wallet should be identifying all spends during the normal refresh flow.

## j-berman | 2026-05-13T18:31:03+00:00
Multiple users have complained about sporadic double spend errors. May be a regression from #185

# Action History
- Created by: j-berman | 2026-05-08T22:13:13+00:00
