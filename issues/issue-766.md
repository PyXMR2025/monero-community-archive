---
title: GUI says "Synchronizing" when it hasn't connected yet
source_url: https://github.com/monero-project/monero-gui/issues/766
author: fresheneesz
assignees: []
labels:
- feature
- resolved
created_at: '2017-06-15T07:19:29+00:00'
updated_at: '2018-11-18T16:18:32+00:00'
type: issue
status: closed
closed_at: '2018-11-18T16:18:32+00:00'
---

# Original Description
See this issue: https://github.com/monero-project/monero/issues/2083

Basically, the daemon wasn't connected, and yet the GUI said it was synchronizing. Only after going into the status log did I find out it wasn't.

# Discussion History
## medusadigital | 2017-08-07T18:40:24+00:00
@Jaqueeee considered adding the status _"connecting.."_ 

not to be mistaken with the status _"connected"_


Since this is a new GUI state, it should be added carefully and be threated as a new feature.

+feature

## erciccione | 2018-11-18T13:45:33+00:00
Resolved with double bar 'syncronizing wallet' and 'syncronizing daemon'

+resolved

# Action History
- Created by: fresheneesz | 2017-06-15T07:19:29+00:00
- Closed at: 2018-11-18T16:18:32+00:00
