---
title: Use xdg-desktop-menu to install menu shortcut instead of writing to the file.
source_url: https://github.com/monero-project/monero-gui/issues/2598
author: tobtoht
assignees: []
labels: []
created_at: '2019-12-15T19:25:57+00:00'
updated_at: '2019-12-15T19:27:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Some menus will not refresh when a .desktop file is updated until the system is restarted.

If the menu entry is used before the system is restarted it is overwritten back to the older version causing confusion.

See: https://linux.die.net/man/1/xdg-desktop-menu

# Discussion History
# Action History
- Created by: tobtoht | 2019-12-15T19:25:57+00:00
