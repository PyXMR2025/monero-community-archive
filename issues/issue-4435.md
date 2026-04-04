---
title: Right-click in Docker, Quit -- makes Monero freeze forever and requires Force
  Quite
source_url: https://github.com/monero-project/monero-gui/issues/4435
author: meglio
assignees: []
labels: []
created_at: '2025-04-22T00:14:07+00:00'
updated_at: '2025-04-23T14:35:48+00:00'
type: issue
status: closed
closed_at: '2025-04-23T14:35:47+00:00'
---

# Original Description
In MacOS, if I open the Monero GUI and quit it through its menu, it finalizes correctly and quits successfully.

However, if I right-click on its icon in the Docker panel, and choose Quit from the menu, it freezes and the only way to quit it is to go to the Activity Monitor and Force Quit.

It is stably reproducible in my MacOS.

# Discussion History
## selsta | 2025-04-23T14:35:47+00:00
We have an open issue for this. For some reason I have never been able to reproduce this on macOS.

# Action History
- Created by: meglio | 2025-04-22T00:14:07+00:00
- Closed at: 2025-04-23T14:35:47+00:00
