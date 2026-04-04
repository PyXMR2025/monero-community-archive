---
title: Gui crash on start
source_url: https://github.com/monero-project/monero-gui/issues/1679
author: RomyWeb
assignees: []
labels:
- resolved
created_at: '2018-10-18T15:32:36+00:00'
updated_at: '2018-10-18T17:45:31+00:00'
type: issue
status: closed
closed_at: '2018-10-18T17:45:31+00:00'
---

# Original Description
Building GUI on windows with mingw64 ok without error but don t want to start. How can I see what could crash the app?
Using qt5-1.11.2 
Using Monero master

# Discussion History
## sanderfoobar | 2018-10-18T15:39:50+00:00
Try to use this specific package: `qt5-5.11.1-3`

1. Remove current qt5: `pacman -R mingw-w64-x86_64-qt5` (or whatever your qt5 package is called)
2. Install: `pacman -U http://repo.msys2.org/mingw/x86_64/mingw-w64-x86_64-qt5-5.11.1-3-any.pkg.tar.xz`
3. Recompile & try


## RomyWeb | 2018-10-18T17:30:32+00:00
Thank you, worked !

## dEBRUYNE-1 | 2018-10-18T17:44:41+00:00
+resolved

# Action History
- Created by: RomyWeb | 2018-10-18T15:32:36+00:00
- Closed at: 2018-10-18T17:45:31+00:00
