---
title: Windows build - Cannot click Cancel or Okay in tx window if buttons fall below
  taskbar
source_url: https://github.com/monero-project/monero-gui/issues/665
author: HugTime
assignees: []
labels: []
created_at: '2017-04-05T22:35:52+00:00'
updated_at: '2017-05-05T09:50:08+00:00'
type: issue
status: closed
closed_at: '2017-05-05T09:50:08+00:00'
---

# Original Description
When sending a transaction, if the "Cancel" and "Ok" buttons fall below the taskbar they become unclickable.  The main GUI window can also not be moved at this point, so the only method I found to continue was to force-quit the GUI.

Version monero-gui-10.3.1-beta2 on Windows 10

# Discussion History
## Jaqueeee | 2017-04-06T15:18:19+00:00
Hmm. So you're saying the confirmation dialog popups with the buttons positioned below the taskbar? It's not centered within the GUI window?

## HugTime | 2017-04-06T15:38:03+00:00
@Jaqueeee the popup confirmation dialogue opens up in the middle of the windowed GUI but the Cancel and Ok buttons may still fall below the Taskbar when the windowed GUI is low enough on the screen.  The windowed GUI cannot be moved at that point after the popup window has been opened and the buttons to close the popup are obscured, making the program inoperable.

## Jaqueeee | 2017-04-06T16:49:38+00:00
OK. Now I understand. Maybe we could change the default position to center of screen instead of relative to the window. 

# Action History
- Created by: HugTime | 2017-04-05T22:35:52+00:00
- Closed at: 2017-05-05T09:50:08+00:00
