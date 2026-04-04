---
title: Advanced Tab Hotkey Broken
source_url: https://github.com/monero-project/monero-gui/issues/415
author: needmoney90
assignees: []
labels: []
created_at: '2017-01-17T21:05:44+00:00'
updated_at: '2017-02-04T15:42:40+00:00'
type: issue
status: closed
closed_at: '2017-02-04T15:42:40+00:00'
---

# Original Description
Pressing ctrl+A to access the Advanced tab does not work. Additionally, Hotkeys for Send, Receive, History, and Settings the hotkeys work properly, but make an error sound.

# Discussion History
## traviss01 | 2017-01-17T21:10:17+00:00
can confirm issue is happening on my computer. windows 10 64bit. 

## Jaqueeee | 2017-01-17T22:02:01+00:00
advanced hotkey fixed in #417, but i can't reproduce the error sound issue. Maybe that's windows only. Had to use "D" for advanced because ctrl+A is reserved for select all. 

## needmoney90 | 2017-01-17T22:03:14+00:00
Error sound issue is on OSX, not Windows. 


## Jaqueeee | 2017-01-17T22:07:42+00:00
Weird. I'm also on OSX. Does it happen with both cmd and ctrl? Which osx version are you on?

## needmoney90 | 2017-01-17T22:35:40+00:00
10.10.1 Yosemite. It does happen with ctrl (except ctrl+A), but with cmd it happens only on the button presses where the keys aren't system hooks (cmd+H, cmd+A)

# Action History
- Created by: needmoney90 | 2017-01-17T21:05:44+00:00
- Closed at: 2017-02-04T15:42:40+00:00
