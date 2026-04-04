---
title: Monero GUI kills the system monerod on Linux
source_url: https://github.com/monero-project/monero-gui/issues/3476
author: Tronic
assignees: []
labels:
- question
created_at: '2021-05-10T16:00:43+00:00'
updated_at: '2021-05-10T17:06:38+00:00'
type: issue
status: closed
closed_at: '2021-05-10T16:02:17+00:00'
---

# Original Description
I am running monerod via systemd, which I expect to be running at all times.

When starting the GUI, it issues a shutdown command to the system service and runs its own monerod instead (as my desktop user). Is there configuration to avoid this, and force using the already running daemon on localhost?


# Discussion History
## selsta | 2021-05-10T16:02:17+00:00
Switch to advanced mode. (Main menu -> Change wallet mode -> advanced mode)

## Tronic | 2021-05-10T16:41:22+00:00
Thanks. So, now I am supposed to add localhost:18081 as remote node, right? For some reason the client doesn't appear to be connecting and just says network status disconnected.

## selsta | 2021-05-10T16:42:28+00:00
Just select local node if it is on localhost.

## Tronic | 2021-05-10T17:06:38+00:00
That works but it still asks to shutdown the server when GUI exits (and I could not find an option to avoid that). I also got localhost as remote node working after disabling socks proxy setting (my mistake), and that doesn't attempt shutdowns anymore.

# Action History
- Created by: Tronic | 2021-05-10T16:00:43+00:00
- Closed at: 2021-05-10T16:02:17+00:00
