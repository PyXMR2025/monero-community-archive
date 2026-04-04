---
title: 'monerod fails to initialize p2p server '
source_url: https://github.com/monero-project/monero/issues/2652
author: notmike-5
assignees: []
labels: []
created_at: '2017-10-14T10:55:05+00:00'
updated_at: '2017-10-14T11:00:20+00:00'
type: issue
status: closed
closed_at: '2017-10-14T10:59:35+00:00'
---

# Original Description
I am running latest Monero 'Helium Hydra' (v.0.11.0.0-86e9de58), however monerod is failing to initialize the p2p server.  Output is below.

$ monerod
2017-10-14 10:47:22.055	    7f356d522500	INFO 	global	src/daemon/main.cpp:283	Monero 'Helium Hydra' (v0.11.0.0-86e9de58)
2017-10-14 10:47:22.055	    7f356d522500	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-10-14 10:47:22.055	    7f356d522500	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-10-14 10:47:22.055	    7f356d522500	INFO 	global	src/daemon/p2p.h:63Initializing p2p server...
connect: Connection timed out
connect: Connection timed out
connect: Connection timed out

# Discussion History
## notmike-5 | 2017-10-14T10:58:01+00:00
So... apparently it actually works fine. It just lags hard on startup, but then it works. I suppose I'm just slow.

# Action History
- Created by: notmike-5 | 2017-10-14T10:55:05+00:00
- Closed at: 2017-10-14T10:59:35+00:00
