---
title: V0.17.2.0 fails to synch daemon
source_url: https://github.com/monero-project/monero/issues/8542
author: synthcube
assignees: []
labels: []
created_at: '2022-08-30T17:42:44+00:00'
updated_at: '2022-08-30T22:07:24+00:00'
type: issue
status: closed
closed_at: '2022-08-30T22:07:24+00:00'
---

# Original Description
Been running this for over a year with no trouble, but this last time opened and not synching. GIU screen says 'Daemon is synchronized(2701062) but the 'Waiting for daemon to synch' progress bar shows zero and not moving. Log says: "2022-08-30 17:35:12.607	17144	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:231	Failed to parse transaction from blob" and I do not know what step(s) to take next. Thank you in advance. 

# Discussion History
## selsta | 2022-08-30T22:06:58+00:00
Monero had a network upgrade, you have to use v0.18.1.0

# Action History
- Created by: synthcube | 2022-08-30T17:42:44+00:00
- Closed at: 2022-08-30T22:07:24+00:00
