---
title: 'Kovri: upgrade ARMv8 box disk space'
source_url: https://github.com/monero-project/meta/issues/1
author: anonimal
assignees: []
labels: []
created_at: '2016-11-06T23:49:47+00:00'
updated_at: '2017-02-13T23:43:20+00:00'
type: issue
status: closed
closed_at: '2017-02-13T23:43:20+00:00'
---

# Original Description
Effects https://github.com/monero-project/kovri/pull/431, build log [here](https://build.getmonero.org/builders/kovri-all-debian-arm8/builds/0/steps/compile/logs/stdio). A fix is currently in-progress, ticketing for housekeeping.

# Discussion History
## anonimal | 2016-11-07T22:09:59+00:00
Build [success](https://build.getmonero.org/builders/kovri-all-debian-arm8/builds/5). Thanks @danrmiller.


## anonimal | 2016-11-12T06:46:29+00:00
@danrmiller the disk is back at 100% but buildbot builds don't appear to be effected. I had to `make clean` to make some room though I can't do any build/testing of my own on the machine.


## danrmiller | 2016-11-17T16:34:35+00:00
All set, host added storage and we moved some things around.


## anonimal | 2016-11-17T16:51:06+00:00
Thank you very much @danrmiller 


## anonimal | 2017-02-13T17:15:35+00:00
ARMv8 is out of space again https://build.getmonero.org/builders/kovri-all-debian-arm8/builds/163/steps/compile/logs/stdio.

## danrmiller | 2017-02-13T21:53:28+00:00
Cleared /tmp. Feel free to re-run any failed builds, or let me know which ones to rebuild. I'm not going to do it otherwise since the builds take so long.

## anonimal | 2017-02-13T23:43:20+00:00
Ok, thanks.

# Action History
- Created by: anonimal | 2016-11-06T23:49:47+00:00
- Closed at: 2017-02-13T23:43:20+00:00
