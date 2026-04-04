---
title: Monero GUI with Local node - Failed to read line. monerod log spam
source_url: https://github.com/monero-project/monero-gui/issues/2958
author: NewEraCracker
assignees: []
labels: []
created_at: '2020-06-15T21:26:31+00:00'
updated_at: '2021-04-21T02:19:29+00:00'
type: issue
status: closed
closed_at: '2021-04-21T02:19:28+00:00'
---

# Original Description
When starting the GUI wallet with local node option, the logs of monerod become filled with:
ERROR	console_handler	contrib/epee/include/console_handler.h:397	Failed to read line.

Workaround to prevent this, is to start wallet in low graphics mode.

![LogSpam](https://user-images.githubusercontent.com/416945/84707257-4c472280-af56-11ea-9959-20d97894afe3.png)

# Discussion History
## selsta | 2021-04-21T02:19:28+00:00
Fixed in #3360

# Action History
- Created by: NewEraCracker | 2020-06-15T21:26:31+00:00
- Closed at: 2021-04-21T02:19:28+00:00
