---
title: Removing monero from Linux install is overly complicated
source_url: https://github.com/monero-project/monero/issues/2650
author: proehlen
assignees: []
labels: []
created_at: '2017-10-14T05:03:29+00:00'
updated_at: '2017-10-14T14:16:17+00:00'
type: issue
status: closed
closed_at: '2017-10-14T08:49:41+00:00'
---

# Original Description
As far as I can tell, these are the commands I need to run to remove all traces of monero from a linux machine:
```
rm -rf ~/Monero
rm -rf ~/.bitmonero/
rm -rf ~/.config/monero-project/
rm -rf <path_to_app>/monero-gui-0.11.0.0
```
There might be one more - I forget right now where the blockchain gets stored by default.

Is it really necessary to scatter this stuff across so many directories?  One could argue that since privacy is a key concern of the Monero project, leaving so many traces of having used monero on a machine is in itself a concern.

# Discussion History
## moneromooo-monero | 2017-10-14T08:09:18+00:00
1 3 and 4 are GUI specific. Anyway, this is normal behaviour, apart from the ~/Monero thing, which I don't really like. The blockchain is in 2.

## proehlen | 2017-10-14T08:49:41+00:00
> 1 3 and 4 are GUI specific

Ok, I thought this was the repo for the gui.  I've looked and I can't find it if it's another repo.  Closing.

## moneromooo-monero | 2017-10-14T08:52:43+00:00
https://github.com/monero-project/monero-core

## radfish | 2017-10-14T14:16:17+00:00
This problem is solved by distro packages. Arch has a package. If you can, please contribute by packaging it for your favorite distro.

# Action History
- Created by: proehlen | 2017-10-14T05:03:29+00:00
- Closed at: 2017-10-14T08:49:41+00:00
