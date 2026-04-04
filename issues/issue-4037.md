---
title: Daemon connection issues recently
source_url: https://github.com/monero-project/monero/issues/4037
author: BKdilse
assignees: []
labels: []
created_at: '2018-06-22T08:30:16+00:00'
updated_at: '2018-06-24T13:08:09+00:00'
type: issue
status: closed
closed_at: '2018-06-24T13:08:09+00:00'
---

# Original Description
I am having intermitent connection issues with monerd, running on Ubuntu 16.04.

The logs show:

COMMAND_HANDSHAKE Invoke Failed -4, LEVIN_ERROR_CONNECTION_TIMEOUT

On occasions it works, and randomly stops with the above issue.  All other internet activity works fine.  I can successfully telnet into the remote node which is falling on.

Any ideas what is going on here?

# Discussion History
## moneromooo-monero | 2018-06-22T10:07:50+00:00
Does https://github.com/monero-project/monero/pull/3962 help ?

## BKdilse | 2018-06-22T11:39:31+00:00
Thanks, I'll try and give it a go and see.

## BKdilse | 2018-06-24T13:08:09+00:00
seems to be a connection issue with my network, so closing.

# Action History
- Created by: BKdilse | 2018-06-22T08:30:16+00:00
- Closed at: 2018-06-24T13:08:09+00:00
