---
title: screen/mouse instability
source_url: https://github.com/monero-project/monero-gui/issues/3921
author: dchmelik
assignees: []
labels: []
created_at: '2022-05-14T04:54:21+00:00'
updated_at: '2023-12-28T09:57:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I started using monero-gui several years ago, but regardless which X Window System (X) window manager (WM) or desktop environment (DE) I use it has problems with screens and the mouse (other programs don't have same problems.)
&nbsp;&nbsp;&nbsp; I have multiple screens and monero-gui usually opens halfway on my top screen (1600x1200) and halfway on my bottom screen (4K.)
&nbsp;&nbsp;&nbsp; When I move monero-gui, often the mouse moves much further than monero-gui does until some seconds later, so sometimes I have to move mouse back and start over, and if I start moving monero-gui over another window, monero-gui usually starts 'shaking'--moving left & right and up & down, back & forth, about an inch each way fast.  So it takes several seconds longer than all other programs to move where I want.
&nbsp;&nbsp;&nbsp; This happens in both X/KDE and XFCE desktop environments (which use different window managers.) 

# Discussion History
## selsta | 2022-05-14T19:13:08+00:00
Is this custom compiled? Installed from package manager or getmonero?

## dchmelik | 2022-05-15T00:27:56+00:00
monero-gui-linux-x64-v0.17.3.2.tar.bz2 (and earlier versions)

## selsta | 2022-05-15T00:29:05+00:00
Does turning off custom decorations in Settings -> Interface help?

## dchmelik | 2022-05-15T01:04:31+00:00
Fixed shakiness but still starts halfway on two screens, when it should only use the active screen (of three or however many.)

# Action History
- Created by: dchmelik | 2022-05-14T04:54:21+00:00
