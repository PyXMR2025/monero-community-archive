---
title: monero db-type option
source_url: https://github.com/monero-project/monero/issues/1533
author: sHAsHiLx
assignees: []
labels: []
created_at: '2017-01-06T21:52:15+00:00'
updated_at: '2017-08-08T12:06:16+00:00'
type: issue
status: closed
closed_at: '2017-08-08T12:06:16+00:00'
---

# Original Description
typed monerod --help and see option "--db-type". tried to use it. tried to give something like "bin" as option. why? because there is no documentation about it so used anything i want. get error about it and at least get what i can provide - berkeley or lmdb. provided "berkeley" as option. received error about berkeley is disabled. then why this option is still here if only lmdb is enabled??? why no documentation about what option this arg accept?? why no any other documentation about other options (i mean about other options what I can get from --help command and see "args" as command option)? why I must provide something like "kdsbndewk" to receive error and see what other args want as options???
sorry for my english

# Discussion History
## moneromooo-monero | 2017-01-07T12:53:40+00:00
It is an obsolete option. Berkeley DB is not usable anymore, as LMDB now works fine on 32 bits, which was the bdb niche.


## sHAsHiLx | 2017-01-07T13:01:12+00:00
remove it then?
also what about other args not documented and can be only understun to provide some fake args and only after it receive whar args can be?

## moneromooo-monero | 2017-08-08T11:50:44+00:00
+resolved

# Action History
- Created by: sHAsHiLx | 2017-01-06T21:52:15+00:00
- Closed at: 2017-08-08T12:06:16+00:00
