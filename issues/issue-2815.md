---
title: Prevent monero-gui.desktop file creation
source_url: https://github.com/monero-project/monero-gui/issues/2815
author: jluttine
assignees: []
labels: []
created_at: '2020-03-30T10:44:55+00:00'
updated_at: '2020-12-11T11:51:09+00:00'
type: issue
status: closed
closed_at: '2020-12-11T11:51:09+00:00'
---

# Original Description
It seems that every time I run Monero GUI, it creates the following desktop file: `~/.local/share/applications/monero-gui.desktop`. I delete it, but it always creates the file when running. Can this be disabled somehow? I don't want that file (I don't want this custom entry to show up in my app menu) and the resulting file doesn't even work in my system. Is there any way to disable it?

# Discussion History
## selsta | 2020-03-30T10:49:21+00:00
See the comment here: https://github.com/monero-project/monero-gui/pull/2802#issuecomment-598161099

We will try to improve it. AFAIK there is no way to disable it currently.

## xiphon | 2020-12-11T11:51:09+00:00
Closed via https://github.com/monero-project/monero-gui/pull/3260, https://github.com/monero-project/monero-gui/pull/3251

# Action History
- Created by: jluttine | 2020-03-30T10:44:55+00:00
- Closed at: 2020-12-11T11:51:09+00:00
