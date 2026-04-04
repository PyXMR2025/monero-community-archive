---
title: 'bitmonerod: armv7: segfault in mdb_cursor_unref with max-concurrency > 1'
source_url: https://github.com/monero-project/monero/issues/1001
author: radfish
assignees: []
labels: []
created_at: '2016-08-29T04:17:28+00:00'
updated_at: '2017-09-24T19:24:11+00:00'
type: issue
status: closed
closed_at: '2017-09-24T19:24:11+00:00'
---

# Original Description
Commit 16e9dbc

Segfault happened while catching up from about 99.6% sync status.

```
(gdb) bt
#0  0x0035540c in mdb_cursor_unref ()
#1  0x00355384 in mdb_page_unref.isra ()
Backtrace stopped: previous frame identical to this frame (corrupt stack?)
```

[thread apply all bt](https://github.com/monero-project/bitmonero/files/441650/bt.txt)

Core file available. Will try to replicate in a debug build.


# Discussion History
## radfish | 2016-08-29T15:28:41+00:00
looks like `max-concurrency 1` prevents this. It must be the same problem I reported earlier in a random comment somewhere. At the time I did not get a core, and it was not reproducible inside gdb. Now I have a core.


## radfish | 2017-09-24T19:24:11+00:00
Been running for weeks on armv7h without amx-concurrency=1 fine.

# Action History
- Created by: radfish | 2016-08-29T04:17:28+00:00
- Closed at: 2017-09-24T19:24:11+00:00
