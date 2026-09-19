---
title: GUI proxy setting silently fails with invalid proxy
source_url: https://github.com/monero-project/monero-gui/issues/4704
author: EntropyHoover
assignees: []
labels: []
created_at: '2026-09-09T05:54:17+00:00'
updated_at: '2026-09-17T20:49:08+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
In monero gui settings, if user inputs an invalid proxy address, for example 127.0.0.1abc, or 127.0.0..1, all the proxy connections just fail silently. No warning is issued in console or gui. At least there should be a warning issued in the console for the invalid proxy, so the user can understand what happened


# Discussion History
## 0x11semprez | 2026-09-17T20:28:37+00:00
Hello, 
I'll try to see what happened

## 0x11semprez | 2026-09-17T20:49:08+00:00
You're right. 
Thanks!  I'll take care of it. @EntropyHoover 

# Action History
- Created by: EntropyHoover | 2026-09-09T05:54:17+00:00
