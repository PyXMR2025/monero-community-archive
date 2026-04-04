---
title: add-exclusive-node appears broken
source_url: https://github.com/monero-project/monero/issues/2346
author: iamsmooth
assignees: []
labels:
- bug
created_at: '2017-08-25T20:06:43+00:00'
updated_at: '2017-09-25T20:54:23+00:00'
type: issue
status: closed
closed_at: '2017-09-25T20:54:23+00:00'
---

# Original Description
The --add-exclusive-node option is supposed to only connect to the specified node or nodes (I think it can be specified multiple times). This may be done for security reasons, including to only connect to friendly nodes and prevent the deamon IP from appearing in foreign nodes' connection tables.

When using --add-exclusive-node I can see the daemon still attempting to connect to other nodes. My guess would be this was due to some of the other p2p enhancements (such as anchor nodes, etc.) not recognizing the exclusive node option.



# Discussion History
## dEBRUYNE-1 | 2017-08-27T13:56:01+00:00
+bug

## moneromooo-monero | 2017-09-10T12:11:18+00:00
This seems to be the "gray list housekeeping" code, which will try to connect to check whether a given node is up. This will not lead to an actual connection "full" connection, as it gets dropped if succesful (and the node moved to the white list). I'll disable this when an exclusive node is set.

## moneromooo-monero | 2017-09-10T12:23:08+00:00
https://github.com/monero-project/monero/pull/2428

## radfish | 2017-09-24T19:42:48+00:00
Is @osensei 's explanation on #848 no longer apply?

## iamsmooth | 2017-09-25T01:38:02+00:00
@radfish #848 is a different issue. That refers to incoming connection this issue to outgoing.

It appears this issue is fixed by the above mentioned 2428 once that is merged.

## moneromooo-monero | 2017-09-25T20:28:56+00:00
+resolved

# Action History
- Created by: iamsmooth | 2017-08-25T20:06:43+00:00
- Closed at: 2017-09-25T20:54:23+00:00
