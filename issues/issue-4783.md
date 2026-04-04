---
title: Syncing
source_url: https://github.com/monero-project/monero/issues/4783
author: gittyhupbub
assignees: []
labels:
- invalid
created_at: '2018-11-02T12:16:08+00:00'
updated_at: '2018-11-03T16:32:56+00:00'
type: issue
status: closed
closed_at: '2018-11-03T16:32:56+00:00'
---

# Original Description
I've recently switched my block chain directories to an external drive and im encountering a very unusual long sync time right after.  I've been stuck in the 89% sync range for 6+ hours doing a consistent small 20 block chunks for a long period of time. My connection is good and it never took no where near as long when i first started syncing to the network. 

# Discussion History
## moneromooo-monero | 2018-11-02T12:24:06+00:00
Syncing requires a lot off the underlying storage. SSDs are good. HDDs are worse. An external drive might be very slow, depending on the details. You may want to keep the blockchain on the fastest drive at least till you've finished the initial sync.

## moneromooo-monero | 2018-11-03T16:27:32+00:00
Not a bug, closing.

+invalid

# Action History
- Created by: gittyhupbub | 2018-11-02T12:16:08+00:00
- Closed at: 2018-11-03T16:32:56+00:00
