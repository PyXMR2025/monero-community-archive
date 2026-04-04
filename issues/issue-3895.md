---
title: Feature Request - Actual log rotation, better log management
source_url: https://github.com/monero-project/monero/issues/3895
author: Gingeropolous
assignees: []
labels: []
created_at: '2018-05-31T20:14:19+00:00'
updated_at: '2018-06-20T21:56:56+00:00'
type: issue
status: closed
closed_at: '2018-06-20T21:56:56+00:00'
---

# Original Description
The current log management is ..... ok. It now creates 100 MB files. If a node is left to run... for a while... you end up with literally a bajillion log files, so many that you need to use a special trick to delete them all because using bitmonero.log-* exceeds bash's whatever whatever.

Thus, if monerod is going to do logrotation, can it do it properly? E.g., only write 50 files, and then delete the old ones as new ones are written? And this could be tunable. Yes, I know, setting the logfile limit to 0 allows the logfile to grow as it used to and then the system logrotate can manage it properly, but i don't think the base behavior of monerod should be to balloon log files until there are so many files a user can't delete them easily. 

# Discussion History
## stoffu | 2018-06-01T03:31:16+00:00
#3897 

## moneromooo-monero | 2018-06-20T21:51:59+00:00
+resolved

# Action History
- Created by: Gingeropolous | 2018-05-31T20:14:19+00:00
- Closed at: 2018-06-20T21:56:56+00:00
