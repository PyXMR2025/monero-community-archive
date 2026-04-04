---
title: Run daemon as a windows service so the user is always synchronized with the
  network
source_url: https://github.com/monero-project/monero-gui/issues/484
author: Gingeropolous
assignees: []
labels:
- duplicate
created_at: '2017-02-22T02:41:05+00:00'
updated_at: '2017-08-07T18:35:11+00:00'
type: issue
status: closed
closed_at: '2017-08-07T18:35:11+00:00'
---

# Original Description
Create an option to run the daemon as a service. This will allow the user relatively instant access to their Monero, wherein they will only have to wait for the wallet to synchronize. 

# Discussion History
## Jaqueeee | 2017-03-03T20:23:29+00:00
can this be closed?

## antanst | 2017-03-04T13:37:01+00:00
In my opinion if, after closing a window, something continues to run in the background, there should be a clear indication of doing so:

- On Windows, a system tray icon.
- On MacOS, a dock icon.
- On Linux (Gnome), a panel icon.

Having something (especially battery intensive like the Monero daemon) running in the background without clear indication of doing so will alienate users.

## medusadigital | 2017-04-18T09:58:39+00:00
Hi @antanst , i openend a new issue regarding your feature request so it wont get lost. 

i hope thats fine. 

thanks for your suggestion

## dEBRUYNE-1 | 2017-08-07T17:50:25+00:00
+duplicate

# Action History
- Created by: Gingeropolous | 2017-02-22T02:41:05+00:00
- Closed at: 2017-08-07T18:35:11+00:00
