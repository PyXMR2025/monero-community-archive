---
title: simplewallet ctrl+d close failture
source_url: https://github.com/monero-project/monero/issues/32
author: monero-project
assignees: []
labels: []
created_at: '2014-06-11T15:01:57+00:00'
updated_at: '2014-06-13T16:01:59+00:00'
type: issue
status: closed
closed_at: '2014-06-13T16:01:59+00:00'
---

# Original Description
Commit 2d755b3d0eef16a0cedc4801bd7fdde894dd649d (merge from fluffypony) prevents a daemon crash relating to console input, however it creates a hang in simplewallet when attempting to ctrl+d to send eof. This is being actively investigated.


# Discussion History
## Neozaru | 2014-06-11T21:39:22+00:00
I've got the same problem when SIGTERMing the 'bitmonerod' process. (I have to SIGKILL it to achieve it)


## monero-project | 2014-06-13T16:01:59+00:00
Fixed via this commit
https://github.com/monero-project/bitmonero/commit/94cc5a7d718a0dc0efe28af8dfc0955c8525a9a1


# Action History
- Created by: monero-project | 2014-06-11T15:01:57+00:00
- Closed at: 2014-06-13T16:01:59+00:00
