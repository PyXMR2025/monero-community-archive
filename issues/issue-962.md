---
title: '''start-low-graphics-mode.bat'' leaves command window open.'
source_url: https://github.com/monero-project/monero-gui/issues/962
author: QuickBASIC
assignees: []
labels:
- resolved
created_at: '2017-11-17T15:33:21+00:00'
updated_at: '2018-11-18T15:09:32+00:00'
type: issue
status: closed
closed_at: '2018-11-18T15:09:32+00:00'
---

# Original Description
Referencing #812 #926, it probably should just be in the repo anyway.

Should change to:
```
@echo off

set QMLSCENE_DEVICE=softwarecontext

start /b monero-wallet-gui.exe
```

Which will allow the batch to terminate after launching the GUI.

![moneroguilowgraphics](https://user-images.githubusercontent.com/7226914/32954803-229b8206-cb82-11e7-9094-6e81fceb8d84.png)


# Discussion History
## medusadigital | 2017-11-21T10:33:23+00:00
dublicate, but leaving this one open instead of the old one https://github.com/monero-project/monero-gui/issues/811, because this one has the solution inside allready. 



## erciccione | 2018-11-18T14:12:02+00:00
+resolved

# Action History
- Created by: QuickBASIC | 2017-11-17T15:33:21+00:00
- Closed at: 2018-11-18T15:09:32+00:00
