---
title: List disk space among the system requirements before installing
source_url: https://github.com/monero-project/monero-gui/issues/1164
author: Bomper
assignees: []
labels:
- resolved
created_at: '2018-03-06T00:08:51+00:00'
updated_at: '2018-03-30T00:00:20+00:00'
type: issue
status: closed
closed_at: '2018-03-30T00:00:20+00:00'
---

# Original Description
First time user on Linux. Ran out of disk space several times, as the wallet keeps download the blockchain.

1. Is there an open-source thin wallet alternative for Linux?
2. Before installing, the user should be warned that they need ample space for the blockchain. On a laptop, 40GB+ is no joke. Ideally the space required would be estimated based on the current state of the blockchain.

# Discussion History
## pazos | 2018-03-06T12:23:49+00:00
@Bomper:

1. You can use the GUI with a [remote node](https://getmonero.org/resources/user-guides/remote_node_gui.html)


## Bomper | 2018-03-06T12:26:22+00:00
@pazos: interesting, didn't realize that. I guess a wizard would be helpful for new users, asking if they'd like to search for a node, vs. run their own daemon.

## sanderfoobar | 2018-03-29T23:46:56+00:00
A diskspace warning is already present during the wallet setup warnings, I wonder why you did not receive one.

https://github.com/monero-project/monero-gui/blob/bf8b8f4512e318ec0beaf465f7d2eb5c74325bc6/main.qml#L1122

As for the wizard(s) themselves, they'll be improved at a later stage so that it is more apparent what the options are for the user.

## sanderfoobar | 2018-03-29T23:48:09+00:00
+resolved

# Action History
- Created by: Bomper | 2018-03-06T00:08:51+00:00
- Closed at: 2018-03-30T00:00:20+00:00
