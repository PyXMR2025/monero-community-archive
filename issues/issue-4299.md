---
title: Desktop GUI Entry Exec path is not in quotes
source_url: https://github.com/monero-project/monero-gui/issues/4299
author: S5NC
assignees: []
labels: []
created_at: '2024-04-02T09:33:58+00:00'
updated_at: '2024-08-13T16:37:28+00:00'
type: issue
status: closed
closed_at: '2024-08-13T16:37:28+00:00'
---

# Original Description
Having spaces in the path name to where the Monero GUI is located causes the desktop file it automatically generates when prompted, to be invalid. It neither launches nor appears in the applications menu. If quotes are added around the path, this will no longer happen.

`Exec=/my path/to/monero-wallet-gui %u`
to
`Exec="/my path/to/monero-wallet-gui" %u`

# Discussion History
# Action History
- Created by: S5NC | 2024-04-02T09:33:58+00:00
- Closed at: 2024-08-13T16:37:28+00:00
