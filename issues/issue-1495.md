---
title: file chooser dialog doesn't show hidden files/folders on Linux
source_url: https://github.com/monero-project/monero-gui/issues/1495
author: salim-b
assignees: []
labels:
- resolved
created_at: '2018-07-05T13:04:50+00:00'
updated_at: '2018-12-17T09:09:34+00:00'
type: issue
status: closed
closed_at: '2018-12-17T09:09:34+00:00'
---

# Original Description
I've just upgraded to GUI 0.12.2.0 and tried to open my wallet file which resides in the folder `~/.monero_wallets`. It seems impossible to navigate to that folder because I can't find a way to make the file chooser dialog show hidden folders. This seems like a major usability flaw to me....

For now possible workarounds include:
- Set the variable `wallet_path` in `~/.config/monero-project/monero-gui.conf` by hand to the correct (hidden) path
- or move the wallet file(s) to a non-hidden folder.

I'm using Ubuntu 16.04 LTS.

# Discussion History
## pazos | 2018-07-08T16:59:38+00:00
Don't remember if being a qml app changes this, but:
on file chooser -> right click -> show hidden folders - doesn't work?


## sanderfoobar | 2018-07-10T08:15:10+00:00
Doubt this is due to Qt. Try the shortcut `CTRL-H` in the file dialog. 

## pazos | 2018-08-19T22:33:44+00:00
I can confirm than right click on the file chooser will display an option to show/hide hidden files. @salim-b, please test

## dEBRUYNE-1 | 2018-12-17T08:14:52+00:00
The author has not responded to the suggestions. I therefore am going to close this issue.



## dEBRUYNE-1 | 2018-12-17T08:14:58+00:00
+resolved

# Action History
- Created by: salim-b | 2018-07-05T13:04:50+00:00
- Closed at: 2018-12-17T09:09:34+00:00
