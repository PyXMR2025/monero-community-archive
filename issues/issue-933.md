---
title: GUI 'start daemon' and 'Show status' ignores custom settings
source_url: https://github.com/monero-project/monero-gui/issues/933
author: ronohara
assignees: []
labels:
- resolved
created_at: '2017-10-28T08:18:44+00:00'
updated_at: '2019-04-26T23:36:35+00:00'
type: issue
status: closed
closed_at: '2019-04-26T23:36:35+00:00'
---

# Original Description
If you set up a remote daemon, in the GUI, under Settings. The Show Status button only checks the localhost daemon (which obviously is not running).

With a remote daemon, you would expect to be able to Show Status, but not 'Start' or 'Stop' the daemon.

# Discussion History
## jnbarlow | 2017-12-18T05:25:11+00:00
+1 to this. I had to set up a local apache proxy on 18081 to trick the GUI into grabbing status from my remote server.

## djfinch | 2018-01-07T14:36:00+00:00
Figured out that Monero GUI just ignoring FQDN address... When I put just IP address there - synchronizing works...

## selsta | 2019-04-26T23:31:07+00:00
The settings page changed a lot. Stop/Start only for a local daemon now. Show status got removed.

+resolved

# Action History
- Created by: ronohara | 2017-10-28T08:18:44+00:00
- Closed at: 2019-04-26T23:36:35+00:00
