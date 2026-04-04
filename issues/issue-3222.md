---
title: GUI v0.17.1.3 'Oxygen Orion' dosen' t show up on Debian Buster
source_url: https://github.com/monero-project/monero-gui/issues/3222
author: ghost
assignees: []
labels: []
created_at: '2020-11-09T10:05:32+00:00'
updated_at: '2020-11-10T07:39:56+00:00'
type: issue
status: closed
closed_at: '2020-11-10T07:39:56+00:00'
---

# Original Description
GUI v0.17.1.3 dosen't  show up on Debian Buster with Backport Kernel and Gnome (Wayland)

`/opt/monero-gui-v0.17.1.3/monero-wallet-gui
Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.
2020-11-09 09:31:20.376	W Qt:5.15.2 GUI:0.17.1.3-158e0c3 | screen: 1920x1080 - dpi: 96 - ratio:1.24485
^C
`

Previous versions work.



# Discussion History
## selsta | 2020-11-09T10:07:25+00:00
Seems to be a libxcb bug affecting some linux distros. We are working on a new release.

Please continue using the previous version in the meantime.

## ghost | 2020-11-09T10:10:15+00:00
I switched back to GUI v17.1.1. Works so far - hope I can send funds if needed.

Regards

## selsta | 2020-11-09T10:12:16+00:00
Sending should work fine with a local node or with a trusted remote node: https://github.com/monero-project/monero-gui/issues/3140#issuecomment-706440354

Simple mode can potentially have issues during sending in v0.17.1.1, use the above link to specify a remote node manually.

## ghost | 2020-11-09T10:24:40+00:00
I'm using pruned node. Should be fine also ? 
Since I don' t understand exactly **do I need trusted node in prune mode?**

Thank you very much!

## selsta | 2020-11-09T10:25:13+00:00
Pruned node is fine.

## selsta | 2020-11-10T07:39:56+00:00
v0.17.1.4 is out

# Action History
- Created by: ghost | 2020-11-09T10:05:32+00:00
- Closed at: 2020-11-10T07:39:56+00:00
