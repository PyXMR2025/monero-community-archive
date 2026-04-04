---
title: No longer works with OSX 10.11 or earlier
source_url: https://github.com/monero-project/monero/issues/3774
author: RetroLemur
assignees: []
labels: []
created_at: '2018-05-07T17:47:38+00:00'
updated_at: '2018-05-09T19:56:48+00:00'
type: issue
status: closed
closed_at: '2018-05-09T19:56:48+00:00'
---

# Original Description
Downloaded the OSX binary and ran on 10.11.

Got this error:
dyld: Symbol not found: _clock_gettime
Referenced from /Users/admin/xmr/./monerod (which was built for Mac OS X 10.12)
Expected in /usr/lib/libSystem.B.dylib

Works OK on OS X 10.12 or later.  Is that really required?


# Discussion History
## moneromooo-monero | 2018-05-07T18:30:08+00:00
Probably just needs to link against whatever library has _clock_gettime on your machine. Not quite clear whether the message is saying "it's in /usr/lib/libSystem.B.dylib" or "it's not in /usr/lib/libSystem.B.dylib".
Did a previous monero version work on that 10.11 system ?
If so, what version ?

## dEBRUYNE-1 | 2018-05-08T09:14:31+00:00
@RetroLemur - Try the `monerod` that is included in the GUI binaries:

https://github.com/monero-project/monero-gui/releases/tag/v0.12.0.0

It was built on a 10.11 system, whereas `monerod` for the CLI binaries was built on a 10.12 system. 

## dEBRUYNE-1 | 2018-05-09T19:54:39+00:00
+resolved

# Action History
- Created by: RetroLemur | 2018-05-07T17:47:38+00:00
- Closed at: 2018-05-09T19:56:48+00:00
