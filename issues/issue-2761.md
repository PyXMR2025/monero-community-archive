---
title: Hidden XMR amount flashes briefly when closing wallet
source_url: https://github.com/monero-project/monero-gui/issues/2761
author: rehrar
assignees: []
labels:
- resolved
created_at: '2020-02-04T00:02:41+00:00'
updated_at: '2020-02-04T20:45:47+00:00'
type: issue
status: closed
closed_at: '2020-02-04T20:45:47+00:00'
---

# Original Description
When an active GUI session times out, the display of the amount changes to ?.?? in an attempt to keep the amount private. 

When I click the "Cancel" button (which takes me back to the "Select wallet" screen, the actual amount flashes briefly, ruining the intended effect. 

Windows 10

GUI version: v0.15.0.2 (Qt 5.9.7)

Embedded Monero version: v0.15.0.1

# Discussion History
## selsta | 2020-02-04T20:41:10+00:00
Already fixed in master :)

+resolved

# Action History
- Created by: rehrar | 2020-02-04T00:02:41+00:00
- Closed at: 2020-02-04T20:45:47+00:00
