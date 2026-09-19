---
title: Gui freezes after RDP disconnect
source_url: https://github.com/monero-project/monero-gui/issues/4712
author: call-eax
assignees: []
labels: []
created_at: '2026-09-16T18:18:08+00:00'
updated_at: '2026-09-16T18:18:39+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm using Monero Gui to mine on a remote machine that I connect to via RDP.
When I close the RDP session and reconnect it, the GUI is frozen, it does not accept any input and can't be closed.
Mining apparently continues in the background, at least according to CPU usage.
When I open a new Gui in parallel and close it again and accept to forcibly stop the node, the old Gui instance can be closed once the node has been stopped, but nothing else can be clicked.

OS: Windows 10
Gui version: Fluorine Fermi 5.2

# Discussion History
# Action History
- Created by: call-eax | 2026-09-16T18:18:08+00:00
