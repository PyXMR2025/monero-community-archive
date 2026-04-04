---
title: Debugging monerod crash issue
source_url: https://github.com/monero-project/monero/issues/1374
author: ghost
assignees: []
labels: []
created_at: '2016-11-24T23:55:01+00:00'
updated_at: '2016-12-01T17:52:07+00:00'
type: issue
status: closed
closed_at: '2016-12-01T17:52:07+00:00'
---

# Original Description
So this crash after 1.5 days has been seen by asok. 

I propose we all choose a point to rewind to and then we can each post which PR we're going to test and post that info here. Once one of us gets to the point where the crash happens it'll make debugging easier.

Interlacing the testing this way will also help speed things up.

# Discussion History
## moneromooo-monero | 2016-11-25T13:37:35+00:00
https://github.com/monero-project/monero/issues/1377

## moneromooo-monero | 2016-11-25T18:42:29+00:00
Fluffypony reports a crash with boost 1.62 on Mac with current master.

## ghost | 2016-11-26T14:54:42+00:00
@moneromooo-monero I'm going to roll back to the commit just before fluffy blocks, #1312 thread_group: fix build with asserts enabled

`git checkout -b old-state acf908c`

## ghost | 2016-12-01T17:52:07+00:00
Seems nobody is coordinating the debugging through this issue so am closing. 

# Action History
- Created by: ghost | 2016-11-24T23:55:01+00:00
- Closed at: 2016-12-01T17:52:07+00:00
