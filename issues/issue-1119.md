---
title: 'low priority : daemon log lvl 0 shows x days ahead when connecting to old
  peers'
source_url: https://github.com/monero-project/monero/issues/1119
author: darentuzi
assignees: []
labels: []
created_at: '2016-09-23T17:59:02+00:00'
updated_at: '2016-12-15T17:13:15+00:00'
type: issue
status: closed
closed_at: '2016-12-15T17:13:15+00:00'
---

# Original Description
Node, version 0.10 running on Ubuntu 14.04
The daemon synchronizes to the latest block fine and works correctly with the wallet but it continuously prints "Sync data returned unknown top block [latest] -> [oldblock] x days ahead SYNCHRONIZATION STARTED
I am assuming its connecting to some peer who is behind in history but its kinda annoying to see this at log level 0.
A possible solution proposed by moneromooo could be to move it to log level 1 if (peer's height is less then latest chain height  && its top hash is part of the main chain).


# Discussion History
## ghost | 2016-10-12T15:43:01+00:00
Hi @darentuzi it seems like we need to change the log levels for quite a few things and formalise just exactly what should appear at each level - see #1187.

@moneromooo-monero also recommends we change the underlying logging system entirely.

I'll try to ask about these at an upcoming dev meeting.


## luigi1111 | 2016-12-15T17:13:15+00:00
Part of #1187. Further discussion can be there.

# Action History
- Created by: darentuzi | 2016-09-23T17:59:02+00:00
- Closed at: 2016-12-15T17:13:15+00:00
