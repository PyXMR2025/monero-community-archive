---
title: 'Monero-Daemon BAT file: Issue with long-term running'
source_url: https://github.com/monero-project/monero-gui/issues/3745
author: hiltonmw
assignees: []
labels: []
created_at: '2021-11-22T18:29:25+00:00'
updated_at: '2021-12-24T10:40:36+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Perhaps I'm just a n00b at this, but I thought what I was supposed to do was to run the MONERO-DAEMON bat file on my Windows PC - that would allow for my Wallet to sync.  It works for a few hours, then stops with errors like this:
[1637593441] libunbound[21156:0] error: can't bind socket: Permission denied. for 0.0.0.0
[1637597010] libunbound[21156:0] error: can't bind socket: Permission denied. for 0.0.0.0
[1637597010] libunbound[21156:0] error: can't bind socket: Permission denied. for 0.0.0.0
[1637597011] libunbound[21156:0] error: can't bind socket: Permission denied. for 0.0.0.0
2021-11-22 17:03:15.813 W No incoming connections - check firewalls/routers allow port 18080
2021-11-22 18:03:15.987 W No incoming connections - check firewalls/routers allow port 18080
[1637604421] libunbound[21156:0] error: can't bind socket: Permission denied. for 0.0.0.0

If I stop the bat file and restart it - it immediately starts working again.  Sometimes it works for hours, sometimes a day, but it ultimately always ends up with this issue.  Is it a bug, or am I doing something wrong?  

(Sorry if this is the wrong place for this... wasn't sure where else to turn)

# Discussion History
## selsta | 2021-11-22T18:35:09+00:00
What is this bat file? We don't ship one.

## rbrunner7 | 2021-12-24T10:40:36+00:00
Looks like one of those sporadic bugs that plague the Monero software on Windows which probably are almost impossible to find and correct; I don't think that you do something wrong if it takes hours to reach this state. In earlier versions of Windows you could be glad if Windows as whole stayed up more than a few days without a bluescreen, so ...

@selsta : The Windows GUI installer installs a bunch of batch files, among them one to start the daemon stand-alone manually instead of automatically through the GUI wallet, e.g. to see messages better, or easier issuing of interactive commands.

# Action History
- Created by: hiltonmw | 2021-11-22T18:29:25+00:00
