---
title: Button for deleting p2pstate.bin
source_url: https://github.com/monero-project/monero-gui/issues/892
author: scoobybejesus
assignees: []
labels:
- resolved
created_at: '2017-09-26T21:58:46+00:00'
updated_at: '2018-12-15T08:36:24+00:00'
type: issue
status: closed
closed_at: '2018-12-15T08:36:24+00:00'
---

# Original Description
Ideally, in the future, there will be no need for this.  But there seem to be a lot of support requests that require people deleting p2pstate.bin.  This file is in a hidden folder.  Newbies can't find it.  A simple fix of "close the GUI, delete p2pstate.bin, and restart the GUI" turns into several hours of going back and forth on reddit.  A button would simplify solving this issue massively.

# Discussion History
## QuickBASIC | 2017-10-01T04:38:46+00:00
How about a batch file in the program directory (Windows) or sh (Linux) that does a taskill and deletes the file? I don't like the idea of needlessly bloating the GUI with things like this.

```
@echo off
taskkill /im monerod.exe
del %PROGRAMDATA%/bitmonero/p2pstate.bin
```
Honestly, deleting the p2pstate.bin is a kludge. We'd be better off solving the root cause.


## sanderfoobar | 2018-12-12T11:32:37+00:00
This issue has not received any attention for over a year. I'd argue we can keep this functionality out of the GUI. @QuickBASIC Feel free to submit your shell script as a PR. Closing for now.

+resolved

## dEBRUYNE-1 | 2018-12-15T08:23:48+00:00
+resolved

# Action History
- Created by: scoobybejesus | 2017-09-26T21:58:46+00:00
- Closed at: 2018-12-15T08:36:24+00:00
