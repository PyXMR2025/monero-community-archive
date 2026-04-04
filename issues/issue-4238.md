---
title: LMDB v3 data format
source_url: https://github.com/monero-project/monero/issues/4238
author: troublesomepony
assignees: []
labels:
- invalid
created_at: '2018-08-08T10:45:08+00:00'
updated_at: '2018-08-08T23:37:50+00:00'
type: issue
status: closed
closed_at: '2018-08-08T16:17:02+00:00'
---

# Original Description
After I merged latest git trunk from this repo to my codebase and did first launch Monero reformatted Blockchain database twice (from 1 to 2 and from 2 to 3). But now seems I lost compatibility with application software used Monero partially too. Please point me where you set this format param so I could check everythins (explorer is broken for example). Thanks.

# Discussion History
## moneromooo-monero | 2018-08-08T16:12:07+00:00
It's not clear what you're asking, but if you have software which reads off the database directly, then fix it to match. See the git log on src/blockchain_db/lmdb/db_lmdb.cpp for the specific changes.

+invalid


## stoffu | 2018-08-08T23:37:49+00:00
@troublesomepony
If you want to make the explorer able to read the new db format, you need to rebuild it with the new Monero core library. 

# Action History
- Created by: troublesomepony | 2018-08-08T10:45:08+00:00
- Closed at: 2018-08-08T16:17:02+00:00
