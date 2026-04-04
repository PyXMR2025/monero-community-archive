---
title: GUI overlap of "Connected" and "Synchronizing blocks" text
source_url: https://github.com/monero-project/monero-gui/issues/349
author: BoscoMurray
assignees: []
labels:
- bug
- resolved
created_at: '2016-12-23T11:37:03+00:00'
updated_at: '2018-07-15T17:27:22+00:00'
type: issue
status: closed
closed_at: '2018-07-15T17:27:22+00:00'
---

# Original Description
After resizing the GUI smaller, the "Connected" and "Synchronizing blocks" text in the bottom left overlaps the menus on the left. Would it be possible to hide the menu's (only the parts of the menu covered by this "Connected" text) and at the same time introduce a scroll bar so that the menu's can still be navigated?

This is kind of related to another reported issue: [https://github.com/monero-project/monero-core/issues/296]
Since this would help make the GUI usable on smaller laptop screens.

# Discussion History
## moneromooo-monero | 2016-12-23T13:44:48+00:00
What height is your screen, for reference ?

## BoscoMurray | 2016-12-23T14:10:43+00:00
1366x768 is the native resolution. Its a Dell E7440 with 14" screen. This is further reduced by the borders and menu's around the VirtualBox VM that I run the wallet in.

## sanderfoobar | 2018-03-30T01:57:41+00:00
+bug

## sanderfoobar | 2018-03-30T01:58:09+00:00
@medusadigital Could you verify you can reproduce this on Windows, with the dark theme?

## leafcutterant | 2018-04-14T18:45:46+00:00
Can verify that it persists on Windows, 0.12, dark theme:

![0](https://user-images.githubusercontent.com/7106231/38771518-c6305b96-4024-11e8-8445-a9d53ac3e77d.png)

## sanderfoobar | 2018-04-14T18:57:10+00:00
#1289

## dEBRUYNE-1 | 2018-07-15T17:23:58+00:00
#1289 is included in GUI v0.12.2.0, so I am going to mark this as resolved.

+resolved

# Action History
- Created by: BoscoMurray | 2016-12-23T11:37:03+00:00
- Closed at: 2018-07-15T17:27:22+00:00
