---
title: add check to make sure arguments of --log-file and --wallet-file are not pointing
  to the same file
source_url: https://github.com/monero-project/monero/issues/820
author: mbg033
assignees: []
labels:
- invalid
created_at: '2016-04-26T12:33:55+00:00'
updated_at: '2017-10-03T10:30:23+00:00'
type: issue
status: closed
closed_at: '2017-10-03T10:30:23+00:00'
---

# Original Description
e.g. following command will silently overwrite the wallet:
`simplewallet --wallet-file wallet_m --password "" --log-file wallet_m --command balance`


# Discussion History
## moneromooo-monero | 2016-04-26T16:28:48+00:00
I guess one could check against other files in the command line, but then why not the lmdb files, well known system files, etc. The program is doing what was asked. But a patch would be fine I guess.


## luigi1111 | 2016-12-15T17:44:07+00:00
It seems like the log file shouldn't overwrite any existing non-text files (and should append to such a file). That might be easy or hard to implement. :)

## moneromooo-monero | 2017-09-20T21:18:15+00:00
Logs do append. Analyzing existing files to see if they're logs or not... Meh.


## moneromooo-monero | 2017-10-03T10:26:38+00:00
I'm not going to do that. Just don't point your log file at your wallet ^_^

+invalid


# Action History
- Created by: mbg033 | 2016-04-26T12:33:55+00:00
- Closed at: 2017-10-03T10:30:23+00:00
