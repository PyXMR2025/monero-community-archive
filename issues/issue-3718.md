---
title: '[macOS] freezes image while minimizing, can cause an information leak when
  maximizing again'
source_url: https://github.com/monero-project/monero-gui/issues/3718
author: selsta
assignees: []
labels: []
created_at: '2021-10-24T12:19:15+00:00'
updated_at: '2021-10-24T12:19:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Reported on H1

macOS freezes OpenGL applications while minimized. This can cause an information leak if the GUI locks while minimized and then later maximized again.

Steps to reproduce:

1) Unlocked GUI wallet
2) Minimize the GUI while still unlocked
3) The GUI locks while minimized, the application does not redraw (macOS does that likely to save resources, battery)
4) Once you maximize the GUI again you can see the unlocked GUI for a short time during the open animation.

Possible workarounds is to force lock before minimize event. 

# Discussion History
# Action History
- Created by: selsta | 2021-10-24T12:19:15+00:00
