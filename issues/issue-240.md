---
title: rcp-bind bitmonerod crashes with too many open files.
source_url: https://github.com/monero-project/monero/issues/240
author: iamsmooth
assignees: []
labels: []
created_at: '2015-03-13T19:18:47+00:00'
updated_at: '2015-11-24T14:49:02+00:00'
type: issue
status: closed
closed_at: '2015-11-24T14:49:02+00:00'
---

# Original Description
Reported by TheKoziTwo:

Problem: Daemon server works for a day or so before getting this error multiple times and shutting down:
[1426196083] libunbound[28839:0] error: can't create socket: Too many open files

https://bitcointalk.org/index.php?topic=652305.msg10755422#msg10755422
http://pastebin.com/raw.php?i=Q7hrxDZz


# Discussion History
## cornfeedhobo | 2015-05-01T13:08:55+00:00
ACK. same issue. Will update in a day or two once it's been running a while again.


## fluffypony | 2015-11-24T14:49:02+00:00
Fixed, will reopen if it occurs again


# Action History
- Created by: iamsmooth | 2015-03-13T19:18:47+00:00
- Closed at: 2015-11-24T14:49:02+00:00
