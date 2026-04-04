---
title: linux x64 gui v 0.12.0.0 will not connect to remote node on LAN
source_url: https://github.com/monero-project/monero/issues/3566
author: cryptoballs
assignees: []
labels:
- invalid
created_at: '2018-04-06T05:36:54+00:00'
updated_at: '2018-06-25T22:48:58+00:00'
type: issue
status: closed
closed_at: '2018-06-25T22:48:58+00:00'
---

# Original Description
Cannot connect to a remote node running on a server on my local network. 

The CLI connects fine, and Cake Wallet on iOS connects fine as well. 

The GUI will not connect by local ip/port. Network status just says disconnected, no activity at all.

# Discussion History
## cryptoballs | 2018-04-06T05:47:01+00:00
Additionally, when I go through the wizard to restore a wallet and choose "remote node", the following summary page still indicates I'm using a node on localhost. However, the terminal window log appears that it's using my correct remote node:

qml: connecting remote node
"initAsync: <MY-SERVER-IP>:18081"
init non async


## dEBRUYNE-1 | 2018-04-06T14:03:36+00:00
Please use the GUI repository. In addition, this issue has already been reported:

https://github.com/monero-project/monero-gui/issues/1261

## moneromooo-monero | 2018-06-25T22:01:29+00:00
Wrong repo.

+invalid

# Action History
- Created by: cryptoballs | 2018-04-06T05:36:54+00:00
- Closed at: 2018-06-25T22:48:58+00:00
