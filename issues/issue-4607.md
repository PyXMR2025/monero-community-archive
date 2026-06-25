---
title: Grab QR from screen does not work in Wayland
source_url: https://github.com/monero-project/monero-gui/issues/4607
author: plowsof
assignees: []
labels: []
created_at: '2026-06-15T14:33:47+00:00'
updated_at: '2026-06-24T23:31:18+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
on Wayland, the Transfer page's "Grab QR code from screen" button does nothing

`OSHelper::grabQrCodesFromScreen() captures via QScreen::grabWindow(0), which doesn't work under Wayland.`

i request displaying a warning under Wayland that it's not supported when the button is clicked (most likely to be accepted) or fix it under Wayland `Capture via org.freedesktop.portal.Screenshot` (which would bring a prompt up where the user is asked if they want to share the screenshot with the application (unlikely to be merged)  

# Discussion History
## FiatDemise | 2026-06-21T14:51:59+00:00
Having Wayland support would be useful for XMRChat. We'd like to test to make sure integrated addresses and amount populate correctly with scan. And then we'd like to make sure scanning QR code works with multiple recipients too.

## waozixyz | 2026-06-24T23:31:18+00:00
i'll look into this 

# Action History
- Created by: plowsof | 2026-06-15T14:33:47+00:00
