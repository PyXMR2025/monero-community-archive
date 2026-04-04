---
title: Loading blockchain on startup
source_url: https://github.com/monero-project/monero/issues/2161
author: jtgrassie
assignees: []
labels: []
created_at: '2017-07-09T14:15:14+00:00'
updated_at: '2017-08-07T18:00:16+00:00'
type: issue
status: closed
closed_at: '2017-08-07T18:00:16+00:00'
---

# Original Description
`src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder...`

This can take quite a few minutes and there is zero user feedback. Might be nice to have some kind of progress indicator.

# Discussion History
## moneromooo-monero | 2017-07-09T14:17:40+00:00
While it's "stuck", get a stack trace for all threads. Chances are it's timing out on some network call.

## moneromooo-monero | 2017-07-30T16:01:14+00:00
I had that problem today, and it was indeed a DNS call, looking up dynamic checkpoints. Guess it's worth adding a message for that.

## moneromooo-monero | 2017-07-31T07:44:37+00:00
https://github.com/monero-project/monero/pull/2230

## moneromooo-monero | 2017-08-07T17:59:52+00:00
+resolved

# Action History
- Created by: jtgrassie | 2017-07-09T14:15:14+00:00
- Closed at: 2017-08-07T18:00:16+00:00
