---
title: The GUI should check RPC version and complain if the daemon is too old
source_url: https://github.com/monero-project/monero-gui/issues/124
author: moneromooo-monero
assignees: []
labels: []
created_at: '2016-11-06T23:57:41+00:00'
updated_at: '2016-11-13T17:58:31+00:00'
type: issue
status: closed
closed_at: '2016-11-13T17:58:31+00:00'
---

# Original Description
Using an old daemon will mean the GUI can't send, as the histogram RPC was modified to add returns which an old daemon won't return, causing the wallet to not find what it's looking for.

# Discussion History
## moneromooo-monero | 2016-11-07T12:05:16+00:00
https://github.com/monero-project/monero-core/pull/128


## dternyak | 2016-11-13T17:52:16+00:00
#128 is merged, this can be closed right @moneromooo-monero ?


## fluffypony | 2016-11-13T17:58:31+00:00
Closing as fixed


# Action History
- Created by: moneromooo-monero | 2016-11-06T23:57:41+00:00
- Closed at: 2016-11-13T17:58:31+00:00
