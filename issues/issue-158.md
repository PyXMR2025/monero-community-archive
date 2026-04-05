---
title: 'Wallet error: prove_membership failed with code: -1'
source_url: https://github.com/seraphis-migration/monero/issues/158
author: j-berman
assignees: []
labels: []
created_at: '2025-10-09T20:13:00+00:00'
updated_at: '2025-12-09T16:20:39+00:00'
type: issue
status: closed
closed_at: '2025-12-09T16:20:39+00:00'
---

# Original Description
Reported by u/Lyza in stressnet channel. Encountered the error while using the GUI wallet:

> the second attempt succeeded so it was a transient error, seemed like it happened as the node received a block during TX construction

Not certain what the cause might be yet.

Tangential point: the code should probably use distinct error codes for each of these potential errors: https://github.com/seraphis-migration/monero/blob/b82832effcd434219d49b247c6fe56dd0584a632/src/fcmp_pp/fcmp_pp_rust/src/lib.rs#L782-L800

# Discussion History
## j-berman | 2025-10-21T23:48:00+00:00
I think this may have been caused by the same issue causing #164. If you still experience this after upgrading, let me know!

EDIT: lol, forgot I opened this. DM'd on matrix.

## j-berman | 2025-12-09T16:20:39+00:00
Seems to be solved by #164

# Action History
- Created by: j-berman | 2025-10-09T20:13:00+00:00
- Closed at: 2025-12-09T16:20:39+00:00
