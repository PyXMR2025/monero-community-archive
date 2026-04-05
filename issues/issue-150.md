---
title: CLI slow `show_transfers` on large pool
source_url: https://github.com/seraphis-migration/monero/issues/150
author: j-berman
assignees: []
labels:
- upstream
created_at: '2025-10-08T21:49:53+00:00'
updated_at: '2025-10-21T23:49:34+00:00'
type: issue
status: closed
closed_at: '2025-10-21T23:49:34+00:00'
---

# Original Description
Reported by @SNeedlewoods.

Caused by the wallet re-fetching and re-scanning the whole pool [here](https://github.com/monero-project/monero/blob/d32b5bfe18e2f5b979fa8dc3a8966c76159ca722/src/simplewallet/simplewallet.cpp#L8574).

This is present upstream (worth an issue there too).

Solution may be to just use the incremental approach in that call linked above. Ping @rbrunner7 in case he has thoughts on why that wasn't done before (I don't recall). Related: https://github.com/monero-project/monero/pull/8076

# Discussion History
## j-berman | 2025-10-21T23:49:34+00:00
Fixed by #162, included in v1.3 of the alpha stressnet release

# Action History
- Created by: j-berman | 2025-10-08T21:49:53+00:00
- Closed at: 2025-10-21T23:49:34+00:00
